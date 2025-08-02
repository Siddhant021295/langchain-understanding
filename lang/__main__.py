"""Main module for the lang package."""

from langchain.schema import BaseMessage, HumanMessage, SystemMessage


def main():
    """Main entry point for the application."""
    print("Hello from Lang!")
    print("LangChain is successfully installed!")
    
    # Create some example messages to demonstrate LangChain is working
    messages = [
        SystemMessage(content="You are a helpful assistant."),
        HumanMessage(content="Hello, how are you?")
    ]
    
    print(f"Created {len(messages)} LangChain messages:")
    for i, message in enumerate(messages, 1):
        print(f"  {i}. {type(message).__name__}: {message.content}")


if __name__ == "__main__":
    main()
