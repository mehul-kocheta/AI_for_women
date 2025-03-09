# Project README

## Overview
This project utilizes an LLM to perform various AI-driven tasks. To get started, you need to install Ollama and set up the required LLM model.

## Prerequisites
- A system with a compatible operating system (Linux/Mac/Windows)
- [Ollama](https://ollama.ai) installed
- Internet connection to download the required model
- Classifier model is available at [drive](https://drive.google.com/drive/folders/1zzn820Zs5hyyFA0Tb27xBcO4wjdZWLKv?usp=sharing)

## Installation

### Step 1: Install Ollama
Download and install Ollama from the official website:

```sh
curl -fsSL https://ollama.ai/install.sh | sh
```

For Windows, follow the installation guide on the [Ollama website](https://ollama.ai).

### Step 2: Install Llama3.2 Model
Once Ollama is installed, download and set up the latest Llama3.2 model:

```sh
ollama pull llama3.2:latest
```

This will download and prepare the model for use.

## Usage
After installation, you can run the model using:

```sh
ollama run llama3.2:latest
```

You can also integrate it into your Python scripts or other applications using Ollama's API.

### Running the Summarizer
After setting up the model, you can run `summarizer.py` to summarize each subreddit and store the results in a text file:

```sh
python summarizer.py
```

The output will be saved as `subreddit_summaries.txt`.

### Running the Topic Classifier
The topic classifier processes subreddit text data and converts it into context vectors using BERT. It then fine-tunes BERT with custom labels for classification. To execute the classifier, run:

```sh
jupyter notebook subreddit_topic_classifier.ipynb
```

The outputs are saved in `subreddit_topic_classifier.ipynb`.

### Running the Toxicity and Misogyny Classifier
The `test.py` script analyzes individual comments by identifying their parent comments and classifying whether they are toxic and if they contain misogynistic content. To execute the classifier, run:

```sh
python test.py
```

## License
This project is open-source. Refer to the LICENSE file for more details.

## Contact
For any queries or support, feel free to reach out.