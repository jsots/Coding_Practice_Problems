class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            # above checks if it exsists. if it doesnt, make it! if it does, continue down the trie
            cur = cur.children[c]
        # Now make the last character the end of the word
        cur.endOfWord = True
    
    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        # Iterate through every letter, and return true/false if it is actually the end of a word
        return cur.endOfWord
    
    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return True