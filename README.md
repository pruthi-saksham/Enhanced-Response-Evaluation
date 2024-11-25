
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
streamlit run app.py
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

# Acknowledgments

- **Streamlit** for making interactive web applications with Python easy.
- **LangChain** for enabling AI-powered responses.
- **HuggingFace** for providing the embeddings and language models used in the evaluation.

