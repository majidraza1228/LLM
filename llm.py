import os
from langchain.llms import OpenAI


api_key = "XXXXXXXXXXß" #os.getenv("OPENAI_API_KEY")

if api_key is None:
    raise ValueError("Please set the OPENAI_API_KEY environment variable.")

# Initiating the OpenAI LLM with the API key
llm = OpenAI(api_key=api_key)

# Query the model
response = llm.invoke("What is the tallest building in the world?")
print(response)