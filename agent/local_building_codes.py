from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, SseServerParams
from google.adk.tools.tool_context import ToolContext

async def analyze_building_codes(feature: str, ctx: ToolContext) -> str:
    """Get the building code relevant for a specific building feature.
    Args:
      feature: The feature to search for in the different building codes for the matching municipality. Such as window replacements or plumbing sinks. 
    Returns:
        A string summarizing local building code requirements
    """
    tools = await MCPToolset.from_server(
        connection_params=SseServerParams(url='https://mcp-601315048597.us-central1.run.app:5000/mcp/sse')
    )
    
    return await tools.get_tool('local_building_code').run_async({"code": feature}, ctx)

