# SCP-Tool
A simple Tool in Python to help you make an SCP syntax

scp-tool
scp-tool is a simple graphical user interface (GUI) application that allows you to copy files from your local machine to a remote server using Secure Copy Protocol (SCP). It supports both Windows and Linux operating systems and can run on Windows Subsystem for Linux (WSL).

Features
Browse for a local file to copy
Enter the remote directory, host, and username
Generate and display the SCP command
Run the SCP command in WSL Debian terminal
Validate the input and output of the SCP command
Installation
To install scp-tool, you need to have the following prerequisites:

Python 3.10 or higher
tkinter package
winget command line tool
WSL Debian terminal
You can install Python from here and tkinter from here for Windows, or from here for Linux. You can install winget from here and WSL Debian from [here].

You can also use pip to install the required Python packages from the requirements.txt file:

pip install -r requirements.txt

Usage
To run scp-tool, you can use the following command in the Terminal app:

python scptool.py

This will open a GUI window like this:

![A screenshot of the GUI]

You can use the button to browse for a local file and enter the other information in the entry widgets. Then, you can click the generate command button to get the SCP command in the text widget. You can copy and paste the command in the WSL Debian terminal to run it.

Contributing
If you want to contribute to scp-tool, you can fork the project from [here] and create a pull request with your changes. Please follow the code style and documentation guidelines of the project.

License
scp-tool is licensed under the MIT License. See the LICENSE file for more details.
