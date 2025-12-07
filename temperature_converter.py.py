# ---------------------------------------------------
#     TEMPERATURE CONVERTER TOOL (C, F, K SUPPORT)
# ---------------------------------------------------

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32


def menu():
    print("\n======================================")
    print("      TEMPERATURE CONVERTER TOOL      ")
    print("======================================")
    print("1. Celsius → Fahrenheit")
    print("2. Fahrenheit → Celsius")
    print("3. Celsius → Kelvin")
    print("4. Kelvin → Celsius")
    print("5. Fahrenheit → Kelvin")
    print("6. Kelvin → Fahrenheit")
    print("7. Exit")
    print("======================================")


while True:
    menu()
    choice = input("Enter your choice (1–7): ")

    try:
        if choice == "1":
            c = float(input("Enter temperature in Celsius: "))
            print(f"{c}°C = {celsius_to_fahrenheit(c):.2f}°F")

        elif choice == "2":
            f = float(input("Enter temperature in Fahrenheit: "))
            print(f"{f}°F = {fahrenheit_to_celsius(f):.2f}°C")

        elif choice == "3":
            c = float(input("Enter temperature in Celsius: "))
            print(f"{c}°C = {celsius_to_kelvin(c):.2f}K")

        elif choice == "4":
            k = float(input("Enter temperature in Kelvin: "))
            print(f"{k}K = {kelvin_to_celsius(k):.2f}°C")

        elif choice == "5":
            f = float(input("Enter temperature in Fahrenheit: "))
            print(f"{f}°F = {fahrenheit_to_kelvin(f):.2f}K")

        elif choice == "6":
            k = float(input("Enter temperature in Kelvin: "))
            print(f"{k}K = {kelvin_to_fahrenheit(k):.2f}°F")

        elif choice == "7":
            print("\nThank you! Exiting the converter. 👋")
            break

        else:
            print("Invalid input! Choose a number between 1 and 7.")

    except ValueError:
        print("❌ Error: Please enter a valid number!")
