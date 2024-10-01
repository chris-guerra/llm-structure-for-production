"""
LLM Script Oriented to using OpenAI structure
"""

from openai import OpenAI

client = OpenAI()

MODEL = "gpt-4o-mini"

TOPIC = "soul"

PROMPT_SYSTEM = "You are a helpfull assistant whose goal is to help write stories."
PROMPT = """
Continue the following story. Write no more than 50 words.

Once upon a time, in a world where animals could speak, a courageous mouse named
Benjamin decided to
"""

response_parameters = {"model": MODEL,
                       "messages": [
                           {"role": "system", "content": PROMPT_SYSTEM},
                           {"role": "user", "content": PROMPT}],
                        "temperature": 0
                        }

response = client.chat.completions.create(**response_parameters)

print(response.choices[0].message.content)
