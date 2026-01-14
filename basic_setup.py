import os
from dotenv import load_dotenv
from openai import OpenAI
from anthropic import Anthropic

load_dotenv(override=True)

openai_api_key = os.getenv("OPENAI_API_KEY")
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
google_api_key = os.getenv("GOOGLE_API_KEY")
deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")

print("Configuración de claves API:")
print(f"OpenAI: {'Configurada' if openai_api_key else 'No configurada'}")
print(f"Anthropic: {'Configurada' if anthropic_api_key else 'No configurada'}")
print(f"Google: {'Configurada' if google_api_key else 'No configurada'}")
print(f"Deepseek: {'Configurada' if deepseek_api_key else 'No configurada'}")
print(f"Groq: {'Configurada' if groq_api_key else 'No configurada'}")
