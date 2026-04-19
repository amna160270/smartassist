# tools/summarizer.py

from tools.base_tool import BaseTool


class TextSummarizerTool(BaseTool):
    name = "summarizer"

    def __init__(self, llm_client):
        self.llm = llm_client

    def execute(self, input_data: str) -> str:
        text_to_summarize = self._extract_text(input_data)

        if len(text_to_summarize.split()) < 10:
            return "❌ Text bohot chota hai. Kam az kam ek paragraph do."

        prompt = f"""Summarize the following text in 2-3 concise sentences.
Preserve the key ideas only.

Text:
\"\"\"{text_to_summarize}\"\"\"

Summary:"""

        try:
            summary = self.llm.complete(prompt)
            return f"📝 Summary:\n{summary}"
        except Exception as e:
            return f"❌ Summarization failed: {str(e)}"

    def _extract_text(self, input_data: str) -> str:
        instruction_words = [
            "summarize this:", "summarize:", "summary of:",
            "give me a summary of:", "tldr:",
            "summarize this paragraph:",
            "summarize the following:"
        ]
        cleaned = input_data.strip()
        for phrase in instruction_words:
            if cleaned.lower().startswith(phrase):
                cleaned = cleaned[len(phrase):].strip()
                break
        return cleaned
