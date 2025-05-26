from mcp.server.fastmcp import FastMCP

mcp = FastMCP("read_the_docs")

@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b

if __name__ == "__main__":
    mcp.run()