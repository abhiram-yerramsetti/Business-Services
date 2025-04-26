# AI/ML Use Case Generator

A multi-agent system that generates relevant AI and Generative AI use cases for companies and industries using Google Gemini and LangChain.

## Features

- Industry and company research
- AI/ML use case generation
- Resource collection from various platforms
- Streamlit-based web interface
- Comprehensive reporting

## Architecture

The system consists of three main agents:

1. **Industry Research Agent**
   - Researches the company and its industry
   - Identifies key offerings and strategic focus areas
   - Uses web search capabilities

2. **Use Case Generator Agent**
   - Analyzes industry trends and standards
   - Proposes relevant AI/ML use cases
   - Focuses on process improvement and innovation

3. **Resource Collector Agent**
   - Collects relevant datasets and resources
   - Searches platforms like Kaggle, HuggingFace, and GitHub
   - Provides resource links and descriptions

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file with your API keys:
```
GOOGLE_API_KEY=your_google_api_key
GOOGLE_CSE_ID=your_google_cse_id
GOOGLE_API_KEY=your_google_api_key
```

3. Run the application:
```bash
streamlit run app.py
```

## Usage

1. Enter a company name in the input field
2. The system will:
   - Research the company and industry
   - Generate relevant use cases
   - Collect available resources
   - Generate a comprehensive report

## Output

The system generates a detailed report including:
- Industry research results
- Generated use cases
- Available resources and datasets
- Implementation recommendations

## Requirements

- Python 3.8+
- Google Gemini API key
- Google Custom Search Engine ID
- Internet connection for web searches 