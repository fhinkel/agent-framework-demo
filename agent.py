from agents import Agent
import vertexai

from instruction import instruction_str

root_agent = Agent(
    model='gemini-2.0-flash',
    tools=[
        create_pdf,
        calculate_materials_list,
        analyze_local_codes,
        analyze_past_jobs,
    ],
    instruction = instruction_str,
)

