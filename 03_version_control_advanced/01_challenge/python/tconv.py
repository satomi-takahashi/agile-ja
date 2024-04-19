def convert_celsius_to_fahrenheit():
    print("Enter the temperature in Celsius:")
    celsius = input()
    celsius = int(celsius)
    fahrenheit = (celsius * 9/5) + 32
    print(f"The Celsius temperature {celsius} you entered is {fahrenheit} in Fahrenheit.")

def convert_fahrenheit_to_celsius():
    print("Enter the temperature in Frenheit:")
    fehrenheit = input()
    fehrenheit = int(fehrenheit)
    celsius = 5/9 * ( fehrenheit - 32)
    print(f"The Fehrenheit temprature {fehrenheit} you entered is {celsius} in Celsius.")

def main():
    convert_celsius_to_fahrenheit()
    convert_fahrenheit_to_celsius()
    user_input == input()
    if user_input == "c":
        convert_celsius_to_fahrenheit
    elif user_input == "f":
        convert_fahrenheit_to_celsius
    else: 
        print("Invalid input. Please try again.")
    
    

main()

