# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

fre_table = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

ignored = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'
ignored_list = [ x for x in ignored if x != ' ']
functuation = [' ', '?', '!', "'", '-', '1', '\n', '_']

"""
    read the input and split each letter in the list
    remove all the white space, ignore letters, funcutations
    create hash table (dict) with a letter for a key and its count as a value
    count total number of letters
    insert frequency into the hash tabel dictionary
    create decode table based on frequency

    read a file again
    decode it (think about reading without creating list)
    in case of not a char, just use as it is
    return the decode text

    

"""

def analyze_text(filename):
    cache = {}
    file = open(filename, 'r') 
  
    while 1: 
    # read by character 
        char = file.read(1)          
        if not char:  
            break
        if char in ignored_list or char in functuation:
            continue
          
        if char not in cache:
            cache[char] = 1
      
        else:
            cache[char] += 1
        
  
    file.close()
    
    cache_list = list(cache.items())
    cache_list.sort(key = lambda x: -x[1])
    cache_list2 = [ x[0] for x in cache_list]


    return cache_list2

# cache = analyze_text('ciphertext.txt')

# print(cache)

def decipher(file):

    """
        call analyze_text saved in 'decode_table'
        define sentence
        read file by char
        get a index for char in decode_table
        get a char for the index in fre_table
        add the char to sentence
        return sentence

    """
    decode_table = analyze_text(file)

    sentence = ""
    f = open(file, 'r')
    while 1:

        char = f.read(1)

        if not char:
            break
        if char in fre_table:
      
            ind = decode_table.index(char)
            decoded = fre_table[ind]
            sentence += decoded
        else:
            sentence += char
    return sentence

def main(file):
    decoded = decipher(file)
    print('\n\n')
    print(decoded)

if __name__ == '__main__':

    main('ciphertext.txt')