PDF QUEST Chat App 📚💬
Introduction 🚀
The QuestChat App is a Python application that allows you to chat with multiple PDF documents. You can ask questions about the PDFs using natural language, and the application will provide relevant responses based on the content of the documents. This app utilizes a language model to generate accurate answers to your queries. Please note that the app will only respond to questions related to the loaded PDFs.

How It Works 🤖
MultiPDF Chat App Diagram

The application follows these steps to provide responses to your questions:

PDF Loading: 📄 The app reads multiple PDF documents and extracts their text content.

Text Chunking: 📝 The extracted text is divided into smaller chunks that can be processed effectively.

Language Model: 🧠 The application utilizes a language model to generate vector representations (embeddings) of the text chunks.

Similarity Matching: 📊 When you ask a question, the app compares it with the text chunks and identifies the most semantically similar ones.

Response Generation: ✍️ The selected chunks are passed to the language model, which generates a response based on the relevant content of the PDFs.

Dependencies and Installation ⚙️
To install the MultiPDF Chat App, please follow these steps:

Clone the repository to your local machine.

Install the required dependencies by running the following command:

Copy code
pip install -r requirements.txt
Obtain an API key from OpenAI and add it to the .env file in the project directory.

commandline
Copy code
OPENAI_API_KEY=your_secret_api_key
Usage 📝
To use the MultiPDF Chat App, follow these steps:

Ensure that you have installed the required dependencies and added the OpenAI API key to the .env file.

Run the main.py file using the Streamlit CLI. Execute the following command:

arduino
Copy code
streamlit run app.py
The application will launch in your default web browser, displaying the user interface.

Load multiple PDF documents into the app by following the provided instructions.

Ask questions in natural language about the loaded PDFs using the chat interface.

Contributing 🌟
This repository is intended for educational purposes and does not accept further contributions. It serves as supporting material for a YouTube tutorial that demonstrates how to build this project. Feel free to utilize and enhance the app based on your own requirements. 🚀👨‍💻






