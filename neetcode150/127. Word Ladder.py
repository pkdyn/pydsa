class Solution:
    #(len(word))^2 * len(wordList), len(word) * len(wordList)
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0
        neiDict = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for w in range(len(word)):
                pattern = word[:w] + "*" + word[w + 1:]
                neiDict[pattern].append(word)
        
        q = deque([beginWord]) #[] cauz we're initializing along with declaring?
        visit = set([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                
                for w in range(len(word)):
                    pattern = word[:w] + "*" + word[w + 1:]
                    for neiWord in neiDict[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)                
            
            res += 1
        return 0 #no such seq exists
        