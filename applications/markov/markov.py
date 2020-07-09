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
            if ll_container[find_index].traverse_node(word_after):  # if the word is in the ll
                ll_container[find_index].traverse_node(word_after).value += 1  # increment the counter
            else:
                new_node = Node(word_after, 1)
                ll_container[find_index].insert_head(new_node)  # if the word is not in the ll
                # add the world to linked list

    # print('new_list', new_list)

    # for item in ll_container:
    #     item.print_ll()  

    return [new_list, ll_container]             
# analyze_word(words)

[new_list, ll_container] = analyze_word(words)

# choose random words to start
# get a collection of start words

def start_words(input):
    # loop thru and find all word starting Uppercase and " + uppercase
    upper_container = [ x for x in input if x[0].isupper() or (x[0]== '"' and x[1].isupper())]
    # print('upper_container', upper_container)

    return upper_container

def get_random_start(input):

    starting_words = start_words(input)  # return a new list of start words
    ran_index = random.randint(0, len(starting_words) - 1)
    return starting_words[ran_index]

# start_words(new_list)


# TODO: construct 5 random sentences
# Your code here

def get_word_after(after_ll):
    prob_list = []
    current = after_ll.head
    while current:
        for x in range(current.value):
            prob_list.append(current.key) # push to list for the number fo value
        
        current = current.next
    random_num = random.randint(0, len(prob_list) -1)

    return prob_list[random_num]
    


# ll_list = LinkedList()
# ll_list.insert_head(Node("a", 1))
# ll_list.insert_head(Node("b", 1))
# ll_list.insert_head(Node("c", 1))
# ll_list.insert_head(Node("d", 1))
# print(get_word_after(ll_list))

def create_sentences(word_list, word_after_list):
    analyze_word(words)
    sentence_list = ['\n\n']

    # get a random start word
    # do while not getting 'stop word' or till 5 random sentences
    # get the random word after for those word
    # get the random word after...
    start_word = get_random_start(word_list)
    sentence_list.append(start_word)  #start word
    counter = 0   #sentence counter
    current = start_word
    while counter < 5:
        word_next_ind = word_list.index(current)
        after_ll = word_after_list[word_next_ind]
        word_after =  get_word_after(after_ll)
        sentence_list.append(word_after)
        current = word_after
        # Stop words are words that end in any of the punctuation `.?!`, or that
        # punctuation followed by a `"`.
        # print('current', current)
        if (current[-1] == '.' or current[-1] == '?' or current[-1] == '!') or (current[-2:] == '."' or current[-2:] == '?"' or current[-2:] == ".!"):
            sentence_list.append('\n\n')
            counter += 1
            if counter is not 5:
                start_word = get_random_start(word_list)
                sentence_list.append(start_word)  #start word
   
    final_sentence = ' '.join(sentence_list)

    return final_sentence

print(create_sentences(new_list, ll_container))