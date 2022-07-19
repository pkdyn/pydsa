class TrieNode:
    def __init__(self):
        self.child = {}
        self.endOfWord = False
        
class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        cur = self.root
        
        for w in word:
            if w not in cur.child:
                cur.child[w] = TrieNode()
            cur = cur.child[w]
        cur.endOfWord = True
        
    def search(self, word: str) -> bool:
        cur = self.root
        for w in word:
            if w not in cur.child:
                return False
            cur = cur.child[w]
        if cur.endOfWord:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        
        for w in prefix:
            if w not in cur.child:
                return False
            cur = cur.child[w]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)