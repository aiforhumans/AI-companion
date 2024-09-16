import json
from state import companion_traits, user_info, scenario, bonding_level

def save_settings():
    settings = {
        "companion_traits": companion_traits,
        "user_info": user_info,
        "scenario": scenario,
        "bonding_level": bonding_level
    }
    with open("companion_settings.json", "w") as f:
        json.dump(settings, f)
    return "Settings saved successfully!"

def load_settings():
    try:
        with open("companion_settings.json", "r") as f:
            settings = json.load(f)
        companion_traits.update(settings["companion_traits"])
        user_info.update(settings["user_info"])
        scenario.update(settings["scenario"])
        global bonding_level
        bonding_level = settings["bonding_level"]
        return f"Settings loaded successfully!\n\nCompanion Traits:\n{companion_traits}\n\nUser Info:\n{user_info}\n\nScenario:\n{scenario}\n\nBonding Level: {bonding_level}/10"
    except FileNotFoundError:
        return "No saved settings found."