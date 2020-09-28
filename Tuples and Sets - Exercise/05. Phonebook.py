def create_contacts(ppl):
    contacts = dict()
    for contact in ppl:
        name, num = contact.split("-")
        if name not in contacts:
            contacts[name] = ""

        contacts[name] = num
    return contacts


def find_contact(contacts_to_find, contacts):
    for contact in contacts_to_find:
        if contact in contacts:
            print(f"{contact} -> {contacts[contact]}")
        else:
            print(f"Contact {contact} does not exist.")


def read_until_command():
    contacts = []
    while True:
        command = input()
        if command.isdigit():
            count_to_find = int(command)
            contacts_to_find = [input() for _ in range(count_to_find)]
            break
        else:
            contacts.append(command)
    return contacts, contacts_to_find

contacts, contacts_to_find = read_until_command()

contacts = create_contacts(contacts)
find_contact(contacts_to_find, contacts)