from google.adk import Agent
import vertexai

from instruction import instruction_str

root_agent = Agent(        
    instruction = instruction_str,
    tools=[
        create_pdf,
        calculate_materials_list,
        analyze_building_codes,
        analyze_past_jobs,
    ],
    model='gemini-2.5-pro-exp',
)

