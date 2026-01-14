"""
COMPARACIÓN DE IAs
Hace competir a múltiples modelos de IA y determinar el que da la respuesta más óptima
"""

import os
from dotenv import load_dotenv
from openai import OpenAI
from anthropic import Anthropic
import json

from unified_clients import *
from competition_logic import *
from judge_system import *

def main():
    print("=" * 50)
    print("INICIANDO COMPARACIÓN DE IAs")
    print("=" * 50)

    # Configurar clientes y modelos
    clients = {
        "Gemini": gemini,
        "OpenAI": openai_client,
        "DeepSeek": deepseek,
        "Claude": anthropic_client,        
        "Groq": groq,
        "Ollama": ollama
    }

    models = {
        "Gemini": "gemini-flash-latest",
        "OpenAI": "gpt-4o-mini",
        "DeepSeek": "deepseek-chat",
        "Claude": "claude-opus-4-5-20251101",
        "Groq": "llama-3.3-70b-versatile",
        "Ollama": "llama3.2"
    }

    try:
        # Paso 1: Generar pregunta desafiante
        question = generate_challenge_question(openai_client, "gpt-4o-mini")
        print(f"Pregunta: {question}\n")
    except Exception as e:
        print(f"Error al generar la pregunta: {e}")
        return
    
    # Paso 2: Recolectar respuestas de los modelos
    print("Recolectando respuestas de los modelos...")
    competitors, answers = collect_responses(clients, models, question) 
    
    # Organizar las respuestas
    organize_responses_with_zip(competitors, answers)

    # Paso 3: Organizar respuestas para el juez
    responses_combined = organize_responses_with_enumerate(answers)

    # Paso 4: Crear prompt para el juez
    judge_prompt = create_judge_prompt(question, responses_combined, len(competitors), models)

    # Paso 5: Juzgar la competencia
    print("Juzgando la competencia...")
    results_dict = judge_competition(openai_client, judge_prompt)

    # Paso 6: Mostrar resultados
    display_results(competitors, results_dict)

if __name__ == "__main__":
    main()
