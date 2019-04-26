class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        top = set(['q','w','e','r','t','y','u','i','o','p','Q','W','E','R','T','Y','U','I','O','P'])
        mid = set(['a','s','d','f','g','h','j','k','l','A','S','D','F','G','H','J','K','L'])
        bot = set(['z','x','c','v','b','n','m','Z','X','C','V','B','N','M'])
        wordList = []
        for word in words:
            include = True
            if word[0] in top:
                checkSet = top
            elif word[0] in mid:
                checkSet = mid
            elif word[0] in bot:
                checkSet = bot
            for letter in word[1:]:
                if letter not in checkSet:
                    include = False
                    break
            if include:
                wordList.append(word)
        return wordList
