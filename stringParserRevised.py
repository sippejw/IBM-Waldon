import boto3
import json

def parseEntity(file):
    comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')
    text = file
    value = json.dumps(comprehend.detect_entities(Text=text, LanguageCode='en'), sort_keys=True, indent=4)
    results = json.loads(value)
    entityArray = results['Entities']
    answer = []
    for i in range(len(entityArray)):
        dict1 = entityArray[i]
        answer.append(dict1.get('Text'))
    return answer
def parseKeyPhrase(file):
    comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')
    text = file
    value = json.dumps(comprehend.detect_key_phrases(Text=text, LanguageCode='en'), sort_keys=True, indent=4)
    results = json.loads(value)
    entityArray = results['KeyPhrases']
    answer = []
    for i in range(len(entityArray)):
        dict1 = entityArray[i]
        answer.append(dict1.get('Text'))
    return answer