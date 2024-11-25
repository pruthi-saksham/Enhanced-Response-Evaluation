
# Enhanced Response Evaluation
This **LLM Response Evaluation System** allows users to generate a response using a local **Ollama** model and compare it to an ideal response. The generated response is evaluated based on its similarity to the ideal response using **HuggingFace Embeddings** and **Cosine Similarity**. The system provides feedback on the quality of the response, including a similarity score and tailored feedback based on the score range.

# Features

- **Prompt-based Response Generation**: Generate AI responses to user-defined prompts.
- **Ideal Response Comparison**: Enter an ideal response for comparison.
- **Cosine Similarity Evaluation**: The generated response is compared with the ideal response using cosine similarity.
- **Feedback Based on Similarity Score**: Provides user-friendly feedback based on the similarity score:
  - **Highly Similar (>0.8)**: Success message with high similarity.
  - **Moderately Similar (0.6 - 0.8)**: Warning message with feedback for improvement.
  - **Low Similarity (<0.6)**: Error message indicating that the response needs significant improvement.
- **Real-Time Processing**: Uses Streamlit’s interactive UI to generate and evaluate responses in real-time.

# Prerequisites

- Python 3.7+
- Streamlit
- LangChain
- HuggingFace Transformers & Sentence-Transformers
- Scikit-learn
- Ollama (for LLM-based generation)
## Run Locally

1. Clone the project

```bash
git clone https://github.com/your-repo/LLM-Response-Evaluation.git
```

2. Go to the project directory

```bash
cd Enhanced Response Evaluation
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Start the server

```bash
python -m streamlit run app.py
```

5. *Open the app in your browser. The Streamlit interface will allow you to*:

- Enter a `prompt`(question) and the `ideal response`(answer).
- Click Generate and Evaluate Response to:
- Then you will generate a response using the Ollama model, evaluate it with Cosine Similarity to compute a similarity score, and provide feedback based on the score.



# Examples

 **Input**:
- Prompt: "What is the capital of France?"
- Ideal Response: "The capital of France is Paris."
**Output**:
- Generated Response: "Paris is the capital city of France."
- Similarity Score: 0.95
- Feedback: "✅ The generated response is highly similar to the ideal response! The response captures most of the key points and is very close to what was expected."

**Feedback Logic**
- *High Similarity (Score > 0.8)*: The response is almost identical to the ideal response. Positive feedback is given.
- *Moderate Similarity (0.6 ≤ Score ≤ 0.8)*: The response captures some of the key points, but room for improvement exists.
- *Low Similarity (Score < 0.6)*: The response deviates significantly from the ideal, and feedback suggests revising the response or the ideal.

  `The response and the similarity score will vary based on the model selected`

# Acknowledgments

- **Streamlit** for making interactive web applications with Python easy.
- **LangChain** for enabling AI-powered responses.
- **HuggingFace** for providing the embeddings and language models used in the evaluation.

This comprehensive set of functions ensures smooth operation, robust document processing, and an interactive user experience.

# 🚀 About Me
Hi, I’m Saksham Pruthi, an AI Engineer passionate about creating innovative AI-powered solutions. I specialize in Generative AI, designing systems that bridge cutting-edge research and practical applications. With expertise in various AI frameworks and an eye for scalable technology, I enjoy tackling challenging projects that drive real-world impact.

# 🛠 Skills
**Programming Languages**: Python, C++
**Generative AI Technologies**: Proficient in deploying and fine-tuning a variety of LLMs including Llama2, GPT (OpenAI), Mistral, Gemini Pro using frameworks like Hugging Face, OpenAI and Groq. Expertise in NLP tasks like tokenization, sentiment analysis, summarization, and machine translation. Skilled in computer vision (CV) with models for image classification, object detection, and segmentation (YOLO). Expertise in MLOps, building and maintaining pipelines for model training and monitoring. Proficient in conversational AI with platforms LangChain. Skilled in synthetic data generation and code generation
**Vector Databases and Embedding Libraries**: Proficient in ChromaDB and FAISS for efficient vector storage, retrieval, and similarity search.
**Frameworks, Tools & Libraries**: LangChain, HuggingFace , OpenAI API, Groq, TensorFlow, PyTorch, Streamlit.
**Databases**: MongoDB, ChromaDB
**Version Control**: Proficient in using Git for version control and GitHub for collaborative development, repository management, and continuous integration workflows.
