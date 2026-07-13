from google.adk import Agent
from google.adk.models import Gemini

# The variable must be named exactly 'root_agent' for the ADK CLI to find it
root_agent = Agent(
    name="greeting_agent",
    model=Gemini(model="gemma-4-31b-it"), 
    instruction="You are a helpful assistant. Greet the user warmly."
)