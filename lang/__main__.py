"""Main module for the lang package."""

import os
from langchain.schema import BaseMessage, HumanMessage, SystemMessage
from openai import OpenAI


def main():
    """Main entry point for the application."""
    print("Hello from Lang!")
    print("LangChain is successfully installed!")
    print(f"OpenAI library is successfully installed! (version: {__import__('openai').__version__})")
    
    # Create some example messages to demonstrate LangChain is working
    messages = [
        SystemMessage(content="You are a helpful assistant."),
        HumanMessage(content="Hello, how are you?")
    ]
    
    print(f"\nCreated {len(messages)} LangChain messages:")
    for i, message in enumerate(messages, 1):
        print(f"  {i}. {type(message).__name__}: {message.content}")
    
    # Demonstrate OpenAI client initialization (without making actual API calls)
    print("\nOpenAI client initialization:")
    try:
        # Note: This doesn't make an API call, just initializes the client
        client = OpenAI(api_key="dummy-key-for-demo")
        print("  ✅ OpenAI client initialized successfully")
        print("  💡 To use OpenAI API, set your OPENAI_API_KEY environment variable")
    except Exception as e:
        print(f"  ❌ Error initializing OpenAI client: {e}")
    
    # Check for API key
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        print("  🔑 OPENAI_API_KEY environment variable is set")
    else:
        print("  ⚠️  OPENAI_API_KEY environment variable is not set")


if __name__ == "__main__":
    main()
