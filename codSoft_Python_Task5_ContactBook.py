''' Author- Jagu Manish || Python Programming Internship at CodSoft

------------------------------ TASK 5 - CONTACT BOOK ---------------------------------
Contact Information: Store name, phone number, email, and address for each contact.
Add Contact: Allow users to add new contacts with their details.
View Contact List: Display a list of all saved contacts with names and phone numbers.
Search Contact: Implement a search function to find contacts by name or phone number.
Update Contact: Enable users to update contact details.
Delete Contact: Provide an option to delete a contact.
User Interface: Design a user-friendly interface for easy interaction.


IDE used: Pycharm
'''


#importing modules
import tkinter as tkr
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

    def __repr__(self):
        return f"{self.name}, {self.phone_number}, {self.email}, {self.address}"

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_user_contact(self, contact):
        self.contacts.append(contact)

    def view_user_contacts(self):
        return self.contacts

    def search_user_contact(self, search_term):
        return [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone_number]

    def update_user_contact(self, index, updated_contact):
        if 0 <= index < len(self.contacts):
            self.contacts[index] = updated_contact
            return True
        return False

    def delete_user_contact(self, index):
        if 0 <= index < len(self.contacts):
            del self.contacts[index]
            return True
        return False

class Contact_App:
    def __init__(self, root):
        self.manager = ContactManager()

        self.root = root
        self.root.title("ᴄᴏɴᴛᴀᴄᴛ ʙᴏᴏᴋ")

        self.create_widgets()

    def create_widgets(self):
        self.add_frame = tkr.Frame(self.root)
        self.add_frame.pack(pady=10)

        tkr.Label(self.add_frame, text="Name:").grid(row=0, column=0)
        tkr.Label(self.add_frame, text="Phone Number:").grid(row=1, column=0)
        tkr.Label(self.add_frame, text="Email:").grid(row=2, column=0)
        tkr.Label(self.add_frame, text="Address:").grid(row=3, column=0)

        self.name_entry = tkr.Entry(self.add_frame)
        self.phone_number_entry = tkr.Entry(self.add_frame)
        self.email_entry = tkr.Entry(self.add_frame)
        self.address_entry = tkr.Entry(self.add_frame)

        self.name_entry.grid(row=0, column=1)
        self.phone_number_entry.grid(row=1, column=1)
        self.email_entry.grid(row=2, column=1)
        self.address_entry.grid(row=3, column=1)

        self.add_button = tkr.Button(self.add_frame, text="Add Contact", command=self.add_user_contact)
        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)

        # View Contacts List
        self.view_frame = tkr.Frame(self.root)
        self.view_frame.pack(pady=10)

        self.contacts_listbox = tkr.Listbox(self.view_frame, width=50)
        self.contacts_listbox.pack()

        self.view_contacts_button = tkr.Button(self.view_frame, text="View Contacts", command=self.view_user_contacts)
        self.view_contacts_button.pack(pady=5)

        # Search Contacts
        self.search_frame = tkr.Frame(self.root)
        self.search_frame.pack(pady=10)

        tkr.Label(self.search_frame, text="Search:").grid(row=0, column=0)
        self.search_entry = tkr.Entry(self.search_frame)
        self.search_entry.grid(row=0, column=1)
        self.search_button = tkr.Button(self.search_frame, text="Search", command=self.search_user_contacts)
        self.search_button.grid(row=0, column=2)

        # Update/Delete Contacts
        self.modify_frame = tkr.Frame(self.root)
        self.modify_frame.pack(pady=10)

        self.update_button = tkr.Button(self.modify_frame, text="Update Selected Contact", command=self.update_user_contact)
        self.update_button.pack(side=tkr.LEFT, padx=5)

        self.delete_button = tkr.Button(self.modify_frame, text="Delete Selected Contact", command=self.delete_user_contact)
        self.delete_button.pack(side=tkr.RIGHT, padx=5)

    def add_user_contact(self):
        name = self.name_entry.get()
        phone_number = self.phone_number_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone_number and email and address:
            new_contact = Contact(name, phone_number, email, address)
            self.manager.add_user_contact(new_contact)
            messagebox.showinfo("Success", "Contact added successfully")
            self.clear_entries()
        else:
            messagebox.showwarning("Input Error", "Please fill in all fields")

    def view_user_contacts(self):
        self.contacts_listbox.delete(0, tkr.END)
        for contact in self.manager.view_user_contacts():
            self.contacts_listbox.insert(tkr.END, f"{contact.name} - {contact.phone_number}")

    def search_user_contacts(self):
        search_term = self.search_entry.get()
        if search_term:
            results = self.manager.search_user_contact(search_term)
            self.contacts_listbox.delete(0, tkr.END)
            for contact in results:
                self.contacts_listbox.insert(tkr.END, f"{contact.name} - {contact.phone_number}")
        else:
            messagebox.showwarning("Input Error", "Please enter a search term")

    def update_user_contact(self):
        try:
            selected_index = self.contacts_listbox.curselection()[0]
            contact = self.manager.view_user_contacts()[selected_index]

            self.name_entry.delete(0, tkr.END)
            self.phone_number_entry.delete(0, tkr.END)
            self.email_entry.delete(0, tkr.END)
            self.address_entry.delete(0, tkr.END)

            self.name_entry.insert(0, contact.name)
            self.phone_number_entry.insert(0, contact.phone_number)
            self.email_entry.insert(0, contact.email)
            self.address_entry.insert(0, contact.address)

            self.add_button.config(text="Save Update", command=lambda: self.save_update(selected_index))
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a contact to update")

    def save_update(self, index):
        name = self.name_entry.get()
        phone_number = self.phone_number_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone_number and email and address:
            updated_contact = Contact(name, phone_number, email, address)
            self.manager.update_user_contact(index, updated_contact)
            messagebox.showinfo("Success", "Contact updated successfully")
            self.add_button.config(text="Add Contact", command=self.add_user_contact)
            self.clear_entries()
            self.view_user_contacts()
        else:
            messagebox.showwarning("Input Error", "Please fill in all fields")

    def delete_user_contact(self):
        try:
            selected_index = self.contacts_listbox.curselection()[0]
            self.manager.delete_user_contact(selected_index)
            messagebox.showinfo("Success", "Contact deleted successfully")
            self.view_user_contacts()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a contact to delete")

    def clear_entries(self):
        self.name_entry.delete(0, tkr.END)
        self.phone_number_entry.delete(0, tkr.END)
        self.email_entry.delete(0, tkr.END)
        self.address_entry.delete(0, tkr.END)

root = tkr.Tk()
app = Contact_App(root)
root.mainloop()
