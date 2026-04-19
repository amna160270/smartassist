# tools/calculator.py

import re
from tools.base_tool import BaseTool


class CalculatorTool(BaseTool):
    name = "calculator"

    def execute(self, input_data: str) -> str:
        expression = self._extract_expression(input_data)

        if not expression:
            return "❌ Valid math expression nahi mila. Example: '25 * 4 + 10'"

        try:
            safe_expr = re.sub(r"[^0-9+\-*/().\s]", "", expression)
            result = eval(safe_expr)
            return f"🧮 Expression: {safe_expr.strip()}\n   Result: {result:,}"

        except ZeroDivisionError:
            return "❌ Error: Zero se divide nahi kar sakte!"
        except Exception as e:
            return f"❌ Calculation failed: {str(e)}"

    def _extract_expression(self, text: str) -> str:
        prefixes = ["calculate", "compute", "what is", "evaluate", "solve"]
        cleaned = text.lower()
        for prefix in prefixes:
            cleaned = cleaned.replace(prefix, "")
        match = re.search(r"[\d\s\+\-\*\/\(\)\.]+", cleaned)
        return match.group(0).strip() if match else ""
