import json
from pyexpat.errors import messages
from typing import List, Dict, Optional

def generate_challenge_question(client, model: str) -> str:
    """Genera una pregunta desafiante usando un modelo específico"""
    solicitud="Crea una pregunta desafiante que pueda hacer a varios LLMs para evaluar su inteligencia."
    response =client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": solicitud}]
    )
    return response.choices[0].message.content

def collect_responses(clients: Dict, models: Dict, question: str) -> tuple:
    """Recolecta respuestas de todos los modelos"""
    competitors = []
    answers = []
    for service_name, client in clients.items():
        try:
            model = models[service_name]
            if service_name != "Claude":
                response = client.chat.completions.create(
                    model=model,
                    messages=[{"role": "user", "content": question + " Elabora la respuesta con profundidad."}]
                )
                competitors.append(f"{service_name} ({model})")
                answers.append(response.choices[0].message.content)
            else:
                response = client.messages.create(
                    model=model,
                    messages=[{"role": "user", "content": question}],
                    max_tokens=5000
                )
                competitors.append(f"{service_name} ({model})")
                answers.append(response.content[0].text)

        except Exception as e:
            print(f"Error al obtener respuesta de {service_name}: {e}")
            continue
    return competitors, answers

def organize_responses_with_zip(competitors: List[str], answers: List[str]):
    """ZIP para iterar dos listas juntas"""
    print("Usando ZIP para iterar dos listas:")
    for competitor, answer in zip(competitors, answers):
        if answer is None:
            print(f"\n***********Competitor: {competitor}")
            print("Preview: La respuesta está vacía o no disponible.")
            print("-" * 50)
            continue
        
        # Asegúrate de que la respuesta sea una cadena y tenga al menos 100 caracteres
        if isinstance(answer, str) and len(answer) > 0:
            #preview = answer[:300]
            preview = answer
            if len(preview) < len(answer):
                preview += "..."
            print(f"\n***********Competitor: {competitor}")
            print(f"Preview: {preview}")  # Muestra solo los primeros 100 caracteres)
        else:
            print(f"\n***********Competitor: {competitor}")
            print("Preview: La respuesta está vacía o no disponible.")
            print("-" * 50)

def organize_responses_with_enumerate(answers: List[Optional[str]]) -> str:
    """Truco 2: ENUMERATE para obtener índices automáticamente"""
    juntas = ""
    for indice, respuesta in enumerate(answers):
        if respuesta is None:
            # Si la respuesta es None, se maneja adecuadamente
            juntas += f"Respuesta del competidor {indice + 1}:\n\n"
            juntas += "La respuesta está vacía o no disponible.\n\n"
            continue
        
        if isinstance(respuesta, str) and len(respuesta.strip()) > 0:
            # Si la respuesta es una cadena válida, se agrega
            juntas += f"Respuesta del competidor {indice + 1}:\n\n"
            juntas += respuesta + "\n\n"
        else:
            # Si la respuesta está vacía o no disponible, se maneja adecuadamente
            juntas += f"Respuesta del competidor {indice + 1}:\n\n"
            juntas += "La respuesta está vacía o no disponible.\n\n"

    return juntas

