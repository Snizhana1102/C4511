import inspect
from colorama import init, Fore, Style

init()

print("--- Дослідження бібліотеки colorama ---")
print("Вміст модуля:", dir())

print("\nКольори тексту (Fore):")
for item in dir(Fore):
    if not item.startswith("_"):
        print(item)

print("\nСтилі (Style):")
for item in dir(Style):
    if not item.startswith("_"):
        print(item)

print("\nЧи є Fore класом?", inspect.isclass(Fore))

print(Fore.RED + "Це червоний текст" + Style.RESET_ALL)
print(Fore.GREEN + "Це зелений текст" + Style.RESET_ALL)
