"""
Your module description
"""
import wikipedia
import stringParserRevised

def answer(a1, a2, a3):
    answer1 = wikipedia.page(a1)
    answer2 = wikipedia.page(a2)
    answer3 = wikipedia.page(a3)
    
    print answer1.summary + "\n --------"
    print answer2.summary + "\n --------"
    print answer3.summary + "\n --------"
    
answer("entertainment website's name Thirty-Mile Zone ESPN", "entertainment website's name Thirty-Mile Zone Deadline Hollwood", "entertainment website's name Thirty-Mile Zone TMZ")