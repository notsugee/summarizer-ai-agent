import os 
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables 
load_dotenv()

# Initialize the ChatGoogleGenerativeAI instance 
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# Testing 
response = llm.invoke("Hello! Are you working?")
print(response.content)
