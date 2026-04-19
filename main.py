# main.py

from llm.client import LLMClient
from tools.calculator import CalculatorTool
from tools.summarizer import TextSummarizerTool
from tools.search import WebSearchTool
from agent import Agent


def display_banner():
    print("\n" + "=" * 60)
    print("       SmartAssist — Tumhara Personal AI Agent")
    print("=" * 60)
    print("  Tools: calculator | summarizer | search")
    print("  'help' likho examples ke liye, 'exit' likho band karne ke liye")
    print("=" * 60)


def display_help():
    print("\n📖 Example queries:")
    print("  • calculate 25 * 18 + 100")
    print("  • summarize this: [koi bhi paragraph yahan paste karo]")
    print("  • search: what is machine learning?")
    print("  • what is 1000 / 4?")
    print()


def display_result(result: str):
    print("\n" + "─" * 60)
    print(result)
    print("─" * 60 + "\n")


def main():
    display_banner()

    try:
        llm_client = LLMClient()
        print("\n[✅ Gemini Connected!]")
    except EnvironmentError as e:
        print(f"\n[❌ Error]\n{e}")
        return

    tools = [
        CalculatorTool(),
        TextSummarizerTool(llm_client=llm_client),
        WebSearchTool(),
    ]

    agent = Agent(tools=tools, llm_client=llm_client)
    print("\n[✅ SmartAssist ready hai! Likho apna sawal]\n")

    while True:
        try:
            user_input = input("Tum: ").strip()

            if not user_input:
                continue

            if user_input.lower() in ("exit", "quit", "q"):
                print("\n👋 Allah Hafiz! SmartAssist band ho raha hai.\n")
                break

            if user_input.lower() == "help":
                display_help()
                continue

            result = agent.run(user_input)
            display_result(result)

        except KeyboardInterrupt:
            print("\n\n👋 Interrupted. Allah Hafiz!\n")
            break
        except Exception as e:
            print(f"\n[Error] {type(e).__name__}: {e}")
            print("Dobara koshish karo.\n")


if __name__ == "__main__":
    main()
