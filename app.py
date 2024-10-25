import streamlit as st
from sentiment_analysis import sentiment_analysis
from translator import translation
from summarization import summarization
from central_LLM import central_router

def main():
    st.title("Multipurpose LLM")
    st.write("Enter your prompt, and bot will assist you.")

    user_input = st.text_area("Your Prompt", height=150)
    if st.button("Submit"):
        if user_input.strip():
            with st.spinner("Analyzing your prompt..."):
                task = central_router(user_input)
            st.write(f"**Selected Task:** {task.replace('_', ' ').title()}")

            with st.spinner(f"Processing with {task.replace('_', ' ').title()}..."):
                if task == 'translation':
                    output = translation(user_input)
                elif task == 'sentiment_analysis':
                    output = sentiment_analysis(user_input)
                elif task == 'summarization':
                    output = summarization(user_input)

            st.success("Done!")
            st.write(output)
        else:
            st.warning("Please enter a prompt.")

if __name__ == "__main__":
    main()




