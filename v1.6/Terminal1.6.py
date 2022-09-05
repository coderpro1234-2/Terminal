import getpass,time,os
from colorama import Fore,Style
print(Style.RESET_ALL)
USERNAME = ""
PASSWORD = ""
CONFPASSWORD = "0"
askpassword = 1
directorydir = "~"
while USERNAME == "" or USERNAME == "0":
  USERNAME = input("Username: ")
  if USERNAME == "" or USERNAME == "0":
    print("Sorry, but you can't use that username. Try again.")
while PASSWORD != CONFPASSWORD:
  while PASSWORD == "" or PASSWORD == "0":
    PASSWORD = getpass.getpass("Password: ")
    if PASSWORD == "" or PASSWORD == "0":
      print("Sorry, but you can't use that password. Try again.")
  CONFPASSWORD = getpass.getpass("Confirm Password: ")
  if PASSWORD != CONFPASSWORD:
    print("Passwords Are Incorrect. Please Try Again")
terminaltext = USERNAME+"@terminal"
if os.name == "nt" or os.name == "Windows":
  os.system("cls")
else:
  os.system("clear")
while True:
  terminal = input((Fore.GREEN+terminaltext)+(Style.RESET_ALL+":")+(Fore.CYAN+directorydir)+(Style.RESET_ALL+"$ ")+(Style.RESET_ALL))
  hassudo = False
  if terminal[0:5] == "sudo " and askpassword == 1:
    TESTPASS = ""
    while TESTPASS != PASSWORD:
      TESTPASS = getpass.getpass("[sudo] password for "+USERNAME+": ")
      if TESTPASS != PASSWORD:
        print("Sorry, try again.")
    askpassword = 0
  if terminal[0:5] == "echo " or terminal[0:10] == "sudo echo ":
    if terminal[0:5] == "echo ":
      print(terminal[5:len(terminal)])
    else:
      print(terminal[10:len(terminal)])
  elif terminal == "exit" or terminal == "sudo exit" or terminal == "logout" or terminal == "sudo logout":
    exit()
  elif terminal == "clear" or terminal == "sudo clear":
    if os.name == "nt" or os.name == "Windows":
      os.system("cls")
    else:
      os.system("clear")
  elif terminal == "time" or terminal == "sudo time":
    print("The current time is: "+time.strftime("%H:%M:%S"))