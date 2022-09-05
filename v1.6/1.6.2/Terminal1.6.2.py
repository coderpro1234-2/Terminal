import getpass,time,os,subprocess
import webbrowser
from colorama import Fore,Style
print(Style.RESET_ALL)
USERNAME = ""
PASSWORD = ""
CONFPASSWORD = "0"
askpassword = 1
directorydir = "~"
while len(USERNAME) > 20 or len(USERNAME) < 2:
  USERNAME = input("Username: ")
  if len(USERNAME) > 20 or len(USERNAME) < 2:
    print("Sorry, but you can't use that username. Try again.")
while PASSWORD != CONFPASSWORD:
  while len(PASSWORD) > 20 or len(PASSWORD) < 2:
    PASSWORD = getpass.getpass("Password: ")
    if len(PASSWORD) > 20 or len(PASSWORD) < 2:
      print("Sorry, but you can't use that password. Try again.")
  CONFPASSWORD = getpass.getpass("Confirm Password: ")
  if PASSWORD != CONFPASSWORD:
    print("Passwords Are Incorrect. Please Try Again")
    PASSWORD = ""
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
  elif terminal == "./rickroll.exe" or terminal == "sudo ./rickroll.exe" or terminal == "bash rickroll.exe" or terminal == "sudo bash rickroll.exe":
    if os.name == "nt":
      subprocess.Popen("ASSets/rickroll.exe")
    for i in range(10):
      print("Get Rick Rolled!")
    USERNAME = "Get Rick Rolled!"
    PASSWORD = "Get Rick Rolled!"
    terminaltext = USERNAME+"@terminal"
    print('PASSWORD = "Get Rick Rolled!"')
  elif terminal == "ls" or terminal == "sudo ls":
    print(Fore.GREEN+"rickroll.exe"+Style.RESET_ALL)