from api_client import get_completion
from message_generator import generate_system_message

def chatbot(message, history):
    system_message = generate_system_message()
    messages = [{"role": "system", "content": system_message}]
    messages.extend([{"role": "user", "content": human} for human, _ in history])
    messages.extend([{"role": "assistant", "content": assistant} for _, assistant in history])
    messages.append({"role": "user", "content": message})
    
    return get_completion("your-model-name", messages)