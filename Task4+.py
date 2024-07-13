from functools import wraps

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Enter contact name."
        except IndexError:
            return "Check the phone number."
    return inner






def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        return "Error: Please provide both name and phone number."
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        return "Error: Please provide both name and new phone number."
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return f"Contact {name}'s phone number has been changed to {new_phone}."
    else:
        return f"No contact found under the name {name}."
    
@input_error
def show_phone_number(args, contacts):
    if len(args) != 1:
        return "Please provide name only."
    name = args[0]
    if name in contacts:
        return f"{name}'s phone number is {contacts[name]}."
    else:
        return f"No contact found under the name {name}."
    
@input_error    
def show_contacts(args, contacts):
    if not contacts:
        return("You have no friends.")
    else:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])


@input_error   
def delete_friend(args, contacts):
    if len(args) != 1:
        return "Please provide name only."
    name = args[0]
    if name in contacts:
        removed = contacts.pop(name)
        return f"{name} was removed from your contacts."
    else:
        return f"No contact found under the name {name}."



def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in {"close", "exit"}:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone_number(args, contacts))
        elif command == "all":
            print(show_contacts(args, contacts))
        elif command == "delete":
            print(delete_friend(args, contacts))
        else:
            print(command, args)
            print("Invalid command.")


if __name__ == "__main__":
    main()
