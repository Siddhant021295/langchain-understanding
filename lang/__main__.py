"""Main module for the lang package."""

import os
from dotenv import load_dotenv
from langchain.schema import BaseMessage, HumanMessage, SystemMessage
from openai import OpenAI
from .config import config

# Load environment variables from .env file
load_dotenv()


def main():
    """Main entry point for the application."""
    print("Hello from Lang!")
    print("LangChain is successfully installed!")
    print(f"OpenAI library is successfully installed! (version: {__import__('openai').__version__})")
    
    # Show configuration status
    print(f"\n📋 Configuration Status:")
    config_status = config.validate_config()
    for key, value in config_status.items():
        status_icon = "✅" if value else "❌"
        if key == "openai_configured":
            print(f"  {status_icon} OpenAI API Key: {'Configured' if value else 'Not configured'}")
        else:
            print(f"  📝 {key.replace('_', ' ').title()}: {value}")
    
    # Create some example messages to demonstrate LangChain is working
    messages = [
        SystemMessage(content="You are a helpful assistant."),
        HumanMessage(content="Hello, how are you?")
    ]
    
    print(f"\n📨 Created {len(messages)} LangChain messages:")
    for i, message in enumerate(messages, 1):
        print(f"  {i}. {type(message).__name__}: {message.content}")
    
    # Demonstrate OpenAI client initialization (without making actual API calls)
    print("\n🔧 OpenAI client initialization:")
    try:
        # Note: This doesn't make an API call, just initializes the client
        api_key = config.get_openai_api_key() or "dummy-key-for-demo"
        client = OpenAI(api_key=api_key)
        print("  ✅ OpenAI client initialized successfully")
        
        if config.is_openai_configured():
            print("  🔑 Using API key from configuration")
        else:
            print("  💡 To use OpenAI API, add your key to the .env file")
            print("     Example: OPENAI_API_KEY=your-api-key-here")
            
    except Exception as e:
        print(f"  ❌ Error initializing OpenAI client: {e}")


if __name__ == "__main__":
    main()
