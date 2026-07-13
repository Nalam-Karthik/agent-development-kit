from google.adk.agents import Agent
from google.adk.models import Gemini

root_agent = Agent(
    name="tool_agent",
    # Keep Gemma, but remove the unsupported tools
    model=Gemini(model="gemma-4-31b-it"), 
    description="Tool agent",
    instruction="You are a helpful assistant.",
    # Note: The tools parameter has been completely removed
)