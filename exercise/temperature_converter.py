def get_valid_input():
    input_temperature = input("Enter temperature ending with C for celsius or F for fahrenheit.\
    \nExample: 50.78C or 212F.\
    \nTemperature: ")
    input_scale = input_temperature[-1].lower()
    input_temperature = input_temperature[0:-1]
    if not (input_temperature.strip("-").isnumeric() and input_scale in ["c", "f"]):
        input_temperature, input_scale = get_valid_input()
    return float(input_temperature), input_scale


def fahrenheit_to_celsius(t):
    if t < -459.67:
        f_to_c_result = "Temperature below -459.67 fahrenheit does not exist"
    else:
        celsius = round((t - 32) * (5 / 9), 2)
        f_to_c_result = f"{t} fahrenheit is {celsius} celsius"
    return f_to_c_result


def celsius_to_fahrenheit(t):
    if t < -273.15:
        c_to_f_result = "Temperature below -273.15 celsius does not exist"
    else:
        fahrenheit = round(t * (9 / 5) + 32, 2)
        c_to_f_result = f"{t} celsius is {fahrenheit} fahrenheit"
    return c_to_f_result


if __name__ == "__main__":
    temperature, scale = get_valid_input()

    if scale == 'c':
        result = celsius_to_fahrenheit(temperature)
    elif scale == 'f':
        result = fahrenheit_to_celsius(temperature)
    print(result)