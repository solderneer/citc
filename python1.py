#!/usr/bin/env python3

# Opening the wordlist file
wordlist = open("word_list.txt", 'r')

# Parsing the wordlist file as a iterable into a hashed set
valid_wordlist = set(wordlist)
used_wordlist = set()

lastword = ""

while True:
    # Need to add the \n so that the words match the set's iterable parsing
    word = input('Please type a word: ') + "\n"

    if word in valid_wordlist:
        if not word in used_wordlist:
            if lastword == "":
                continue
            else:
                if word[0] == lastword [-1]:
                    continue
                else:
                    print("You didn't type a word starting with a '" + lastword[-1] + "'")
                    break
        else: 
            print("You typed a word that has been typed with")
            break
    else:
        print("You didn't type a word found in word_list.txt")
        break
