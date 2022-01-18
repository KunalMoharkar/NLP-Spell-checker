#creates a dictionary file from the text corpus

import os

def clean_data(line):
    
    #convert to lower case
    line = line.lower()
    #remove UFT-8 tab
    line = line.replace("\ufeff"," ")
    #remove punctuations
    punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~“”–'''
    for char in line:
        if char in punc:
            line = line.replace(char," ")
            line = line.rstrip()
            line = line.lstrip()
            
    return line

#remove empty tokens, '\n' , numeric values.
#retain words on len 3 to 12 only
def filter_words(line):

    line = list(filter(lambda x: x != '', line))
    line = list(filter(lambda x: x != '\n', line))
    line = list(filter(lambda x: len(x) >= 3 , line))
    line = list(filter(lambda x: len(x) <= 12 , line))
    line = list(filter(lambda x: x.isnumeric() != True , line))
    
    return line

def create_word_tokens(lines):
    
    tokens_list = []
    
    #create word tokens
    for line in lines:
        line = line.split(" ")
        line = filter_words(line)
        tokens_list.append(line)
     
    word_tokens = []
    
    for tokens in tokens_list:
        
        word_tokens = word_tokens + tokens
    
    return word_tokens
    
print("\n... creating inverted positional index ....\n")

NUM_DOCS = 10
PATH = "./DOCS/"
docs_list = os.listdir(PATH)[:NUM_DOCS]
docs_list.sort()
doc_index = 0


all_tokens = []

for doc in docs_list:
    
    #stores lines and tokens in a doc
    lines = []
    token_list = []
    print(f"processed documents {doc_index+1}/{len(docs_list)}")
    #read the doc file
    f = open(PATH+doc,encoding="utf-8",mode= "r")
    
    #data cleaing
    for x in f:
        x = clean_data(x)
        lines.append(x)
    
    tokens = create_word_tokens(lines)
    
    all_tokens += tokens
    
    doc_index += 1

unique_tokens = list(set(all_tokens))


# Writing to file
with open("dictionary.txt", "w") as file:
    # Writing data to a file
    for word in unique_tokens:
        file.write(word+"\n")

        
print(f"\nCreated dictionary of size - {len(unique_tokens)} words")

