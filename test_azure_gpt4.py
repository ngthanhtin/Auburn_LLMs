# %%
import yaml
import os
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
import dotenv
import base64
from mimetypes import guess_type

dotenv.load_dotenv()

#  %%
# loading the openAI API key and Azure endpoint
with open("azure_openai_config.yaml") as f:
    config_yaml = yaml.load(f, Loader=yaml.FullLoader)
api_key = config_yaml['api_key']
azure_endpoint = config_yaml['azure_endpoint']

client = AzureOpenAI(
    azure_endpoint = azure_endpoint,
    api_key=api_key,
      api_version="2024-02-15-preview"    
    )
    
# define the message here    
message_text = [{"role":"system","content":"What is the habitat of the Chipping Sparrow?"}]
deployment_name='testgpt4' #This will correspond to the custom name you chose for your deployment when you deployed a model.
response = client.chat.completions.create(
  model=deployment_name,
  messages = message_text,
  temperature=0.7,
  max_tokens=800,
  top_p=0.95,
  frequency_penalty=0,
  presence_penalty=0,
  stop=None
)

print(response)





