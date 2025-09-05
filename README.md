# langExtract-ollama-vs-gemini
This repository demonstrates how to use the `langextract` library for structured data extraction with two different approaches:
1.  A free, locally-run model via Ollama (`gemma3:4b`).
2.  A paid, cloud-based model via the Google Gemini API (`gemini-1.5-flash`).

## Prerequisites

1.  **Python 3.8+**
2.  **Required libraries**:
    ```bash
    pip install langextract python-dotenv
    ```
3.  **(For Ollama)**: Install [Ollama](https://ollama.com/) and pull the model:
    ```bash
    ollama pull gemma3:4b
    ```
4.  **(For Gemini API)**: Get a [Google AI API Key](https://aistudio.google.com/app/apikey) and create a `.env` file in this directory with the following content:
    ```
    GOOGLE_API_KEY="YOUR_API_KEY_HERE"
    ```

## How to Run

### 1. Ollama (Local)

Make sure the Ollama application is running in your terminal. Then, execute the script:
```bash
python extract_ollama.py
```

### 2. Gemini API (Cloud)

Ensure your `.env` file is set up correctly. Then, run:
```bash
python extract_gemini.py
```

Of course. Here is the comparison in a clean, copy-and-paste-ready markdown format.

***

### Comparison: Ollama (Free & Local) vs. Gemini API (Paid & Cloud)

| Feature                 | Ollama (Free & Local) 💻                                                                    | Gemini API (Paid & Cloud) ☁️                                                                |
| ----------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| **Cost** 💰             | **Completely free.** The only costs are the hardware you own and the electricity to run it.       | **Pay-per-use.** You are billed based on the number of input and output tokens processed.     |
| **Privacy & Data** 🔒     | **Maximum privacy.** All data and processing happen on your local machine and never leave it. | Data is sent to Google's servers for processing, subject to their privacy policy.             |
| **Performance** 🚀      | Speed depends entirely on your computer's CPU, GPU, and RAM. Can be slow on older machines. | Very fast and highly scalable. Performance is consistent, with minor network latency.       |
| **Setup & Maintenance** 🛠️ | Requires one-time setup (install Ollama, download models). You manage updates yourself.       | **Minimal setup.** Just sign up for an API key. No maintenance is required from your side.      |
| **Hardware** 🖥️         | **High requirements.** Needs a significant amount of RAM (8GB+) and preferably a modern GPU.      | **No requirements.** Works on any device with a stable internet connection.                     |
| **Scalability** 📈      | Limited to the capacity of your single machine. Not designed for high-traffic applications.   | **Highly scalable.** Built to handle millions of requests for production-level applications.   |
| **Model Access** 🧠     | Access to a wide range of popular open-source models (Llama, Mistral, Gemma, etc.).           | Access to Google's state-of-the-art, proprietary models (Gemini Pro, Flash, Ultra).       |
| **Best For** ✅         | Hobbyists, developers prioritizing privacy, offline applications, and academic research.      | Production applications, businesses needing scalability, and projects requiring top-tier models. |
