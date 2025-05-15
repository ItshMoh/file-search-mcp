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


