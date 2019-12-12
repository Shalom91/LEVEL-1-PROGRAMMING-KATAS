# print the longest string in a list

my_list = ['blood', 'air', 'fire']

def longest_string(word_list):
    longest_len = 0
    longest_words = []
    for s in my_list:
        if len(s) > longest_len:
            longest_len = len(s)
            longest_words = [s]
        elif len(s) == longest_len:
            longest_words.append(s)
        return longest_words

print(longest_string(my_list))

    
