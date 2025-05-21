from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser

def answer_question(context: str, question: str) -> str:
    prompt = ChatPromptTemplate.from_template("""
You are an intelligent assistant that analyzes datasets.
Based on the following dataset summary, answer the question in clear, concise English.

Dataset Summary:
{context}

Question:
{question}
        """
    )
    
    parser = StrOutputParser()
    
    llm = ChatOpenAI(temperature=0.2, model="gpt-3.5-turbo")
    
    chain = prompt | llm | parser
    
    result = chain.invoke({"context": context, "question": question})
    
    return result

def suggest_visualization(context: str, question: str) -> dict:
    prompt = ChatPromptTemplate.from_template("""
You are a data visualization assistant.

Based on the following dataset summary and the user question, suggest an appropriate chart to visualize the answer.

Return a JSON with the following fields:
- x_axis (categorical column)
- y_axis (numeric column, optional if histogram)
- chart_type (one of: bar, box, histogram)
- justification (a short explanation in natural English why this chart fits)

Dataset Summary:
{context}

Question:
{question}
""")
    parser = JsonOutputParser()
    llm = ChatOpenAI(temperature=0.2, model="gpt-3.5-turbo")
    chain = prompt | llm | parser
    
    result = chain.invoke({"context": context, "question": question})
    
    return result