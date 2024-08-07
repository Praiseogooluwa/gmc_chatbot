# GMCc_Chatbot
This project involves developing an intelligent chatbot that uses Natural Language Processing (NLP) techniques to understand and respond to user queries then we use tensor flow to build and train the NLP model on a data set. Additionally, implementing sentiment analysis and entity recognition to create a robust and interactive chatbot.

## BUILDING GMC CHATBOT

- `Sentiment analysis`: Sentiment analysis is the process of determining the emotional tone behind a series of words, used to understand attitudes, opinions, and emotions; it includes positive, negative, or neutral. 

- `NLP`: It stands for Natural Language Processing which is a field of artificial intelligence that focuses on the interaction between computers and humans using natural language. NLP enables computers to understand, interpret, and generate human language in a valuable way. 

- `Entity Recognition`: Entity recognition, also known as named entity recognition (NER), is a natural language processing task that involves identifying and categorizing key information (entities) within a text, such as names of persons, organizations, locations, dates, and other specific types of information

- `TensorFlow`: TensorFlow empowers users to explore, experiment, and innovate in the field of machine learning, enabling the development of intelligent applications that can solve diverse problems across different domains.

- `Chatbot`: The primary goal of a chatbot is to understand user input, process it using natural language understanding (NLU) techniques, and generate appropriate responses. Depending on their complexity, chatbots can perform a wide range of tasks, including answering questions, providing customer support, assisting with transactions, and even engaging in casual conversation.

## ABOUT THE DATA
The dataset available is a comprehensive collection of conversations related to educational consultation. It encompasses various conversation types, including basic exchanges, and frequent asked question. 

`Dataset Source`: My Brain and series of questions from people

STEPS TAKEN
---

1. `Data Collection and Preprocessing`: Gather data of user queries and corresponding responses and use it to train the model.

2. `Use NLP Techniques`: Select NLP techniques such as tokenization, stemming, and lemmatization based on the requirements of the chatbot for data preprocessing and cleaning.

3. Choose a suitable framework or library for NLP development, such as TensorFlow.keras, based on the project's requirements

4. Implement and train the chatbot
- Select a development platform
- Implement the NLP Technique
- Train the chatbot
***Ensure building and training the NLP model using the selected framework.***

5. `Implement Sentiment Analysis`: Integrate sentiment analysis techniques to determine sentiment (positive, negative, or neutral) understand the emotional tone of user queries, and provide appropriate responses.

6. `Incorporate Entity Recognition`: Implement entity recognition to identify and extract specific entities such as names, dates, and locations from user queries.

7. `Testing and Evaluation`: Test the chatbot with a variety of queries to ensure that it accurately understands and responds to user input. Evaluate its performance and make adjustments when needed. `Adam Optimizer` and `Accuracy metrics` was used to evaluate the model's performance.

8. `Deployment`: Deploy your chatbot to a suitable platform or environment where users can interact with it. Streamlit was used to deploy the chatbot.

***Two environments were created; one containing the chatbot algorithm `bot.py` and the other contains the deployment of the chatbot using Streamlit app `my_bot.py`***

WEB APP LINK: https://gmc-bot-praise.streamlit.app
