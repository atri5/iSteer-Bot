#api key: sk-proj-GV5pRioFfMlefnoAwuPpT3BlbkFJgLWRgjOaJG26GkSwJBl1
import requests
from openai import OpenAI
client = OpenAI(api_key="sk-proj-GV5pRioFfMlefnoAwuPpT3BlbkFJgLWRgjOaJG26GkSwJBl1")


def get_assistants():
    api_key = "sk-proj-GV5pRioFfMlefnoAwuPpT3BlbkFJgLWRgjOaJG26GkSwJBl1"  # Replace with your actual OpenAI API key
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
def testing_api():
    thread = client.beta.threads.create()
    print(thread.id)
    message = client.beta.threads.messages.create(

    thread_id=thread.id,
    role="user",
    content="What is Tibco EBX?"
    )
    print("compiled message")
    run = client.beta.threads.runs.create_and_poll(
    thread_id=thread.id,
    assistant_id='asst_TzVYkTtxAeoFFu6xgrCUO4jr',
    instructions="Please address the user as Jane Doe. The user has a premium account."
    )

    print("started run")
    if run.status == 'completed': 
        messages = client.beta.threads.messages.list(
        thread_id=thread.id
    )
        print(messages)
    else:
        print(run.status)

# Example usage
assistants = get_assistants()
print(assistants)