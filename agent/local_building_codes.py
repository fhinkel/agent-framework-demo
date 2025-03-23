from agents.tools.toolbox_tool import ToolboxTool
from toolbox_langchain import ToolboxClient

toolbox = ToolboxClient("https://toolbox-601315048597.us-central1.run.app/")
local_building_codes_tool = toolbox.load_tool("local-building-codes")

def analyze_building_codes(feature: str) -> str:
    """Get the building code relevant for a specific building feature.
    Args:
      feature: The feature to search for in the different building codes for the matching municipality. Such as toilet or water heaters. 
    Returns:
        A string summarizing local building code requirements
    """
    return local_building_codes_tool.invoke({"description": feature})  