

import os
import google.generativeai as genai
from dotenv import load_dotenv


load_dotenv()

class GeminiService:
    """
    A service to interact with the Google Gemini API.
    """
    def __init__(self):
        """
        Initializes the Gemini service by configuring the API key.
        """
        try:
            # Get the API key from environment variables
            api_key = os.getenv("GEMINI_API_KEY")
            if not api_key:
                raise ValueError("GEMINI_API_KEY not found in environment variables.")
            
            
            genai.configure(api_key=api_key)
            
            
            self.model = genai.GenerativeModel('gemini-1.5-flash-latest')
            print("Gemini service initialized successfully with model 'gemini-1.5-flash-latest'.")

        except Exception as e:
            print(f"Error initializing Gemini service: {e}")
            self.model = None

    def generate_text(self, prompt: str) -> str:
        """
        Generates text based on a given prompt.

        Args:
            prompt: The input text prompt for the model.

        Returns:
            The generated text as a string, or an error message if generation fails.
        """
        if not self.model:
            return "Error: Gemini model is not initialized."

        try:
            
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"An error occurred during text generation: {e}")
            return f"Error: Could not generate text. Details: {e}"

#explanation
if __name__ == '__main__':

    gemini_client = GeminiService()
    if gemini_client.model:
        test_prompt = "Explain the importance of modular code structure in 50 words."
        print(f"Testing Gemini Service with prompt: '{test_prompt}'")
        generated_text = gemini_client.generate_text(test_prompt)
        print("\n--- Generated Text ---")
        print(generated_text)
        print("----------------------")
