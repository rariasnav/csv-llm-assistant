import pandas as pd
import streamlit as st

def generate_csv_summary(df: pd.DataFrame, max_rows: int = 5) -> str:
    """
    Generates a text summary of a DataFrame for use as LLM context.
    """
    summary = []
    
    # General information
    summary.append(f"Tha data set has {df.shape[0]} rows and {df.shape[1]} columns.\n")
    
    # Data types
    summary.append("Column types:\n")
    for col in df.columns:
        dtype = df[col].dtype
        summary.append(f"- {col}: {dtype}")
        
    # Null values
    nulls = df.isnull().sum()
    if nulls.any():
        summary.append("\n Missing values:\n")
        for col, count in nulls.items():
            if count > 0:
                summary.append(f"- {col}: {count} missing")
    
    # Basic statistics
    desc = df.describe(include='all').transpose()
    summary.append("\n Summary statistics (first 3 columns):\n")
    for col in desc.head(3).index:
        stats = desc.loc[col].to_dict()
        summary.append(f" - {col}:")
        for k, v in stats.items():
            summary.append(f"    {k}: {v}")
    
    # Data sample
    summary.append("\n Sample rows:\n")
    summary.append(df.head(max_rows).to_string(index=False))
    
    return "\n".join(summary)

def display_csv_summary(df: pd.DataFrame, max_rows: int = 5):
    """
    Displays a structured summary in Streamlit (interactive + visual).
    """    
    st.subheader("Preview")
    st.dataframe(df.head())
    
    st.subheader("Column types")
    col_types = pd.DataFrame(df.dtypes.astype(str), columns=["Type"])
    st.dataframe(col_types)
    
    nulls = df.isnull().sum()
    if nulls.any():
        st.subheader("Missing values")
        st.dataframe(nulls[nulls > 0].to_frame(name="Missing values"))
        
    st.subheader("Summary statistics")
    desc = df.describe(include='all').transpose()
    st.dataframe(desc)
    
    if max_rows is None:
        max_rows = 5
    
    st.subheader("Sample rows (text)")
    st.code(df.head(max_rows).to_string(index=False))
    