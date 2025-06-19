from colorama import Fore, Style

def printRed(text, end='\n'):
    print(Fore.RED + str(text), end=end)

def printGreen(text, end='\n'):
    print(Fore.GREEN + str(text), end=end)

def printBlue(text, end='\n'):
    print(Fore.BLUE + str(text), end=end)

def printYellow(text, end='\n'):
    print(Fore.YELLOW + str(text), end=end)

def printCyan(text, end='\n'):
    print(Fore.CYAN + str(text), end=end)

def printMagenta(text, end='\n'):
    print(Fore.MAGENTA + str(text), end=end)

def printWhite(text, end='\n'):
    print(Fore.WHITE + str(text), end=end)

## Janky temp solution to formatting bold text properlly 

def printBoldRed(text, end='\n'):
    print(Style.BRIGHT + Fore.RED + str(text), end=end)

def printBoldGreen(text, end='\n'):
    print(Style.BRIGHT + Fore.GREEN + str(text), end=end)

def printBoldBlue(text, end='\n'):
    print(Style.BRIGHT + Fore.BLUE + str(text), end=end)

def printBoldYellow(text, end='\n'):
    print(Style.BRIGHT + Fore.YELLOW + str(text), end=end)

def printBoldCyan(text, end='\n'):
    print(Style.BRIGHT + Fore.CYAN + str(text), end=end)

def printBoldMagenta(text, end='\n'):
    print(Style.BRIGHT + Fore.MAGENTA + str(text), end=end)

def printBoldWhite(text, end='\n'):
    print(Style.BRIGHT + Fore.WHITE + str(text), end=end)
