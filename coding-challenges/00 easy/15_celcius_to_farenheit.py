"""
Celsius to Fahrenheit

Given a temperature in Celsius degrees, convert it to Fahrenheit 
and return the result rounded to two decimal places.

Formula:
F = (C * 9/5) + 32

Notes:
- The result must be a float.
- Round to exactly two decimal places.
"""

def celsius_to_fahrenheit(celsius: float) -> float:
    return round(celsius * 9/5 +32, 2)

# Examples
print(celsius_to_fahrenheit(0))    # 32
print(celsius_to_fahrenheit(100))  # 212
print(celsius_to_fahrenheit(37))   # 98.6
print(celsius_to_fahrenheit(-40))  # -40