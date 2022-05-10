import svgwrite
from synonym_finder import *
import pylexicon.core as lex

sf = synonym_finder(bert_model = 'nli-bert-large')

dwg = svgwrite.Drawing('test.svg', profile='tiny')
dwg.add(dwg.line((0, 0), (10, 0), stroke=svgwrite.rgb(10, 10, 16, '%')))
dwg.add(dwg.text('Test', insert=(0, 0.2), fill='red'))
dwg.save()

class Designer():

    def __init__(self) -> None:

        self.primaryCompStrategy = None
        self.secondaryCompStrategy = None
        self.compStyle = None
        self.compElements = []
        
    def design(wordList):

        pass

        

def main():
    input("Welcome to the Ev(3)ocative Painting Studio! \nAfter a short questionnaire, painterBot will capture your essence in a painting! \nPlease provide as many descriptive words as possible for the best results. \n\nExample: \n\tQ: What words do you use to describe yourself? \n\tA: artistic zany spiritual quiet diplomatic \n\nPress 'enter' to continue: ")
    words1 = input("\nQ1: What words would you use to describe your current state of mind? \n\t--> ")
    analyzeReponse(words1)
        
    # words2 = input("\nQ2: What words would you use to describe how you currently feel about your past? \n\t--> ")

def analyzeReponse(wordsString):

    wordList = wordsString.split()
    print(wordList)

    for word in wordList:
        synonyms = sf.get_synonyms(word)
        print(word + " synonyms: " + synonyms)
    

if __name__ == '__main__':
    main()
