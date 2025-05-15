from mcp.server.fastmcp import FastMCP
import json
server = FastMCP("ExamBOT")


import re

def search_ques(query, filepath="/home/kayden/Desktop/python_projects/SearchMCP/qa.txt"):
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            if "::" not in line:
                continue
            question, answer = line.strip().split("::", 1)
            # Simple substring search; you can improve this with fuzzy matching
            if query.lower() in question.lower():
                print(answer)
                return answer
    return "No answer found."

# if __name__ == "__main__":
#     print(search_qa("What is Python?"))

@server.tool()
def search_qa(query: str) -> str:
    """Search for an answer to the query asked by the user"""
    return search_ques(query)


if __name__ == "__main__":
    server.run(transport="stdio")