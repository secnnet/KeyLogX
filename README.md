# Keyboard Event Logger

This is a Python script that logs keyboard events by capturing and recording each key press. It utilizes the `pynput` library to monitor keyboard activity and stores the logged data in a specified file.

## Features

- Logs all keyboard key presses.
- Captures the timestamp, logged-in username, hostname, and the pressed key for each event.
- Saves the log file in the user's Downloads folder with a customizable name.

## Prerequisites

Before running the script, ensure that you have the following dependencies installed:

- Python 3.x
- `pynput` library

To install the `pynput` library, use the following command:

pip install pynput

## Usage

1. Clone the repository or download the `script.py` file.

2. Open the `script.py` file in a text editor.

3. Modify the following variables according to your preferences:

   - `log_filename`: The name of the log file. You can change it to a more descriptive name if desired.
   - `download_folder`: The path to the folder where the log file will be saved. By default, it is set to the user's Downloads folder.

4. Save the changes to the `script.py` file.

5. Run the script using the following command:

python script.py


6. The script will start capturing keyboard events and logging them to the specified file.

7. To stop the script, press `Ctrl + C` in the terminal.

## Privacy and Legal Considerations

It is important to note that capturing keyboard events without explicit consent may raise privacy concerns. Ensure that you use this script responsibly and comply with all applicable laws and regulations. Consider informing users about the presence of such a script and obtain their consent before logging their keyboard activity.

## License

This project is licensed under the [MIT License](LICENSE).
