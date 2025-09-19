from dotenv import load_dotenv
import os
load_dotenv()  # take environment variables from .env.
def main():
    print("Hello from langchain-course!")
    print('OPEN_API_KEY : ', os.getenv('OPEN_API_KEY'))

if __name__ == "__main__":
    main()
