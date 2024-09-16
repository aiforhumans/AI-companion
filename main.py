import gradio as gr
from interface_creator import create_interface
from state import initialize_state

def main():
    initialize_state()

    companion_traits_interface = create_interface("form", "companion_traits")
    user_info_interface = create_interface("form", "user_info")
    scenario_interface = create_interface("form", "scenario")
    bonding_interface = create_interface("form", "bonding_level")

    tabbed_interface = gr.TabbedInterface(
        [create_interface("chat"), companion_traits_interface, user_info_interface,
         scenario_interface, bonding_interface, create_interface("settings")],
        ["Chat", "Companion Traits", "User Info", "Scenario", "Bonding", "Settings"]
    )

    tabbed_interface.launch()

if __name__ == "__main__":
    main()