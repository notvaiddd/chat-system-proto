# services/gemini_service.py

import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
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
            
            # Configure the generative AI client
            genai.configure(api_key=api_key)
            
            # --- MODEL NAME UPDATED ---
            # Switched to the 'flash' model for faster generation.
            # The correct model name is 'gemini-1.5-flash-latest'.
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
            # Generate content using the model
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"An error occurred during text generation: {e}")
            return f"Error: Could not generate text. Details: {e}"

# Example of how to use the service
if __name__ == '__main__':
    # This block will only run when the script is executed directly
    # It's useful for testing the service in isolation
    gemini_client = GeminiService()
    if gemini_client.model:
        test_prompt = "Explain the importance of modular code structure in 50 words."
        print(f"Testing Gemini Service with prompt: '{test_prompt}'")
        generated_text = gemini_client.generate_text(test_prompt)
        print("\n--- Generated Text ---")
        print(generated_text)
        print("----------------------")
