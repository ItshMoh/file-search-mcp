
from mcp.server.fastmcp import FastMCP
from search import search_ques
mcp = FastMCP("Example tools")




@mcp.tool()
def search_qa(query: str) -> str:
    """Search for an answer to the query asked by the user in the file qa.txt. It finds the answer from the qa.txt file"""
    return search_ques(query)




