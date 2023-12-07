# Import tkinter and filedialog modules
import tkinter as tk
from tkinter import filedialog

# Create a root window
root = tk.Tk()
root.title("SCP Command Generator")

# Create a function to browse for a local file
def browse_file():
    # Use filedialog to ask for a file
    filename = filedialog.askopenfilename()
    # Set the entry widget text to the filename
    file_entry.delete(0, tk.END)
    file_entry.insert(0, filename)

# Create four labels and four entry widgets
file_label = tk.Label(root, text="Local file:")
file_entry = tk.Entry(root)
dir_label = tk.Label(root, text="Remote directory:")
dir_entry = tk.Entry(root)
host_label = tk.Label(root, text="Remote host:")
host_entry = tk.Entry(root)
user_label = tk.Label(root, text="Username:")
user_entry = tk.Entry(root)

# Create a button widget to generate the command
button = tk.Button(root, text="Generate command")

# Create a text widget to display the command
text = tk.Text(root, height=2, width=40)

# Define a function to generate the command
def generate_command():
    # Get the input values from the entry widgets
    file = file_entry.get()
    directory = dir_entry.get()
    host = host_entry.get()
    user = user_entry.get()
    # Format the input values as a SCP command
    command = f"scp {file} {user}@{host}:{directory}"
    # Set the text widget text to the command
    text.delete(1.0, tk.END)
    text.insert(1.0, command)

# Bind the button widget to the function
button.config(command=generate_command)

# Pack all the widgets in the root window
file_label.pack()
file_entry.pack()
button.pack()
dir_label.pack()
dir_entry.pack()
host_label.pack()
host_entry.pack()
user_label.pack()
user_entry.pack()
text.pack()

# Enter the main loop
root.mainloop()
