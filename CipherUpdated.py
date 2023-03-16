Text_Output = ""
Text_Input = "Initialize"
Current_Word = 0
SentenceList = []
vowels = ["a","e","i","o","u","y"]
LOWALPHABET = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

VigenereKey = "Pitch"
ChangeVKey = input(f'The Vigenere Key is currently "{VigenereKey}"\nIf you would like to change the key then enter it now. Leave this blank to keep the key as is.\n\n')

if ChangeVKey != "":
    VigenereKey = ChangeVKey

while Text_Input != "":
    Text_Input = input("\nWhat would you like translated to Alyrian?\nTo exit the program simply hit enter.\n\n")
    Text_Input = Text_Input.lower()
    SplitSentence = Text_Input.split(" ",-1)
    
    if Text_Input != "":
        for Word in SplitSentence:
            vowelcount = {}
            character = ""
            punct = ''
            VigenereKey = VigenereKey.lower()
            SpecialKeyValue = []
            SpecialKeyLen = len(VigenereKey)
            keycount = 0
            VKeyIndex = 0
            
            for vowel in "aeiou":  # Counts vowels in a dict format
                vowelcounter = Word.count(vowel)
                vowelcount[vowel] = vowelcounter
            
            counts = vowelcount.values()
            vowelcount = sum(counts)  # Turns the dict format into a number
            
            for i in VigenereKey:
                SpecialKeyValue.append(i)
            for character in Word:
                if character == "'":
                    Word = Word.replace("'", "")
                elif character == '.' or character == '?' or character == '!' or character == ',' or character == ';' or character == "'" or character == '"' or character == ':':
                    Word = Word.replace(f"{str(character)}", "")
                    punct = str(character)

            Encrypted = ""
            length = len(Word)
                
            while length > 5:
                length = length - 6  # Ensures that B never errors if there are more than 6 vowels in a word.
            
            for character in Word:            
                VKeyIndex += 1
                if VKeyIndex > SpecialKeyLen:
                    VKeyIndex = 1
                keycount += 1
                if keycount > 3:
                    keycount = 1
                if keycount == 1:
                    key = LOWALPHABET[vowelcount - 1]  # How many vowels in non-translated word. First letter within key.
                elif keycount == 2:
                    key = vowels[length - 1]  # How many letters in non-translated word, shown by vowel. Second letter within key.
                else:
                    key = Word[0]  # First letter of non-translated word. Third letter within key.
                if character.isnumeric():
                    Encrypted = Encrypted + character
                else:
                    letterreplace = LOWALPHABET.index(character) + LOWALPHABET.index(SpecialKeyValue[VKeyIndex - 1])  # Uses the special key inputted above.
                    if letterreplace > 25:
                        letterreplace = letterreplace - 26
                        Encrypted = Encrypted + LOWALPHABET[letterreplace]
                    else:
                        Encrypted = Encrypted + LOWALPHABET[letterreplace]

            A = str(LOWALPHABET[vowelcount - 1]) # Left off here, look for a way to work around this with capitals too.
            B = str(vowels[length - 1])  # 3 Letter Key
            C = str(Word[0])
            
            if length % 2 == 0:  # Decides where the key is tacked on.
                Text_Output = Text_Output + " " + A+B+C+ Encrypted + punct
            else:
                Text_Output = Text_Output + " " + Encrypted + A+B+C + punct
    else:
        pass
        
print(f'{Text_Output.lstrip(" ")}\n')
print("Cipher program successfully exited.\n")