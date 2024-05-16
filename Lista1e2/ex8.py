# Escreva um programa que converta uma temperatura digitada em "C” em “F”. A fórmula para essa conversão é: F = (9/5)*C+32

def celsius_para_fahrenheit(temp_celsius):
    return (9/5) * temp_celsius + 32

temp_celsius = float(input("Informe a temperatura em Celsius: "))
temp_fahrenheit = celsius_para_fahrenheit(temp_celsius)
print("A temperatura de {:.2f}°C corresponde a {:.2f}°F".format(temp_celsius, temp_fahrenheit))