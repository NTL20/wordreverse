# This part of the program establishes a variable (word), and it also asks you to input word(s) to reverse.
word = input("Input word(s) to reverse:")

# This part of the program is a for loop. In the for loop, it gets the length of the word you type. Next, the
# '-1, -1, -1 part of the program converts it into backwards text, and the next line plays a big part in successfully
# doing this as well, since the end part of the program ends a significant part of the program, which is converting
# word(s) we enter into backwards text. Finally, the "\n" command ends a line of text, and this ends the program too.
for char in range(len(word) - 1, -1, -1):
  print(word[char], end="")
print("\n")