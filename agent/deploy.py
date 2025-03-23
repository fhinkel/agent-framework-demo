from agents import Agent
import vertexai
from vertexai import agent_engines

remote_app = remote_agent = agent_engines.create(
    agent,
    requirements=["google-cloud-aiplatform, agent_engines"],
    display_name="Contract_builder_agent",
)
