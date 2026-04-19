# tools/base_tool.py

class BaseTool:
    name: str = "base_tool"

    def execute(self, input_data: str) -> str:
        raise NotImplementedError(
            f"Tool '{self.name}' must implement execute() method."
        )

    def __repr__(self) -> str:
        return f"<Tool: {self.name}>"
