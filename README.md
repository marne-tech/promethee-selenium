# Promethee-Selenium

*[English version below | Version française plus bas]*

---

# 🇬🇧 English Description

**Promethee-Selenium** is a professional-grade automation library designed to eliminate **Selenium flakiness** while bringing a structured, industrial approach to UI testing. 

Built on the **Page Object Model (POM)** pattern and powered by Pytest, it ensures your automation remains stable, maintainable, and scalable from day one.

## 🚀 Key Value Propositions

-   **Zero-Flakiness approach**: Tired of fragile tests? Promethee-Selenium implements smart waiting mechanisms and robust element interactions to ensure your tests only fail when they should.
-   **Professional POM Structure**: It enforces a clean separation of concerns. Page locators and actions are decoupled from test logic, making maintenance effortless.
-   **Rapid Automation CLI**: Don't waste time setting up boilerplate. Our interactive CLI bootstraps a complete, production-ready POM architecture in seconds.
-   **Scaffolding**: Run `promethee-selenium init` to generate a best-practice project structure instantly.
-   **Bilingual Support**: Both CLI and documentation are natively available in English and French.

## Installation

```bash
pip install promethee-selenium
```

## Getting Started in 60 Seconds

1.  **Launch the CLI**:
    ```bash
    promethee-selenium
    ```
    Choose your language and select **Init** to bootstrap your project.

2.  **Project Structure**:
    The CLI generates a professional layout:
    -   `scenarios/`: Your Page Object classes.
    -   `tests/`: Your clean test scripts.
    -   `data/`: Configuration and CSV test data.
    -   `conftest.py`: Industrial-grade Pytest fixtures.

3.  **Run Your Tests**:
    ```bash
    pytest lib/tests/
    ```

## Documentation

Access the full guide via:
```bash
promethee-selenium docs
```

## Contributors

-   **Yann Dipita** ([kingcrud12](https://github.com/kingcrud12))
-   **Loïc Roxan Milandou** ([roxanmlr](https://github.com/roxanmlr))

---

# 🇫🇷 Description Française

**Promethee-Selenium** est une bibliothèque d'automatisation professionnelle conçue pour éradiquer l'instabilité (**flakiness**) de Selenium tout en apportant une structure industrielle à vos tests UI.

Basée sur le pattern **Page Object Model (POM)** et propulsée par Pytest, elle garantit que votre automatisation reste stable, maintenable et évolutive dès le premier jour.

## Valeur Ajoutée

-   **Adieu aux tests "fragiles"** : Marre des tests qui échouent sans raison ? Promethee-Selenium implémente des mécanismes d'attente intelligents et des interactions robustes avec le DOM.

-   **Architecture POM Professionnelle** : Elle impose une séparation claire des responsabilités. Les sélecteurs et actions sont découplés de la logique de test, simplifiant la maintenance.

-   **Automatisation Rapide via CLI** : Ne perdez plus de temps sur la configuration. Notre CLI interactif génère une architecture POM complète et prête pour la production en quelques secondes.

-   **Scaffolding** : Lancez `promethee-selenium init` pour créer instantanément une structure de projet respectant les meilleures pratiques.

-   **Support Bilingue** : Le CLI et la documentation sont disponibles nativement en anglais et en français.

## Installation

```bash
pip install promethee-selenium
```

## Démarrage en 60 Secondes

1.  **Lancez le CLI** :
    ```bash
    promethee-selenium
    ```
    Choisissez votre langue et sélectionnez **Init** pour initialiser votre projet.

2.  **Structure du Projet** :
    Le CLI génère une organisation professionnelle :
    -   `scenarios/` : Vos classes Page Object.
    -   `tests/` : Vos scripts de test épurés.
    -   `data/` : Configuration et données CSV.
    -   `conftest.py` : Fixtures Pytest de niveau industriel.

3.  **Lancez Vos Tests** :
    ```bash
    pytest lib/tests/
    ```

## Documentation

Consultez le guide complet via :
```bash
promethee-selenium docs
```

## Contributeurs

-   **Yann Dipita** ([kingcrud12](https://github.com/kingcrud12))
-   **Loïc Roxan Milandou** ([roxanmlr](https://github.com/roxanmlr))
