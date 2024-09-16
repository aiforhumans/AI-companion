# Global variables
companion_traits = {}
user_info = {}
scenario = {}
bonding_level = 1

def initialize_state():
    global companion_traits, user_info, scenario, bonding_level
    companion_traits = {}
    user_info = {}
    scenario = {}
    bonding_level = 1

def update_setting(setting_type, **kwargs):
    global companion_traits, user_info, scenario, bonding_level
    
    if setting_type == "companion_traits":
        companion_traits.update(kwargs)
        return f"Companion AI Traits set:\n\n{companion_traits}"
    elif setting_type == "user_info":
        user_info.update(kwargs)
        return f"User Info set:\n\n{user_info}"
    elif setting_type == "scenario":
        scenario.update(kwargs)
        return f"Scenario set:\n\n{scenario}"
    elif setting_type == "bonding_level":
        bonding_level = kwargs.get("level", bonding_level)
        return f"Bonding level set to: {bonding_level}/10"
    else:
        return "Invalid setting type"