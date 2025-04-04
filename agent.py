from google.adk import Agent
from . import instruction, create_pdf, calculate_materials_list, analyze_building_codes, analyze_past_jobs

root_agent = Agent(        
    instruction=instruction,
    tools=[
        create_pdf,
        calculate_materials_list,
        analyze_building_codes,
        analyze_past_jobs,
    ],
    model='gemini-2.5-pro-exp',
)