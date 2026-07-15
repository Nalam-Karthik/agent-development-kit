from google.adk.agents import LlmAgent
from pydantic import BaseModel, Field

class EmailContent(BaseModel):
    subject: str = Field(
        description="The subject line of the email. Should be concise and descriptive."
    )
    body: str = Field(
        description="The main content of the email. Should be well-formatted with proper greeting, paragraphs, and signature."
    )

root_agent = LlmAgent(
    name="email_agent",
    # Updated to the active 2026 free-tier model
    model="gemini-3.5-flash", 
    instruction="""
        You are an Email Generation Assistant.
        Your task is to generate a professional email based on the user's request.

        IMPORTANT: Your response MUST be valid JSON matching this structure:
        {
            "subject": "Subject line here",
            "body": "Email body here",
        }
    """,
    description="Generates professional emails with structured subject and body",
    output_schema=EmailContent,
    output_key="email",
)