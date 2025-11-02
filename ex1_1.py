#Exercise 1.1: Temperature Converter
# F = C × 9/5 + 32
# K = C + 273.15
def temperature_converter():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    
    choice = input("Choose conversion (1-4): ")
    
    if choice == '1':
        celsius = float(input("Enter temperature: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C = {fahrenheit}°F")
        
    elif choice == '2':
        fahrenheit = float(input("Enter temperature: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F = {celsius}°C")
        
    elif choice == '3':
        celsius = float(input("Enter temperature: "))
        kelvin = celsius + 273.15
        print(f"{celsius}°C = {kelvin}K")
        
    elif choice == '4':
        kelvin = float(input("Enter temperature: "))
        celsius = kelvin - 273.15
        print(f"{kelvin}K = {celsius}°C")
        
    else:
        print("Invalid choice. Please select a number between 1 and 4.")



temperature_converter()


