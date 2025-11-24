import os
from dotenv import load_dotenv

load_dotenv()

# Model Configurations
OPEN_API_KEY = os.getenv("OPEN_API_KEY", "")
MODEL_PROVIDER = os.getenv("MODEL_PROVIDER", "huggingface")
HF_MODEL_NAME = os.getenv("HF_MODEL_NAME", "distilgpt2")

# logging configurations
LOG_FILE = os.getenv("LOG_FILE", "../logs/chat_assistant.log")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")