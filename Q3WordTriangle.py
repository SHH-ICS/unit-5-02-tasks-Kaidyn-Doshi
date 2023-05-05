while True: 
    word = input("Enter a word or type quit to exit: ")
    if word == "quit":
        break
    if word.isalpha() and " " not in word:
      for i in range(1, len(word)+1): 
        print(word[:i])
    else: 
      print("Invalid input. Please enter a single word with only letters.") 
