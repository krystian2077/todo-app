# import glob
#
# my_files = glob.glob("files/*.txt")
#
# for filepath in my_files:
#     with open(filepath, 'r') as file:
#         print(file.read())
#
# print(my_files)
import webbrowser

# import csv
#
# with open('weather.csv', 'r') as file:
#     data = list(csv.reader(file))
#
#
# city = input("Enter city: ")
#
# for row in data:
#     if row[0] == city:
#         print(row[1])

# import shutil
#
# shutil.make_archive("output", "zip", "files")

user_term = input("Enter your search term: ")

webbrowser.open(f"https://www.google.com/search?q={user_term}")
