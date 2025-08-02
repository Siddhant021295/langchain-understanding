"""Example integration of LangChain with OpenAI."""

import os
from typing import Optional
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage


def create_openai_chat_model(api_key: Optional[str] = None) -> Optional[ChatOpenAI]:
    """
    Create a LangChain ChatOpenAI model.
    
    Args:
        api_key: OpenAI API key. If None, will try to get from environment.
        
    Returns:
        ChatOpenAI model instance or None if no API key available.
    """
    if api_key is None:
        api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        print("⚠️  No OpenAI API key found. Set OPENAI_API_KEY environment variable.")
        return None
    
    try:
        # Create a ChatOpenAI instance with LangChain
        chat_model = ChatOpenAI(
            model="gpt-3.5-turbo",
            temperature=0.7,
            api_key=api_key
        )
        return chat_model
    except Exception as e:
        print(f"❌ Error creating ChatOpenAI model: {e}")
        return None


def example_chat_completion():
    """Example of using LangChain with OpenAI for chat completion."""
    print("\n🤖 LangChain + OpenAI Chat Example")
    print("=" * 40)
    
    # Try to create the chat model
    chat_model = create_openai_chat_model()
    
    if chat_model is None:
        print("Cannot run example without OpenAI API key.")
        print("To run this example:")
        print("1. Get an API key from https://platform.openai.com/api-keys")
        print("2. Set it as environment variable: export OPENAI_API_KEY='your-key'")
        return
    
    # Create messages
    messages = [
        SystemMessage(content="You are a helpful assistant that responds concisely."),
        HumanMessage(content="Explain what LangChain is in one sentence.")
    ]
    
    try:
        print("🔄 Sending request to OpenAI...")
        # This would make an actual API call
        # response = chat_model.invoke(messages)
        # print(f"🤖 Response: {response.content}")
        
        # For demo purposes, just show what would happen
        print("📝 Messages that would be sent:")
        for i, msg in enumerate(messages, 1):
            print(f"   {i}. {type(msg).__name__}: {msg.content}")
        print("✅ (Actual API call commented out for demo)")
        
    except Exception as e:
        print(f"❌ Error making API call: {e}")


if __name__ == "__main__":
    example_chat_completion()
