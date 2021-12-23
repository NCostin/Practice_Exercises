import sys

def open_file(file_name, mode):
	"""Open a file."""
	try:
		the_file = open(file_name, mode)
	except IOError as e:
		print("Unable to open the file", file_name, "Ending program.\n", e)
		input("\n\nPress the enter key to exit.")
		sys.exit()
	else:
		return the_file


def next_line(the_file):
	"""Return next line from trivia file, formatted."""
	line = the_file.readline()
	line = line.replace("/", "\n")
	return line


def next_block(the_file):
	"""Return the next block of data from the trivia file."""
	category = next_line(the_file)

	question = next_line(the_file)

	answers = []
	for i in range(4):
		answers.append(next_line(the_file))

	correct = next_line(the_file)
	if correct:
		correct = correct[0]

	explanation = next_line(the_file)

	return category, question, answers, correct, explanation


def welcome(title):
	"""Welcome the player and get his/her name."""
	print("\t\tWelcome to Trivia Challenge!\n")
	print("\t\t", title, "\n")


def main():
    trivia_file = open_file("trivia.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0
    
    #get first block
    category, question, answers, correct, explanation = next_block(trivia_file)
    while category:
        #ask a question
        print(category)
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])
            
        #get asnwer
        answer = input("What's you answer?: ")
        
        #check answer
        if answer == correct:
            print("\nRight!", end=" ")
            score += 1
        else:
            print("\nWrong.", end=" ")
        print(explanation)
        print("Score:", score, "\n\n")
        
        #get next block
        category, question, answers, correct, explanation = next_block(trivia_file)
        
    trivia_file.close()
    
    print("That was the last question!")
    print("You're final score is", score)

main()
input("\n\nPress the enter key to exit.")

"""
open_file(file_name, mode)
-deschide fisierul si efectueaza o serie de verificari
-returnreaza fisiserul the_file

next_line(the_file)
-citeste linia din fisiser si o formateaza
-returneaza line

next_block(the_file)
-stocheaza in variabila category, linia aferenta din fisier
-stocheaza in variabila question, linia aferenta din fisier
-stocheaza in lista answers, liniile aferente cu raspunsurile din fisier
-stocheaza in variabila corect, linia aferenta din fisier
    -daca este adevarat, correct = correct[0]
-stocheaza in variabila explanation, linia aferenta din fisier
-returneaza category, question, answers, correct, explanation

welcome(title)
-afiseaza titlul


main()
-stocheaza in variabila trivia_file valoarea returnata de funct open_file
-stocheaza in variabila title primul rand din fisier
-ruleaza functia welcome(title)
-stocheaza in variabilele category, question, answers, correct, explanation, valorile returnate de functia next_block(trivia_file)
-intra intr-un loop while unde afiseaza categoria, intrebarile si raspunsurile, daca categoria este inexistenta, iese din loop
    -asteapta un raspuns de la utilizator
    -verifica daca raspunsul este corect
    -afiseaza explicatia
    -afiseaza scorul
    -sunt colectate datele de la urmatoarea intrebare
-se inchide fisierul
"""