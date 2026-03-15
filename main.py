from agent import agent


def main():
    while True:
        query = input("\nAsk a research question (or 'exit'): ")

        if query.lower() == "exit":
            break

        response = agent.invoke({"messages": [{"role": "user", "content": query}]})

        print("\nAnswer:\n")
        print(response["messages"][-1].content)


if __name__ == "__main__":
    main()
