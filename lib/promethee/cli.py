import argparse
import os
import shutil
import webbrowser
import sys

# ANSI Color Codes
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"
BOLD = "\033[1m"

BANNER = f"""{CYAN}
  _____                            _   _                 
 |  __ \                          | | | |                
 | |__) | __ ___  _ __ ___   ___  | |_| |__   ___  ___   
 |  ___/ '__/ _ \| '_ ` _ \ / _ \ | __| '_ \ / _ \/ _ \  
 | |   | | | (_) | | | | | |  __/ | |_| | | |  __/  __/  
 |_|   |_|  \___/|_| |_| |_|\___|  \__|_| |_|\___|\___|  
      {YELLOW}Selenium UI Test Automation Framework{RESET}
"""

TEXTS = {
    "en": {
        "welcome": "Welcome to Promethee-Selenium!",
        "intro": "This library helps you create automated UI tests using the Page Object Model (POM) pattern.",
        "select_option": "Please select an option:",
        "opt_init": "Initialize a new test project structure",
        "opt_docs": "Open documentation in your browser",
        "opt_quit": "Quit",
        "enter_choice": "Enter your choice",
        "goodbye": "Goodbye!",
        "invalid": "Invalid choice. Please try again.",
        "init_msg": "Initializing new test project in:",
        "created_dir": "Created directory:",
        "created_file": "Created",
        "project_ready": "Project initialized successfully!",
        "run_test_cmd": "Run your tests with: pytest tests/",
        "lang_prompt": "Select Language / Choisissez votre langue",
        "lang_en": "English",
        "lang_fr": "Français",
    },
    "fr": {
        "welcome": "Bienvenue sur Promethee-Selenium !",
        "intro": "Cette librairie vous aide à créer des tests automatisés UI en utilisant le modèle Page Object Model (POM).",
        "select_option": "Veuillez choisir une option :",
        "opt_init": "Initialiser une nouvelle structure de projet de test",
        "opt_docs": "Ouvrir la documentation dans votre navigateur",
        "opt_quit": "Quitter",
        "enter_choice": "Entrez votre choix",
        "goodbye": "Au revoir !",
        "invalid": "Choix invalide. Veuillez réessayer.",
        "init_msg": "Initialisation du nouveau projet de test dans :",
        "created_dir": "Dossier créé :",
        "created_file": "Créé",
        "project_ready": "Projet initialisé avec succès !",
        "run_test_cmd": "Lancez vos tests avec : pytest tests/",
        "lang_prompt": "Select Language / Choisissez votre langue",
        "lang_en": "English",
        "lang_fr": "Français",
    }
}

CURRENT_LANG = "en"

def t(key):
    return TEXTS[CURRENT_LANG].get(key, key)

def open_docs():
    """
    Opens the framework documentation in the default web browser.
    """
    try:
        # Try to locate the docs using pkg_resources (older but reliable) or file path relative to this file
        # Since we are in promethee/cli.py, docs are in promethee/docs/index.html
        
        # Method 1: Relative path from __file__
        current_dir = os.path.dirname(os.path.abspath(__file__))
        docs_path = os.path.join(current_dir, "docs", "index.html")
        
        if os.path.exists(docs_path):
            print(f"{GREEN}Opening documentation: {docs_path}{RESET}")
            webbrowser.open(f"file://{docs_path}")
        else:
            print(f"{RED}Documentation file not found locally.{RESET}")
            print("You can view it online on PyPI or GitHub.")
            
    except Exception as e:
        print(f"{RED}Failed to open documentation: {e}{RESET}")

def init_project():
    """
    Initializes a new test project with the recommended structure.
    """
    base_dir = os.getcwd()
    print(f"\n{CYAN}{t('init_msg')} {base_dir}{RESET}")

    # Define directories to create
    dirs = ["scenarios", "tests", "data", "utils"]
    for d in dirs:
        path = os.path.join(base_dir, d)
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"{GREEN}{t('created_dir')} {d}{RESET}")
    
    # Create __init__.py in scenarios and utils to make them packages
    for pkg in ["scenarios", "utils"]:
        init_path = os.path.join(base_dir, pkg, "__init__.py")
        if not os.path.exists(init_path):
            with open(init_path, "w") as f:
                pass

    # Create utils/scenario_provider.py
    scenario_provider_path = os.path.join(base_dir, "utils", "scenario_provider.py")
    if not os.path.exists(scenario_provider_path):
        with open(scenario_provider_path, "w") as f:
            f.write("""import csv
import os

class ScenarioProvider:
    # Look for credentials in the data directory
    CREDENTIALS_FILE = os.path.join(os.getcwd(), 'data', 'credentials.csv')

    @staticmethod
    def get_data_for_scenario(scenario_name):
        if not os.path.exists(ScenarioProvider.CREDENTIALS_FILE):
             raise FileNotFoundError(f"Credentials file not found at {ScenarioProvider.CREDENTIALS_FILE}")

        with open(ScenarioProvider.CREDENTIALS_FILE, mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['scenario'] == scenario_name:
                    user_env_key = f"TEST_USER_{scenario_name.upper().replace(' ', '_')}"
                    pass_env_key = f"TEST_PASS_{scenario_name.upper().replace(' ', '_')}"
                    os.environ[user_env_key] = row['email']
                    os.environ[pass_env_key] = row['password']
                    
                    return {
                        "username_env": user_env_key,
                        "password_env": pass_env_key
                    }
        
        raise ValueError(f"Scenario '{scenario_name}' not found in credentials.csv")

    @staticmethod
    def prompt_for_scenario(default_scenario="login"):
        # In automated environments (CI), you might want to switch this to read an env var
        print(f"Using default scenario: {default_scenario}")
        return default_scenario, ScenarioProvider.get_data_for_scenario(default_scenario)
""")
        print(f"{GREEN}{t('created_file')} utils/scenario_provider.py{RESET}")

    # Create credentials.csv
    creds_path = os.path.join(base_dir, "data", "credentials.csv")
    if not os.path.exists(creds_path):
        with open(creds_path, "w") as f:
            f.write("scenario,email,password\\nlogin,test@example.com,secret123\\n")
        print(f"{GREEN}{t('created_file')} data/credentials.csv{RESET}")

    # Create conftest.py
    conftest_path = os.path.join(base_dir, "conftest.py")
    if not os.path.exists(conftest_path):
        with open(conftest_path, "w") as f:
            f.write("""import pytest
from promethee.conftest import driver, base_url

# You can add local fixtures here
""")
        print(f"{GREEN}{t('created_file')} conftest.py{RESET}")

    # Create sample scenario (login.py)
    login_scenario_path = os.path.join(base_dir, "scenarios", "login.py")
    if not os.path.exists(login_scenario_path):
        with open(login_scenario_path, "w") as f:
            f.write("""from promethee.base import Base
from selenium.webdriver.common.by import By
from selenium_ui_test_tool import fill_input, click_element, wait_for_element

class LoginPage(Base):
    def fill_login_form(self, username, password):
        print(f"Logging in with {username}...")
        # Example implementation
        # fill_input(self.driver, By.ID, "username", username)
        # fill_input(self.driver, By.ID, "password", password)
        # click_element(self.driver, By.ID, "login-btn")
""")
        print(f"{GREEN}{t('created_file')} scenarios/login.py{RESET}")

    # Create generic sample test
    test_path = os.path.join(base_dir, "tests", "test_login.py")
    if not os.path.exists(test_path):
        with open(test_path, "w") as f:
            f.write("""from utils.scenario_provider import ScenarioProvider
from scenarios.login import LoginPage

def test_login(driver, base_url):
    print("Running test_login...")
    scenario_name, data = ScenarioProvider.prompt_for_scenario()
    
    page = LoginPage(driver)
    page.fill_login_form(data['username_env'], data['password_env'])
    
    assert True
""")
        print(f"{GREEN}{t('created_file')} tests/test_login.py{RESET}")
    
    print(f"\n{BOLD}{t('project_ready')}{RESET}")
    print(f"{t('run_test_cmd')}")

def main():
    global CURRENT_LANG
    
    if len(sys.argv) == 1:
        print(BANNER)
        
        # Language Selection Loop
        while True:
            print(f"{CYAN}Select Language / Choisissez votre langue :{RESET}")
            print("  [1] English")
            print("  [2] Français")
            
            lang_choice = input(f"\n{YELLOW}Choice/Choix [1/2]: {RESET}").strip()
            
            if lang_choice == '1':
                CURRENT_LANG = "en"
                break
            elif lang_choice == '2':
                CURRENT_LANG = "fr"
                break
            else:
                print(f"{RED}Invalid choice/Choix invalide.{RESET}\n")

        print(f"\n{BOLD}{t('welcome')}{RESET}")
        print(f"{t('intro')}\n")
        
        while True:
            print(f"{CYAN}{t('select_option')}{RESET}")
            print(f"  [1] promethee-selenium init    - {t('opt_init')}")
            print(f"  [2] promethee-selenium docs    - {t('opt_docs')}")
            print(f"  [q] {t('opt_quit')}")
            
            choice = input(f"\n{YELLOW}{t('enter_choice')} [1/2/q]: {RESET}").strip().lower()
            
            if choice == '1':
                init_project()
                sys.exit(0)
            elif choice == '2':
                open_docs()
                sys.exit(0)
            elif choice == 'q':
                print(f"{t('goodbye')}")
                sys.exit(0)
            else:
                print(f"{RED}{t('invalid')}{RESET}\n")


    parser = argparse.ArgumentParser(description="Promethee-Selenium UI Test Library CLI")
    subparsers = parser.add_subparsers(dest="command")

    init_parser = subparsers.add_parser("init", help="Initialize a new test project")
    docs_parser = subparsers.add_parser("docs", help="Open the documentation in browser")

    args = parser.parse_args()

    if args.command == "init":
        init_project()
    elif args.command == "docs":
        open_docs()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
