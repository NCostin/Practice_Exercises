print("Creating a text file with the writelines() method.")
text_file = open("write_it2.txt", "w")

lines = ["Line 1\n",
		"This is line 2\n",
		"That makes this line 3\n"]

text_file.writelines(lines)
text_file.close()

print("\nReading the newly created file.")
text_file = open("write_it2.txt", "r")
print(text_file.read())
text_file.close()

input("\n\nPress the enter key to exit.")