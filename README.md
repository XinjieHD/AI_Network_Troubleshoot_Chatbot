# Network Troubleshooting Assistant Chatbot

A basic AI chatbot with Python designed to help general users troubleshoot common network issues. This assistant leverages the **Llama 3.3 model** via **OpenRouter.ai's free API** for intelligent, step-by-step guidance.

## Features

* **AI-Powered Troubleshooting:** Utilizes Llama 3.3 to provide contextual, actionable advice.
* **User-Friendly Interface:** Guides users through common problems (Internet access, Wi-Fi, website issues).
* **Contextual Understanding:** Adapts responses based on the ongoing conversation.
* **Extensible:** Easily adaptable for specific network equipment troubleshooting or advanced diagnostics.

## Setup & Usage

1.  **Get an OpenRouter.ai API Key:** Sign up at [OpenRouter.ai](https://openrouter.ai/) and obtain your API key.
    **Note:**
       * Please be aware that while the Llama 3.3 model on OpenRouter.ai might currently be available as a "free model API," the pricing structure of AI models and APIs can change. Always check OpenRouter.ai's official pricing page to confirm any potential costs associated with your usage.
3.  **Replace Placeholder:** In `network_troubleshoot_chatbot.py`, replace `"<YOUR_OPENROUTER_API_KEY>"` with your actual API key.
4.  **Run:**
    ```bash
    python network_troubleshoot_chatbot.py
    ```

Interact with the chatbot by choosing numbered options or typing your questions. Type `menu` to see options again, or `exit` to quit.

<img width="905" height="397" alt="Screenshot 2025-07-30 at 19 00 52" src="https://github.com/user-attachments/assets/80d805c7-441f-4ecf-a793-efa638970f47" />
