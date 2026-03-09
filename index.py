cat > index.html << 'EOF'
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PetCare Shop - Alimentos Premium para Mascotas</title>
    <link rel="stylesheet" href="css/styles.css">
</head>
<body>
    <!-- Header y Navegación -->
    <header>
        <nav class="navbar">
            <div class="logo">
                <span class="logo-icon">🐾</span>
                <span class="logo-text">PetCare Shop</span>
            </div>
            <ul class="nav-links">
                <li><a href="#inicio">Inicio</a></li>
                <li><a href="#productos">Productos</a></li>
                <li><a href="#suscripcion">Suscripciones</a></li>
                <li><a href="#contacto">Contacto</a></li>
            </ul>
            <div class="cart-icon">
                🛒 <span id="cart-count">0</span>
            </div>
        </nav>
    </header>

    <!-- Sección Hero -->
    <section id="inicio" class="hero">
        <div class="hero-content">
            <h1>Nutrición Natural para tus Mascotas</h1>
            <p>Alimentos orgánicos y productos ecológicos con entrega mensual. Cuida a tu mascota con amor natural.</p>
            <div class="hero-buttons">
                <button class="btn-primary" onclick="scrollToSection('suscripcion')">Explorar Suscripciones</button>
            </div>
        </div>
    </section>

    <!-- Beneficios -->
    <section class="beneficios">
        <h2>¿Por qué elegirnos?</h2>
        <div class="beneficios-grid">
            <div class="beneficio-card">
                <div class="icon">🥇</div>
                <h3>Calidad Premium</h3>
                <p>Ingredientes naturales y nutritivos</p>
            </div>
            <div class="beneficio-card">
                <div class="icon">🚚</div>
                <h3>Envío Gratis</h3>
                <p>En compras mayores a $500</p>
            </div>
            <div class="beneficio-card">
                <div class="icon">💰</div>
                <h3>Ahorra 20%</h3>
                <p>Con suscripción mensual</p>
            </div>
            <div class="beneficio-card">
                <div class="icon">⭐</div>
                <h3>Garantía Total</h3>
                <p>100% satisfacción garantizada</p>
            </div>
        </div>
    </section>

    <!-- Productos -->
    <section id="productos" class="productos">
        <h2>Nuestros Productos</h2>
        <div class="categorias">
            <button class="cat-btn active" onclick="filterProducts('todos')">Todos</button>
            <button class="cat-btn" onclick="filterProducts('perros')">Perros</button>
            <button class="cat-btn" onclick="filterProducts('gatos')">Gatos</button>
        </div>
        <div class="productos-grid">
            <!-- Producto 1 -->
            <div class="producto-card" data-category="perros">
                <div class="producto-badge">Más vendido</div>
                <div class="producto-img">🦴</div>
                <h3>Alimento Premium Perro Adulto</h3>
                <p class="descripcion">Fórmula balanceada con pollo y arroz - 15kg</p>
                <div class="rating">⭐⭐⭐⭐⭐ (127)</div>
                <p class="precio">$450 <span class="precio-antes">$550</span></p>
                <button class="btn-add-cart" onclick="addToCart('Alimento Premium Perro', 450)">Agregar al Carrito</button>
            </div>

            <!-- Producto 2 -->
            <div class="producto-card" data-category="gatos">
                <div class="producto-badge nuevo">Nuevo</div>
                <div class="producto-img">🐟</div>
                <h3>Alimento Premium Gato</h3>
                <p class="descripcion">Con salmón y atún natural - 10kg</p>
                <div class="rating">⭐⭐⭐⭐⭐ (89)</div>
                <p class="precio">$380 <span class="precio-antes">$450</span></p>
                <button class="btn-add-cart" onclick="addToCart('Alimento Premium Gato', 380)">Agregar al Carrito</button>
            </div>

            <!-- Producto 3 -->
            <div class="producto-card" data-category="perros">
                <div class="producto-img">🥩</div>
                <h3>Alimento Cachorro</h3>
                <p class="descripcion">Especial para cachorros - 12kg</p>
                <div class="rating">⭐⭐⭐⭐⭐ (95)</div>
                <p class="precio">$520</p>
                <button class="btn-add-cart" onclick="addToCart('Alimento Cachorro', 520)">Agregar al Carrito</button>
            </div>

            <!-- Producto 4 -->
            <div class="producto-card" data-category="gatos">
                <div class="producto-img">🍗</div>
                <h3>Alimento Gatito</h3>
                <p class="descripcion">Para gatitos hasta 12 meses - 8kg</p>
                <div class="rating">⭐⭐⭐⭐ (67)</div>
                <p class="precio">$340</p>
                <button class="btn-add-cart" onclick="addToCart('Alimento Gatito', 340)">Agregar al Carrito</button>
            </div>

            <!-- Producto 5 -->
            <div class="producto-card" data-category="perros">
                <div class="producto-img">🌾</div>
                <h3>Alimento Senior</h3>
                <p class="descripcion">Para perros mayores de 7 años - 15kg</p>
                <div class="rating">⭐⭐⭐⭐⭐ (112)</div>
                <p class="precio">$480</p>
                <button class="btn-add-cart" onclick="addToCart('Alimento Senior', 480)">Agregar al Carrito</button>
            </div>

            <!-- Producto 6 -->
            <div class="producto-card" data-category="gatos">
                <div class="producto-img">🦐</div>
                <h3>Alimento Light Gato</h3>
                <p class="descripcion">Bajo en calorías - 10kg</p>
                <div class="rating">⭐⭐⭐⭐ (78)</div>
                <p class="precio">$395</p>
                <button class="btn-add-cart" onclick="addToCart('Alimento Light Gato', 395)">Agregar al Carrito</button>
            </div>
        </div>
    </section>

    <!-- Suscripción -->
    <section id="suscripcion" class="suscripcion">
        <h2>Planes de Suscripción Natural</h2>
        <p class="subtitle">Nutrición orgánica mensual para cada tipo de mascota</p>
        <div class="planes-grid">
            <!-- Plan Básico -->
            <div class="plan-card">
                <div class="plan-header">
                    <h3>Plan Básico</h3>
                    <div class="plan-icon">🐕</div>
                </div>
                <div class="plan-precio">
                    <span class="precio-grande">$400</span>
                    <span class="precio-periodo">/mes</span>
                </div>
                <ul class="plan-beneficios">
                    <li>✓ 1 bolsa de 15kg al mes</li>
                    <li>✓ Envío gratis</li>
                    <li>✓ 10% de descuento</li>
                    <li>✓ Soporte por email</li>
                </ul>
                <button class="btn-plan" onclick="selectPlan('Básico', 400)">Seleccionar Plan</button>
            </div>

            <!-- Plan Premium (Destacado) -->
            <div class="plan-card destacado">
                <div class="plan-badge">Más Popular</div>
                <div class="plan-header">
                    <h3>Plan Premium</h3>
                    <div class="plan-icon">🐕🐈</div>
                </div>
                <div class="plan-precio">
                    <span class="precio-grande">$700</span>
                    <span class="precio-periodo">/mes</span>
                </div>
                <ul class="plan-beneficios">
                    <li>✓ 2 bolsas de 15kg al mes</li>
                    <li>✓ Envío gratis prioritario</li>
                    <li>✓ 20% de descuento</li>
                    <li>✓ Snacks gratis</li>
                    <li>✓ Soporte 24/7</li>
                    <li>✓ Cambio de sabor gratis</li>
                </ul>
                <button class="btn-plan premium" onclick="selectPlan('Premium', 700)">Seleccionar Plan</button>
            </div>

            <!-- Plan Familia -->
            <div class="plan-card">
                <div class="plan-header">
                    <h3>Plan Familia</h3>
                    <div class="plan-icon">🐕🐕🐈</div>
                </div>
                <div class="plan-precio">
                    <span class="precio-grande">$1,000</span>
                    <span class="precio-periodo">/mes</span>
                </div>
                <ul class="plan-beneficios">
                    <li>✓ 3 bolsas de 15kg al mes</li>
                    <li>✓ Envío gratis express</li>
                    <li>✓ 25% de descuento</li>
                    <li>✓ Snacks premium gratis</li>
                    <li>✓ Soporte VIP 24/7</li>
                    <li>✓ Consulta veterinaria gratis</li>
                </ul>
                <button class="btn-plan" onclick="selectPlan('Familia', 1000)">Seleccionar Plan</button>
            </div>
        </div>
    </section>

    <!-- Testimonios -->
    <section class="testimonios">
        <h2>Lo que dicen nuestros clientes</h2>
        <div class="testimonios-grid">
            <div class="testimonio-card">
                <div class="stars">⭐⭐⭐⭐⭐</div>
                <p>"Mi perro Max está más saludable que nunca. El servicio de suscripción es muy conveniente."</p>
                <div class="autor">- María González</div>
            </div>
            <div class="testimonio-card">
                <div class="stars">⭐⭐⭐⭐⭐</div>
                <p>"Excelente calidad y precio. La entrega siempre es puntual. 100% recomendado."</p>
                <div class="autor">- Carlos Ramírez</div>
            </div>
            <div class="testimonio-card">
                <div class="stars">⭐⭐⭐⭐⭐</div>
                <p>"Mis gatos aman la comida. El plan premium vale totalmente la pena."</p>
                <div class="autor">- Ana Martínez</div>
            </div>
        </div>
    </section>

    <!-- Contacto -->
    <section id="contacto" class="contacto">
        <h2>Contáctanos</h2>
        <div class="contacto-container">
            <div class="contacto-info">
                <h3>Estamos aquí para ayudarte</h3>
                <div class="info-item">
                    <span class="icon">📧</span>
                    <span>info@petcareshop.com</span>
                </div>
                <div class="info-item">
                    <span class="icon">📱</span>
                    <span>+52 961 123 4567</span>
                </div>
                <div class="info-item">
                    <span class="icon">📍</span>
                    <span>Tuxtla Gutiérrez, Chiapas, MX</span>
                </div>
                <div class="info-item">
                    <span class="icon">🕐</span>
                    <span>Lun - Vie: 9:00 AM - 6:00 PM</span>
                </div>
            </div>
            <form class="contacto-form" onsubmit="submitForm(event)">
                <input type="text" placeholder="Tu nombre" required>
                <input type="email" placeholder="Tu email" required>
                <input type="tel" placeholder="Teléfono">
                <textarea placeholder="Tu mensaje" rows="5" required></textarea>
                <button type="submit" class="btn-primary">Enviar Mensaje</button>
            </form>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <div class="footer-content">
            <div class="footer-section">
                <h4>🐾 PetCare Shop</h4>
                <p>Alimenta a tu mascota con amor desde 2024</p>
            </div>
            <div class="footer-section">
                <h4>Enlaces Rápidos</h4>
                <ul>
                    <li><a href="#inicio">Inicio</a></li>
                    <li><a href="#productos">Productos</a></li>
                    <li><a href="#suscripcion">Suscripción</a></li>
                    <li><a href="#contacto">Contacto</a></li>
                </ul>
            </div>
            <div class="footer-section">
                <h4>Síguenos</h4>
                <div class="social-links">
                    <a href="#">📘 Facebook</a>
                    <a href="#">📷 Instagram</a>
                    <a href="#">🐦 Twitter</a>
                </div>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2026 PetCare Shop. Todos los derechos reservados.</p>
        </div>
    </footer>

    <script src="js/script.js"></script>
</body>
</html>
EOF
