import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API Key
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("Missing GOOGLE_API_KEY environment variable")

# Initialize Gemini Client
client = genai.Client(api_key=GOOGLE_API_KEY)

# Set the model
model_name = "models/gemini-2.0-flash"

# Get user input
user_prompt = input("Enter your prompt: ")

# Create content from user input
contents = [
    types.Content(
        role="user",
        parts=[types.Part(text=user_prompt)]
    )
]

# Generate content
response = client.models.generate_content(
    model=model_name,
    contents=contents
)

# Print the output
print("\nResponse:\n")
print(response.candidates[0].content.parts[0].text)
