# member = input("Add a new member: ")
#
# file = open("members.txt", "r")
# members = file.readlines()
# file.close()
#
# members.append(member + "\n")
#
# file = open("members.txt", "w")
# file.writelines(members)
# file.close()

filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for filename in filenames:

    file = open(f"../files/{filename}", "w")
    file.write("Hello")
    file.close()

