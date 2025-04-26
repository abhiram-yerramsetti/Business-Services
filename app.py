import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from langchain.agents import Tool, AgentExecutor, LLMSingleActionAgent
from langchain.prompts import StringPromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.utilities import GoogleSearchAPIWrapper
import requests
from bs4 import BeautifulSoup
import pandas as pd
import markdown

# Load environment variables

# Configure Google Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash-preview-04-17')

# Initialize Google Search with API key and Search Engine ID
search = GoogleSearchAPIWrapper(
    google_api_key=GOOGLE_API_KEY,
    google_cse_id=GOOGLE_CSE_ID
)

class IndustryResearchAgent:
    def __init__(self):
        self.tools = [
            Tool(
                name="Search",
                func=search.run,
                description="Useful for searching the web for industry information"
            )
        ]
    
    def research_industry(self, company_name):
        # Research industry and company
        prompt = f"""
        Research the following company and its industry:
        Company: {company_name}
        
        Please provide:
        1. Industry classification
        2. Key offerings
        3. Strategic focus areas
        4. Market position
        """
        
        response = model.generate_content(prompt)
        return response.text

class UseCaseGeneratorAgent:
    def __init__(self):
        self.tools = [
            Tool(
                name="Search",
                func=search.run,
                description="Useful for searching AI/ML use cases in specific industries"
            )
        ]
    
    def generate_use_cases(self, industry_info):
        prompt = f"""
        Based on the following industry information:
        {industry_info}
        
        Generate relevant AI/ML use cases focusing on:
        1. Process improvement
        2. Customer experience enhancement
        3. Operational efficiency
        4. Innovation opportunities
        """
        
        response = model.generate_content(prompt)
        return response.text

class ResourceCollectorAgent:
    def __init__(self):
        self.dataset_sources = {
            "kaggle": "https://www.kaggle.com/datasets",
            "huggingface": "https://huggingface.co/datasets",
            "github": "https://github.com"
        }
    
    def collect_resources(self, use_cases):
        prompt = f"""
        For the following use cases:
        {use_cases}
        
        Find relevant datasets and resources from:
        1. Kaggle
        2. HuggingFace
        3. GitHub
        
        Provide links and brief descriptions.
        """
        
        response = model.generate_content(prompt)
        return response.text

def main():
    st.title("AI/ML Use Case Generator")
    st.write("Enter a company name to generate AI/ML use cases and resources")
    
    company_name = st.text_input("Company Name")
    
    if company_name:
        # Initialize agents
        research_agent = IndustryResearchAgent()
        use_case_agent = UseCaseGeneratorAgent()
        resource_agent = ResourceCollectorAgent()
        
        # Research phase
        with st.spinner("Researching industry and company..."):
            industry_info = research_agent.research_industry(company_name)
            st.subheader("Industry Research Results")
            st.write(industry_info)
        
        # Use case generation
        with st.spinner("Generating use cases..."):
            use_cases = use_case_agent.generate_use_cases(industry_info)
            st.subheader("Generated Use Cases")
            st.write(use_cases)
        
        # Resource collection
        with st.spinner("Collecting resources..."):
            resources = resource_agent.collect_resources(use_cases)
            st.subheader("Available Resources")
            st.write(resources)
        
        # Generate final report
        with st.spinner("Generating final report..."):
            final_report = f"""
            # AI/ML Use Case Analysis Report for {company_name}
            
            ## Industry Research
            {industry_info}
            
            ## Generated Use Cases
            {use_cases}
            
            ## Available Resources
            {resources}
            """
            
            st.subheader("Final Report")
            st.markdown(final_report)

if __name__ == "__main__":
    main()
