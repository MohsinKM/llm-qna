
# LLM Based Question and Answering App


This project is a simple question and answering app that utilizes state-of-the-art language models and tools such as OpenAI, Langchain, Llama_index, and Gradio. The app is designed to answer user’s questions based on a previously given document. With its advanced natural language processing capabilities, the app provides accurate and relevant answers to user queries

## Environment Setup

Before running this script make sure that you have the environment setup. I have tested it python3.10. 
This script will use OpenAI API Key. So make sure you have the API Key ready and set it in the environment.
The full Windows environment snapshot is shared in **_full_environment_windows.txt_** file. 
For linux/Ubuntu please use **_full_environment.txt_** file. If you encounter pip failing to resolve dependancy then edit the 
requirement file by removing specific version. 
Packages: gradio, langchain, llama-index, tiktoken, openai, pypdf

You can run this following command to install all the required packages.
```bash
pip install -r requirements.txt
```

## Usage

Make sure that you have OpenAI API key as a environment variable named as **_OPENAI_API_KEY_**

```bash
$ python -m main.py
```

## Author

KM Mohsin (mohsin.eee@gmail.com) 
