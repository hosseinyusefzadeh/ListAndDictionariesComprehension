# numbers = [1, 2, 3]
# new_numbers = [n + 1 for n in numbers]
# print(new_numbers)

# name = "hossein"
# new_list = [letter for letter in name]
# print(new_list)


# new_numbers = [n * 2 for n in range(1, 5)]
# print(new_numbers)


# names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
# show_us_four_letter = [letter for letter in names if len(letter) == 4]
# show_us_more_than_four_letter = [letter.upper() for letter in names if len(letter) > 4]
# print(show_us_four_letter)
# print(show_us_more_than_four_letter)


################# power of list ########################
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# square_numbers = [number * number for number in numbers]
# print(square_numbers)


################ even number #################
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# result = [number for number in numbers if number % 2 == 0]
# print(result)


############### compare two list ##############
# with open("file1.txt") as file1:
#     file_1_data = file1.readlines()
#
# with open("file2.txt") as file2:
#     file_2_data = file2.readlines()
#
# result = [int(num) for num in file_1_data if num in file_2_data]
# print(result)

# import random
# names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
# students_score = {student:random.randint(1, 100) for student in names}
# print(students_score)
#
# new_dict = {student:random.randint(1, 100) for (student, score) in students_score.items() if score >= 60}
# print(new_dict)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {letter: len(letter) for letter in sentence.split()}
# print(result)


########### Converting Celcius to Farenhite ######################
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
#
# new_dict = {temp: (farenhite * 9/5) + 32 for (temp,farenhite) in weather_c.items()}
# print(new_dict)

# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

# student_data_frame = pandas.DataFrame(student_dict)
# # print(student_data_frame)
#
# for (index, row) in student_data_frame.iterrows():
#     print(row.student)

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet = {row.letter: row.code for (index, row) in data.iterrows()}
print(alphabet)

word = input("enter a word : ").upper()
output_list = [alphabet[letter] for letter in word]
print(output_list)