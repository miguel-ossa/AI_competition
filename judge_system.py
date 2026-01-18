import json
from openai import OpenAI

def create_judge_prompt(question: str, responses: str, num_competitors: int, models: dict) -> str:
    juez = f"""Estás juzgando una competencia entre {num_competitors} competidores.
A cada modelo se le ha dado esta pregunta:

{question}

Aquí están las respuestas:

{responses}

Tu trabajo es evaluar cada respuesta y clasificarlas de mejor a peor.

Criterios de evaluación:
1. Precisión y exactitud
2. Creatividad y originalidad
3. Claridad de explicación
4. Profundidad del análisis
5. Utilidad práctica
6. Se tienen en cuenta todas las posibles problemáticas relacionadas

Responde SOLO en formato JSON con esta estructura exacta:
{{
    "resultados": [1, 2, 3, 4, 5, 6, 7],
    "razonamiento": "Explicación breve del ranking"
}}

Los números representan el ranking (1=mejor, 2=segundo mejor, etc.)
No reveles el nombre del modelo en tu evaluación.
"""
    
    return juez

def judge_competition(openai_client: OpenAI, judge_prompt: str) -> dict:
    """Ejecuta el juicio usando o4-mini"""
    mensajes_juez = [{"role": "user", "content": judge_prompt}]

    response = openai_client.chat.completions.create(
        model="o4-mini",
        messages=mensajes_juez
    )

    results = response.choices[0].message.content
    return json.loads(results)

def display_results(competitors: list, results_dict: dict):
    """Muestra los resultados del torneo"""
    ranks = results_dict["resultados"]
    reasoning = results_dict["razonamiento"]

    print("RESULTADOS DEL TORNEO DE IAs")
    print("=" * 50)
    for index, result in enumerate(ranks):
        competitor = competitors[int(result) - 1]
        medals = ["🥇", "🥈", "🥉", "4", "5", "6", "7"]
        print(f"{medals[index]} Top {index + 1}: {competitor}")

    print(f"\nRazonamiento del juez: {reasoning}")
