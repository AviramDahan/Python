Sentence = input("Please enter Sentence: \n")
Sentence_SPLIT = Sentence[:len(Sentence)//2].lower() + Sentence[len(Sentence)//2:].upper()
print(Sentence_SPLIT)