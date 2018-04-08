"""
Your module description
"""
import stringParserRevised
question = []
answers = []
def questionParser(file, typ):
    question = file.split('?')
    question = question[0]
    if typ == 1:
        return stringParserRevised.parseEntity(question)
    else:
        return stringParserRevised.parseKeyPhrase(question)
def answersParser(file):
    finalAnswers = [[],[],[]]
    answers = file.split('?')
    answers = answers[1].split('\n')
    x = 0
    while "" in answers:
        if answers[x] == "":
            del answers[x]
            x -= 1
        x += 1
    for i in range(0, 3):
        finalAnswers[i] = answers[i].split(' ')
    return finalAnswers