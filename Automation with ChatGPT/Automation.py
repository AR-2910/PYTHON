import requests
import argparse
import os

# Parse command-line arguments
my_parser = argparse.ArgumentParser()
my_parser.add_argument("askAI", help="Prompt for the AI to generate a Python script")
my_parser.add_argument("filename", help="Name of the file to save the generated script")
args = my_parser.parse_args()

# Endpoint URL for ChatGPT API
gpt_endpoint = "https://api.openai.com/v1/chat/completions"

# Get API key from environment variable
gpt_key = os.getenv("OPENAI_API_KEY")

# Headers for HTTP request to ChatGPT API
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + gpt_key
}

# Data input for the ChatGPT API request
data_input = {
    "model": "gpt-3.5-turbo",
    "messages": [{
        "role": "user",
        "content": f"write a python script for {args.askAI}. provide only code, no text"
    }],
    "max_tokens": 100,  # Maximum number of tokens in the generated response
    "temperature": 0.5  # Creativity level of the response
}

# Send HTTP POST request to ChatGPT API
prompt = requests.post(gpt_endpoint, headers=headers, json=data_input)

# Process API response
if prompt.status_code == 200:
    # Extract the generated response from the API
    result = prompt.json()["choices"][0]["message"]["content"]
    with open(args.filename, "w") as file:  #Opens the file in write mode or creates a new one if it doesn't exist.
        file.write(result)
else:
    # Print error message if API request fails
    print(f"Request failed with status code = {str(prompt.status_code)}")


