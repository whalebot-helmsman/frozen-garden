from live_trie import LiveTrie

trie = LiveTrie()
test_strings=['a', 'aa', 'ab' , 'aaa', 'aaac' , 'dfff', 'baa' , 'abb' ]
test_dict={}

for word in test_strings:
    
    end_state = trie.add_word(word)
    
    if end_state == trie.invalid_state:
        raise Exception('couldnot add %(word)s', {'word' : word})
    
    test_dict[word] = end_state

for word in test_strings:
    
    end_state = trie.find_word(word)
    
    if end_state == trie.invalid_state:
        raise Exception('couldnot find %(word)s', {'word' : word})
        
    if end_state != test_dict[word]:
        raise Exception('wrong end state for %(word)s, \n\t expected : %(expected) \n\t get : %(get)', {'word' : word, 'expected' : test_dict[word], 'get' : end_state})
        
print test_dict