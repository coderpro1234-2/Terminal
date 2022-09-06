import getpass,time,os,subprocess
from datetime import datetime
from colorama import Fore,Style
print(Style.RESET_ALL)
now = datetime.now()
USERNAME = ""
PASSWORD = ""
CONFPASSWORD = "0"
askpassword = 1
actdir = "/home/user"
directorydir = "~"
def checksudo(terminal, text, reqsudo):
  if terminal[0:5] == "sudo ":
    if terminal[5:len(terminal)] == text:
      if reqsudo == 0:
        print("sudo: unknown command")
        return False
      else:
        return True
  else:
    if terminal[0:len(terminal)] == text:
      if reqsudo == 1:
        print("command requires sudo")
        return False
      else:
        return True
  return False
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
actdir = "/home/"+USERNAME
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
  if checksudo(terminal,"echo",2):
    if terminal[0:5] == "echo ":
      print(terminal[6:len(terminal)])
    else:
      print(terminal[10:len(terminal)])
  elif checksudo(terminal,"exit",0) or checksudo(terminal,"logout",0):
    exit()
  elif checksudo(terminal,"clear",2):
    if os.name == "nt" or os.name == "Windows":
      os.system("cls")
    else:
      os.system("clear")
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
  elif checksudo(terminal,"pwd",2):
    print(actdir)
  elif checksudo(terminal,"date",2):
    day = now.strftime("%A")
    month = now.strftime("%B")
    print(now.strftime(day[0:3]+" %d "+month[0:3]+" %Y %I:%M:%S %p"))