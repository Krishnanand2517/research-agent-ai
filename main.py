from langchain_core.messages import AIMessage, ToolMessage
from agent import agent


def print_separator():
    print("\n" + "=" * 40 + "\n")


def main():
    while True:
        query = input("\nAsk a research question (or 'exit'): ")

        if query.lower() == "exit":
            break

        print_separator()
        print("🧠 Agent starting...\n")
        final_started = False
        seen_tool_calls = set()

        for chunk, metadata in agent.stream(
            {"messages": [{"role": "user", "content": query}]},
            stream_mode="messages",
        ):
            # TOOL CALL
            if isinstance(chunk, AIMessage) and chunk.tool_calls:
                for tool in chunk.tool_calls:
                    name = tool.get("name")
                    args = tool.get("args")

                    if not name:
                        continue

                    key = f"{name}-{args}"

                    if key in seen_tool_calls:
                        continue

                    seen_tool_calls.add(key)

                    print("\n🧠 Thinking...")
                    print(f"🔧 Calling tool: {tool['name']}")

            # TOOL RESULT
            elif isinstance(chunk, ToolMessage):
                print("📦 Tool returned results:\n")
                print(chunk.content)
                print()

            # LIVE TOKEN STREAMING
            elif isinstance(chunk, AIMessage):
                if chunk.content:
                    if not final_started:
                        print_separator()
                        print("✅ Final Answer\n")
                        final_started = True

                    print(chunk.content, end="", flush=True)

        print_separator()


if __name__ == "__main__":
    main()
