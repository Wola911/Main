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
    def add(self, command):
        _, *args = command.split()
        name, phone = args
        if name in self.contacts.keys():
            name = f'{name}2'
        new_contact = {name: phone}
        self.contacts = dict(self.contacts | new_contact)
        return f"Contact {name} added with phone {phone}"

    @input_error
    def change(self, command):
        _, *args = command.split()
        name, phone = args
        if name in self.contacts:
            self.contacts[name] = phone
            return f"Phone number for {name} changed to {phone}"
        else:
            return f"Contact {name} not found. Use 'add' to create a new contact."

    @input_error
    def phone(self, command):
        _, *args = command.split()
        name, = args
        return f"Phone number for {name}: {self.contacts.get(name, 'Contact not found')}"

    @input_error
    def show_all(self):
        return "\n".join([f"{name}: {phone}" for name, phone in self.contacts.items()])

    def exit(self):
        return "Good bye!"


def main():
    bot = ContactBot()

    while True:
        command = input("Enter command: ").lower()

        if command in {"good bye", "close", "exit"}:
            print(bot.exit())
            break
        elif command == "hello":
            print(bot.hello())
        elif command == "add":
            print(bot.add(command))
        elif command == "change":
            print(bot.change(command))
        elif command == "phone":
            print(bot.phone(command))
        elif command == "show all":
            print(bot.show_all())
        else:
            print("Unknown command. Please try again.")


if __name__ == "__main__":
    main()