


# Legislative Impact Advisor App

The Legislative Impact Advisor simplifies understanding the economic impact of legislation for individuals, translating complex bills into actionable insights. Developed for the MongoDB GenAI Hackathon, this app uses MongoDB to store data, Fireworks AI for generating embeddings, LlamaIndex for document reading, and Streamlit for the frontend.

### Mission Statement:
Our mission is to demystify legislative complexity, enabling every citizen to grasp the financial and personal implications of new laws. With insightful analytics, we convert legalese into clear, actionable intelligence, fostering informed decision-making for over 250 million adults in the U.S.

### Abstract:
The legislative landscape in the U.S. is vast, with over 10,000 bills passed annually, touching the lives of millions and influencing public spending in the trillions. Yet, the average citizen remains disengaged, a consequence of the overwhelming volume and complexity of information. Our application addresses this gap by synthesizing data from myriad sources — government sites to social platforms like Reddit — providing concise, personalized legislative summaries. With a potential reach to 2.5 million civically-engaged users, even a conservative market penetration represents a multi-million dollar opportunity. Our solution streamlines the fragmented process, offering an estimated monthly interaction with information pertinent to over 20% of the population, translating legislative changes into real-world financial impacts. By quantifying the potential cost or savings of each bill, typically ranging from hundreds to thousands of dollars per individual, we bring legislative awareness to the forefront, empowering communities with the knowledge to adapt, respond, and participate in the democratic process proactively.

### Brief on Solution, Efficacy, and Feasibility:
Our solution, an intelligent legislative impact app, is designed for efficacy and user engagement. It simplifies the complex maze of monthly bills and legal texts, which currently leads to community oblivion due to the opaqueness of legal terminology and scattered information. With legislative actions impacting the finances of millions, often altering monthly expenses by substantial margins, our app stands to offer crucial insights. By collating data from trusted and diverse sources, including official government sites and community-driven platforms like Reddit, the app promises a reliable and holistic view. Its feasibility is underpinned by advanced AI algorithms capable of parsing and interpreting vast amounts of legislative text, rendering it into understandable, relatable content. The app also features user-centric design, ensuring ease of navigation and personalization. In an ecosystem where public spending is intricately linked to personal budgets, and where a single bill can mean savings or costs in the hundreds to thousands of dollars for an individual, the app’s role in simplifying this complexity is both necessary and timely. With the public increasingly seeking transparency and simplicity, the app is not just a tool but a necessity for an informed, financially aware, and empowered populace.
## Project Structure

- **/data**: Contains raw and processed data used by the app.
- **/src**: Source code for the application logic and AI models.
- **/embeddings**: Generated embeddings from legislative documents.
- **app.py**: Main application script for the Streamlit frontend.
- **user.py**: User class definition for managing user profiles.
- **vectorsearch.py**: Handles vector search functionality for embeddings.
- **requirements-dev.lock & requirements.lock**: Locked dependencies for consistent builds.

## Tech Stack

- **Frontend**: Streamlit
- **Database**: MongoDB Atlas Cluster
- **AI Model**: Fireworks AI (`gte-large` model hosted on Fireworks AI by Alibaba)
- **Document Processing**: LlamaIndex  and agents for RAG Contex Enhacement and document readers + Mongo

+-----------------+         +------------------+         +-------------------+
|                 |  Read   |                  | Process |                   |
| LlamaIndex +      +-------->+ Fireworks AI     +-------->+ MongoDB Atlas     |
| Document Reader |         | Embedding Model  |         | Cluster (Document)           |
|                 |<--------+                  |<--------+                   |
+-----------------+  Update |                  |  Store  |                   |
                            +------------------+         +-------------------+
                                   ^                             |
                                   |                             |
                                   |                             v
                            +------------------+         +-------------------+
                            |                  |  Fetch  |                   |
                            | User Feedback    +<--------+ Streamlit Frontend|
                            | Processing       |         |                   |
                            +------------------+         +-------------------+


## Description:
- LlamaIndex Document Reader: This component reads and parses legislative documents, converting them into a format that can be further processed.
- Fireworks AI Embedding Model: This service processes the parsed documents from LlamaIndex, creating embeddings that capture the semantic essence of the text.
MongoDB Atlas Cluster: The processed embeddings are stored in MongoDB, which acts as the persistent data store for the application.
- Streamlit Frontend: This is the user interface that displays information to the user, collects user feedback, and sends it back to the processing services.
User Feedback Processing: A dedicated component or functionality within the Fireworks AI or Streamlit layer that processes user feedback to update the document analysis models, thus improving accuracy over time.

## Overview

The app parses complex legislative documents to extract meaningful data, processes this data into user-friendly formats, and stores the information in a MongoDB database. The processed data is then used to generate personalized insights, delivered through a Streamlit-based frontend.

## Process Flow

1. **Document Ingestion**: LlamaIndex agents scan and read legislative documents.
2. **Data Processing**: Fireworks AI's `gte-large` model creates embeddings from the document data.
3. **Database Storage**: The embeddings and processed data are stored in a MongoDB Atlas Cluster.
4. **User Interface**: Streamlit renders the frontend, displaying the latest legislative news and a chat interface for personalized inquiries.

## Key Features

- Real-time analysis of new bills and legislative actions.
- Personalized impact summaries reflecting the individual's specific concerns and interests.
- Seamless user experience with an intuitive chatbot powered by AI.

## Setup

Ensure you have MongoDB, Fireworks AI, LlamaIndex, and Streamlit set up in your development environment:

```shell
# Install necessary packages
pip install streamlit llama-index pymongo[srv] fireworks-ai
```

## Usage

To run the app, execute the Streamlit run command:

```shell
streamlit run app.py
```

---

This project is a testament to how AI can bridge the gap between complex legislation and the average person, promoting a well-informed and engaged community.

