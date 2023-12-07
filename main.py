# Import tkinter and filedialog modules
import tkinter as tk
from tkinter import filedialog

# Create a root window
root = tk.Tk()
root.title("SCP Command Generator")

# Create a function to copy the text widget content to the clipboard
def generate_and_copy():
  file = file_entry.get()
  directory = dir_entry.get() 
  host = host_entry.get()
  user = user_entry.get()

  command = f"scp {file} {user}@{host}:{directory}"
  
  text.delete(1.0, tk.END)
  text.insert(1.0, command)
  
  root.clipboard_clear()
  root.clipboard_append(command)


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
button = tk.Button(root, text="Generate and Copy", command=generate_and_copy)

# Create a text widget to display the command
text = tk.Text(root, height=2, width=40)

# Create a function to browse for a local directory
def browse_directory():
    # Use filedialog to ask for a directory
    directory = filedialog.askdirectory()
    # Set the entry widget text to the directory
    dir_entry.delete(0, tk.END)
    dir_entry.insert(0, directory)

# Pack all the widgets in the root window
file_label.pack()
file_entry.pack()
dir_label.pack()
dir_entry.pack()
host_label.pack()
host_entry.pack()
user_label.pack()
user_entry.pack()
button.pack()
text.pack()

# Enter the main loop
root.mainloop()
