cat > js/script.js << 'EOF'
// Variables globales
let cartCount = 0;
let cartItems = [];

// Función para scroll suave
function scrollToSection(sectionId) {
    const section = document.getElementById(sectionId);
    if (section) {
        section.scrollIntoView({ behavior: 'smooth' });
    }
}

// Agregar al carrito
function addToCart(productName, price) {
    cartCount++;
    cartItems.push({ name: productName, price: price });
    
    document.getElementById('cart-count').textContent = cartCount;
    
    const cartIcon = document.querySelector('.cart-icon');
    cartIcon.style.transform = 'scale(1.2)';
    setTimeout(() => {
        cartIcon.style.transform = 'scale(1)';
    }, 300);
    
    showNotification(`${productName} agregado al carrito! 🎉`);
}

// Filtrar productos
function filterProducts(category) {
    const productos = document.querySelectorAll('.producto-card');
    const buttons = document.querySelectorAll('.cat-btn');
    
    buttons.forEach(btn => btn.classList.remove('active'));
    event.target.classList.add('active');
    
    productos.forEach(producto => {
        if (category === 'todos') {
            producto.style.display = 'block';
        } else {
            if (producto.dataset.category === category) {
                producto.style.display = 'block';
            } else {
                producto.style.display = 'none';
            }
        }
    });
}

// Seleccionar plan
function selectPlan(planName, price) {
    showNotification(`¡Plan ${planName} seleccionado! Precio: $${price}/mes 💳`);
    
    setTimeout(() => {
        alert(`Procesando suscripción al Plan ${planName}...\n\nSerás redirigido al proceso de pago.`);
    }, 500);
}

// Enviar formulario
function submitForm(event) {
    event.preventDefault();
    
    const form = event.target;
    showNotification('¡Mensaje enviado exitosamente! 📧 Te responderemos pronto.');
    form.reset();
}

// Sistema de notificaciones
function showNotification(message) {
    const notification = document.createElement('div');
    notification.className = 'notification';
    notification.textContent = message;
    notification.style.cssText = `
        position: fixed;
        top: 100px;
        right: 20px;
        background: linear-gradient(135deg, #9FD5C0, #D4917B);
        color: white;
        padding: 1rem 2rem;
        border-radius: 10px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
        z-index: 10000;
        animation: slideIn 0.3s ease-out;
        font-weight: 600;
    `;
    
    const style = document.createElement('style');
    style.textContent = `
        @keyframes slideIn {
            from {
                transform: translateX(400px);
                opacity: 0;
            }
            to {
                transform: translateX(0);
                opacity: 1;
            }
        }
        @keyframes slideOut {
            from {
                transform: translateX(0);
                opacity: 1;
            }
            to {
                transform: translateX(400px);
                opacity: 0;
            }
        }
    `;
    document.head.appendChild(style);
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.style.animation = 'slideOut 0.3s ease-out';
        setTimeout(() => {
            document.body.removeChild(notification);
        }, 300);
    }, 3000);
}

// Animación al scroll
window.addEventListener('scroll', () => {
    const elements = document.querySelectorAll('.producto-card, .beneficio-card, .plan-card');
    
    elements.forEach(element => {
        const position = element.getBoundingClientRect().top;
        const screenPosition = window.innerHeight / 1.3;
        
        if (position < screenPosition) {
            element.style.opacity = '1';
            element.style.transform = 'translateY(0)';
        }
    });
});

// Inicializar animaciones
document.addEventListener('DOMContentLoaded', () => {
    const elements = document.querySelectorAll('.producto-card, .beneficio-card, .plan-card');
    
    elements.forEach(element => {
        element.style.opacity = '0';
        element.style.transform = 'translateY(50px)';
        element.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    });
    
    console.log('🐾 PetCare Shop cargado correctamente!');
    console.log(`Total de productos: ${document.querySelectorAll('.producto-card').length}`);
});
EOF
