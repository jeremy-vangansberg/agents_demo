from openai import OpenAI
from pydantic import BaseModel
from dotenv import load_dotenv
import json

_ = load_dotenv()

client = OpenAI()

class CalendarEvent(BaseModel):
    """Calendrier d'événement"""
    name: str
    date: str
    participants: list[str]

# Afficher le schéma JSON généré pour l'API
schema = CalendarEvent.model_json_schema()
print("Schéma JSON envoyé à l'API:")
print(json.dumps(schema, indent=2, ensure_ascii=False))

response = client.responses.parse(
    model="gpt-4o-2024-08-06",
    input=[
        {"role": "system", "content": "Extract the event information."},
        {
            "role": "user",
            "content": "Alice and Bob are going to a science fair on Friday.",
        },
    ],
    text_format=CalendarEvent,
)

event = response.output_parsed
print("\nRésultat parsé:")
print(event)


from pydantic import BaseModel, Field
from typing import List

class Address(BaseModel):
    """Adresse physique complète d'une personne"""
    street: str = Field(description="Numéro et nom de rue")
    city: str = Field(description="Ville")
    postal_code: str = Field(description="Code postal")

class Person(BaseModel):
    """Informations personnelles complètes d'un individu"""
    name: str = Field(description="Prénom et nom complets")
    addresses: List[Address] = Field(description="Adresses connues")
