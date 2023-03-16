# Initialization shit
LOWALPHABET = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
vowels = ["a","e","i","o","u","y"]
Punctuation = [',', '.', '?', ';', "'", '"', '<', ">", "?", ":", "[", "]", "{", "}", '|', "-", "+", '`', '~', "!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
punctuationcount = {}
Decoded = ""
vowelcount = {}
CipherType = 'V' #input("What Cipher would you like to use?\n[C] or [V]?\n")
Encoded = input("What would you like translated to Alyrian?\n") # To allow a sentence input I would need to put in a whole new block of code below this line.
Sentence = 'Y'#input("Is your input a sentence?\n [Y] or [N]?\n")
if Sentence == "Y":
    SentenceList = []
    SplitSentence = Encoded.split(" ",-1)
    if CipherType == "V":
        SpecialKey = "Orion"#input("Enter the Special Key, leave blank for no special key.\n")
    for i in SplitSentence:
        Decoded = ""
        vowelcount = {}
        CurrentWord = i
        
        for punctuation in "',./;'][-=<>?:}{|_+!@#$%^&*()`~'":  # Counts vowels in a dict format
            punctuationcounter = CurrentWord.count(punctuation)
            punctuationcount[punctuation] = punctuationcounter
        
        length = len(CurrentWord)  # I think I would need to take the input and then split it into a list that seperates everything by spaces. Then would need to translate each piece and replace it back into the list.
        lower = CurrentWord.lower()

        keycount = 0
        specialcount = 0

        for vowel in "aeiou":  # Counts vowels in a dict format
            vowelcounter = lower.count(vowel)
            vowelcount[vowel] = vowelcounter

        counts = vowelcount.values()
        vowelcount = sum(counts)  # Turns the dict format into a number

        variable1lol = length
        while variable1lol > 5:
            variable1lol = variable1lol - 6  # Ensures that B never errors if there are more than 6 vowels in a word.

        A = str(LOWALPHABET[vowelcount - 1])
        B = str(vowels[variable1lol - 1])  # 3 Letter Key
        C = str(lower[0])

        if CipherType == "V":
            SpecialKey = SpecialKey.lower()
            SpecialKeyValue = []
            SpecialKeyLen = len(SpecialKey)
            for i in SpecialKey:
                SpecialKeyValue.append(i)
            for i in lower:  # Vigenere Cipher
                specialcount += 1
                if specialcount > SpecialKeyLen:
                    specialcount = 1
                keycount += 1
                if keycount > 3:
                    keycount = 1
                if keycount == 1:
                    key = LOWALPHABET[
                        vowelcount - 1]  # How many vowels in non-translated word. First letter within key.
                elif keycount == 2:
                    key = vowels[
                        variable1lol - 1]  # How many letters in non-translated word, shown by vowel. Second letter within key.
                else:
                    key = lower[0]  # First letter of non-translated word. Third letter within key.

                if lower.isnumeric():
                    print("Not a word")
                    break
                if SpecialKey == "":
                    letterreplace = LOWALPHABET.index(i) + LOWALPHABET.index(
                        key)  # Uses 3 letter key that is tacked on to word.
                else:
                    letterreplace = LOWALPHABET.index(i) + LOWALPHABET.index( # This line is where punctuation breaks the program.
                        SpecialKeyValue[specialcount - 1])  # Uses the special key inputted above.
                    if letterreplace > 25:
                        letterreplace = letterreplace - 26
                Decoded = Decoded + str(LOWALPHABET[letterreplace])
            #     SentenceList.append(Decoded)
            # print(*SentenceList, sep=" ")
            # exit()

        elif CipherType == "C":
            for i in lower:  # Caesar Cipher
                if lower.isnumeric():
                    print("Not a word")
                    break
                lettermove = (LOWALPHABET.index(i) + 1) + length + vowelcount - (LOWALPHABET.index(C) + 1)  # The last thing is subtracting the index of the first letter
                lettermove = lettermove - 1
                if lettermove > 26:
                    lettermove = lettermove - 26
                Decoded = Decoded + str(LOWALPHABET[lettermove])
        else:
            print("Invalid Cipher Type.")

        if length % 2 == 0:  # Decides where the key is tacked on.
            Decoded = A + B + C + Decoded
        else:
            Decoded = Decoded + A + B + C

        SentenceList.append(Decoded)
    print(*SentenceList, sep= " ")
    exit()
elif Sentence == "N":
    length = len(Encoded)  # I think I would need to take the input and then split it into a list that seperates everything by spaces. Then would need to translate each piece and replace it back into the list.
    lower = Encoded.lower()
else:
    print("Improper input")
    exit()

keycount = 0
specialcount = 0

for vowel in "aeiou": # Counts vowels in a dict format
    vowelcounter = lower.count(vowel)
    vowelcount[vowel] = vowelcounter

counts = vowelcount.values()
vowelcount = sum(counts) # Turns the dict format into a number

variable1lol = length
while variable1lol > 5:
    variable1lol = variable1lol - 6 #Ensures that B never errors if there are more than 6 vowels in a word.

A = str(LOWALPHABET[vowelcount-1])
B = str(vowels[variable1lol-1]) # 3 Letter Key
C = str(lower[0])

if CipherType == "V":
    SpecialKey = input("Enter the Special Key, leave blank for no special key.\n")
    SpecialKey = SpecialKey.lower()
    SpecialKeyValue = []
    SpecialKeyLen = len(SpecialKey)
    for i in SpecialKey:
        SpecialKeyValue.append(i)
    for i in lower: # Vigenere Cipher
        specialcount += 1
        if specialcount > SpecialKeyLen:
            specialcount = 1
        keycount += 1
        if keycount > 3:
            keycount = 1
        if keycount == 1:
            key = LOWALPHABET[vowelcount-1] # How many vowels in non-translated word. First letter within key.
        elif keycount == 2:
            key = vowels[variable1lol-1] # How many letters in non-translated word, shown by vowel. Second letter within key.
        else:
            key = lower[0] # First letter of non-translated word. Third letter within key.

        if lower.isnumeric():
             print("Not a word")
             break
        if SpecialKey == "":
            letterreplace = LOWALPHABET.index(i) + LOWALPHABET.index(key) # Uses 3 letter key that is tacked on to word.
        else:
            letterreplace = LOWALPHABET.index(i) + LOWALPHABET.index(SpecialKeyValue[specialcount-1]) # Uses the special key inputted above.
        if letterreplace > 25:
            letterreplace = letterreplace -26
        Decoded = Decoded + str(LOWALPHABET[letterreplace])

elif CipherType == "C":
    for i in lower: # Caesar Cipher
        if lower.isnumeric():
            print("Not a word")
            break
        lettermove = (LOWALPHABET.index(i)+1) + length + vowelcount - (LOWALPHABET.index(C)+1) # The last thing is subtracting the index of the first letter
        lettermove = lettermove -1
        if lettermove > 26:
            lettermove = lettermove - 26
        Decoded = Decoded + str(LOWALPHABET[lettermove])
else:
    print("Invalid Cipher Type.")

if length % 2 == 0: # Decides where the key is tacked on.
    Decoded = A + B + C + Decoded
else:
        Decoded = Decoded + A + B + C

# print(vowelcount)
# print(length)
print(Decoded)