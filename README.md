# Promt-Engineering

## Introduction
Large Language Models (LLM) coupled with multiple AI capabilities are able to generate images and text, and also approach/achieve human level performance on a number of tasks.  The world is going through a revolution in art (DALL-E, MidJourney, Imagine, etc.), science (AlphaFold), medicine, and other key areas, and this approach is playing a role in this revolution.

### Goal 
to explore strategies that generate prompts for LLMs to extract relevant entities from job descriptions and also to classify web pages given only a few examples of human scores.   


## Data
### Dataset 1
A client has a system that collects news artifacts from web pages, tweets, facebook posts, etc. The client is interested in scoring a given new artifact against a topic. The client has hired experts to score a few of these news items. The range of results between 0 and 10 signifies the degree of relevance of the news item to the topic “breaking news that may lead to public unrest”.

Some columns of this data are as follows
* Title: title of the item 
* Description: the content of the item
* Body: the content of the item
* Analyst_Average_Score: target variable - the score to be estimated

### Dataset 2
The data are job descriptions ( together named entities)  and  relationships between entities in json format. To understand more about where the data comes from, read [How to Train a Joint Entities and Relation Extraction Classifier using BERT Transformer with spaCy 3 | by Walid Amamou | Towards Data Science](https://towardsdatascience.com/how-to-train-a-joint-entities-and-relation-extraction-classifier-using-bert-transformer-with-spacy-49eb08d91b5c)

[Dataset Dev](https://github.com/walidamamou/relation_extraction_transformer/blob/main/relations_dev.txt): For development and training
[Dataset Test](https://github.com/walidamamou/relation_extraction_transformer/blob/main/relations_test.txt): For testing and final reportin


## Repo Structure
### Folders
#### Notebooks
* EDA is done in notebook [data_eda.ipynb](https://github.com/emtinanseo/Prompt-Engineering/blob/main/notebooks/data_eda.ipynb)
* Classification of news items using Cohere’s Few-shot classification in notebook [classification.ipynb](https://github.com/emtinanseo/Prompt-Engineering/blob/main/notebooks/classification.ipynb)
* Entity Extraction from job descriptions using Cohere's generative models in notebook [entity_extraction.ipynb](https://github.com/emtinanseo/Prompt-Engineering/blob/main/notebooks/entity_extraction.ipynb)


## Installation Guide
```
git clone https://github.com/emtinanseo/Prompt-Engineering.git
cd Prompt-Engineering
pip install -r requirements.txt
```
