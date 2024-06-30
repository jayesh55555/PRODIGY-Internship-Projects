# Contact Management System

This is a simple Contact Management System written in Python. It allows users to store and manage contact information, including options to add, view, edit, and delete contacts. The program uses a JSON file for persistent storage of the contact information.

## Features

- Add new contacts with name, phone number, and email address
- View the list of all contacts
- Edit existing contacts
- Delete contacts
- Persistent storage using a JSON file

## Requirements

- Python 3.x

## Installation

1. Clone the repository or download the `contact_management_system.py` file.
2. Make sure you have Python 3 installed on your system.

## Usage

1. Run the `contact_management_system.py` script using Python:

    ```bash
    python contact_management_system.py
    ```

2. Follow the on-screen menu to manage your contacts:

    - **1. Add Contact**: Add a new contact by entering the name, phone number, and email address.
    - **2. View Contacts**: Display all saved contacts.
    - **3. Edit Contact**: Edit an existing contact by selecting its number from the list.
    - **4. Delete Contact**: Delete an existing contact by selecting its number from the list.
    - **5. Exit**: Exit the program.

## Example

```bash
Contact Management System
1. Add Contact
2. View Contacts
3. Edit Contact
4. Delete Contact
5. Exit
Enter your choice: 1
Enter contact name: John Doe
Enter contact phone number: 1234567890
Enter contact email address: john@example.com
Contact added successfully!

Contact Management System
1. Add Contact
2. View Contacts
3. Edit Contact
4. Delete Contact
5. Exit
Enter your choice: 2
1. John Doe - 1234567890 - john@example.com
