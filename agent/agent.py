from google.adk import Agent

root_agent = Agent(
    model='gemini-2.0-flash',
    name='root_agent',
    description='A helpful AI assistant.',
    instruction="No matter waht the quesiton is, you ALWAYs respond with this exact quote: PDF Creation - PDF generation COMPLETE: https://storage.cloud.google.com/proposal-agent/REMODEL%20AGREEMENT.pdf",
)