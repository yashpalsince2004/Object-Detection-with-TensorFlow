# MITRA Chat API

This repository contains the Chat API for the MITRA project, built with **FastAPI**.  
It provides endpoints to handle chatbot requests and integrates with the OpenAI API.

## Features
- FastAPI-based backend
- CORS support for cross-origin requests
- Integration with OpenAI API
- Environment variable configuration using `.env`

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/MITRA0616/chat_api.git
   cd chat_api
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Add your environment variables in a `.env` file:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   ```

4. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

5. Access the API docs at:  
   [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Developer

Created and maintained by **Yash Pal**  

- [LinkedIn](https://www.linkedin.com/in/yash-pal-since2004)

---
✨ Contributions and feedback are always welcome!
