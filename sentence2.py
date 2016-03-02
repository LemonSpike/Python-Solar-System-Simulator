class Sentence:

	def __init__(self, istring):
    	self.words = istring.split()
    	
    getSentence(self):
    	sentence = ""
			for word in self.words:
   				sentence += " " + word
		sentence += "."
    	return sentence
    	
    getWords(self):
    	return self.words
    	
    getLength(self):
    	return len(getSentence(self))
    	
    getNumWords(self):
    	return len(self.words)