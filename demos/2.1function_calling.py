from pydantic_ai import Agent

from dotenv import load_dotenv

_ = load_dotenv()

agent = Agent(
    'gpt-5-nano'
)

@agent.tool_plain  
def get_weather(city: str) -> str:
    """Get current weather for a specific city."""
    weather_data = {
        "Paris": "18°C, ensoleillé avec quelques nuages",
        "Berlin": "12°C, pluvieux et nuageux",
        "Lille": "15°C, nuageux avec quelques éclaircies"
    }
    return weather_data.get(city, f"{city}: Données météo non disponibles")

result = agent.run_sync('Quel est le temps à Lille aujourd\'hui?') 

print(result)