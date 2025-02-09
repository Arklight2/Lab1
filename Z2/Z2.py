import random

def shuffle_words(sentence):
    words = sentence.split()
    random.shuffle(words)
    return ' '.join(words)


sentence = input("Введите строку: ")
shuffled_sentence = shuffle_words(sentence)
print("Перемешанная строка:", shuffled_sentence)