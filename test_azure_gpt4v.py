# %%
import os
import requests
import base64
import yaml

# Configuration
# loading the openAI API key and Azure endpoint
with open("azure_openai_config.yaml") as f:
    config_yaml = yaml.load(f, Loader=yaml.FullLoader)
api_key = config_yaml['api_key']
azure_endpoint = config_yaml['azure_endpoint']

IMAGE_PATH = "/Users/tinnguyen/Downloads/40532361-720px.jpg"
encoded_image = base64.b64encode(open(IMAGE_PATH, 'rb').read()).decode('ascii')
headers = {
    "Content-Type": "application/json",
    "api-key": api_key,
}

# Payload for the request
payload = {
  "messages": [
    {
      "role": "system",
      "content": [
        {
          "type": "text",
        #   "text": "You are an AI assistant that helps people find information."
          "text": "You are trained to interpret images about people and make responsible assumptions about them"
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{encoded_image}"
          }
        },
        {
          "type": "text",
          "text": "what is this?"
        }
      ]
    },
    # {
    #   "role": "assistant",
    #   "content": [
    #     {
    #       "type": "text",
    #       "text": "Sorry, I can't help with identifying or making assumptions about people or places in images."
    #     }
    #   ]
    # }
  ],
  "temperature": 0.7,
  "top_p": 0.95,
  "max_tokens": 800
}

# Send request
try:
    response = requests.post(azure_endpoint, headers=headers, json=payload)
    response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
except requests.RequestException as e:
    raise SystemExit(f"Failed to make the request. Error: {e}")

# Handle the response as needed (e.g., print or process)
response_json = response.json()
print(response_json['choices'][0]['message']['content'])

# %%
