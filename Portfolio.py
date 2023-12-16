def is_in_range(number):
    return 0 <= number <= 100
user_input = int(input("Enter an integer: "))
if is_in_range(user_input):
    print(f"{user_input} is in the range 0 to 100.")
else:
    print(f"{user_input} is outside the range 0 to 100.")
if __name__ == '__main__':
    def count_upper_lower(input_string):
        upper_count = 0
        lower_count = 0
        for char in input_string:
            if char.isupper():
                upper_count += 1
            elif char.islower():
                lower_count += 1
        return upper_count, lower_count
    user_input = input("Enter a string: ")
    upper, lower = count_upper_lower(user_input)
    print(f"Uppercase letters: {upper}")
    print(f"Lowercase letters: {lower}")
if __name__ == '__main__':
    def greet_user():
        user_name = input("Enter your name: ")
        formatted_name = user_name.capitalize()
        print(f"Hello, {formatted_name}!")
    greet_user()
if __name__ == '__main__':
    def remove_last_character(input_string):
        if len(input_string) <= 1:
            return input_string
        else:
            return input_string[:-1]
    user_input = input("Enter a string: ")
    result = remove_last_character(user_input)
    print(f"Original string: {user_input}")
    print(f"String with last character removed: {result}")
if __name__ == '__main__':
    def celsius_to_fahrenheit(celsius):
        fahrenheit = (celsius * 9 / 5) + 32
        return fahrenheit
    def fahrenheit_to_celsius(fahrenheit):
        celsius = (fahrenheit - 32) * 5 / 9
        return celsius
    celsius_value = 25
    fahrenheit_value = 77
    result_fahrenheit = celsius_to_fahrenheit(celsius_value)
    print(f"{celsius_value} degrees Celsius is equal to {result_fahrenheit:.2f} degrees Fahrenheit")
    result_celsius = fahrenheit_to_celsius(fahrenheit_value)
    print(f"{fahrenheit_value} degrees Fahrenheit is equal to {result_celsius:.2f} degrees Celsius")
if __name__ == '__main__':
    def celsius_to_fahrenheit(celsius):
        fahrenheit = (celsius * 9 / 5) + 32
        return fahrenheit
    user_input = input("Enter the temperature in centigrade (e.g., 25C): ")
    numeric_part = float(user_input[:-1])
    if user_input[-1].lower() == 'c':
        result_fahrenheit = celsius_to_fahrenheit(numeric_part)
        print(f"{user_input} is equal to {result_fahrenheit:.2f}F")
    else:
        print("Invalid input. Please enter a number followed by 'C'.")
if __name__ == '__main__':
    def calculate_average():
        values = []

        while True:
            user_input = input("Enter a value (press Enter to finish): ")

            if user_input == '':
                break

            try:
                value = float(user_input)
                values.append(value)
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        if not values:
            print("No values entered.")
        else:
            average = sum(values) / len(values)
            print("Average:", average)