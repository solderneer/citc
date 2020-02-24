#!/usr/bin/env python3

# Opening the wordlist file
wordlist = open("word_list.txt", 'r')

valid_wordlist = set()
used_wordlist = set()

# Parsing the wordlist file as a iterable into a hashed set and normalize capitalization
for word in wordlist:
   valid_wordlist.add(word.strip("\n").lower()) 

lastword = ""

while True:
    # Need to add the \n so that the words match the set's iterable parsing
    word = input('Please type a word: ')

    # Normalize capitalization
    word = word.lower()

    if word in valid_wordlist:
        if not word in used_wordlist:
            if lastword == "":
                lastword = word
                continue
            else:
                if word[0] == lastword[-1]:
                    lastword = word
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
