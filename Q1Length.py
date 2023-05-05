while True:
  word = input("Enter a word or type quit to exit: ")
  if word == "quit":
    break
  elif word.isalpha() and " " not in word:
    length = len(word)
    print(f"There are {length} characters in the word \"{word}\"")
  else:
    print("Invalid input. Please enter a single word with only letters.")
