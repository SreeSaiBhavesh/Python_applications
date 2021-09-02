import json
from difflib import get_close_matches
data = json.load(open("data.json"))
word = input("Enter the word you want to search for : ")
def find(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))>0:
        print("Did you mean the word %s instead" %get_close_matches(word,data.keys())[0])
        decide = input("press y for yes / n for no")
        if decide == "y":
            return data[get_close_matches(word,data.keys())[0]]
        elif decide == "n":
            print("Did you mean the word %s instead" %get_close_matches(word,data.keys())[1])
            decide = input("press y for yes / n for no")
            if decide == "y":
                return data[get_close_matches(word,data.keys())[1]]
            elif decide == "n":
                return("Sorry! The word you search for was not found")
            else:
                return("You have entered wrong key, please select either y or n")
        else:
            return("You have entered wrong key, please select either y or n")

        
        

    else:
        print("You have entered wrong key, please select either y or n")


output = find(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
    

