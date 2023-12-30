# GroupChat AI Bot

This project implements a Flask-based AI bot to interact with a GroupMe chat. The bot, named Jarvis, leverages the OpenAI GPT-3.5 model to respond to specific triggers and engage in conversations within a group chat.

## Technologies Used

-   **Flask**: Web framework used for handling HTTP requests and responses.
-   **OpenAI GPT-3.5 and 4.0**: AI language model used for generating conversational responses.
-   **requests**: Python library for making HTTP requests.
-   **dotenv**: Python library for loading environment variables from a `.env` file.

## Setup

### Environment Variables

1.  Create a `.env` file in the project root.
2.  Add the following environment variables to the `.env` file:
        
    `OPENAI_API_KEY=<Your_OpenAI_API_Key>
    GROUPME_BOT_ID=<Your_GroupMe_Bot_ID>` 
    

### Installation

1.  Clone the repository:
        
    `git clone https://github.com/your-username/groupchat-ai-bot.git
    cd groupchat-ai-bot` 
    
2.  Install dependencies:
    
    `pip install -r requirements.txt` 
    

### Run the Application

Run the Flask application using the following command:

`python app.py` 

## Usage

1.  Configure the GroupMe webhook to point to `<your_server_url>/webhook`.
2.  Jarvis will respond to messages containing "jarvis" or "ultron" within the GroupMe chat by using the OpenAI GPT-3.5 model to generate witty responses.
3.  Messages sent to Jarvis trigger responses based on predefined scenarios, maintaining humorous and engaging interactions within the chat.

## Notes

-   Ensure the proper setup of environment variables for `OPENAI_API_KEY` and `GROUPME_BOT_ID`.
-   Customize the AI responses, triggers, and scenarios as needed within the codebase.

