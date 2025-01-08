sentence = input("Enter a sentence: ")
word_count = len(sentence.split())
search_word = input("Enter the word to search for: ")
print(f"Word count: {word_count}, '{search_word}' found: {search_word in sentence}")
