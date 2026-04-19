# tools/search.py

from tools.base_tool import BaseTool


class WebSearchTool(BaseTool):
    name = "search"

    def execute(self, input_data: str) -> str:
        search_query = self._extract_query(input_data)

        if not search_query:
            return "❌ Search query do please."

        return self._mock_search(search_query)

    def _extract_query(self, input_data: str) -> str:
        prefixes = [
            "search:", "search for:", "look up:", "find:",
            "find information about:", "what is", "who is"
        ]
        cleaned = input_data.strip()
        for prefix in prefixes:
            if cleaned.lower().startswith(prefix):
                cleaned = cleaned[len(prefix):].strip()
                break
        return cleaned

    def _mock_search(self, query: str) -> str:
        mock_database = {
            "python": "Python ek high-level programming language hai jo 1991 mein Guido van Rossum ne banai. Web development, AI, aur automation mein use hoti hai.",
            "machine learning": "Machine Learning AI ki ek branch hai jisme computers khud seekhte hain bina explicitly program kiye.",
            "neural network": "Neural Network ek algorithm hai jo human brain ki tarah kaam karta hai. Image recognition aur AI mein use hota hai.",
            "api": "API (Application Programming Interface) alag alag software applications ko aapas mein communicate karne deti hai.",
            "anthropic": "Anthropic ek AI safety company hai jisne Claude AI assistant banaya hai.",
            "gemini": "Gemini Google ka AI model hai jo text, images aur code samajh sakta hai.",
        }

        query_lower = query.lower()
        for keyword, result in mock_database.items():
            if keyword in query_lower:
                return (
                    f"🔍 Search results for: '{query}'\n\n"
                    f"{result}\n\n"
                    f"[Source: SmartAssist Knowledge Base]"
                )

        return (
            f"🔍 Search results for: '{query}'\n\n"
            f"Is topic ke baare mein abhi database mein information nahi hai. "
            f"Real search mein live results aate.\n\n"
            f"[Source: SmartAssist Knowledge Base — Mock Data]"
        )
