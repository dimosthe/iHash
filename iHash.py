######## reverseHash #########
# Finds an n letter string of characters that contains only letters
# from acdeghilmnoprstuwz such that the iHash(le_string) is x 

# returns the iHash number of a given n-length string
def iHash(string):
    t = 7
    letters = "acdeghilmnoprstuwz" 
    
    for i in range(len(string)):
        t = t * 41 + letters.index(string[i])

    return t

# returns the n-length string of a given iHash number
def reverseHash(hash_num, string_length):
    t = 7
    letters = "acdeghilmnoprstuwz" 
    cur_string = ""
    
    for j in range(string_length):
        for i in range(len(letters)):
            cur_hash = hash_num/(41**(string_length-(j+1)))
            if iHash(cur_string + letters[i]) == cur_hash:
                cur_string += letters[i]

    return cur_string

if __name__ == '__main__':
    print reverseHash(56721274917700, 8)
