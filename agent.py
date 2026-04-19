# agent.py

from tools.base_tool import BaseTool
from llm.client import LLMClient


class Agent:
    def __init__(self, tools: list, llm_client: LLMClient):
        self.llm = llm_client
        self.tools: dict = {
            tool.name: tool for tool in tools
        }
        print(f"[Agent] Tools ready: {list(self.tools.keys())}")

    def decide_tool(self, query: str) -> str:
        tool_list = "\n".join(f"- {name}" for name in self.tools.keys())

        decision_prompt = f"""You are a routing system for an AI agent.

Available tools:
{tool_list}

Tool descriptions:
- calculator: Use for any math calculation or arithmetic
- summarizer: Use for summarizing or condensing text
- search: Use for factual questions or general knowledge

User query: "{query}"

Instructions:
- Select exactly ONE tool
- Reply with ONLY the tool name, nothing else

Tool selection:"""

        raw_decision = self.llm.complete(decision_prompt)
        cleaned = raw_decision.strip().lower().rstrip(".")

        if cleaned in self.tools:
            return cleaned

        for tool_name in self.tools.keys():
            if tool_name in cleaned:
                return tool_name

        print(f"[Agent Warning] '{cleaned}' nahi mila. Default: search")
        return "search"

    def run(self, query: str) -> str:
        if not query.strip():
            return "❌ Kuch toh likho!"

        print(f"\n[🤖 Agent soch raha hai...]", flush=True)
        tool_name = self.decide_tool(query)

        tool = self.tools[tool_name]
        print(f"[🔧 Running: {tool.__class__.__name__}]", flush=True)

        try:
            result = tool.execute(query)
            return result
        except Exception as e:
            return f"❌ Error in {tool_name}: {str(e)}"
