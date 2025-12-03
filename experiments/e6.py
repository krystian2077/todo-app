contents = ["Python is best programming language",
            "Java is ok programming language",
            "C++ is bad programming language"]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"../files/{filename}", "w")
    file.write(content)
    file.close()
