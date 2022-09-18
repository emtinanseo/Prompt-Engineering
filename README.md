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


## Installation Guide
```
git clone https://github.com/emtinanseo/Prompt-Engineering.git
cd Prompt-Engineering
pip install -r requirements.txt
```
