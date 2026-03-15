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

        for step in agent.stream(
            {"messages": [{"role": "user", "content": query}]}, stream_mode="updates"
        ):
            for node, output in step.items():
                if "messages" not in output:
                    continue

                message = output["messages"][-1]

                # MODEL THINKING
                if (
                    node == "model"
                    and hasattr(message, "tool_calls")
                    and message.tool_calls
                ):
                    for tool in message.tool_calls:
                        print("🧠 Thinking...")
                        print(f"🔧 Calling tool: {tool['name']}")
                        print(f"   args: {tool['args']}\n")

                # TOOL RESULT
                elif node == "tools":
                    print("📦 Tool returned results:\n")
                    print(message.content)
                    print()

                # FINAL ANSWER
                elif node == "model":
                    if message.content:
                        print("🤖 Final Answer:\n")
                        print(message.content)

        print_separator()


if __name__ == "__main__":
    main()
