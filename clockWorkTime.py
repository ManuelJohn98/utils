"""
This file provides functionality to automatically clock in and out of work, as well as register breaks. It will store them in a csv file.
"""

import os
import logging
import datetime
import locale

# set locale for datetime to Germany
locale.setlocale(locale.LC_ALL, "de_DE")

# setup logging to console and file
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s", handlers=[logging.StreamHandler(), logging.FileHandler("C:\\Users\\{}\\Documents\\Coding\\utils\\logging\\clock_work_time.log".format(os.getlogin()))])

def clock_in() -> str:
    """
    Returns the current time in the format "mm;dd;hh,mm;"
    """
    logging.info("Clocking in...")
    return datetime.datetime.now().strftime("%B;%d;%H,%M;")

def clock_out() -> str:
    """
    Returns the current time in the format "hh,mm;"
    """
    logging.info("Clocking out...")
    return datetime.datetime.now().strftime("%H,%M;")
    

def create_employer(employer:str) -> None:
    """
    Creates a new employer-specific csv clocking file.
    """
    logging.info("Creating new employer {}...".format(employer))
    # create clocking file
    os.makedirs("C:\\Users\\{}\\Documents\\Coding\\utils\\clocking".format(os.getlogin()), exist_ok=True)
    with open("C:\\Users\\{}\\Documents\\Coding\\utils\\clocking\\{}.csv".format(os.getlogin(), employer), "w") as f:
        f.write("month;day;in;out;\n")

def main() -> None:
    """
    Prompts the user to clock in or out and registers the time in the appropriate csv file.
    """
    while True:
        try:
            logging.info("Starting clocking...")
            while True:
                employer = input("Enter employer: ").lower()
                if not employer == "":
                    break
                logging.warning("No employer entered.")
            if not os.path.exists("C:\\Users\\{}\\Documents\\Coding\\utils\\clocking\\{}.csv".format(os.getlogin(), employer)):
                create_employer(employer)
            clock_in_out_time:str # stores the time when the user clocked in and out in the format "mm;dd;hh,mm;hh,mm;"
            input("Press enter to clock in...")
            clock_in_out_time = clock_in()
            logging.info("Currently clocked in at {} for {}.".format(clock_in_out_time, employer))
            input("Press enter to clock out...")
            clock_in_out_time += clock_out()
            logging.info("Clocked out at {} for {}.".format(clock_in_out_time, employer))
            try:
                with open("C:\\Users\\{}\\Documents\\Coding\\utils\\clocking\\{}.csv".format(os.getlogin(), employer), "a") as f:
                    f.write(clock_in_out_time + "\n")
                logging.info("Successfully clocked in and out for {}.".format(employer))
            except Exception as e:
                logging.error("Failed to clock in and out for {}: {}".format(employer, e))
            if input("Press enter to exit or enter '0' to clock in and out again...\n") == "0":
                continue
            break
        except KeyboardInterrupt:
            if input("\nAre you sure you want to exit? Press enter to exit or enter '0' to clock in and out again...\n") == "0":
                continue
            logging.info("Keyboard interrupt.\nExiting...")
            break


if __name__ == "__main__":
    main()
