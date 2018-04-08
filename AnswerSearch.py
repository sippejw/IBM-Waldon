"""
This will scan the wikipedia articles related to the given keywords and answers
"""
# @param wordSearch word being searched
# @param inputString string that that you're searching through
import wikipedia
def countOccurences(wordSearch, inputString):
    import re
    return sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(wordSearch), inputString))
    # return inputString.count(wordSearch)

#attempts to find a page using the key words
def keyWordWikiPageAttempt(questionList, qIndex, whole):
    try:
        print wikipedia.page(whole + " " + questionList[qIndex]).url
        return wikipedia.page(whole + " " + questionList[qIndex])
    except wikipedia.exceptions.PageError:
        if len(questionList) != qIndex + 1:
            keyWordWikiPageAttempt(questionList, 1+qIndex, whole)
        else:
            return wikipedia.page("Null Character")

# @param question list of keywords from the question
# @param answers list containing a list for every answer
def answerReturn(question, questionPhrases, answers):
    confidence = [0, 0, 0]
    page = wikipedia.page("Null Character")

    wholeAnswer = ""
    for a in range(len(question)):
        wholeAnswer += question[a] + " "

    try:
        page = wikipedia.page(wholeAnswer)
        print page.url
    except wikipedia.exceptions.PageError:
        try:
            for a in range(len(questionPhrases)):
                wholeAnswer += questionPhrases[a] + " "
                page = wikipedia.page(wholeAnswer)
        except wikipedia.exceptions.PageError:
            print "Couldn't find question-based page: Moving on!"
    except UserWarning:
        print "Couldn't find question-based page: Moving on!"
    except wikipedia.exceptions.WikipediaException:
        print "Couldn't find question-based page: Moving on!"

    for a in range(len(answers)):
        for b in range(len(answers[a])):
            confidence[a] += countOccurences(answers[a][b], page.content)

    bigBoiQ = question + questionPhrases
    for a in range(len(answers)):
        wholeAnswer = ""
        for b in range(len(answers[a])):
            wholeAnswer += answers[a][b] + " "
        try:
            page = wikipedia.page(wholeAnswer)
            print page.url
        except wikipedia.exceptions.PageError:
            page = keyWordWikiPageAttempt(bigBoiQ, 0, wholeAnswer)
        except UserWarning:
            page = keyWordWikiPageAttempt(bigBoiQ, 0, wholeAnswer)
        except wikipedia.exceptions.WikipediaException:
            print "Couldn't find question-based page: Moving on!"

        for b in range(len(bigBoiQ)):
            confidence[a] += countOccurences(bigBoiQ[b], page.content)

    confCount = confidence[0] + confidence[1] + confidence[2]
    confidenceP = [0.0, 0.0, 0.0]
    if confCount > 0:
        confidenceP[0] = float(confidence[0])/confCount
        confidenceP[1] = float(confidence[1])/confCount
        confidenceP[2] = float(confidence[2])/confCount


    if confidence[0] > confidence[1] and confidence[0] > confidence[2]:
        return str(confidence) + "\n" + " ".join(answers[0])
    elif confidence[1] > confidence[0] and confidence[1] > confidence[2]:
        return str(confidence) + "\n" + " ".join(answers[1])
    else:
        return str(confidence) + "\n" + " ".join(answers[2])