import streamlit as st
import pandas as pd
from dotenv import load_dotenv
from utils.data_summary import generate_csv_summary, display_csv_summary
from utils.question_answering import answer_question, suggest_visualization
from utils.visualizer import plot_chart


load_dotenv()

st.title("CSV Insights Assistant")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    display_csv_summary(df)
    
    context_text = generate_csv_summary(df)
    
    st.subheader("Ask a question about the dataset")
    question = st.text_input("Your question")

    if question:
        with st.spinner("Generating answer..."):
            answer = answer_question(context_text, question)
            st.success("Answer:")
            st.write(answer)
            
            try:
                suggestion = suggest_visualization(context_text, question)
                st.markdown("Suggested Visualization:")
                
                x_axis = suggestion.get("x_axis")
                y_axis = suggestion.get("y_axis")
                chart_type = suggestion.get("chart_type")
                
                if x_axis not in df.columns or (y_axis and y_axis not in df.columns):
                    st.warning("LLM suggested invalid columns for visualization.")
                    
                else:
                    st.info(f"LLM suggests a **{chart_type.upper()}** chart for `{x_axis}` vs `{y_axis}`")
                    justification = suggestion.get("justification")
                    
                    if justification:
                        st.markdown(f"**Why this chart?** {justification}")
                    
                    fig = plot_chart(df, chart_type, x_axis, y_axis)
                    st.pyplot(fig)
                    
            except Exception as e:
                st.warning(f"Could not generate a visualization suggestion: {e}")
                    
            
    st.subheader("Generate a manual Visualization from the dataset")
    
    # Separate columns by type
    categorical_cols  = df.select_dtypes(include=["object", "category"]).columns.tolist()
    numeric_cols  = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
    
    # Verify valid columns
    if categorical_cols and numeric_cols :
        x_axis = st.selectbox("Choose a categorical column (X axis)", categorical_cols)
        y_axis = st.selectbox("Choose a numeric column (Y axis)", numeric_cols)
        chart_type = st.selectbox("Select chart type", ["Bar Plot", "Box Plot", "Histogram"])
        
        if st.button("Generate Chart"):
            fig = plot_chart(df, chart_type, x_axis, y_axis)
            st.pyplot(fig)
            
        else:
            st.warning("No suitable categorical or numeric columns found to generate charts.")
    
            
else:
    st.info("Please upload a CSV file to get started.")