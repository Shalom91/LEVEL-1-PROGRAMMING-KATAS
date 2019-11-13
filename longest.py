# print the longest string in a list

my_list = ['blood', 'air', 'fire'] # define a list

def find_longest_word(word_list):  
    longest_word =  max(word_list, key=len)
    print(longest_word)

find_longest_word(my_list)
    
    