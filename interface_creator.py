import gradio as gr
from state import update_setting
from utils import chatbot
from settings_manager import save_settings, load_settings

def create_interface(interface_type, setting_type=None):
    if interface_type == "chat":
        return gr.ChatInterface(
            fn=chatbot,
            chatbot=gr.Chatbot(height=600),
            title="Companion AI Roleplay",
            description="Interact with your personalized AI companion in a rich roleplay scenario.",
            examples=[["Tell me about yourself"], ["What's our current adventure?"]],
            theme="soft"
        )
    elif interface_type == "form":
        input_config = get_input_config(setting_type)
        return gr.Interface(
            fn=lambda *args: update_setting(setting_type, **dict(zip(input_config["input_names"], args))),
            inputs=input_config["inputs"],
            outputs="text",
            title=input_config["title"],
            description=input_config["description"],
            allow_flagging="never"
        )
    elif interface_type == "settings":
        return gr.Interface(
            fn=lambda action: save_settings() if action == "save" else load_settings(),
            inputs=gr.Radio(["save", "load"], label="Action"),
            outputs="text",
            title="Settings",
            description="Save or load your companion AI settings.",
            allow_flagging="never"
        )

def get_input_config(setting_type):
    if setting_type == "companion_traits":
        return {
            "input_names": ["name", "age", "personality", "primary_role", "communication_style"],
            "inputs": [
                gr.Textbox(label="Name"),
                gr.Number(label="Age"),
                gr.Textbox(label="Personality", lines=3),
                gr.Dropdown(["Emotional support", "Problem-solver", "Adventurer", "Listener", "Motivator"], label="Primary Role"),
                gr.Dropdown(["Direct", "Suggestive", "Enthusiastic", "Reserved"], label="Communication Style")
            ],
            "title": "Companion AI Traits",
            "description": "Set the essential traits for your AI companion."
        }
    elif setting_type == "user_info":
        return {
            "input_names": ["name", "age", "relationship", "preferences"],
            "inputs": [
                gr.Textbox(label="Name of User"),
                gr.Number(label="User Age"),
                gr.Dropdown(["Best friend", "Guardian", "Partner", "Confidant", "Pet"], label="Relationship with AI"),
                gr.Textbox(label="User's Preferences", lines=3)
            ],
            "title": "User Info",
            "description": "Set your information for the roleplay."
        }
    elif setting_type == "scenario":
        return {
            "input_names": ["setting", "time_period", "objective", "events", "rules"],
            "inputs": [
                gr.Textbox(label="Setting", lines=3),
                gr.Dropdown(["Present day", "Medieval Fantasy", "Futuristic Sci-fi", "Post-apocalyptic"], label="Time Period"),
                gr.Textbox(label="Main Objective or Theme", lines=3),
                gr.Textbox(label="Key Events or Milestones", lines=3),
                gr.Textbox(label="Special Rules/Boundaries", lines=3)
            ],
            "title": "Roleplay Scenario",
            "description": "Set the scenario for your roleplay experience."
        }
    elif setting_type == "bonding_level":
        return {
            "input_names": ["level"],
            "inputs": [gr.Slider(1, 10, label="Bonding Level")],
            "title": "Emotional Bonding",
            "description": "Set the current level of connection between you and your AI companion."
        }