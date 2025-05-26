import streamlit as st
import openai
import os

# Set OpenAI API Key securely
openai.api_key = "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"  # Replace with your key or use environment variables

def ask_energy_question(question):
    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an expert in energy efficiency and HVAC systems."},
                {"role": "user", "content": question}
            ],
            temperature=0.5,
            max_tokens=300
        )
        return response.choices[0].message.content
    except openai.APIError as e:
        return f"OpenAI API Error: {e}"
    except Exception as ex:
        return f"Unexpected error: {ex}"

# --- Streamlit UI ---
st.set_page_config(page_title="Energy Estimator", page_icon="💡")

# Header
st.markdown(
    """
    <div style='text-align: center;'>
        <h1 style='color: #2c3e50;'>🔋 AI Energy Estimation Assistant</h1>
        <p style='font-size:18px;'>Smart energy estimates powered by GPT-4o — built by IntuiNext Inc.</p>
    </div>
    """, unsafe_allow_html=True
)

# Input section
with st.container():
    st.subheader("💭 Ask a Question About Energy Usage")
    st.markdown("*Examples:*\n- How much energy is needed to cool a 1200 sq ft house?\n- What's the average electricity cost for heating in winter?")
    
    question = st.text_input("Enter your question:", placeholder="e.g., energy needed to cool a 1200 sq ft house")

    if st.button("🔍 Get Estimate"):
        if question.strip():
            with st.spinner("Crunching numbers..."):
                answer = ask_energy_question(question)
                st.success("✅ Estimate Ready:")
                st.write(answer)
        else:
            st.warning("Please enter a question.")

# Footer
st.markdown(
    """
    <hr style="margin-top: 2em;">
    <div style='text-align: center; font-size: 14px; color: gray;'>
        ⚡ Built with OpenAI and Streamlit by IntuiNext Inc. | Designed for energy-conscious users
    </div>
    """, unsafe_allow_html=True
)
