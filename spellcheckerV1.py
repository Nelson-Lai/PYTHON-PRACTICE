import string
lowercaseLetters = string.ascii_lowercase
uppercaseLetters = string.ascii_uppercase

class Spellchecker:
    def __init__(self):

        self.wordSet = set(line.lower().strip() for line in open('words'))
        self.vowels = set(['a','e','i','o','u','y'])
        self.dictStarred = {}
        '''
        Pre Initialization of Dictionary step: Replace all vowels with asterisks and remove all repeated lettering and add them to dictionary with pointers to real word to catch vowel mispellings
        Additionally removes all capitalization
        ex. Bookkeeper -> b*k*p*r
            floor -> fl*r
        '''
        for word in self.wordSet:
            wordStarred = self.wordPrimer(word)
            if wordStarred in self.dictStarred:
                self.dictStarred[wordStarred].append(word)
            else:
                self.dictStarred[wordStarred] = [word]
        print(f'Dictionary Succesfully Imported with {len(self.wordSet)} words')

    def wordPrimer(self, word):
        wordMutable = list(word.lower())
        for index, letter in enumerate(wordMutable, start = 0):
            if index != len(wordMutable)-1:
                if wordMutable[index] == wordMutable[index + 1]:
                    wordMutable[index] = ''
                    continue
            if letter in self.vowels:
                wordMutable[index] = '*'
        return ''.join(wordMutable)

    def isCapitalized(self,word):
        return word[0] in uppercaseLetters

    def start(self):
        while True:
            wordTest = str(input('>>'))
            capitalization = self.isCapitalized(wordTest)
            if wordTest in self.wordSet:
                outputString = 'Spelled Correctly'
                print(outputString)
                continue

            primed = self.wordPrimer(wordTest)
            if primed in self.dictStarred:
                print('Did you mean:')
                outputString = self.dictStarred[primed]
                if capitalization == True:
                    for index, word in enumerate(outputString):
                        outputString[index] = word.capitalize()
                for eachWord in outputString:
                    print(eachWord)



            else:
                print('No suggestions found')


check = Spellchecker()
check.start()
