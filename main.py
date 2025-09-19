from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate 
from langchain_openai import ChatOpenAI
from langchain_ollama  import Ollama

load_dotenv()  # take environment variables from .env.


def main():
    print("Hello from langchain-course!")

    information = """
    Elon Reeve Musk (/ˈiːlɒn/ EE-lon; born June 28, 1971) is an international businessman and entrepreneur...
    """

    summary_template = """
    Given the information {information} about a person I want you to create:
    1. A short summary
    2. Two interesting facts about them
    """    

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], 
        template=summary_template
    )

    # LLM setup
   # llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    llm = ChatOpenAI(temperature = 0, model= "gemma3:270m")
    # Build the chain
    chain = summary_prompt_template | llm

    # Run the chain
    response = chain.invoke({"information": information})

    # Print the response
    print(response.content)


if __name__ == "__main__":
    main()
