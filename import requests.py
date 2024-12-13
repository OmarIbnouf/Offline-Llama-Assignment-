import requests
import json

# Define the URL for the Llama API
url = "http://localhost:11434/api/generate"

# Read the input text from the file
with open("input.txt", "r", encoding="utf-8") as file:
    input_text = file.read()

# Prepare the headers and data for the API request
headers = {
    "Content-Type": "application/json"
}

data = {
    "model": "llama2",
    "prompt": f"Summarize the following text in French using simple language suitable for a 5th grader: {input_text}",
    "stream": False
}

# Make the POST request to the Llama API
response = requests.post(url, headers=headers, data=json.dumps(data))

# Process the API response
if response.status_code == 200:
    response_text = response.text
    response_data = json.loads(response_text)
    summary = response_data.get("response", "")

    # Save the summary to a file
    with open("summary.txt", "w", encoding="utf-8") as output_file:
        output_file.write(summary)

    print("Summary generated and saved to summary.txt")
else:
    print("Error:", response.status_code, response.text)
