from google.adk import Agent

from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, SseServerParams, StdioServerParameters

import asyncio
from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from google.adk.artifacts.in_memory_artifact_service import InMemoryArtifactService

load_dotenv()


async def get_tools_async():
    """Gets tools from MCP Server."""
    tools, exit_stack = await MCPToolset.from_server(
        connection_params=SseServerParams(
            url='http://127.0.0.1:5000/mcp/sse'
        )
    )
    # MCP requires maintaining a connection to the local MCP Server.
    # Using exit_stack to clean up server connection before exit.
    return tools, exit_stack


async def get_agent_async():
    """Creates an ADK Agent with tools from MCP Server."""
    tools, exit_stack = await get_tools_async()
    # print names of all tools
    # for tool in tools:
    # print(tool._get_declaration().description)
    # print()

    my_tool = tools[0]

    root_agent = Agent(
        model='gemini-2.0-flash',
        name='porposal_builder',
        instruction='Help the user get hotel information',
        tools=tools,
    )
    return root_agent, exit_stack


async def async_main():
    session_service = InMemorySessionService()
    artifacts_service = InMemoryArtifactService()
    session = session_service.create_session(
        state={}, app_name='proposal_builder', user_id='123'
    )
    query = "Find hotels in Basel"
    # query = "SELECT * FROM hotels WHERE location ILIKE 'Basel'"

    print('user: ', query)
    content = types.Content(role='user', parts=[types.Part(text=query)])
    root_agent, exit_stack = await get_agent_async()
    runner = Runner(
        app_name='proposal_builder',
        agent=root_agent,
        artifact_service=artifacts_service,
        session_service=session_service,
    )
    events_async = runner.run_async(
        session_id=session.id, user_id='123', new_message=content

    )
    async for event in events_async:
        print(event)
    await exit_stack.aclose()

if __name__ == '__main__':
    asyncio.run(async_main())
