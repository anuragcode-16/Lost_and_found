import tkinter as tk
from tkinter import messagebox
import csv

class LostAndFoundApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lost and Found Software")

        self.welcome_label = tk.Label(root, text="Welcome to Lost and Found Portal", font=("Helvetica", 16, "bold"))
        self.welcome_label.pack(pady=10)

        self.lost_listbox = tk.Listbox(root, width=50)
        self.lost_listbox.pack(side=tk.LEFT, padx=10, pady=10)

        self.found_listbox = tk.Listbox(root, width=50)
        self.found_listbox.pack(side=tk.RIGHT, padx=10, pady=10)

        self.item_name_label = tk.Label(root, text="Item Name:")
        self.item_name_label.pack()
        self.item_name_entry = tk.Entry(root)
        self.item_name_entry.pack()

        self.owner_name_label = tk.Label(root, text="Owner Name:")
        self.owner_name_label.pack()
        self.owner_name_entry = tk.Entry(root)
        self.owner_name_entry.pack()

        self.contact_details_label = tk.Label(root, text="Contact Details:")
        self.contact_details_label.pack()
        self.contact_details_entry = tk.Entry(root)
        self.contact_details_entry.pack()

        self.description_label = tk.Label(root, text="Description:")
        self.description_label.pack()
        self.description_entry = tk.Entry(root)
        self.description_entry.pack()

        self.add_button = tk.Button(root, text="Add Lost Item", command=self.add_lost_item)
        self.add_button.pack()

        self.mark_button = tk.Button(root, text="Mark Item as Found", command=self.mark_item_as_found)
        self.mark_button.pack()

        self.search_button = tk.Button(root, text="Search for Item", command=self.search_item)
        self.search_button.pack()

        self.clear_lost_button = tk.Button(root, text="Clear Lost Items", command=self.clear_lost_items)
        self.clear_lost_button.pack()

        self.clear_found_button = tk.Button(root, text="Clear Found Items", command=self.clear_found_items)
        self.clear_found_button.pack()

        self.quit_button = tk.Button(root, text="Exit", command=self.root.destroy)
        self.quit_button.pack()

        self.file_name = "lost_and_found.csv"
        self.create_csv_file()

    def create_csv_file(self):
        # Create the CSV file if it doesn't exist with the necessary headers
        with open(self.file_name, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Item Name", "Owner Name", "Contact Details", "Status", "Description"])

    def validate_fields(self):
        item_name = self.item_name_entry.get()
        owner_name = self.owner_name_entry.get()
        contact_details = self.contact_details_entry.get()

        if not item_name or not owner_name or not contact_details:
            messagebox.showerror("Error", "Please fill in all the required fields.")
            return False
        return True

    def check_for_duplicates(self, item_name, owner_name, contact_details):
        with open(self.file_name, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == item_name and row[1] == owner_name and row[2] == contact_details:
                    return True
        return False

    def move_item_to_found(self, item_name, owner_name, contact_details):
        found = False

        with open(self.file_name, "r", newline="") as file:
            reader = csv.reader(file)
            rows = list(reader)

        with open(self.file_name, "w", newline="") as file:
            writer = csv.writer(file)
            for row in rows:
                if row[0] == item_name and row[1] == owner_name and row[2] == contact_details and row[3] == "Lost":
                    found = True
                    row[3] = "Found"
                    writer.writerow(row)
                    messagebox.showinfo("Success", f"Item '{item_name}' marked as found.")
                else:
                    writer.writerow(row)

        if not found:
            messagebox.showerror("Error", f"Item '{item_name}' not found in lost items.")

        self.refresh_lists()

    def add_lost_item(self):
        if not self.validate_fields():
            return

        item_name = self.item_name_entry.get()
        owner_name = self.owner_name_entry.get()
        contact_details = self.contact_details_entry.get()
        description = self.description_entry.get()

        if self.check_for_duplicates(item_name, owner_name, contact_details):
            messagebox.showerror("Error", "Duplicate entry found. This item already exists in the lost items.")
            return

        with open(self.file_name, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([item_name, owner_name, contact_details, "Lost", description])
        messagebox.showinfo("Success", "Item added to the lost and found.")
        self.item_name_entry.delete(0, tk.END)
        self.owner_name_entry.delete(0, tk.END)
        self.contact_details_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.refresh_lists()

    def mark_item_as_found(self):
        if not self.validate_fields():
            return

        item_name = self.item_name_entry.get()
        owner_name = self.owner_name_entry.get()
        contact_details = self.contact_details_entry.get()

        self.move_item_to_found(item_name, owner_name, contact_details)

    def search_item(self):
        keyword = self.item_name_entry.get().lower()
        found_items = []

        with open(self.file_name, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if keyword in row[0].lower():
                    found_items.append(row)

        if found_items:
            list_text = "\n".join([f"Item: {row[0]}, Owner: {row[1]}, Contact: {row[2]}, Description: {row[4]}" for row in found_items])
            messagebox.showinfo("Search Results", list_text)
        else:
            messagebox.showinfo("Search Results", "No matching items found.")

    def clear_lost_items(self):
        with open(self.file_name, "r", newline="") as file:
            reader = csv.reader(file)
            rows = list(reader)

        with open(self.file_name, "w", newline="") as file:
            writer = csv.writer(file)
            for row in rows:
                if row[3] != "Lost":
                    writer.writerow(row)

        self.refresh_lists()

    def clear_found_items(self):
        with open(self.file_name, "r", newline="") as file:
            reader = csv.reader(file)
            rows = list(reader)

        with open(self.file_name, "w", newline="") as file:
            writer = csv.writer(file)
            for row in rows:
                if row[3] != "Found":
                    writer.writerow(row)

        self.refresh_lists()

    def refresh_lists(self):
        self.lost_listbox.delete(0, tk.END)
        self.found_listbox.delete(0, tk.END)

        with open(self.file_name, "r", newline="") as file:
            reader = csv.reader(file)
            lost_count = 0
            found_count = 0
            found_items = []

            for row in reader:
                if row[3] == "Lost":
                    lost_count += 1
                    self.lost_listbox.insert(tk.END, f"{lost_count}. Item: {row[0]}, Owner: {row[1]}, Contact: {row[2]}, Description: {row[4]}")
                elif row[3] == "Found":
                    found_count += 1
                    found_items.append(f"{found_count}. Item: {row[0]}, Owner: {row[1]}, Contact: {row[2]}, Description: {row[4]}")

            if self.lost_listbox.size() == 0:
                self.lost_listbox.insert(tk.END, "Lost Item List")

            if not found_items:
                self.found_listbox.insert(tk.END, "Found Item List")
            else:
                for item in found_items:
                    self.found_listbox.insert(tk.END, item)

if __name__ == "__main__":
    root = tk.Tk()
    app = LostAndFoundApp(root)
    app.refresh_lists()
    root.mainloop()
