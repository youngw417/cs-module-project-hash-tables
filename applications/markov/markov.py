import random
from linkedList import LinkedList


class Node:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return f"{self.key}, {self.value}"
# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# create empty array
# loop thru all worlds
# if new word, put it in array, if it is not new word, find the word after
# with word after, check if it is new word after. if it is new, add it to linked list and set counter 1
# if it is not new word after, increase counter the counter (value)


# TODO: analyze which words can follow other words
# Your code here
def analyze_word(input):
    word_list = input.split()
    new_list = [] # container to hold list of words
    ll_container = [] # container to hold linked list for words after

    for ind in range(len(word_list)):
        if ind >= len(word_list) -  1:
            continue
        if word_list[ind] not in new_list: # if the word is not in the word list
            new_list.append(word_list[ind]) # add the word
            word_after = word_list[ind +  1]  # get the word after
            new_node = Node(word_after, 1) # add it to the node
            my_ll = LinkedList()
            my_ll.insert_head(new_node)  
            ll_container.append(my_ll)  # add the ll in the ll container
        else:
            find_index = new_list.index(word_list[ind]) # if the word is in the word list
            # get the index for the word in word list

            # get the next word and add it to corresponding ll
            word_after = word_list[ind +  1]
            if ll_container[find_index].traverse_node(word_after):  # if the word in the ll
                ll_container[find_index].traverse_node(word_after).value += 1  # increment the counter
            else:
                new_node = Node(word_after, 1)
                ll_container[find_index].insert_head(new_node)  # if the word is not in the ll
                # add the world to linked list

    # print('new_list', new_list)
    print(len(new_list))
    print(len(ll_container))

    # for item in ll_container:
    #     item.print_ll()  

    return [new_list, ll_container]             


analyze_word(words)



# TODO: construct 5 random sentences
# Your code here

