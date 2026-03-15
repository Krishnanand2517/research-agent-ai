from agent import agent


def main():
    while True:
        query = input("\nAsk a research question (or 'exit'): ")

        if query.lower() == "exit":
            break

        print("\n--- Agent Steps ---\n")

        for step in agent.stream(
            {"messages": [{"role": "user", "content": query}]}, stream_mode="updates"
        ):
            for node, output in step.items():
                if "messages" not in output:
                    continue

                message = output["messages"][-1]

                print(f"\nNODE: {node}")
                print("TYPE:", type(message).__name__)

                if hasattr(message, "tool_calls") and message.tool_calls:
                    print("TOOL CALL:", message.tool_calls)

                elif message.__class__.__name__ == "ToolMessage":
                    print("TOOL RESULT:")
                    print(message.content)

                else:
                    print("Answer:", message.content)

        print("\n------------------\n")


if __name__ == "__main__":
    main()
