# Conversational AI Chatbot with Gemini API

## Project Overview

A Python-based conversational AI chatbot integrated with Google's Gemini API. The chatbot maintains conversation history, allowing it to retain context from previous interactions and generate more relevant, context-aware responses.

## Key Features

- **Gemini API Integration:** Connects Python with Google's Gemini language model.
- **Conversational History:** Maintains previous interactions between the user and chatbot.
- **Context-Aware Responses:** Uses conversation history to provide responses based on previous messages.
- **Prompt Handling:** Sends user queries to the Gemini model and processes generated responses.
- **Secure API Authentication:** Uses environment variables to manage API credentials securely.

## Technologies Used

- Python
- Google Gemini API
- Google GenAI SDK
- Python-dotenv

## Project Structure

```text
Conversational-AI-Chatbot/
│
├── chatbot1.py
├── chatbot2.py
├── requirements.txt
├── .gitignore
└── README.md
```

**Main Implementation:** `chatbot2.py` contains the conversational history functionality.

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/snehaahuja11/Conversational-AI-Chatbot.git
```

### 2. Navigate to the Project Directory

```bash
cd Conversational-AI-Chatbot
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API Key

Create a `.env` file in the project directory and add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

Get your API key from Google AI Studio.

### 5. Run the Chatbot

```bash
python chatbot2.py
```

## Security

The Gemini API key is stored in an environment variable using a `.env` file. Sensitive credentials are excluded from version control using `.gitignore`.

## Project Objective

To understand LLM integration with Python and explore how conversation history can be used to maintain context and build more interactive conversational AI applications.



[GitHub Profile](https://github.com/snehaahuja11)
