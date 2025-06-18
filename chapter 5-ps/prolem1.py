words = { "madad": "help", "kursi": "chair", "billi": "cat" }
word = input("Enter the word you want the meaning of: ")

print(words.get(word, "Word not found in dictionary."))