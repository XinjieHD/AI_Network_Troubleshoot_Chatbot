import requests
import json

def send_chat_message(user_message: str) -> str:
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": "Bearer <<YOUR_OPENROUTER_API_KEY>>",
            "Content-Type": "application/json",
        },
        data=json.dumps({
            "model": "meta-llama/llama-3.3-70b-instruct:free",
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You are a helpful network troubleshooting assistant for general users. "
                        "Provide concise and clear answers to help users resolve network issues. "
                        "Guide users step-by-step. "
                        "If a user asks a follow-up question related to a previous context "
                        "interpret it based on the ongoing conversation and provide specific, actionable advice. "
                        "When suggesting follow-up actions or options within your response, explain them clearly. "
                        "After providing a response, simply wait for the user's next input. "
                        "If the user types 'menu', display the main options. "
                        "If they type 'exit', end the conversation. "
                        "Do not automatically re-display the main menu or ask 'What else can I help you with?' "
                        "unless directly prompted by the user's action or if they type 'menu'."
                    )
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": user_message
                        }
                    ]
                }
            ],
        })
    )

    try:
        response_data = response.json()
        if response.status_code == 200 and "choices" in response_data and len(response_data["choices"]) > 0:
            return response_data["choices"][0]["message"]["content"]
        else:
            return f"Error: Could not get a valid response from the chatbot. Status: {response.status_code}, Error: {response_data.get('error', 'No error details provided')}"
    except json.JSONDecodeError:
        return f"Error: Failed to decode JSON response. Raw response: {response.text}"


def display_main_menu():
    print("What kind of network issue are you experiencing?\nYou can choose from the options below, or type your question directly:")
    print("1. Cannot access the internet")
    print("2. Wi-Fi connection problems")
    print("3. Specific websites not opening")
    print("\n(Type 'menu' to show options again, 'exit' to quit)")


if __name__ == "__main__":
    print("Hello! I'm your Network Troubleshooting Chatbot. How can I help you today?")
    display_main_menu()
    current_context = None

    predefined_main_options_map = {
        "1": {"text": "My device cannot access the internet.", "context": "internet_access"},
        "2": {"text": "My device cannot connect to Wi-Fi.", "context": "wifi_problems"},
        "3": {"text": "I cannot open a specific website.", "context": None}
    }

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == 'exit':
            print("Network Troubleshooting Chatbot: Goodbye! Hope your network runs smoothly!")
            break
        elif user_input.lower() == 'menu':
            display_main_menu()
            continue

        processed_input = user_input

        if user_input in predefined_main_options_map:
            option_info = predefined_main_options_map[user_input]
            processed_input = option_info["text"]
            current_context = option_info["context"]
            print(f"Network Troubleshooting Chatbot: You selected: {processed_input}")
        else:
            processed_input = user_input

        chatbot_response = send_chat_message(processed_input)
        print(f"Network Troubleshooting Chatbot: {chatbot_response}")
