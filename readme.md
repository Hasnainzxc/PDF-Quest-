# MultiPDF Chat App 📚💬

**Discover the Tutorial on YouTube!** 📺

## Introduction 🚀
The MultiPDF Chat App is a Python marvel that lets you engage in conversations with multiple PDF documents. Using natural language, you can inquire about the PDFs, and the app will deliver insightful responses based on the document content. It's your personal chat companion, driven by a powerful language model, providing precise answers to your queries. Please keep in mind that the app exclusively answers questions related to the loaded PDFs.

## How It Works 🤖
![MultiPDF Chat App Diagram](./docs/PDF-LangChain.jpg)

Here's how the magic unfolds:

1. **PDF Loading**: 📄 The app dives into multiple PDF documents, extracting their textual essence.

2. **Text Chunking**: 📝 The extracted text is intelligently divided into bite-sized chunks for efficient processing.

3. **Language Model**: 🧠 The app employs a language model to create vector representations (embeddings) of these text chunks.

4. **Similarity Matching**: 📊 When you pose a question, the app compares it with the text chunks, identifying the most semantically aligned ones.

5. **Response Generation**: ✍️ The selected chunks visit the language model, which crafts responses grounded in the pertinent PDF content.

## Dependencies and Installation ⚙️
Get your app up and running with these steps:

1. **Clone the Repository**: 📦 Bring the repository home to your local machine.

2. **Install Dependencies**: 🛠️ Fire up your terminal and run:
   ```
   pip install -r requirements.txt
   ```

3. **API Key from OpenAI**: 🔑 Obtain an API key from OpenAI and tuck it into the `.env` file in the project directory.
   ```env
   OPENAI_API_KEY=your_secret_api_key
   ```

## Usage 📝
Unleash the magic of the MultiPDF Chat App with these steps:

1. **Dependency Check**: 🧐 Make sure you've got the dependencies sorted and that your API key is resting comfortably in the `.env` file.

2. **Launch the App**: 💻 Fire up the app by running `main.py` using the Streamlit CLI:
   ```
   streamlit run app.py
   ```

3. **User Interface**: 🌐 Your default web browser will usher in the app's user interface.

4. **Load PDFs**: 📂 Follow the instructions to load multiple PDF documents into the app.

5. **Ask Away**: 💬 Utilize the chat interface to ask questions in plain language about the PDFs.

## Contributing 🌟
This repository is an educational gem and isn't open for further contributions. It stands as a cornerstone for a YouTube tutorial, showcasing the art of building this project. Feel free to adapt and elevate the app to meet your unique needs.

## License 📜
The MultiPDF Chat App is set free under the MIT License. 🌐
