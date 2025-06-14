import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types

def main():
        if len(sys.argv) < 2:
              print("Usage: python3 main.py <prompt text>")
              sys.exit(1)


        prompt = sys.argv[1]
        messages = [
               types.Content(role="user", parts=[types.Part(text=prompt)]),
               ]
        

        load_dotenv()
        api_key = os.environ.get("GEMINI_API_KEY")

        verbose = "--verbose" in sys.argv    
        prompt_parts = [arg for arg in sys.argv[1:] if arg != "--verbose"]
        user_prompt = " ".join(prompt_parts)


        
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents = messages,
        )


        print(response.text)

        if verbose:
              usage = response.usage_metadata
              print(f"\nUser prompt: {user_prompt}")
              print(f"Prompt tokens: {usage.prompt_token_count}")
              print(f"Response tokens: {usage.candidates_token_count}")

main()
