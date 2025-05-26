from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts import base
import httpx
import os

BRAVE_API_KEY = os.environ.get("BRAVE_API_KEY")

mcp = FastMCP("read_the_docs")

@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b

@mcp.tool()
async def search_brave(query: str) -> list:
    headers = {"X-Subscription-Token": BRAVE_API_KEY}
    params = {"q": query, "count": 3}
    async with httpx.AsyncClient() as client:
        r = await client.get("https://api.search.brave.com/res/v1/web/search", headers=headers, params=params)
        data = r.json()
        results = []
        for item in data["web"]["results"]:
            results.append({"내용": item["title"], "URL": item["url"]})
        return results

@mcp.prompt()
def choose_best_result(query: str, results: list) -> list:
    return [
        base.UserMessage(f"User Query: {query}"),
        base.UserMessage("Here are the top search results:"),
        *[
            base.UserMessage(f"{i+1}. {r['title']}\n{r['snippet']}\nURL: {r['url']}")
            for i, r in enumerate(results)
        ],
        base.UserMessage("Which result is the most relevant to the query, and why?")
    ]

if __name__ == "__main__":
    mcp.run()