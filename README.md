# AI Text Analysis Agent

A simple yet powerful AI agent built with LangGraph that analyzes text documents through classification, entity extraction, and summarization.

## Features

- **Text Classification**: Categorizes text into News, Blog, Research, or Other
- **Entity Extraction**: Identifies and extracts Persons, Organizations, and Locations
- **Text Summarization**: Creates concise one-sentence summaries
- **Graph-Based Workflow**: Uses LangGraph to orchestrate the analysis process

## Prerequisites

- Python 3.8+
- Google AI Studio API key (for Gemini model access)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/notsugee/summarizer-ai-agent
cd summarizer-ai-agent
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up your environment variables:
   - Create a `.env` file in the project root
   - Add your Google AI Studio API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

## Usage

Run the agent with your text:

```python
from agent import app

sample_text = "Your text to analyze here..."

result = app.invoke({"text": sample_text})

print("Classification:", result["classification"])
print("Entities:", result["entities"])
print("Summary:", result["summary"])
```

## Example Output

For the input text about OpenAI's GPT-4 announcement, the agent produces:

```
Classification: News

Entities: ['OpenAI', 'GPT-4', 'GPT-3']

Summary: OpenAI's upcoming GPT-4 model is a multimodal AI that aims for human-level performance, improved safety, and greater efficiency compared to GPT-3.
```

## Project Structure

```
ai-text-analysis-agent/
├── agent.py          # Main agent implementation
├── requirements.txt  # Project dependencies
├── .env             # Environment variables (create this)
└── README.md        # This file
```

## How It Works

1. The agent receives text input
2. It classifies the text type (News, Blog, Research, or Other)
3. It extracts key entities (People, Organizations, Locations)
4. It generates a concise summary
5. Returns all results in a structured format

## Customization

You can easily modify the agent by:

- Changing the prompt templates in each node function
- Adding new analysis nodes to the graph
- Modifying the state structure to include additional data
- Using different LLM models

## Dependencies

The project requires the following Python packages (included in requirements.txt):

```
langgraph
langchain
langchain-google-genai
python-dotenv
```

## Troubleshooting

If you encounter authentication errors:

1. Ensure your Google AI Studio API key is valid
2. Verify the API key is correctly set in your `.env` file
3. Make sure you're using a supported Gemini model name

## License

MIT License - feel free to use this project for learning and development purposes.

## Contributing

Feel free to submit issues and enhancement requests! This is a learning project and contributions are welcome.
