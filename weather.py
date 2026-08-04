import httpx
from mcp.server.fastmcp import FastMCP
##FastMCP--it is a helper class that handles MCP protocol

mcp = FastMCP("Weather Server")##Naming the MCP as Weather Server


@mcp.tool()##telling claude that it is a callable tool
async def get_weather(city: str) -> str:
    """Get current weather for a city"""
    
    url = f"https://wttr.in/{city}?format=3"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.text
    
##wrttr.in-->a free weather api,no key needed
##httpx.AsyncClient makes an async HTTP request

if __name__ == "__main__":
    mcp.run(transport="stdio")##server communicates through standard input/output