from edit_distance import calDistance


print("Reading dictionary ...")
#read dictionary from file
with open("dictionary.txt","r") as file:
    words = file.readlines()

#clean and create DICT 
#list representation
DICT = []
for word in words:
    DICT.append(word.rstrip())

print(f"Dictionary size {len(DICT)} words...")

#check if word is present in dictionary
def check_spell(str):

    if str in DICT:
        return True
    return False

#get top n words ordered by edit distance
def get_top_suggestions(str,n):

    suggestions = []
    suggested_words = []

    for word in DICT:        
        dis = calDistance(str,word)
        suggestions.append((dis,word))

    suggestions.sort()

    top_suggestions = suggestions[:n]

    for s in top_suggestions:
        suggested_words.append(s[1])

    return suggested_words

input_string = input("Enter the word:")

#incorrect spelling
if not check_spell(input_string):

    print("Incorrect word !!!!")
    print("Did you mean ?")

    #top 10 words with minimum edit distance
    suggestion_list = get_top_suggestions(input_string,10)
    for word in suggestion_list:
        print(word)

else:

    print("Correct word")





