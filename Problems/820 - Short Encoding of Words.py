class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        s = set(words)
        for w in words:
            for i in range(1, len(w)):
                s.discard(w[i:])
                #print(s)
        return sum(len(w) + 1 for w in s)

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        #loop through all possible suffixes of each word and count the number of occurrences of each suffix.
        #If a particular suffix only occurs once, that indicates that the 'suffix' is actually a word to be added into the resultant string.

        words = set(words)  # important - e.g. ["time","time"] -> "time#"
        counter = Counter(word[i:] for word in words for i in range(len(word)))
        return sum(len(word)+1 for word in words if counter[word] == 1)

def minimumLengthEncoding(self, words: List[str]) -> int:
	trie = {}
	for word in words:
		node = trie
		for ch in reversed(word):
			if ch not in node:
				node[ch] = {}
			node = node[ch]

	if not trie: return 0

	def dfs(node=trie, curlvl=1):
		if not node: return curlvl
		return sum([dfs(child, curlvl+1) for child in node.values()])

	return dfs()
