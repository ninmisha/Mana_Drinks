// Mobile menu functionality
document.addEventListener('DOMContentLoaded', function() {
    const mobileMenuButton = document.querySelector('.mobile-menu-button');
    const mobileMenu = document.querySelector('.mobile-menu');

    mobileMenuButton.addEventListener('click', () => {
        mobileMenu.classList.toggle('hidden');
        mobileMenu.classList.toggle('active');
    });

    // Close mobile menu when clicking outside
    document.addEventListener('click', (e) => {
        if (!mobileMenu.contains(e.target) && !mobileMenuButton.contains(e.target)) {
            mobileMenu.classList.add('hidden');
            mobileMenu.classList.remove('active');
        }
    });
});

// Scroll indicator
window.addEventListener('scroll', () => {
    const scrollIndicator = document.querySelector('.scroll-indicator');
    const windowHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    const scrolled = (window.scrollY / windowHeight) * 100;
    
    if (scrollIndicator) {
        scrollIndicator.style.width = `${scrolled}%`;
    }
});

// Cart functionality
class Cart {
    constructor() {
        this.items = JSON.parse(localStorage.getItem('cart')) || [];
        this.total = 0;
        this.updateCartCount();
        this.setupEventListeners();
    }

    addItem(product) {
        const existingItem = this.items.find(item => item._id === product._id);
        
        if (existingItem) {
            existingItem.quantity += 1;
        } else {
            this.items.push({ ...product, quantity: 1 });
        }

        this.saveCart();
        this.updateCartCount();
        this.showNotification('Product added to cart');
    }

    removeItem(productId) {
        this.items = this.items.filter(item => item._id !== productId);
        this.saveCart();
        this.updateCartCount();
        this.showNotification('Product removed from cart');
    }

    updateQuantity(productId, quantity) {
        const item = this.items.find(item => item._id === productId);
        if (item) {
            item.quantity = parseInt(quantity);
            if (item.quantity <= 0) {
                this.removeItem(productId);
            }
        }
        this.saveCart();
        this.updateCartCount();
    }

    saveCart() {
        localStorage.setItem('cart', JSON.stringify(this.items));
        this.calculateTotal();
    }

    calculateTotal() {
        this.total = this.items.reduce((sum, item) => sum + (item.price * item.quantity), 0);
        return this.total;
    }

    updateCartCount() {
        const cartCount = document.getElementById('cart-count');
        if (cartCount) {
            const totalItems = this.items.reduce((sum, item) => sum + item.quantity, 0);
            cartCount.textContent = totalItems;
            cartCount.classList.add('cart-badge');
            setTimeout(() => cartCount.classList.remove('cart-badge'), 300);
        }
    }

    showNotification(message) {
        const notification = document.createElement('div');
        notification.className = 'fixed bottom-4 right-4 bg-green-500 text-white px-6 py-3 rounded-lg shadow-lg transform translate-y-0 opacity-100 transition-all duration-300';
        notification.textContent = message;
        
        document.body.appendChild(notification);
        
        setTimeout(() => {
            notification.style.transform = 'translateY(100%)';
            notification.style.opacity = '0';
            setTimeout(() => notification.remove(), 300);
        }, 2000);
    }

    setupEventListeners() {
        // Add to cart buttons
        document.addEventListener('click', (e) => {
            if (e.target.matches('.add-to-cart')) {
                const productId = e.target.dataset.productId;
                fetch(`/api/products/${productId}`)
                    .then(response => response.json())
                    .then(product => this.addItem(product))
                    .catch(error => console.error('Error adding to cart:', error));
            }
        });
    }
}

// Initialize cart
const cart = new Cart();

// Intersection Observer for animations
const observeElements = () => {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-fade-in');
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1
    });

    document.querySelectorAll('.animate-on-scroll').forEach(el => observer.observe(el));
};

// Initialize animations
document.addEventListener('DOMContentLoaded', observeElements); 