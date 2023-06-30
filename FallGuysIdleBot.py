# FallGuysIdleBot.py

# IMPORTS
from pynput.keyboard import Key, Controller  # importing pynput to control keyboard
import pygetwindow as gw                     # importing pygetwindow to get fall guys window
from time import sleep                       # importing time.sleep to being able to wait a few seconds
from os import system, name
from colorama import Fore, Style

#############################################################################################################################
# CHANGE THOSE VALUES IF YOU WANT
time_to_wait = 10             # in seconds, the higher it is, the less you will get screen flickering when changing windows
key_to_press = Key.enter      # change to "Key.space" or "Key.h" for example
change_window = True          # if you change this to false, Fall Guys must be open all the time!
#############################################################################################################################


banner = Fore.GREEN + r"""
  ______ _____             ______ _  __   ____        _   
 |  ____/ ____|      /\   |  ____| |/ /  |  _ \      | |  
 | |__ | |  __      /  \  | |__  | ' /   | |_) | ___ | |_ 
 |  __|| | |_ |    / /\ \ |  __| |  <    |  _ < / _ \| __|
 | |   | |__| |   / ____ \| |    | . \   | |_) | (_) | |_ 
 |_|    \_____|  /_/    \_\_|    |_|\_\  |____/ \___/ \__|

 V.1.0                   created by kk, github.com/kk-dev7

""" + Style.RESET_ALL

if name == 'nt':                                                                                    # if you're on Windows...
    system('cls')                                                                                   # clear the screen
else:                                                                                               # if you're on macOS, linux, or other...
    system('clear')                                                                                 # clear the screen
print(banner)                                                                                       # print the splash screen

keyboard = Controller()                                                                             # to be able to send inputs to fall guys
gw.getAllTitles()                                                                                   # getting all processes

if change_window is True:                                                                               # if we are allowed to change the window
    try:
        handle = gw.getWindowsWithTitle("FallGuys_client")[0]                                           # getting fall guys process
        print(Fore.BLUE + "\n[-] Auto Clicker started. Press 'Ctrl + C' to stop.\n" + Style.RESET_ALL)
        while True:
            # handle.activate()     # this function is kind of broken... do not uncomment
            handle.maximize()                                                                           # Maximizing fall guys
            keyboard.press(key_to_press)                                                                # pressing enter to start new round / end round in fall guys
            keyboard.release(key_to_press)                                                              # releasing enter because we don't want space to be pressed permanently
            handle.minimize()                                                                           # minimizing the window again, so you can continue to do your work
            sleep(time_to_wait)                                                                         # waiting x seconds then repeat the same thing again :)
    except IndexError:                                                                                  # if Fall Guys is not running, send error message
        print(Fore.RED + "[!] Fall Guys is not running. Please start Fall Guys and run this script again." + Style.RESET_ALL)

else:                                                                                                   # if we are not allowed to change the window
    print(Fore.BLUE + "\n[-] Auto Clicker started. Press 'Ctrl + C' to stop.\n" + Style.RESET_ALL)
    while True:
        keyboard.press(key_to_press)                                                                    # pressing enter to start new round / end round in fall guys
        keyboard.release(key_to_press)                                                                  # releasing enter because we don't want space to be pressed permanently
        sleep(time_to_wait)                                                                             # waiting x seconds then repeat the same thing again :)
