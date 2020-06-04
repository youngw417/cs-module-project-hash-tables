# Your code here
# read file robin.txt
with open('robin.txt', 'r') as file:
    words = file.read()

def display(list_of_words, length):
    """
        Loop thru the list
        create a string to show key and count in the number # into the list

        loop thru the new list to display
    """
    word_display = []
    for item in list_of_words:
        cont =''
        for each in range(item[1]):
            cont += '#'
        word_display.append([item[0], cont])
    print('\n\n\n')
    for each in word_display:
        each_len = length + 2
        revised_each = each[0].ljust(each_len)
        print(f'{revised_each}{each[1]}')


def create_histo(input):
    # split the file strings and store into the list
    # remove ignored chars and make all to lowercase
    # loop thru and store the word in dictonary as a key for word and a value for count
    # find the length of longest word (for 2 extra space justification)
    # convert the dic to list
    # sort the list
    # print the list
    ignored = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'
    word_list = input.split()
    cache = {}
    max_length = 0
    for item in word_list:
        str = ''.join(list(filter(lambda e: e not in ignored, item))).lower()
        # print(str)
        if str not in cache:
            cache[str] = 1
            if len(str) > max_length:
                max_length = len(str)
        else:
            cache[str] += 1
            if len(str) > max_length:
                max_length = len(str)
    cached_list = list(cache.items())
    cached_list.sort(key = lambda e: (-e[1], e[0]))    
    # print(cached_list)
    # print(max_length)
    return [cached_list, max_length]

def main():
    [cached_list, max_length] = create_histo(words)
    display(cached_list, max_length)


if __name__ == '__main__':

    main()