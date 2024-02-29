# class Fraction:
#     count = 0
#
#     def __init__(self, numerator, denominator):
#         self.numerator = numerator
#         self.denominator = denominator
#         Fraction.count += 1
#
#     @staticmethod
#     def get_instance_count():
#         return Fraction.count
#
#
# fraction1 = Fraction(1, 2)
# fraction2 = Fraction(3, 4)
# fraction3 = Fraction(4, 6)
#
# print(Fraction.get_instance_count())


# 2


# class TemperatureConverter:
#     count = 0
#
#     @staticmethod
#     def celsius_to_fahrenheit(celsius):
#         TemperatureConverter.count += 1
#         return (celsius * 9/5) + 32
#
#     @staticmethod
#     def fahrenheit_to_celsius(fahrenheit):
#         TemperatureConverter.count += 1
#         return (fahrenheit - 32) * 5/9
#
#     @staticmethod
#     def get_conversion_count():
#         return TemperatureConverter.count
#
#
# celsius_temp = 25
# fahrenheit_temp = TemperatureConverter.celsius_to_fahrenheit(celsius_temp)
# print(f"{celsius_temp} градусов Цельсия = {fahrenheit_temp} градусов Фаренгейта")
#
# new_celsius_temp = TemperatureConverter.fahrenheit_to_celsius(fahrenheit_temp)
# print(f"{fahrenheit_temp} градусов Фаренгейта = {new_celsius_temp} градусов Цельсия")
#
# print(f"Количество конвертаций температуры: {TemperatureConverter.get_conversion_count()}")



# 3



# class LengthConverter:
#     @staticmethod
#     def meters_to_feet(meters):
#         return meters * 3.28084
#
#     @staticmethod
#     def feet_to_meters(feet):
#         return feet / 3.28084
#
# meters_length = 10
# feet_length = LengthConverter.meters_to_feet(meters_length)
# print(f"{meters_length} метров = {feet_length}")
#
# new_meters_length = LengthConverter.feet_to_meters(feet_length)
# print(f"{feet_length} футов = {new_meters_length} метров")

