def count_even_length_words(sentence):
    words = sentence.split()
    return sum(1 for word in words if len(word) % 2 == 0)


sentence = input("Введите строку: ")
print("Количество слов с четным количеством символов:", count_even_length_words(sentence))