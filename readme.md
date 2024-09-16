# AI Companion Roleplay Application

This application creates an interactive AI companion for roleplay scenarios using a large language model. It allows users to customize the AI's traits, set up scenarios, and engage in immersive conversations.

## Features

- Customizable AI companion traits
- User information settings
- Configurable roleplay scenarios
- Dynamic bonding level adjustment
- Save and load functionality for settings
- Immersive chat interface

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/ai-companion-roleplay.git
   cd ai-companion-roleplay
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Configuration

1. Open `api_client.py` and set your API credentials:
   ```python
   OPENAI_BASE_URL = "your_api_base_url"
   OPENAI_API_KEY = "your_api_key"
   ```

2. In `utils.py`, replace `"your-model-name"` with the name of the language model you want to use.

## Usage

1. Run the application:
   ```
   python main.py
   ```

2. Open your web browser and go to the URL displayed in the terminal (usually `http://127.0.0.1:7860`).

3. Use the tabs to set up your AI companion's traits, your user info, and the roleplay scenario.

4. Start chatting with your AI companion in the Chat tab!

5. Use the Settings tab to save or load your configurations.

## File Structure

- `main.py`: The entry point of the application
- `api_client.py`: Handles API interactions
- `state.py`: Manages the global state
- `message_generator.py`: Generates system messages
- `settings_manager.py`: Handles saving and loading settings
- `interface_creator.py`: Creates various Gradio interfaces
- `utils.py`: Utility functions

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
