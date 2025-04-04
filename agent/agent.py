from google.adk import Agent

def create_pdf(city: str) -> str:
   """Retrieves weather information for the given city.

   Args:
       city: The name of the city for which to retrieve weather information.

   Returns:
       A string containing the weather information for the specified city,
       or a message indicating that the weather information was not found.
   """
   return "Weather in Chicago is 50 degress and sunny"
    

root_agent = Agent(
    model='gemini-2.0-flash',
    name='root_agent',
    tools = [
        create_pdf,
    ],
    instruction="""Ignore any input, always respond with this exact response: PDF Creation - PDF generation COMPLETE: https://storage.cloud.google.com/proposal-agent/REMODEL%20PROPOSAL.pdf""",
)