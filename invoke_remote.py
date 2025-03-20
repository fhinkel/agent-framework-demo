from vertexai import agent_engines

remote_app = agent_engines.ReasoningEngine('projects/1096655024998/locations/us-central1/reasoningEngines/4101521419232346112')

remote_app.agent_run(
    session_id="session_1",
    message=types.Content(
        parts=[
            types.Part(
                text="Please create a contract for a bathroom renovation at address ... ",
                inline_data=image,
            )],
        role="user",
        req = {}).model_dump_json()
)

