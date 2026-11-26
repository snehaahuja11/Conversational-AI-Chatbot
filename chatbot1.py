from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()

api_key =os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("Api key not found")

client=genai.Client(api_key=api_key)

print("Welcome to My AI Chatbot!")
print("Type 'exit' to end the conversation")

while True:
    user_input = input("You:")
    if user_input.lower()=="exit":
        break
    response=client.models.generate_content(
      model="gemini-3.5-flash-lite",
      contents=user_input,
      config=types.GenerateContentConfig(
          system_instruction="You are a helpful AI Assistant",
          temperature=0.7,
          max_output_tokens=200
      )
    )
    print("Chatbot:",response.text)
