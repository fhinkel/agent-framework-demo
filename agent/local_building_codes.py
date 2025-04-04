from google.adk.tools.toolbox_tool import ToolboxTool
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, SseServerParams
from google.adk.tools.tool_context import ToolContext

async def analyze_building_codes(feature: str, tool_context: ToolContext) -> str:
    """Get the building code relevant for a specific building feature.
    Args:
      feature: The feature to search for in the different building codes for the matching municipality. Such as window replacements and sinks. 
    Returns:
        A string summarizing local building code requirements
    """
    tools, exit_stack = await MCPToolset.from_server(
        connection_params=SseServerParams(
            url='https://127.0.0.1:5000/mcp/sse'
        )
    )
    
    local_building_codes_tool = [
        t for t in tools if t.name == 'local_building_codes'][0]
    return local_building_codes_tool.run_async({"description": feature}, tool_context)
