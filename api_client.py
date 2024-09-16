from openai import OpenAI

# API constants
OPENAI_BASE_URL = "http://localhost:1234/v1"
OPENAI_API_KEY = "lm-studio"

# API setup
openai_client = OpenAI(base_url=OPENAI_BASE_URL, api_key=OPENAI_API_KEY)

def get_completion(model_name, messages):
    completion = openai_client.chat.completions.create(model=model_name, messages=messages)
    return completion.choices[0].message.content