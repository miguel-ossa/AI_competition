import os
import sys
import logging
import requests
from dotenv import load_dotenv
from openai import OpenAI
from anthropic import Anthropic

EXECUTE_MODEL_QUERIES = False

load_dotenv(override=True)

# Gemini
gemini = OpenAI(
    api_key=os.getenv("GOOGLE_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)

# DeepSeek
deepseek = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com/v1"
)

# Groq
groq = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

# OpenAI
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Anthropic (Claude) OK
anthropic_client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# Ollama
ollama = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"  # Ollama does not require an API key
)

print("Clientes de IA configurados exitosamente")
print("Una sola librería para múltiples proveedores de IA.")

if EXECUTE_MODEL_QUERIES:
    # Configuración del logging para guardar los logging.info en models.txt y mostrarlos también en la consola.
    logging.basicConfig(
        filename="models.txt",
        filemode='w',  # 'w' para sobrescribir el archivo cada vez que se ejecuta
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.INFO,
    )

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logging.getLogger('').addHandler(console_handler)

    logging.info("*" * 50)
    logging.info("Modelos Gemini")
    logging.info("*" * 50)
    modelos_gemini_disponibles = gemini.models.list()
    # Imprimir la lista de modelos
    for modelo in modelos_gemini_disponibles:
        logging.info(f"Modelo Gemini: {modelo}")

    logging.info("*" * 50)
    logging.info("Modelos Claude")
    logging.info("*" * 50)
    modelos_anthropic_disponibles = anthropic_client.models.list()
    # Imprimir la lista de modelos
    for modelo in modelos_anthropic_disponibles:
        logging.info(f"Modelo Claude: {modelo}")

    logging.info("*" * 50)
    logging.info("Modelos OpenAI")
    logging.info("*" * 50)
    modelos_openai_disponibles = openai_client.models.list()
    # Imprimir la lista de modelos
    for modelo in modelos_openai_disponibles:
        logging.info(f"Modelo OpenAI: {modelo}")

    logging.info("*" * 50)
    logging.info("Modelos Deepseek")
    logging.info("*" * 50)
    modelos_deepseek_disponibles = deepseek.models.list()
    # Imprimir la lista de modelos
    for modelo in modelos_deepseek_disponibles:
        logging.info(f"Modelo Deepseek: {modelo}")

    logging.info("*" * 50)
    logging.info("Modelos Groq")
    logging.info("*" * 50)
    modelos_groq_disponibles = groq.models.list()
    # Imprimir la lista de modelos
    for modelo in modelos_groq_disponibles:
        logging.info(f"Modelo Groq: {modelo}")

    logging.info("*" * 50)
    logging.info("Modelos Ollama")
    logging.info("*" * 50)
    modelos_ollama_disponibles = ollama.models.list()
    # Imprimir la lista de modelos
    for modelo in modelos_ollama_disponibles:
        logging.info(f"Modelo Ollama: {modelo}")

    sys.exit(0)