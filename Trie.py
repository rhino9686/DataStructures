##
##  Trie.py
##  Learning
##
##  Created by Robert Cecil on 11/13/19.
##  Copyright © 2019 Robert Cecil. All rights reserved.
##


## Struct for my Trie
class TrieNode: 
    
    datum = None
    children = {}
    isWord = False
    



##Class wrapper to wrap in accessible methods
class RCTrie:
    

    ##Root Node
    ##TrieNode root
    
    ## used to track all the nodes to prevent memory leaks
    ## std::vector<TrieNode*> allNodes
    
    
    def __init__(self): 
        self.root = TrieNode()
    
    
    def containsWord(self, word):
        
        ## Keep a pointer to whatever level of the trie you're on
        ref = self.root
        
        ## For each letter, see if it is in the correponding Node level of the Trie.
        for letter in  word:
            
            if not letter in ref.children:
                return False
            
            else: 
                newRef = ref.children[letter]
                ref = newRef
            
        ## If the last character node exists and is flagged as a word, this will be true, else not
        return (ref.isWord)
    
    
    def addWord(self, word): 
        ## Keep a pointer to whatever level of the trie you're on
        ref = self.root
        
        for letter in word:
            
            if not letter in ref.children:  
                
                ## Create a new node, store it in the vector
                entry = TrieNode()
                
                ## add character to the level's children
                ref.children[letter] = entry
                
            
            newRef = ref.children[letter]
            ref = newRef
        
        ref.isWord = True
    