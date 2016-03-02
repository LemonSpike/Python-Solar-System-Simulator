class Sentence:

	def __init__(self, istring):
    	self.string = istring
    	self.wordDict = {
				"hello" : "avast",
				"excuse" : "arrr",
				"sir" : "matey",
				"boy" : "matey",
				"man" : "matey",
				"madam" : "proud beauty",
				"officer" : "foul blaggart",
				"the" : "th'",
				"my" : "me",
				"your" : "yer",
				"is" : "be",
				"are" : "be",
				"restroom" : "head",
				"restaurant" : "galley",
				"hotel" : "fleabag inn",
				}
        
    def getSentence(self):
        return self.string
        
    def getWords(self):
    	words = getSentence(self).split()
    	return words
    	
    def getLength(self):
    	length = len(self.string)
    	return length

	def getNumWords(self):
		numwords =  len(getWords(self))
		return numwords
		
	def capitalise(self):
		self.string.title()
		
	def addPunctuationMark(self,mark):
		self.string = self.string + mark
		
	def toPirate(self):
    	for key in self.wordDict:
       	 translated = self.string.replace(key, wordDict[key])
    return translated