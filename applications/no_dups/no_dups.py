def no_dups(s):
    # Your code here
    # split word into list
    # create empty list to hold new no dup words
    # loop the list
    # if new word, append it in the list
    # return the list

    word_list = s.split()
    new_list = []

    for item in word_list:
        if item not in new_list:
            new_list.append(item)
    word_str = ' '.join(new_list)
    return word_str



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))