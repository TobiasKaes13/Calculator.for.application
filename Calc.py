# Importiere das colorama-Modul
from colorama import init, Fore, Style

# Definition der Funktionen für die vier Grundrechenarten

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Fehler, da du durch 0 geteilt hast"


# Initialisiere colorama
init()

# Begrüßungsnachricht

print("Willkommen zum Taschenrechner!")

# Hauptschleife, um Benutzerinteraktion fortzusetzen

while True:
    # Menüoptionen anzeigen

    print("Bitte wählen Sie eine Operation:")
    print("1. Addition")
    print("2. Subtraktion")
    print("3. Multiplikation")
    print("4. Division")
    print("5. Beenden")

    # Benutzereingabe für die gewählte Option

    choice = input("deine Auswahl: ")

    # Beenden, wenn Option "5" ausgewählt wurde

    if choice == "5":
        print("Taschenrechner wird beendet.")
        break

    # Benutzereingabe für die beiden Zahlen

    num1 = float(input("Geben Sie die erste Zahl ein: "))
    num2 = float(input("Geben Sie die zweite Zahl ein: "))

    # Variablendefinition für das Ergebnis

    result = None

    # Durchführen der gewählten Operation

    if choice == "1":
        result = add(num1, num2)
    elif choice == "2":
        result = subtract(num1, num2)
    elif choice == "3":
        result = multiply(num1, num2)
    elif choice == "4":
        result = divide(num1, num2)

    # Ausgabe des Ergebnisses mit Farbhervorhebung

    if result is not None:
        print("Ergebnis: " + Fore.GREEN + str(result) + Style.RESET_ALL)
