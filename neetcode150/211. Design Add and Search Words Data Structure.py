class TrieNode:
    def __init__(self):
        self.child = {}
        self.endOfWord = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        cur = self.root
        
        for w in word:
            if w not in cur.child:
                cur.child[w] = TrieNode()
            cur = cur.child[w]
        cur.endOfWord = True
        
    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root
            for i in range(j, len(word)):
                w = word[i]
                if w == ".":
                    for children in cur.child.values():
                        if dfs(i + 1, children):
                            return True
                    return False
                else:
                    if w not in cur.child:
                        return False
                    cur = cur.child[w]
            return cur.endOfWord
        
        return dfs(0, self.root)
            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)