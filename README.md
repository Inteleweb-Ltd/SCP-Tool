# SCP-Tool
A simple Tool in Python to help you make an SCP syntax

### scp-tool
scp-tool is a simple graphical user interface (GUI) application that allows you to copy files from your local machine to a remote server using Secure Copy Protocol (SCP). It supports both Windows and Linux operating systems and can run on Windows Subsystem for Linux (WSL).

### Features
- Browse for a local file to copy (copy as path)
- Enter the remote directory, host, and username
- Generate and display the SCP command
- Run the SCP command in WSL Debian terminal
- Validate the input and output of the SCP command
### Installation
To install scp-tool, you need to have the following prerequisites:

- Python 3.10 or higher
- tkinter package
    - Windows

    ```console
    pip install tk
    ```
    - Linux
    ```console
    sudo apt install python3-tk
    ```

### Usage
To run scp-tool, you can use the following command in the Terminal app:

```console
python scptool.py
```

This will open a GUI window like this:

![A screenshot of the GUI](/src/Screenshot.png)

Browse for a local file and enter the other information. Then, you can click the generate command button to get the SCP command in the text widget. You can copy and paste the command in the terminal to run it.

## Build
You can build an executable file using CX_Freeze for your relevant OS. MAC, Linux and Windows are all supported
```console
pip install cx_Freeze
```
```console
python setup.py build
```

### Contributing
If you want to contribute to scp-tool, you can fork the project and create a pull request with your changes. Please follow the code style and documentation guidelines of the project.

### License
scp-tool is licensed under the MIT License. See the LICENSE file for more details.
