import collections.abc
import re

vowels = ['а', 'е', 'и', 'о', 'у', 'ъ', 'я', 'ю']
bg_en = {}
def main ():


    f = open("bg-en.txt", encoding='utf-8', mode="r")
    arr = f.read().split('\n')
    bg_en_arr = [re.split('\t| | ', a) for a in arr]


    for pair in bg_en_arr:
        if len(pair) == 2:
            bg_en[pair[0]] = pair[1]

    sentence = input("Type something in bulgarian to translate:\n")

    #isinstance([0, 10, 20, 30], collections.abc.Sequence)

    while True:
        english = ""
        s_arr = sentence.split()
        if len(s_arr) == 0:
            continue
        for word in s_arr:
            en_word = bg_en[word] if word in bg_en else "?"
            if not isinstance(en_word, str):
                en_word = en_word[0]

            # check if last letter is vowel, if so, change for all other vowels to find definition
            if en_word == '?':
                en_word = checkVowels(word)

            english = english + en_word + " "

        print(english)
        sentence = input()
        if sentence == 'quit':
            break

def checkVowels(word):
    if word[-1] in vowels:
        new_word = word
        for v in vowels:
            new_word[-1] = v
            if new_word in bg_en:
                return new_word
    return "?"


if __name__ == '__main__':
    main()


