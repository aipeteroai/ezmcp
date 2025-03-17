"""
A simple example of using ezmcp to create a server with tools.
"""

import base64
import json
import requests
from bs4 import BeautifulSoup
from ezmcp import ImageContent, TextContent, ezmcp
from typing import Annotated
from lxml import etree

# Create an ezmcp application
app = ezmcp("simple-server", debug=True)


def getAzureOpenAIModelInfo():
    return ""

def getClaudeModelInfo():
    return ""

def getGPTModelInfo():
    return ""


def getGeminiModelInfo():
    return ""

@app.tool(description="""This tool provides the latest model information for OpenAI GPT, Gemini, Claude, and Azure OpenAI GPT.
          If you are using an LLM model, please check the latest information and use the correct model, version, etc.          
          """)
async def llmModels(message: Annotated[str, "Enter the LLM model name to search. Example: claude, openai-gpt, gemini, azure-gpt"]):
    print(f"message: ", message)
    
    if "claude" in message.lower():
        model_info = getClaudeModelInfo()
        return [TextContent(type="text", text=model_info)]
    elif "openai-gpt" in message.lower():
        model_info = getGPTModelInfo()
        return [TextContent(type="text", text=model_info)]
    elif "azure-gpt" in message.lower():
        model_info = getAzureOpenAIModelInfo()
        return [TextContent(type="text", text=model_info)]
    elif "gemini" in message.lower():
        model_info = getGeminiModelInfo()
        return [TextContent(type="text", text=model_info)]
    else:
        return [TextContent(type="text", text=f"The requested '{message}' model information is not supported yet.")]


if __name__ == "__main__":
    for name, tool_info in app.tools.items():
        print(f"  - {name}: {tool_info['schema'].description}")
    print("\nPress Ctrl+C to stop the server")

    # Run the application
    app.run(host="0.0.0.0", port=7777)
