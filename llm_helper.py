from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

# Note: the original tutorial used "llama-3.2-90b-text-preview", which Groq
# has since deprecated. openai/gpt-oss-120b is their current recommended
# general-purpose model. Swap this if Groq deprecates it again -
# check https://console.groq.com/docs/models for the live list.
llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"), model_name="openai/gpt-oss-120b")

if __name__ == "__main__":
    response = llm.invoke("Two most important ingredients in samosa are ")
    print(response.content)