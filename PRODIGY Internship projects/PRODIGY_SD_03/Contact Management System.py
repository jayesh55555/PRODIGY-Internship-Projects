import json
import os

CONTACTS_FILE = 'contacts.json'

# Load contacts 
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return []

# Save contacts 
def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

# Add new contact
def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email address: ")
    
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("Contact added successfully!")

# View all contacts
def view_contacts():
    if not contacts:
        print("No contacts found.")
        return
    
    for idx, contact in enumerate(contacts, 1):
        print(f"{idx}. {contact['name']} - {contact['phone']} - {contact['email']}")

# Edit contact
def edit_contact():
    view_contacts()
    contact_index = int(input("Enter the contact number to edit: ")) - 1
    
    if 0 <= contact_index < len(contacts):
        contact = contacts[contact_index]
        print(f"Editing contact: {contact['name']}")
        
        contact['name'] = input(f"Enter new name (current: {contact['name']}): ") or contact['name']
        contact['phone'] = input(f"Enter new phone (current: {contact['phone']}): ") or contact['phone']
        contact['email'] = input(f"Enter new email (current: {contact['email']}): ") or contact['email']
        
        save_contacts(contacts)
        print("Contact updated successfully!")
    else:
        print("Invalid contact number.")

# Delete contact
def delete_contact():
    view_contacts()
    contact_index = int(input("Enter the contact number to delete: ")) - 1
    
    if 0 <= contact_index < len(contacts):
        contacts.pop(contact_index)
        save_contacts(contacts)
        print("Contact deleted successfully!")
    else:
        print("Invalid contact number.")

def main():
    global contacts
    contacts = load_contacts()
    
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            edit_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
