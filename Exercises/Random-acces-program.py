import random

word = "index"
print(f"The word is: {word}")

high = len(word)
low = -len(word)

for i in range(10):
    position = random.randrange(low,high)
    print("word[", position, "]\t", word[position])