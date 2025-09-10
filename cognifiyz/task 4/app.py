# Temperature Converter Program
# Author: Srimayee (Customized Advanced Version)

def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9


def get_temperature_input() -> float:
    """Prompt user for temperature input with validation."""
    while True:
        try:
            temp = float(input("Enter the temperature value: "))
            return temp
        except ValueError:
            print("❌ Invalid input! Please enter a valid numeric temperature.")


def get_conversion_choice() -> str:
    """Prompt user for conversion choice with validation."""
    print("\nChoose conversion direction:")
    print("1. Celsius → Fahrenheit")
    print("2. Fahrenheit → Celsius")
    while True:
        choice = input("Enter choice (1/2): ").strip()
        if choice in ["1", "2"]:
            return choice
        print("❌ Invalid choice! Please enter 1 or 2.")


def main():
    print("🌡️ Welcome to the Temperature Converter 🌡️")
    temperature = get_temperature_input()
    choice = get_conversion_choice()

    if choice == "1":
        result = celsius_to_fahrenheit(temperature)
        print(f"\n✅ {temperature}°C = {result:.2f}°F")
    else:
        result = fahrenheit_to_celsius(temperature)
        print(f"\n✅ {temperature}°F = {result:.2f}°C")

    print("\n🎯 Conversion Completed Successfully!")


if __name__ == "__main__":
    main()
