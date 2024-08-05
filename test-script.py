import requests
from openai import OpenAI
import os
import json
import time
from dotenv import load_dotenv

load_dotenv()


api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)


def get_assistants():
    url = "https://api.openai.com/v1/assistants"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "OpenAI-Beta": "assistants=v2"
    }

    # Sending GET request
    response = requests.get(url, headers=headers)

    # Checking if the request was successful
    if response.status_code == 200:
        return response.json()  # Returns the JSON response with the list of assistants
    else:
        return f"Failed to fetch assistants: {response.status_code}, {response.text}"



class Chatbot:
    def __init__(self):
        self.conversation_history = []

    def add_message(self, user_message, bot_response):
        self.conversation_history.append({"user": user_message, "bot": bot_response})

    def get_context(self):
        return self.conversation_history[-5:]  # Get the last 5 messages for context

    def get_assistants(self):
        url = "https://api.openai.com/v1/assistants"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "OpenAI-Beta": "assistants=v2"
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return f"Failed to fetch assistants: {response.status_code}, {response.text}"

    def create_thread(self):
        return client.beta.threads.create()

    def add_message_to_thread(self, thread, user_message):
        return client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=user_message
        )

    def create_run(self, thread, assistant_id):
        return client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=assistant_id,
        )

    def wait_on_run(self, run, thread):
        while run.status == "queued" or run.status == "in_progress":
            run = client.beta.threads.runs.retrieve(
                thread_id=thread.id,
                run_id=run.id,
            )
            time.sleep(0.5)
        return run

    def pretty_print(self, messages):
        print("# Messages\n")
        str = ""
        for m in messages:
            str += f"{m.role}: {m.content[0].text.value}"
        return str

    def chat(self, user_message, assistant_id="asst_QSzB2T0DjTV8on1Cm1kSINch"):
        thread = self.create_thread()
        self.add_message_to_thread(thread, user_message)
        run = self.create_run(thread, assistant_id)
        run = self.wait_on_run(run, thread)
        messages = client.beta.threads.messages.list(thread_id=thread.id)

        bot_response = self.pretty_print(messages) 
        self.add_message(user_message, bot_response)
        
        return bot_response

if __name__ == "__main__":
    chatbot = Chatbot()
    while True:
        user_message = input("You: ")
        if user_message.lower() == "exit":
            break

        response = chatbot.chat(user_message)
        print(f"Bot: {response}")

        # Print the current context for debugging
#         # print("Context:", chatbot.get_context())
