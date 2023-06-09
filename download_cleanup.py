import os
import logging

"""
This file provides functionality to sort downloaded files into their respective folders regarding their file extension.
"""

# setup logging to console and file
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s", handlers=[logging.StreamHandler(), logging.FileHandler("C:\\Users\\{}\\Documents\\Coding\\utils\\logging\\download_cleanup.log".format(os.getlogin()))])


def cleanup():
    """
    Sorts the files in the download folder into their respective folders.
    """
    # Get all files in the download folder
    files = os.listdir("C:\\Users\\{}\\Downloads".format(os.getlogin()))
    files_moved = 0
    # Iterate over all files
    for file in files:
        # Check if file is a folder
        if os.path.isdir("C:\\Users\\{}\\Downloads\\{}".format(os.getlogin(), file)):
            continue
        files_moved += 1
        # Get the extension of the file
        extension = file.split(".")[-1]
        # Check if the extension is known
        if os.path.exists("C:\\Users\\{}\\Downloads\\{}".format(os.getlogin(), extension)):
            # Move the file into the respective folder
            os.rename("C:\\Users\\{}\\Downloads\\{}".format(os.getlogin(), file), "C:\\Users\\{}\\Downloads\\{}\\{}".format(os.getlogin(), extension, file))
        else:
            # Create a new folder for the extension
            os.mkdir("C:\\Users\\{}\\Downloads\\{}".format(os.getlogin(), extension))
            logging.info("Created new folder for extension {}.".format(extension))
            # Move the file into the respective folder and catch the exception if the file already exists
            try:
                os.rename("C:\\Users\\{}\\Downloads\\{}".format(os.getlogin(), file), "C:\\Users\\{}\\Downloads\\{}\\{}".format(os.getlogin(), extension, file))
            except FileExistsError:
                conflicting_target_files = [target_file if file in target_file else ... for target_file in os.listdir("C:\\Users\\{}\\Downloads\\{}".format(os.getlogin(), extension))]
                # Rename the file to avoid overwriting
                os.rename("C:\\Users\\{}\\Downloads\\{}".format(os.getlogin(), file), "C:\\Users\\{}\\Downloads\\{}\\{}-{}".format(os.getlogin(), extension, len(conflicting_target_files), file))
    logging.info("Moved {} files.".format(files_moved))


if __name__ == "__main__":
    cleanup()
