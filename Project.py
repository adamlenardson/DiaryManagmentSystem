import tkinter as tk
from tkinter import messagebox
import csv

def login():
    # Get the username and password entered by the user
    username = username_entry.get()
    password = password_entry.get()

    # Check if the username and password are correct
    if username == "admin" and password == "password":
        window.destroy()
    else:
        message_label.config(text="Incorrect username or password", fg="red")
        password_entry.delete(0, END)

# Create a new Tkinter window
window = tk.Tk()
window.title("Login Page")
window.resizable(width=False, height=False)

# Create a username label and entry widget
username_label = tk.Label(window, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=10)
username_entry = tk.Entry(window)
username_entry.grid(row=0, column=1, padx=10, pady=10)

# Create a password label and entry widget
password_label = tk.Label(window, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=10)
password_entry = tk.Entry(window)
password_entry.grid(row=1, column=1, padx=10, pady=10)

# Create a login button
login_button = tk.Button(window, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Create a message label to display login status
message_label = tk.Label(window, text="")
message_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)



# Run the Tkinter event loop
window.mainloop()


# Remove Window
def remove_entry():
    remove_window = tk.Toplevel(window)
    remove_window.title("Remove Entry")
    remove_window.geometry("500x400")
    remove_window.resizable(width=False, height=False)
    
    # Title
    remove_title = tk.Label(remove_window, text="Select entry to remove:")
    remove_title.pack(pady=10)
    
    # Listbox
    remove_listbox = tk.Listbox(remove_window, width=50)
    remove_listbox.pack(pady=10)
    
    # Load saved entries
    saved_entries = []
    try:
        with open("diary_entries.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                saved_entries.append(row)
    except FileNotFoundError:
        pass
    
    # Populate listbox with saved entries
    for i, entry in enumerate(saved_entries):
        remove_listbox.insert(i, f"{entry[0]} - {entry[1]} - {entry[2]}")
    
    # Remove Selected
    def remove_selected_entry():
        selection = remove_listbox.curselection()
        if not selection:
            messagebox.showwarning("Warning", "Please select an entry to remove.")
            return
        selected_entry = saved_entries[selection[0]]
        saved_entries.remove(selected_entry)
        with open("diary_entries.csv", "w", newline="") as file:
            writer = csv.writer(file)
            for entry in saved_entries:
                writer.writerow(entry)
        remove_listbox.delete(selection[0])
        messagebox.showinfo("Entry Removed", "Entry has been removed.")
    
    remove_button = tk.Button(remove_window, text="Remove Selected Entry", command=remove_selected_entry)
    remove_button.pack(pady=10)

# Edit Window - Partially functional
def edit_entry():
    edit_window = tk.Toplevel(window)
    edit_window.title("Edit Entry")
    edit_window.geometry("500x400")
    edit_window.resizable(width=False, height=False)
    
    # Title
    edit_title = tk.Label(edit_window, text="Select entry to edit:")
    edit_title.pack(pady=10)
    
    # Listbox
    edit_listbox = tk.Listbox(edit_window, width=50)
    edit_listbox.pack(pady=10)
    
    # Load saved entries
    saved_entries = []
    try:
        with open("diary_entries.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                saved_entries.append(row)
    except FileNotFoundError:
        pass
    
    # Populate listbox with saved entries
    for i, entry in enumerate(saved_entries):
        edit_listbox.insert(i, f"{entry[0]} - {entry[1]} - {entry[2]}")

# Settings Window - Functional but not fully implemented
def settings():
    # Create a new window for adding users
    settings_window = tk.Toplevel(window)
    settings_window.title("Settings")
    settings_window.geometry("300x150")
    settings_window.resizable(width=False, height=False)

    # Create a label that explains what is being inputted
    add_label = tk.Label(settings_window, text="Add New User:", font=('Ariel', 14))
    add_label.grid(row=0, column=0)

    # Create a label and entry widget for entering the user's name
    name_label = tk.Label(settings_window, text="Name:")
    name_label.grid(row=1, column=0, pady=5)

    name_entry = tk.Entry(settings_window)
    name_entry.grid(row=1, column=1, pady=5)

    # Create a label and entry widget for entering the user's password
    password_label = tk.Label(settings_window, text="Password:")
    password_label.grid(row=2, column=0, padx=5)

    password_entry = tk.Entry(settings_window)
    password_entry.grid(row=2, column=1, padx=5)

    # Create a button to save the user's information to a file
    def save_user():
        # Get the username and password from the entry fields
        username = name_entry.get()
        password = password_entry.get()
        
        # Write the credentials to a CSV file
        with open('users.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([username, password])
        
        # Clear the entry fields
        name_entry.delete(0, END)
        password_entry.delete(0, END)

    # Save button
    save_button = tk.Button(settings_window, text="Save", command=save_user)
    save_button.grid(row=3, column=0, padx=5, pady=5, columnspan=2)


# Save Entry Function
def save_entry():
    # Get Input Values
    time_value = time_entry.get()
    place_value = place_entry.get()
    duration_value = duration_entry.get()
    description_value = description_entry.get("1.0", "end-1c")
    priority_value = priority_var.get()
    
    # Check Required Fields
    if not time_value or not place_value or not duration_value or not description_value:
        messagebox.showwarning("Warning", "Please complete all fields.")
        return
    
    # Save Entry to CSV File
    with open("diary_entries.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([time_value, place_value, duration_value, description_value, priority_value])
    
    # Clear Entry Fields
    clear_entries()
    
    # Show Confirmation Message
    messagebox.showinfo("Entry Saved", "Your diary entry has been saved.")

# Clear Entry Fields Function
def clear_entries():
    time_entry.delete(0, "end")
    place_entry.delete(0, "end")
    duration_entry.delete(0, "end")
    description_entry.delete("1.0", "end")
    priority_var.set(priority_options[0])

# Create Main Window
window = tk.Tk()
window.title("Diary Entry")
window.geometry("800x450")
window.resizable(width=False, height=False)

# Create Entry Frame
diary_entry_frame = tk.Frame(window)
diary_entry_frame.pack(pady=10)

# Time Input
time_label = tk.Label(diary_entry_frame, text="Time:")
time_label.grid(row=0, column=0, padx=10, pady=5)
time_entry = tk.Entry(diary_entry_frame)
time_entry.grid(row=0, column=1)

# Place Input
place_label = tk.Label(diary_entry_frame, text="Place:")
place_label.grid(row=1, column=0, padx=10, pady=5)
place_entry = tk.Entry(diary_entry_frame)
place_entry.grid(row=1, column=1)

# Duration Input
duration_label = tk.Label(diary_entry_frame, text="Duration:")
duration_label.grid(row=2, column=0, padx=10, pady=5)
duration_entry = tk.Entry(diary_entry_frame)
duration_entry.grid(row=2, column=1)

# Description Input
description_label = tk.Label(diary_entry_frame, text="Description:")
description_label.grid(row=3, column=0, padx=10, pady=5)
description_entry = tk.Text(diary_entry_frame, height=5)
description_entry.grid(row=3, column=1)

# Priority Input
priority_label = tk.Label(diary_entry_frame, text="Priority:")
priority_label.grid(row=4, column=0, padx=10, pady=5)
priority_options = ["Low", "Medium", "High"]
priority_var = tk.StringVar()
priority_var.set(priority_options[0])
priority_dropdown = tk.OptionMenu(diary_entry_frame, priority_var, *priority_options)
priority_dropdown.grid(row=4, column=1)

# Save Entry Button
save_button = tk.Button(window, text="Save Entry", command=save_entry)
save_button.pack(pady=10)

# Remove Entry Button
remove_button = tk.Button(window, text="Remove Entry", command=remove_entry)
remove_button.pack(pady=10)

# Edit Button
edit_button = tk.Button(window, text="Edit Entry", command=edit_entry)
edit_button.pack(pady=10)

# Settings Button
settings_button = tk.Button(window, text="Settings", command=settings)
settings_button.pack(pady=10)



window.mainloop()
