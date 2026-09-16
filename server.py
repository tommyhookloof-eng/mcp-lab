# FastMCP practice server: calculations and Adeoti notes.
from fastmcp import FastMCP

app = FastMCP("MCP Lab")


class CalculationsServer:
@staticmethod
@app.tool
def add(a: float, b: float) -> float:
"""Add two numbers."""
return a + b

@staticmethod
@app.tool
def multiply(a: float, b: float) -> float:
"""Multiply two numbers."""
return a * b

@staticmethod
@app.prompt
def explain_calculation(expression: str) -> str:
"""Create a prompt for explaining a calculation."""
return f"Explain this calculation step by step, then verify it: {expression}"


class AdeotiNotesServer:
notes = {
"architecture": "Adeoti is organized into docs, lore, characters, scripts, and production.",
"vault": "The canonical repository is tommyhookloof-eng/adeoti-vault.",
}

@staticmethod
@app.resource("adeoti://notes/{topic}")
def note(topic: str) -> str:
"""Read a small Adeoti practice note by topic."""
return AdeotiNotesServer.notes.get(topic, "No note found for that topic.")

@staticmethod
@app.tool
def list_note_topics() -> list[str]:
"""List available Adeoti note topics."""
return sorted(AdeotiNotesServer.notes)

@staticmethod
@app.prompt
def lore_brief(topic: str) -> str:
"""Create a prompt for a focused Adeoti lore brief."""
return f"Give a concise, canon-aware Adeoti lore brief about: {topic}"


if __name__ == "__main__":
app.run(transport="streamable-http", host="0.0.0.0", port=8000)
