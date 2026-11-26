from google import genai
from dotenv import load_dotenv
from google.genai import types
import os

load_dotenv()
api_key=os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("API key is required")

client=genai.Client(api_key=api_key)
print("Chatbot")
print("Type 'exit' to end the conversation")

messages =[]  # empty history list


# chat loop
while True:
    user_input=input("YOU:")
    if user_input.lower() == "exit":
        break

# messages to be saved here
    messages.append(
        types.Content(
          role="user",
          parts=[types.Part.from_text(text=user_input)]
       )
   )

    response=client.models.generate_content(
       model="gemini-3.5-flash-lite",
       contents=messages,
       config=types.GenerateContentConfig(
          system_instruction="You are a helpful AI Assistant",
          max_output_tokens=200,
          temperature=0.8
      )
   )

    answer=response.text

 # Step 9: Store chatbot answer
    messages.append(
       types.Content(
          role="model",
          parts=[types.Part.from_text(text=answer)]
      )
    )

    print("Chatbot:", answer)
    print()

client.close()