import csv
import os

class ScenarioProvider:
    
    CREDENTIALS_FILE = os.path.join(os.path.dirname(__file__), '../data/credentials.csv')

    @staticmethod
    def get_data_for_scenario(scenario_name):
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
        scenario_name = input(f"Entrez le nom du scénario (ex: 'login') [défaut: {default_scenario}] : ").strip()
        
        if not scenario_name:
            scenario_name = default_scenario
            print(f"Aucun scénario entré, utilisation par défaut de : {scenario_name}")

        data = ScenarioProvider.get_data_for_scenario(scenario_name)
        # On retourne aussi le nom pour les tests qui en ont besoin (ex: test_login)
        return scenario_name, data
