# Напишіть консольного бота помічника, який розпізнаватиме команди, що вводяться з клавіатури, та буде відповідати відповідно 
# до введеної команди.

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    name = name.strip().lower()
    if not phone.startswith("+") or not phone[1:].isdigit():
        return "Invalid phone number format. Must be in format +<country_code><number>"
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    if not args:
        return "No name provided"
    name = args[0]
    phone = args[1]
    if not phone.startswith("+") or not phone[1:].isdigit():
        return "Invalid phone number format. Must be in format +<country_code><number>"
    name = name.strip().lower()
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return f"Contact '{name}' not found."

def show_phone (args, contacts):
    if not args:
        return "No name provided"
    name = args[0]
    name = name.strip().lower()
    if name in contacts:
        return f"Phone number for {name.capitalize()}: {contacts[name]}"
    else:
        return f"Contact '{name}' not found."

def all_contact(contacts):
    result = "Contacts:\n"
    for name, phone in contacts.items():
        display_name = name.capitalize()
        result += f"{display_name}: {phone}\n"
    return result

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(all_contact(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
