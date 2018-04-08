"""
Your module description
"""
import imageAnalyze
import stringParser
import AnswerSearch
import warnings
import screenshot
def runner():
    warnings.filterwarnings("error")
    screenshot.runner()
    fileName = "Questions/image.png"
    fileString = imageAnalyze.image(fileName)
    question = stringParser.questionParser(fileString, 1)
    questionp = stringParser.questionParser(fileString, 0)
    answers = stringParser.answersParser(fileString)
    print answers
    return str(AnswerSearch.answerReturn(question, questionp, answers)) + "\n-------"