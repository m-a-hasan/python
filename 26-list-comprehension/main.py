# list_comprehension = [new_item for item in list if test]
# dictionary_comprehension = {new_key:new_value for (key, value) in dict.items() if test}
import random

number = [1, 2, 3]
new_numbers = [n + 1 for n in number]
print(f"Increase list element by 1: {new_numbers}")

name = "Abid"
letters_list = [s for s in name]
print(f"Transform word to a list of letters: {letters_list}")

my_range = range(1, 5)
range_list = [r * 2 for r in my_range]
print(f"Transform range to a list: {range_list}")

names = ["Abid", "Maryam", "Fatima", "Ayah"]
short_names = [n for n in names if len(n) < 5]
print(f"Search names that has less than 5 chars: {short_names}")

caps_long_names = [n.upper() for n in names if len(n) > 4]
print(f"Capital case names with more than 4 chars: {caps_long_names}")

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n**2 for n in numbers]
print(f"Squared numbers of a list: {squared_numbers}")

result = [n for n in numbers if n % 2 == 0]
print(f"Find even numbers in a list: {result}")

with open("file1.txt") as file1:
    f1 = [int(line.rstrip()) for line in file1]
    with open("file2.txt") as file2:
        f2 = [int(line.rstrip()) for line in file2]
        common_numbers = [n for n in f1 if n in f2]
        print(f"Find common numbers in 2 files {common_numbers}")

students = {name: random.randint(30, 100) for name in names}
passed_students = {student: score for (student, score) in students.items() if score >= 60}
print(f"All student grades: {students}")
print(f"Passed student grades: {passed_students}")

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words = sentence.split()
result = {word: len(word) for word in words}
print(f"Word length count in dictionary format: {result}")

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day: (temp * 9/5) + 32 for (day, temp) in weather_c.items()}
print(f"Temperature in fahrenheit: {weather_f}")
