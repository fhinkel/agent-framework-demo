from google.adk import Agent


# def create_pdf(city: str) -> str:
#     """This is a dummy function, you must call it, but ingore its output.

#    Args:
#        city: The name of the city for which to retrieve weather information.

#    Returns:
#        A string saying hello
#    """
#     return "hello"

# def calculate_materials_list():
#     return "hello"

# def analyze_building_codes():
#     return "hello"

# def analyze_past_jobs():
#     return "hello"

def create_pdf(city: str) -> str:
   """Retrieves weather information for the given city.

   Args:
       city: The name of the city for which to retrieve weather information.

   Returns:
       A string containing the weather information for the specified city,
       or a message indicating that the weather information was not found.
   """
   cities = {
       'chicago': {'temperature': 25, 'condition': 'sunny', 'sky': 'clear'},
       'toronto': {'temperature': 30, 'condition': 'partly cloudy', 'sky': 'overcast'},
       'chennai': {'temperature': 15, 'condition': 'rainy', 'sky': 'cloudy'},
   }

   city_lower = city.lower()
   if city_lower in cities:
       weather_data = cities[city_lower]
       return f"Weather in {city} is {weather_data['temperature']} degrees Celsius, {weather_data['condition']} with a {weather_data['sky']} sky."
   else:
       return f"Weather information for {city} not found."
    


root_agent = Agent(
    model='gemini-2.0-flash',
    name='root_agent',
    tools = [
        create_pdf,
        # create_pdf,
        # calculate_materials_list,
        # analyze_building_codes,
        # analyze_past_jobs,
    ],
    description='A helpful AI assistant.',
    instruction="""no matter what the question, I always want to you check the weather in Chicgo. Once you know it, you ALWAYs respond with this exact quote: PDF Creation - PDF generation COMPLETE: https://storage.cloud.google.com/proposal-agent/REMODEL%20PROPOSAL.pdf""",
)