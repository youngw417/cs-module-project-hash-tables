
def word_count(s):
    # Your code here
    # split sentence to list of word
    # make word to lowercase
    # delete the ignored charactor
    # loop the list
    # use the word as key and count as value to record in cache
    # at the end of list, return the cache
    cache = {}
    ignored = '" : ; , . - + = / \ | [ ] { } ( ) * ^ & "'
    ignored_list = ignored.split()
    str_list = s.split()
    for item in range(len(str_list)):
        # filter out ignored cha, put it in list, join the list to word, and make it lowercase
        str = ''.join(list(filter( lambda x: x not in ignored_list, str_list[item]))).lower()
        str_list[item] = str
        # the word was only with ignored char
        if not len(str_list[item]):  # pass to next iteration
            continue
        if str_list[item] not in cache: # not in cache, initialize it
            cache[str_list[item]] = 1
        else:
            cache[str_list[item]] += 1
    
    return cache

if __name__ == "__main__":
    print(word_count('":;,.-+=/\\|[]{}()*^&'))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
 
#  {'hello': 2, 'my': 2, 'cat': 2, 'and': 1, "doesn't": 1, 'say': 1, 'back': 1}
   