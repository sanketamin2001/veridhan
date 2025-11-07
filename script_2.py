
# 2. Update index.html with AI mentions, SEO meta tags, and LinkedIn link
index_updated = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Veridhan Research & Advisory | Investment Research & Advisory Firm</title>
    <meta name="description" content="Investment research & advisory firm focused on clarity, ethics, and client-first perspective. Launching in 2026 after SEBI registration.">
    
    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://veridhan.in">
    <meta property="og:title" content="Veridhan Research & Advisory | Investment Research & Advisory Firm">
    <meta property="og:description" content="Investment research & advisory firm focused on clarity, ethics, and client-first perspective. Launching in 2026 after SEBI registration.">
    <meta property="og:image" content="https://veridhan.in/assets/og-preview.png">
    
    <!-- Twitter -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:url" content="https://veridhan.in">
    <meta name="twitter:title" content="Veridhan Research & Advisory | Investment Research & Advisory Firm">
    <meta name="twitter:description" content="Investment research & advisory firm focused on clarity, ethics, and client-first perspective. Launching in 2026 after SEBI registration.">
    <meta name="twitter:image" content="https://veridhan.in/assets/og-preview.png">
    
    <!-- Favicon -->
    <link rel="icon" type="image/png" sizes="32x32" href="favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="favicon-16x16.png">
    <link rel="shortcut icon" href="favicon.ico">
    
    <link rel="stylesheet" href="styles.css">
</head>
<body>
<div class="container">
    <nav class="nav">
        <div class="logo">
            <div class="logo-mark">V</div>
            Veridhan Research & Advisory LLP
        </div>
        <div>
            <a href="index.html">Home</a>
            <a href="about.html">About</a>
            <a href="services.html">Services</a>
            <a href="technology.html">Technology</a>
            <a href="contact.html">Contact</a>
            <a href="disclaimer.html">Disclaimer</a>
        </div>
    </nav>

    <div class="notice">
        <strong>🚀 AI-Powered Research Coming Soon:</strong> We're developing advanced AI technology to enhance research quality and insights. All tools will launch post-SEBI compliance in 2026. <a href="technology.html" style="text-decoration: underline;">Learn more →</a>
    </div>

    <section class="hero">
        <div>
            <h1 class="h1">Research-First. Client-First. Future-Ready.</h1>
            <p class="p">
                We combine disciplined research with a long-term view. Veridhan Research & Advisory LLP is preparing for SEBI registration and will open to clients in <strong>2026</strong>.
            </p>
            <p class="p">
                Our upcoming <strong>AI-powered research engine</strong> will augment human expertise with cutting-edge technology to deliver deeper insights, smarter analysis, and better investment decisions.
            </p>
            <div class="btns">
                <a href="services.html" class="btn primary">Our Services</a>
                <a href="technology.html" class="btn">AI Technology</a>
                <a href="about.html" class="btn">About Us</a>
            </div>
        </div>
        <div class="card pad">
            <div class="kv">
                <span class="badge">Status</span>
                <span>SEBI Registration In Progress</span>
            </div>
            <div class="kv">
                <span class="badge">Launch</span>
                <span>2026</span>
            </div>
            <div class="kv">
                <span class="badge">Location</span>
                <span>Anand, Gujarat</span>
            </div>
        </div>
    </section>

    <section class="section">
        <h2 style="font-size:28px;margin-bottom:16px;">What We Offer</h2>
        <div class="grid grid-3">
            <div class="card pad">
                <h3 style="font-size:20px;margin-bottom:8px;">💼 Advisory Services</h3>
                <p class="p" style="font-size:15px;">
                    Goal-aligned advice focused on risk management and transparent processes. Services available post-SEBI authorization.
                </p>
            </div>
            <div class="card pad">
                <h3 style="font-size:20px;margin-bottom:8px;">🔍 Research Solutions</h3>
                <p class="p" style="font-size:15px;">
                    Independent equity & market research, frameworks, and insights designed to reduce noise and improve clarity.
                </p>
            </div>
            <div class="card pad">
                <h3 style="font-size:20px;margin-bottom:8px;">🎓 Education & Literacy</h3>
                <p class="p" style="font-size:15px;">
                    Workshops and resources to build financial literacy. Educational content may be published ahead of launch.
                </p>
            </div>
        </div>
    </section>

    <section class="section">
        <h2 style="font-size:28px;margin-bottom:16px;">AI-Enhanced Research Capabilities</h2>
        <div class="card pad">
            <p class="p">
                Veridhan is building proprietary <strong>AI research technology</strong> to complement human analysis and deliver superior insights. Our platform will feature:
            </p>
            <ul class="clean" style="margin-top: 12px;">
                <li class="tile">🧠 <strong>Intelligent document analysis</strong> for faster processing of financial statements and reports</li>
                <li class="tile">📊 <strong>Quantitative screening tools</strong> powered by machine learning algorithms</li>
                <li class="tile">📈 <strong>Market sentiment analysis</strong> from news, social media, and alternative data</li>
                <li class="tile">⚡ <strong>Real-time alerts</strong> for portfolio-relevant events and opportunities</li>
            </ul>
            <p class="p" style="margin-top: 16px;">
                <strong>Note:</strong> AI tools will be launched only after SEBI registration and regulatory approvals. <a href="technology.html" style="text-decoration: underline;">Explore our technology roadmap →</a>
            </p>
        </div>
    </section>

    <section class="section">
        <div class="notice">
            <strong>📋 Regulatory Notice:</strong> Operations have <strong>not started yet</strong>. SEBI registration is currently in process. The company expects to commence services in <strong>2026</strong>.
        </div>
    </section>

    <footer class="footer">
        © 2025 Veridhan Research & Advisory LLP. All rights reserved.<br>
        Registered address: 35A, Vaishnav Parivar, near Nehru Baugh, Anand 388001 • Phone: +91 8460902001
    </footer>
</div>
</body>
</html>"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_updated)

print("✅ Updated index.html")
