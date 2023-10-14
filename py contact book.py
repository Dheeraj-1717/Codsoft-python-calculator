import json

# Initialize an empty contact list
contacts = []

def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            global contacts
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = []

def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)

def add_contact():
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email address: ")
    address = input("Enter the contact's address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    save_contacts()
    print("Contact added successfully.")

def view_contacts():
    print("Contact List:")
    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. {contact['name']}: {contact['phone']}")

def search_contacts(query):
    matching_contacts = []
    for contact in contacts:
        if query in contact["name"] or query in contact["phone"]:
            matching_contacts.append(contact)
    return matching_contacts

def update_contact():
    view_contacts()
    try:
        index = int(input("Enter the number of the contact to update: ")) - 1
        if 0 <= index < len(contacts):
            contact = contacts[index]
            print(f"Updating contact: {contact['name']}")
            new_name = input("Enter the updated name (press Enter to keep it unchanged): ")
            new_phone = input("Enter the updated phone number (press Enter to keep it unchanged): ")
            new_email = input("Enter the updated email address (press Enter to keep it unchanged): ")
            new_address = input("Enter the updated address (press Enter to keep it unchanged): ")

            if new_name:
                contact["name"] = new_name
            if new_phone:
                contact["phone"] = new_phone
            if new_email:
                contact["email"] = new_email
            if new_address:
                contact["address"] = new_address

            save_contacts()
            print("Contact updated successfully.")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a valid contact number.")

def delete_contact():
    view_contacts()
    try:
        index = int(input("Enter the number of the contact to delete: ")) - 1
        if 0 <= index < len(contacts):
            deleted_contact = contacts.pop(index)
            save_contacts()
            print(f"Contact {deleted_contact['name']} deleted successfully.")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a valid contact number.")

def main():
    load_contacts()
    print("Welcome to the Contact Management System!")

    while True:
        print("\nMenu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contacts")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            query = input("Enter a name or phone number to search: ")
            matching_contacts = search_contacts(query)
            if matching_contacts:
                print("Matching Contacts:")
                for contact in matching_contacts:
                    print(f"{contact['name']}: {contact['phone']}")
            else:
                print("No matching contacts found.")
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
