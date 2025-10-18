
# I'll create a complete, production-ready HTML/CSS/JS website replicating the Aidoc design
# This will be a modern, responsive single-page website with all the sections

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AIUnic | Clinical AI Solutions for Healthcare Providers</title>
    <link rel="stylesheet" href="styles.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
</head>
<body>
    <!-- Navigation Header -->
    <header class="navbar">
        <div class="container">
            <div class="nav-wrapper">
                <div class="logo">
                    <h1>AIUnic</h1>
                </div>
                <nav class="nav-menu">
                    <ul>
                        <li><a href="#learn">Learn</a></li>
                        <li><a href="#solutions">Solutions</a></li>
                        <li><a href="#platform">Platform</a></li>
                        <li><a href="#healthcare-ai">Healthcare AI</a></li>
                    </ul>
                </nav>
                <button class="menu-toggle" id="menuToggle">
                    <span></span>
                    <span></span>
                    <span></span>
                </button>
            </div>
        </div>
    </header>

    <!-- Mobile Menu -->
    <div class="mobile-menu" id="mobileMenu">
        <ul>
            <li><a href="#learn">Learn</a></li>
            <li><a href="#solutions">Solutions</a></li>
            <li><a href="#platform">Platform</a></li>
            <li><a href="#healthcare-ai">Healthcare AI</a></li>
        </ul>
    </div>

    <!-- Hero Section -->
    <section class="hero">
        <div class="container">
            <div class="hero-content">
                <h1 class="hero-title">AIUnic AI is always on, running in the background to change the foreground</h1>
                <p class="hero-subtitle">Empowering healthcare teams to optimize patient treatment</p>
                <button class="cta-button">Get Started</button>
            </div>
        </div>
        <div class="hero-overlay"></div>
    </section>

    <!-- Platform Section -->
    <section class="platform-section" id="platform">
        <div class="container">
            <div class="platform-content">
                <h2>The aiOS™ tackles the challenges of a fragmented healthcare system</h2>
                <p>Creating a unified healthcare AI platform that improves workflows, data accuracy and overall patient care.</p>
                <button class="explore-button">EXPLORE THE aiOS™</button>
            </div>
        </div>
    </section>

    <!-- Coverage Section -->
    <section class="coverage-section">
        <div class="container">
            <div class="coverage-content">
                <h2>AIUnic's clinical AI solutions <strong>cover 75% of patients in your health system</strong></h2>
                <p>Connecting care teams across specialties and departments, unifying a patient's journey.</p>
            </div>
        </div>
    </section>

    <!-- Solutions Grid -->
    <section class="solutions-section" id="solutions">
        <div class="container">
            <div class="solutions-grid">
                <div class="solution-card">
                    <div class="solution-icon">
                        <svg viewBox="0 0 64 64" width="48" height="48">
                            <circle cx="32" cy="32" r="30" fill="none" stroke="currentColor" stroke-width="2"/>
                            <path d="M32 12 L32 52 M12 32 L52 32" stroke="currentColor" stroke-width="2"/>
                        </svg>
                    </div>
                    <h3>Medical Imaging</h3>
                    <p>Automatically analyze medical imaging to streamline workflows, prioritize findings, activate care teams and facilitate patient follow-up.</p>
                </div>

                <div class="solution-card">
                    <div class="solution-icon">
                        <svg viewBox="0 0 64 64" width="48" height="48">
                            <path d="M32 12 C18 12 12 20 12 32 C12 44 18 52 32 52 C46 52 52 44 52 32 C52 20 46 12 32 12 Z" fill="none" stroke="currentColor" stroke-width="2"/>
                            <path d="M22 28 L28 34 L42 22" fill="none" stroke="currentColor" stroke-width="2"/>
                        </svg>
                    </div>
                    <h3>Cardiac Care</h3>
                    <p>Enhance cardiac care with imaging and text-based AI insights to automatically – and consistently – measure disease and capture the incidental findings you want to see.</p>
                </div>

                <div class="solution-card">
                    <div class="solution-icon">
                        <svg viewBox="0 0 64 64" width="48" height="48">
                            <circle cx="32" cy="24" r="8" fill="none" stroke="currentColor" stroke-width="2"/>
                            <path d="M20 44 C20 36 25 32 32 32 C39 32 44 36 44 44 L44 52 L20 52 Z" fill="none" stroke="currentColor" stroke-width="2"/>
                        </svg>
                    </div>
                    <h3>Neurology</h3>
                    <p>High performing algorithms for stroke, hemorrhage, c-spine fracture and brain aneurysm paired with care coordination tools with real time notification and clinical context from EHR.</p>
                </div>

                <div class="solution-card">
                    <div class="solution-icon">
                        <svg viewBox="0 0 64 64" width="48" height="48">
                            <rect x="16" y="12" width="32" height="40" rx="4" fill="none" stroke="currentColor" stroke-width="2"/>
                            <line x1="24" y1="22" x2="40" y2="22" stroke="currentColor" stroke-width="2"/>
                            <line x1="24" y1="30" x2="40" y2="30" stroke="currentColor" stroke-width="2"/>
                            <line x1="24" y1="38" x2="32" y2="38" stroke="currentColor" stroke-width="2"/>
                        </svg>
                    </div>
                    <h3>Vascular</h3>
                    <p>Streamline workflows, enhance care coordination and centralize patient management for aortic diseases, pulmonary embolism, deep vein thrombosis and IVC filters.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- About Section -->
    <section class="about-section">
        <div class="container">
            <div class="about-content">
                <h2>AIUnic empowers healthcare teams to optimize patient treatment</h2>
                <p>Resulting in improved economic value and clinical outcomes. Powered by our exclusive aiOS™, we analyze and aggregate medical data to enable care teams to operationalize the unexpected and work seamlessly with a continued focus on the patient. AIUnic AI is always on, running in the background to change the foreground.</p>
            </div>
        </div>
    </section>

    <!-- Stats Section -->
    <section class="stats-section">
        <div class="container">
            <div class="stats-grid">
                <div class="stat-item">
                    <div class="stat-number" data-target="1000">0</div>
                    <div class="stat-suffix">+</div>
                    <div class="stat-label">medical centers with AIUnic solutions</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number" data-target="75">0</div>
                    <div class="stat-suffix">%</div>
                    <div class="stat-label">of employees in AI and software engineering</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number" data-target="2000000">0</div>
                    <div class="stat-suffix"></div>
                    <div class="stat-label">patients analyzed each month</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number" data-target="150">0</div>
                    <div class="stat-suffix">+</div>
                    <div class="stat-label">clinical studies illustrating value</div>
                </div>
                <div class="stat-item">
                    <div class="stat-prefix">$</div>
                    <div class="stat-number" data-target="50">0</div>
                    <div class="stat-suffix">M</div>
                    <div class="stat-label">annual net contribution potential from enterprise solution*</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number" data-target="15">0</div>
                    <div class="stat-suffix"></div>
                    <div class="stat-label">market leading FDA clearances</div>
                </div>
            </div>
        </div>
    </section>

    <!-- Resources Section -->
    <section class="resources-section" id="learn">
        <div class="container">
            <div class="resources-grid">
                <div class="resource-card">
                    <h3>Implementation Resources</h3>
                    <p>Navigate AI implementation with resources, workshops and training that guide health systems on the journey to harness AI's full potential.</p>
                    <a href="#" class="resource-link">Learn More →</a>
                </div>
                <div class="resource-card">
                    <h3>AI Strategy</h3>
                    <p>Go beyond the algorithm to develop a scalable AI strategy and governance plan with insights from leading healthcare executives.</p>
                    <a href="#" class="resource-link">Learn More →</a>
                </div>
                <div class="resource-card">
                    <h3>News & Updates</h3>
                    <p>Get updates on what AIUnic is doing and discovering, as we bring better care across the continuum of health.</p>
                    <a href="#" class="resource-link">Learn More →</a>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-info">
                    <p>© Copyright 2025 AIUnic</p>
                    <p class="footer-disclaimer">*This is an example calculation assuming a 1k bed health system with 25% net contribution margin. Payor mix of private/self pay/other 67%; Medicare/Medicaid 28%; and no pay 5%. To understand the potential ROI for your facility, please reach out to AIUnic to understand how we can provide a customized calculation for you.</p>
                </div>
            </div>
        </div>
    </footer>

    <script src="script.js"></script>
</body>
</html>"""

# Save HTML file
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("✓ index.html created successfully")
