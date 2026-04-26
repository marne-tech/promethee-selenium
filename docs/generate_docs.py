import os

template = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Promethee-Selenium</title>
    <link rel="stylesheet" href="styles.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <!-- Font Awesome for icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>

<body>

    <header class="top-header">
        <div class="header-left">
            <a href="index.html" class="logo-container">
                <i class="fa-solid fa-fire logo-icon"></i>
                <span class="logo-text">Promethee<span class="logo-highlight">Selenium</span></span>
            </a>
        </div>
        <nav class="header-middle">
            <a href="#" class="nav-link">Product</a>
            <a href="#" class="nav-link">Features <i class="fa-solid fa-chevron-down nav-chevron"></i></a>
            <a href="#" class="nav-link">Github</a>
            <a href="#" class="nav-link">PyPI</a>
            <a href="#" class="nav-link">Resources <i class="fa-solid fa-chevron-down nav-chevron"></i></a>
        </nav>
        <div class="header-right">
            <a href="#install" class="btn-download"><i class="fa-solid fa-download"></i> Download <i
                    class="fa-solid fa-chevron-down btn-chevron"></i></a>
        </div>
    </header>

    <div class="main-container">
        <aside class="left-sidebar">
            <div class="sidebar-section">
                <h3 class="section-title">Home <i class="fa-solid fa-chevron-up"></i></h3>
                <ul class="nav-list">
                    <li><a href="index.html" class="nav-item">Getting Started</a></li>
                </ul>
            </div>

            <div class="sidebar-section">
                <h3 class="section-title">Core Library <i class="fa-solid fa-chevron-up"></i></h3>
                <ul class="nav-list">
                    <li><a href="page-object-model.html" class="nav-item{pom_active}">Page Object Model</a></li>
                    <li><a href="scaffolding.html" class="nav-item{scaff_active}">Scaffolding</a></li>
                    <li><a href="built-in-utilities.html" class="nav-item{bu_active}">Built-in Utilities</a></li>
                    <li><a href="environment-mgmt.html" class="nav-item{env_active}">Environment Mgmt</a></li>
                    <li><a href="bilingual-support.html" class="nav-item{bi_active}">Bilingual Support</a></li>
                </ul>
            </div>

            <div class="sidebar-section">
                <h3 class="section-title">CLI Commands <i class="fa-solid fa-chevron-down"></i></h3>
                <ul class="nav-list" style="display: none;">
                    <li><a href="#" class="nav-item">init</a></li>
                    <li><a href="#" class="nav-item">docs</a></li>
                </ul>
            </div>
        </aside>

        <main class="content-area">
            <div class="breadcrumbs">
                <span class="breadcrumb-item">Promethee-Selenium</span>
                <span class="breadcrumb-separator"><i class="fa-solid fa-chevron-right"></i></span>
                <span class="breadcrumb-item">Core Library</span>
                <span class="breadcrumb-separator"><i class="fa-solid fa-chevron-right"></i></span>
                <span class="breadcrumb-item current-page">{title}</span>
            </div>

            {main_content}
        </main>

        <aside class="right-sidebar">
            <div class="toc-container">
                <h4 class="toc-title">On this Page</h4>
                <div class="toc-line"></div>
                <ul class="toc-list">
                    {toc_content}
                </ul>
            </div>
        </aside>
    </div>

    <script src="script.js"></script>
</body>

</html>"""

pages = [
    {
        "filename": "page-object-model.html",
        "title": "Page Object Model",
        "active": "pom",
        "main_content": """<article class="document-content">
                <h1 class="page-title">Page Object Model (POM)</h1>
                <p class="intro-text">
                    The <strong>Page Object Model</strong> is a design pattern that creates an object repository for storing all web elements. Promethee-Selenium natively builds on this to reduce code duplication and improve test maintenance.
                </p>

                <h2 id="concept">🧠 The Concept</h2>
                <p>For each UI page of an application, a corresponding page class is created. This page class is responsible for finding the WebElements of that page and executing operations on them.</p>

                <h2 id="implementation">🛠️ Implementation</h2>
                <p>To implement your own page object, inherit from our <code>Base</code> class available in Promethee.</p>

                <h3 id="example">Example</h3>
                <div class="code-block">
                    <button class="copy-btn"><i class="fa-regular fa-copy"></i></button>
                    <code class="language-python">from promethee.core.base import Base
from selenium.webdriver.common.by import By

class LoginPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        
    def login(self, username, password):
        self.type_text(self.username_input, username)
        self.type_text(self.password_input, password)
        self.click_element(self.login_button)
</code>
                </div>

                <h2 id="benefits">📈 Benefits</h2>
                <ul>
                    <li><strong>Maintainability</strong>: Update the locator in the page class instead of replacing it in every test.</li>
                    <li><strong>Reusability</strong>: Write the code once to get the element or perform an action, and use it across multiple scripts.</li>
                    <li><strong>Readability</strong>: Test scripts read more like actual user scenarios.</li>
                </ul>
            </article>""",
        "toc_content": """<li><a href="#concept" class="toc-link">The Concept</a></li>
                    <li><a href="#implementation" class="toc-link">Implementation</a></li>
                    <li><a href="#example" class="toc-link">Example</a></li>
                    <li><a href="#benefits" class="toc-link">Benefits</a></li>"""
    },
    {
        "filename": "scaffolding.html",
        "title": "Scaffolding",
        "active": "scaff",
        "main_content": """<article class="document-content">
                <h1 class="page-title">Scaffolding</h1>
                <p class="intro-text">
                    Promethee-Selenium comes with powerful <strong>scaffolding</strong> capabilities, enabling you to bootstrap a complete automation project structure with a single CLI command.
                </p>

                <h2 id="init-command">The Init Command</h2>
                <p>To initialize a new project, navigate to your desired directory and run:</p>
                <div class="code-block">
                    <button class="copy-btn"><i class="fa-regular fa-copy"></i></button>
                    <code class="language-bash">promethee-selenium init</code>
                </div>

                <h2 id="directory-structure">Standard Structure</h2>
                <p>The CLI populates your directory with best-practices architecture tailored for Selenium and Pytest:</p>
                
                <div class="code-block">
                    <button class="copy-btn"><i class="fa-regular fa-copy"></i></button>
                    <code class="language-plaintext">.
├── conftest.py
├── data/
│   └── test_data.csv
├── scenarios/
│   └── login_page.py
├── tests/
│   └── test_login.py
└── utils/
    └── browser_factory.py</code>
                </div>

                <h3 id="breakdown">Directory Breakdown</h3>
                <ul>
                    <li><strong>scenarios/</strong>: Contains all your Page Object Model schemas. Locators and actions defining UI structures go here.</li>
                    <li><strong>tests/</strong>: Pytest test scripts (e.g. <code>test_login.py</code>) running your assertions via the scenario layer.</li>
                    <li><strong>data/</strong>: Static files, configs, and raw test data.</li>
                    <li><strong>utils/</strong>: Auxiliary logic, external bridges, API clients, reporting plugins.</li>
                    <li><strong>conftest.py</strong>: Pytest entry point containing the fixtures.</li>
                </ul>
            </article>""",
        "toc_content": """<li><a href="#init-command" class="toc-link">The Init Command</a></li>
                    <li><a href="#directory-structure" class="toc-link">Standard Structure</a></li>
                    <li><a href="#breakdown" class="toc-link">Directory Breakdown</a></li>"""
    },
    {
        "filename": "built-in-utilities.html",
        "title": "Built-in Utilities",
        "active": "bu",
        "main_content": """<article class="document-content">
                <h1 class="page-title">Built-in Utilities</h1>
                <p class="intro-text">
                    Speed up your development cycle with a curated set of <strong>robust utilities</strong> included in the <code>Base</code> class, pre-configured with explicit waits and reliable DOM interactions.
                </p>

                <h2 id="core-methods">⚡ Core Methods</h2>
                <p>Here are some of the most frequently used functions provided natively:</p>

                <h3 id="clicking">Clicking Elements</h3>
                <p>Waits for an element to be clickable before performing the action:</p>
                <div class="code-block">
                    <button class="copy-btn"><i class="fa-regular fa-copy"></i></button>
                    <code class="language-python">self.click_element((By.ID, "submit-btn"), timeout=10)</code>
                </div>

                <h3 id="typing">Typing Text</h3>
                <p>Clears the field and enters text after ensuring the input element is ready:</p>
                <div class="code-block">
                    <button class="copy-btn"><i class="fa-regular fa-copy"></i></button>
                    <code class="language-python">self.type_text((By.NAME, "email"), "user@example.com")</code>
                </div>

                <h3 id="assertions">Assertions &amp; Verification</h3>
                <p>Quick checks to synchronize automation flows securely:</p>
                <div class="code-block">
                    <button class="copy-btn"><i class="fa-regular fa-copy"></i></button>
                    <code class="language-python">is_visible = self.is_element_visible((By.CLASS_NAME, "success-msg"))
text_content = self.get_element_text((By.XPATH, "//header/h1"))</code>
                </div>

                <h2 id="waits">⏳ Advanced Waiting</h2>
                <p>Selenium can be flaky; Promethee\'s utilities wrap standard WebDriverWaits efficiently to prevent stale elements and synchronization bugs.</p>
            </article>""",
        "toc_content": """<li>
                        <a href="#core-methods" class="toc-link">Core Methods</a>
                        <ul class="toc-sublist">
                            <li><a href="#clicking" class="toc-link sub-link">Clicking</a></li>
                            <li><a href="#typing" class="toc-link sub-link">Typing</a></li>
                            <li><a href="#assertions" class="toc-link sub-link">Assertions</a></li>
                        </ul>
                    </li>
                    <li><a href="#waits" class="toc-link">Advanced Waiting</a></li>"""
    },
    {
        "filename": "environment-mgmt.html",
        "title": "Environment Management",
        "active": "env",
        "main_content": """<article class="document-content">
                <h1 class="page-title">Environment Mgmt</h1>
                <p class="intro-text">
                    Handle multile stages of delivery effortlessly. The <strong>Environment Management</strong> features let you run the same test suite cleanly against Local, Dev, Staging, and Production layers.
                </p>

                <h2 id="configuration">The configuration pattern</h2>
                <p>Manage environments via dynamic fixtures and JSON mappings. Centralize your URLs and keys under one structure.</p>
                
                <div class="code-block">
                    <button class="copy-btn"><i class="fa-regular fa-copy"></i></button>
                    <code class="language-json">{
  "dev": {
    "url": "https://dev.example.com"
  },
  "staging": {
    "url": "https://staging.example.com"
  }
}</code>
                </div>

                <h2 id="cli-options">Pass via CLI</h2>
                <p>Switching environment happens right at the pytest invocation level, ensuring absolute isolation:</p>

                <div class="code-block">
                    <button class="copy-btn"><i class="fa-regular fa-copy"></i></button>
                    <code class="language-bash">pytest tests/ --env staging</code>
                </div>
            </article>""",
        "toc_content": """<li><a href="#configuration" class="toc-link">The Configuration Pattern</a></li>
                    <li><a href="#cli-options" class="toc-link">Pass via CLI</a></li>"""
    },
    {
        "filename": "bilingual-support.html",
        "title": "Bilingual Support",
        "active": "bi",
        "main_content": """<article class="document-content">
                <h1 class="page-title">Bilingual Support</h1>
                <p class="intro-text">
                    Promethee-Selenium breaks down language barriers. Enjoy complete framework interactions, documentation, and error handling natively in both <strong>English</strong> and <strong>French</strong>.
                </p>

                <h2 id="cli">In the CLI</h2>
                <p>When you start the interactive CLI using <code>promethee-selenium</code>, the very first prompt will ask you to select your preferred language interaction. Every menu options, confirmation messages, and hints automatically translates to match your preference.</p>
                
                <h3 id="example-cli">CLI Demonstration</h3>
                <div class="code-block">
                    <button class="copy-btn"><i class="fa-regular fa-copy"></i></button>
                    <code class="language-bash">? Select Language / Choisissez la langue: 
  English
❯ Français</code>
                </div>

                <h2 id="documentation">In the Documentation</h2>
                <p>Along with English, full French guides are continuously updated, ensuring that teams from diverse linguistic backgrounds achieve absolute clarity over the implementation structure.</p>
            </article>""",
        "toc_content": """<li><a href="#cli" class="toc-link">In the CLI</a></li>
                    <li><a href="#example-cli" class="toc-link">CLI Demonstration</a></li>
                    <li><a href="#documentation" class="toc-link">In the Documentation</a></li>"""
    }
]

for page in pages:
    kwargs = {
        "title": page["title"],
        "main_content": page["main_content"],
        "toc_content": page["toc_content"],
        "pom_active": " active" if page["active"] == "pom" else "",
        "scaff_active": " active" if page["active"] == "scaff" else "",
        "bu_active": " active" if page["active"] == "bu" else "",
        "env_active": " active" if page["active"] == "env" else "",
        "bi_active": " active" if page["active"] == "bi" else ""
    }
    html = template.format(**kwargs)
    with open(f"/Users/Hugotestas/Automated_tests_ui_framework/docs_website/{page['filename']}", "w") as f:
        f.write(html)
