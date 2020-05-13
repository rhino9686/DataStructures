##
##  TrieTester.py
##  Learning
##
##  Created by Robert Cecil on 5/13/20.
##  Copyright © 2020 Robert Cecil. All rights reserved.
##

from Trie import TrieNode, RCTrie



def main():
    print("Hello")

    myTrie = RCTrie()

    myTrie.addWord("Steve")

    assert(myTrie.containsWord("Steve"))






if __name__ == "__main__":
    main()