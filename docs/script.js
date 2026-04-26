document.addEventListener('DOMContentLoaded', () => {
    const sectionTitles = document.querySelectorAll('.section-title');

    sectionTitles.forEach(title => {
        title.addEventListener('click', () => {
            const navList = title.nextElementSibling;
            const icon = title.querySelector('i');

            if (navList && navList.classList.contains('nav-list')) {
                const isClosed = window.getComputedStyle(navList).display === 'none';

                if (isClosed) {
                    navList.style.display = 'block';
                    if (icon) {
                        icon.classList.remove('fa-chevron-down');
                        icon.classList.add('fa-chevron-up');
                    }
                } else {
                    navList.style.display = 'none';
                    if (icon) {
                        icon.classList.remove('fa-chevron-up');
                        icon.classList.add('fa-chevron-down');
                    }
                }
            }
        });
    });

    // Language toggle
    const translations = {
        'header.features': { en: 'Features', fr: 'Fonctionnalités' },
        'header.installation': { en: 'Installation', fr: 'Installation' },
        'header.quickStart': { en: 'Quick Start', fr: 'Démarrage rapide' },
        'header.download': { en: 'Download', fr: 'Télécharger' },

        'sidebar.home': { en: 'Home', fr: 'Accueil' },
        'sidebar.coreLibrary': { en: 'Core Library', fr: 'Bibliothèque principale' },
        'sidebar.pageObjectModel': { en: 'Page Object Model', fr: 'Modèle Page Object' },
        'sidebar.scaffolding': { en: 'Scaffolding', fr: 'Génération' },
        'sidebar.builtInUtilities': { en: 'Built-in Utilities', fr: 'Utilitaires intégrés' },
        'sidebar.environmentMgmt': { en: 'Environment Mgmt', fr: 'Gestion des environnements' },
        'sidebar.bilingualSupport': { en: 'Bilingual Support', fr: 'Support bilingue' },
        'sidebar.cliCommands': { en: 'CLI Commands', fr: 'Commandes CLI' },
        'sidebar.gettingStarted': { en: 'Getting Started', fr: 'Prise en main' },
        'sidebar.init': { en: 'init', fr: 'init' },
        'sidebar.docs': { en: 'docs', fr: 'docs' },

        'page.gettingStarted.title': { en: 'Getting Started', fr: 'Prise en main' },
        'page.gettingStarted.intro': { en: '<strong>Promethee-Selenium</strong> is a robust, Page Object Model (POM) based library for automated UI testing using Selenium and Pytest. It is designed to streamline your end-to-end testing workflow by providing a structured architecture, ensuring your tests are maintainable, scalable, and easy to read.', fr: '<strong>Promethee-Selenium</strong> est une bibliothèque robuste basée sur le pattern, Page Object Model (POM) pour les tests UI automatisés avec Selenium, Pytest et Selenium-ui-test-tool. Elle simplifie les workflows E2E en fournissant une architecture structurée.' },
        'page.gettingStarted.featuresTitle': { en: 'Features', fr: 'Fonctionnalités' },
        'page.gettingStarted.features.li1': { en: 'Page Object Model (POM): Enforces a clean separation between page interactions (locators, actions) and test logic (assertions, workflows).', fr: 'Page Object Model (POM) : Imposer une séparation claire entre les interactions de page (locators, actions) et la logique des tests (assertions, workflows).' },
        'page.gettingStarted.features.li2': { en: 'Interactive CLI: A user-friendly command-line interface to guide you through project initialization and documentation.', fr: 'CLI interactive : Une interface en ligne de commande conviviale pour guider l\'initialisation du projet et la documentation.' },
        'page.gettingStarted.features.li3': { en: 'Scaffolding: Quickly generate a production-ready project structure with promethee-selenium init.', fr: 'Génération (Scaffolding) : Générez rapidement une structure de projet prête pour la production avec promethee-selenium init.' },
        'page.gettingStarted.features.li4': { en: 'Built-in Utilities: A rich set of helper functions for common Selenium actions (clicking, typing, waiting).', fr: 'Utilitaires intégrés : Un ensemble de fonctions d\'aide pour les actions Selenium courantes (clic, saisie, attentes).' },
        'page.gettingStarted.features.li5': { en: 'Environment Management: Native support for managing test environments and credentials securely.', fr: 'Gestion des environnements : Support natif pour gérer les environnements de test et les credentials en toute sécurité.' },
        'page.gettingStarted.features.li6': { en: 'Bilingual Support: The CLI and documentation are available in both English and French.', fr: 'Support bilingue : Le CLI et la documentation sont disponibles en anglais et en français.' },
        'page.gettingStarted.installationTitle': { en: 'Installation', fr: 'Installation' },
        'page.gettingStarted.installationText': { en: 'Install the package easily via pip:', fr: 'Installez le package facilement via pip :' },
        'page.gettingStarted.quickStartTitle': { en: 'Quick Start', fr: 'Démarrage rapide' },
        'page.gettingStarted.step1Title': { en: '1. Launch the CLI', fr: '1. Lancer le CLI' },
        'page.gettingStarted.step1Text': { en: 'After installation, run the following command to access the interactive menu:', fr: 'Après l\'installation, exécutez la commande suivante pour accéder au menu interactif :' },
        'page.gettingStarted.step1Note': { en: 'You will be prompted to select your language (English/French) and then choose an action.', fr: 'Vous serez invité à choisir votre langue (Anglais/Français) puis à sélectionner une action.' },
        'page.gettingStarted.step2Title': { en: '2. Initialize a Project', fr: '2. Initialiser un projet' },
        'page.gettingStarted.step2Text': { en: 'Select the Init option from the menu or run:', fr: 'Sélectionnez l\'option Init depuis le menu ou exécutez :' },
        'page.gettingStarted.step2Note': { en: 'This creates a standard directory layout:', fr: 'Ceci crée une structure de répertoires standard :' },
        'page.gettingStarted.step3Title': { en: '3. Run Your Tests', fr: '3. Exécuter vos tests' },
        'page.gettingStarted.step3Text': { en: 'Execute your tests using pytest:', fr: 'Exécutez vos tests avec pytest :' },
        'toc.onThisPage': { en: 'On this Page', fr: 'Sur cette page' },

        // Page Object Model
        'page.pom.title': { en: 'Page Object Model (POM)', fr: 'Modèle Page Object (POM)' },
        'page.pom.intro': { en: 'The Page Object Model is a design pattern that creates an object repository for storing all web elements.', fr: 'Le Modèle Page Object est un patron de conception qui crée un répertoire d\'objets pour stocker tous les éléments web.' },
        'page.pom.concept': { en: 'The Concept', fr: 'Le Concept' },
        'page.pom.implementation': { en: 'Implementation', fr: 'Implémentation' },
        'page.pom.conceptText': { en: 'For each UI page of an application, a corresponding page class is created. This page class is responsible for finding the WebElements of that page and executing operations on them.', fr: 'Pour chaque page UI d\'une application, une classe de page correspondante est créée. Cette classe est responsable de trouver les WebElements et d\'exécuter les opérations.' },
        'page.pom.implementationText': { en: 'To implement your own page object, inherit from our Base class available in Promethee.', fr: 'Pour implémenter votre propre page object, héritez de la classe Base fournie par Promethee.' },
        'page.pom.benefits.li1': { en: 'Maintainability: Update the locator in the page class instead of replacing it in every test.', fr: 'Maintenabilité : Mettez à jour le locator dans la classe de page au lieu de modifier chaque test.' },
        'page.pom.benefits.li2': { en: 'Reusability: Write the code once to get the element or perform an action, and use it across multiple scripts.', fr: 'Réutilisabilité : Écrivez le code une fois et réutilisez-le dans plusieurs scripts.' },
        'page.pom.benefits.li3': { en: 'Readability: Test scripts read more like actual user scenarios.', fr: 'Lisibilité : Les scripts de test se lisent comme de vrais scénarios utilisateurs.' },
        'page.pom.example': { en: 'Example', fr: 'Exemple' },
        'page.pom.benefits': { en: 'Benefits', fr: 'Avantages' },

        // Scaffolding
        'page.scaffolding.title': { en: 'Scaffolding', fr: 'Génération' },
        'page.scaffolding.init': { en: 'The Init Command', fr: 'La commande Init' },
        'page.scaffolding.structure': { en: 'Standard Structure', fr: 'Structure standard' },
        'page.scaffolding.breakdown': { en: 'Directory Breakdown', fr: 'Détail des dossiers' }
        ,
        'page.scaffolding.intro': { en: 'Promethee-Selenium comes with powerful scaffolding capabilities, enabling you to bootstrap a complete automation project structure with a single CLI command.', fr: 'Promethee-Selenium propose de puissantes capacités de génération pour créer rapidement une structure de projet d\'automatisation via une seule commande CLI.' },
        'page.scaffolding.initText': { en: 'To initialize a new project, navigate to your desired directory and run:', fr: 'Pour initialiser un nouveau projet, placez-vous dans le répertoire souhaité puis exécutez :' },
        'page.scaffolding.structureText': { en: 'The CLI populates your directory with best-practices architecture tailored for Selenium and Pytest:', fr: 'Le CLI génère une structure conforme aux bonnes pratiques, adaptée à Selenium et Pytest :' },
        // Environment
        'page.environment.title': { en: 'Environment Mgmt', fr: 'Gestion des environnements' },
        'page.environment.intro': { en: 'Handle multile stages of delivery effortlessly. The Environment Management features let you run the same test suite cleanly against Local, Dev, Staging, and Production layers.', fr: 'Gérez facilement plusieurs environnements. Les fonctionnalités de gestion d\'environnements permettent d\'exécuter la même suite de tests contre Local, Dev, Staging et Production.' },
        // Bilingual support
        'page.bilingual.title': { en: 'Bilingual Support', fr: 'Support bilingue' },
        'page.bilingual.intro': { en: 'Promethee-Selenium breaks down language barriers. Enjoy complete framework interactions, documentation, and error handling natively in both English and French.', fr: 'Promethee-Selenium abolit les barrières linguistiques. Profitez d\'interactions complètes du framework, documentation et gestion d\'erreurs en natif en anglais et en français.' }
        ,
        // Built-in utilities
        'page.utils.title': { en: 'Built-in Utilities', fr: 'Utilitaires intégrés' },
        'page.utils.intro': { en: 'Speed up your development cycle with a curated set of robust utilities included in the Base class.', fr: 'Accélérez votre cycle de développement avec un ensemble d\'utilitaires robustes inclus dans la classe Base.' },
        'page.utils.coreMethods': { en: 'Core Methods', fr: 'Méthodes principales' },
        'page.utils.coreMethods.text': { en: 'Here are some of the most frequently used functions provided natively:', fr: 'Voici quelques-unes des fonctions les plus utilisées fournies nativement :' },
        'page.utils.clicking': { en: 'Clicking Elements', fr: 'Cliquer sur des éléments' },
        'page.utils.clicking.text': { en: 'Waits for an element to be clickable before performing the action:', fr: 'Attend qu\'un élément soit cliquable avant d\'exécuter l\'action :' },
        'page.utils.typing': { en: 'Typing Text', fr: 'Saisie de texte' },
        'page.utils.typing.text': { en: 'Clears the field and enters text after ensuring the input element is ready:', fr: 'Efface le champ et saisit le texte après vérification que l élément est prêt :' },
        'page.utils.assertions': { en: 'Assertions & Verification', fr: 'Assertions & Vérification' },
        'page.utils.assertions.text': { en: 'Quick checks to synchronize automation flows securely:', fr: 'Vérifications rapides pour synchroniser les flux d\'automatisation en toute sécurité :' },
        'page.utils.waits': { en: 'Advanced Waiting', fr: 'Attentes avancées' },
        'page.utils.waits.text': { en: "Selenium can be flaky; Promethee's utilities wrap standard WebDriverWaits efficiently to prevent stale elements and synchronization bugs.", fr: "Selenium peut être instable ; les utilitaires Promethee encapsulent WebDriverWait pour éviter les éléments obsolètes et les problèmes de synchronisation." },

        // CLI Commands
        'page.cliCommands.title': { en: 'CLI Commands', fr: 'Commandes CLI' },
        'page.cliCommands.intro': { en: 'Promethee-Selenium provides a powerful command-line interface to streamline your automation workflow. This guide covers all available commands and their usage.', fr: 'Promethee-Selenium fournit une interface en ligne de commande puissante pour optimiser votre flux de travail d\'automatisation. Ce guide couvre toutes les commandes disponibles et leur utilisation.' },
        'page.cliCommands.initTitle': { en: 'The init Command', fr: 'La commande init' },
        'page.cliCommands.initDesc': { en: 'The <code>promethee-selenium init</code> command scaffolds a complete, production-ready project structure with best-practice architecture. This is the fastest way to get started with Promethee-Selenium.', fr: 'La commande <code>promethee-selenium init</code> génère une structure de projet complète et prête pour la production avec une architecture conforme aux bonnes pratiques. C est le moyen le plus rapide de démarrer avec Promethee-Selenium.' },
        'page.cliCommands.initUsage': { en: 'Usage', fr: 'Utilisation' },
        'page.cliCommands.initUsageText': { en: 'Run the following command in your desired project directory:', fr: 'Exécutez la commande suivante dans le répertoire du projet souhaité :' },
        'page.cliCommands.initOptions': { en: 'Options', fr: 'Options' },
        'page.cliCommands.initExample': { en: 'Example', fr: 'Exemple' },
        'page.cliCommands.initOutput': { en: 'Generated Structure', fr: 'Structure générée' },
        'page.cliCommands.initOutputText': { en: 'After running <code>init</code>, your directory will contain:', fr: 'Après avoir exécuté <code>init</code>, votre répertoire contiendra :' },
        'page.cliCommands.docsTitle': { en: 'The docs Command', fr: 'La commande docs' },
        'page.cliCommands.docsDesc': { en: 'The <code>promethee-selenium docs</code> command opens the interactive documentation and quick-reference guide in your default browser.', fr: 'La commande <code>promethee-selenium docs</code> ouvre la documentation interactive et le guide de référence rapide dans votre navigateur par défaut.' },
        'page.cliCommands.docsUsage': { en: 'Usage', fr: 'Utilisation' },
        'page.cliCommands.docsUsageText': { en: 'Simply run:', fr: 'Exécutez simplement :' },
        'page.cliCommands.docsFeatures': { en: 'Features', fr: 'Fonctionnalités' },
        'page.cliCommands.docsFeature1': { en: 'Full HTML documentation with code examples and best practices', fr: 'Documentation HTML complète avec exemples de code et bonnes pratiques' },
        'page.cliCommands.docsFeature2': { en: 'Interactive Code Object Model (POM) guide', fr: 'Guide interactif du modèle Page Object (POM)' },
        'page.cliCommands.docsFeature3': { en: 'Built-in utilities reference', fr: 'Référence des utilitaires intégrés' },
        'page.cliCommands.docsFeature4': { en: 'Environment management guide', fr: 'Guide de gestion des environnements' },
        'page.cliCommands.docsFeature5': { en: 'Bilingual support (English and French)', fr: 'Support bilingue (anglais et français)' },
        'page.cliCommands.docsExample': { en: 'Example', fr: 'Exemple' },
        'page.cliCommands.docsExampleText': { en: 'This will automatically open <code>http://localhost:8000</code> in your default browser, displaying the full documentation site you are currently viewing.', fr: 'Cela ouvrira automatiquement <code>http://localhost:8000</code> dans votre navigateur par défaut, affichant le site de documentation complet que vous consultez actuellement.' },
        'page.cliCommands.docsOptions': { en: 'Tips', fr: 'Conseils' },
        'page.cliCommands.docsTip1': { en: 'Use the language toggle to switch between English and French', fr: 'Utilisez le bouton de langue pour basculer entre l\'anglais et le français' },
        'page.cliCommands.docsTip2': { en: 'Use the theme toggle to switch between light and dark modes', fr: 'Utilisez le bouton de thème pour basculer entre les modes clair et sombre' },
        'page.cliCommands.docsTip3': { en: 'Bookmark this page for quick reference during development', fr: 'Mettez cette page en signet pour une référence rapide pendant le développement' },
        'breadcrumb.home': { en: 'Home', fr: 'Accueil' }
    };

    const langToggle = document.getElementById('lang-toggle');
    const themeToggle = document.getElementById('theme-toggle');
    function applyTheme(theme) {
        if (theme === 'light') {
            document.documentElement.classList.add('light-theme');
            if (themeToggle) themeToggle.textContent = '☀';
        } else {
            document.documentElement.classList.remove('light-theme');
            if (themeToggle) themeToggle.textContent = '🌙';
        }
        localStorage.setItem('promethee-theme', theme);
    }
    function applyLanguage(lang) {
        const els = document.querySelectorAll('[data-i18n]');
        els.forEach(el => {
            const key = el.getAttribute('data-i18n');
            const entry = translations[key];
            if (entry && entry[lang]) {
                el.innerHTML = entry[lang];
            }
        });
        document.documentElement.lang = (lang === 'fr') ? 'fr' : 'en';
        if (langToggle) langToggle.textContent = (lang === 'fr') ? 'FR' : 'EN';
        localStorage.setItem('promethee-lang', lang);
    }

    // init language from localStorage or browser setting
    const saved = localStorage.getItem('promethee-lang') || (navigator.language && navigator.language.startsWith('fr') ? 'fr' : 'en');
    applyLanguage(saved);

    // Init theme from localStorage or prefers-color-scheme
    const savedTheme = localStorage.getItem('promethee-theme') || (window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark');
    applyTheme(savedTheme);

    if (langToggle) {
        langToggle.addEventListener('click', () => {
            const current = localStorage.getItem('promethee-lang') || 'en';
            const next = current === 'en' ? 'fr' : 'en';
            applyLanguage(next);
        });
    }

    if (themeToggle) {
        themeToggle.addEventListener('click', () => {
            const current = localStorage.getItem('promethee-theme') || 'dark';
            const next = current === 'dark' ? 'light' : 'dark';
            applyTheme(next);
        });
    }

    const copyButtons = document.querySelectorAll('.copy-btn');

    copyButtons.forEach(button => {
        button.addEventListener('click', () => {
            const codeBlock = button.nextElementSibling;

            if (codeBlock) {
                const textToCopy = codeBlock.textContent;

                navigator.clipboard.writeText(textToCopy).then(() => {
                    const icon = button.querySelector('i');
                    if (icon) {
                        icon.classList.remove('fa-copy', 'fa-regular');
                        icon.classList.add('fa-check', 'fa-solid');

                        setTimeout(() => {
                            icon.classList.remove('fa-check', 'fa-solid');
                            icon.classList.add('fa-copy', 'fa-regular');
                        }, 2000);
                    }
                }).catch(err => {
                    console.error('Failed to copy text: ', err);
                });
            }
        });
    });
});
