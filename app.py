import streamlit as st
from langchain_community.llms import Ollama
from langchain.embeddings import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

# Initialize Streamlit
st.set_page_config(page_title="Enhanced Response Evaluation", layout="centered")
st.title("🧠 LLM Response Evaluation System")
st.write("Generate an AI response and evaluate it against your ideal response!")

# Load models
llm = Ollama(model="gemma:2b")  # Local Ollama model
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Input section
st.subheader("🔍 Input Section")
user_prompt = st.text_area("Enter your prompt:", placeholder="Type your question or task here...", height=150)
ideal_response = st.text_area("Enter the ideal response for evaluation:", placeholder="Provide the expected correct answer...", height=150)

# Button to generate and evaluate the response
if st.button("🚀 Generate and Evaluate Response"):
    if not user_prompt or not ideal_response:
        st.warning("Please enter both the prompt and the ideal response to proceed.")
    else:
        # Generate response using LLM
        with st.spinner("Generating the AI response..."):
            llm_response = llm.invoke(user_prompt)
            llm_response = llm_response.strip() if isinstance(llm_response, str) else llm_response.content

        # Display the LLM response
        st.subheader("🤖 LLM Response:")
        st.info(llm_response)

        # Calculate similarity to the ideal response
        with st.spinner("Evaluating response..."):
            ideal_embedding = embedding_model.embed_query(ideal_response)
            generated_embedding = embedding_model.embed_query(llm_response)
            similarity_score = cosine_similarity([ideal_embedding], [generated_embedding])[0][0]

        # Display similarity score
        st.subheader("📊 Similarity Score:")
        st.progress(float(similarity_score))
        st.write(f"**{similarity_score:.2f}** (Higher is better)")

        # Provide feedback based on similarity score
        st.subheader("📝 Evaluation Feedback:")

        if similarity_score > 0.8:
            st.success("✅ The generated response is highly similar to the ideal response!")
            st.write("The response captures most of the key points and is very close to what was expected.")
        elif similarity_score > 0.6:
            st.warning("⚠️ The generated response is moderately similar. Some improvements are needed.")
            st.write("The response captures some of the key points but could be clearer or more relevant to the prompt.")
        else:
            st.error("❌ The generated response has low similarity to the ideal response. Consider revising the prompt or ideal response.")
            st.write("The response is significantly different from the ideal. Review the prompt or consider rewording the expected response for clarity.")

# Footer
st.markdown("---")
st.caption("✨ Developed with ❤️ using Streamlit and LangChain")
