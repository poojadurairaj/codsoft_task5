import pickle

class ContactBook:
    def __init__(self):
        # Initialize an empty contact list
        self.contacts = self.load_contacts()

    def add_contact(self, name, phone, email, address):
        """Add a new contact to the contact list."""
        self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
        self.save_contacts()

    def view_contacts(self):
        """Display the list of all contacts."""
        if not self.contacts:
            print("No contacts found.")
        else:
            print("\nContact List:")
            for name, details in self.contacts.items():
                print(f"Name: {name}, Phone: {details['phone']}")

    def search_contact(self, search_term):
        """Search for contacts by name or phone number."""
        found = False
        print("\nSearch Results:")
        for name, details in self.contacts.items():
            if search_term.lower() in name.lower() or search_term in details['phone']:
                print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
                found = True
        if not found:
            print("No contacts found.")

    def update_contact(self, name, phone=None, email=None, address=None):
        """Update the contact details."""
        if name in self.contacts:
            if phone:
                self.contacts[name]['phone'] = phone
            if email:
                self.contacts[name]['email'] = email
            if address:
                self.contacts[name]['address'] = address
            self.save_contacts()
            print("Contact updated successfully.")
        else:
            print("Contact not found.")

    def delete_contact(self, name):
        """Delete a contact from the contact list."""
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    def save_contacts(self):
        """Save contacts to a file."""
        with open('contacts.pkl', 'wb') as file:
            pickle.dump(self.contacts, file)

    def load_contacts(self):
        """Load contacts from a file."""
        try:
            with open('contacts.pkl', 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError:
            return {}

def main():
    contact_book = ContactBook()

    while True:
        print("\n===== Contact Book Menu =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Quit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone, email, address)
        elif choice == "2":
            contact_book.view_contacts()
        elif choice == "3":
            search_term = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_term)
        elif choice == "4":
            name = input("Enter contact name to update: ")
            phone = input("Enter new phone number (or leave blank to keep current): ")
            email = input("Enter new email (or leave blank to keep current): ")
            address = input("Enter new address (or leave blank to keep current): ")
            contact_book.update_contact(name, phone if phone else None, email if email else None, address if address else None)
        elif choice == "5":
            name = input("Enter contact name to delete: ")
            contact_book.delete_contact(name)
        elif choice == "6":
            print("Exiting the Contact Book.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()

