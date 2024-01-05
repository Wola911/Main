def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "User not found"

    return wrapper


class ContactBot:
    def __init__(self):
        self.contacts = {}

    @input_error
    def hello(self):
        return "How can I help you?"

    @input_error
    def add(self, *args):
        name, phone = args
        self.contacts[name] = phone
        return f"Contact {name} added with phone {phone}"

    @input_error
    def change(self, *args):
        name, phone = args
        self.contacts[name] = phone
        return f"Phone number for {name} changed to {phone}"

    @input_error
    def phone(self, *args):
        name, = args
        return f"Phone number for {name}: {self.contacts[name]}"

    @input_error
    def show_all(self):
        return "\n".join([f"{name}: {phone}" for name,
                          phone in self.contacts.items()])

    def exit(self):
        return "Good bye!"


def main():
    bot = ContactBot()

    while True:
        command = input("Enter command: ").lower()

        if command == "good bye" or command == "close" or command == "exit":
            print(bot.exit())
            break
        elif command == "hello":
            print(bot.hello())
        elif command.startswith("add"):
            _, *args = command.split()
            print(bot.add(*args))
        elif command.startswith("change"):
            _, *args = command.split()
            print(bot.change(*args))
        elif command.startswith("phone"):
            _, *args = command.split()
            print(bot.phone(*args))
        elif command == "show all":
            print(bot.show_all())
        else:
            print("Unknown command. Please try again.")


if __name__ == "__main__":
    main()