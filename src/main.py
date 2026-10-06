from alfred.agent import AlfredAgent


def main():
    alfred = AlfredAgent()

    message = input("Tú: ")
    response = alfred.process_message(message)

    print(f"{alfred.name}: {response}")


if __name__ == "__main__":
    main()