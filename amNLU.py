import json
import math
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, KeywordsOptions

authenticator = IAMAuthenticator('aXRmyLBXKBVqn07xQwlNX260YBxA2mlZkZ0YhYF2CUNj')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2020-10-28',
    authenticator=authenticator
)

natural_language_understanding.set_service_url('https://api.jp-tok.natural-language-understanding.watson.cloud.ibm.com/instances/d02ad13e-8d1b-4cf6-9d97-d83d5c11f705')

def analyze(textInput):

    response = natural_language_understanding.analyze(
        text=textInput,
        features=Features(keywords=KeywordsOptions(emotion=True,limit=2))).get_result()

    anger = response['keywords'][0]['emotion']['anger']
    fear = response['keywords'][0]['emotion']['fear']
    sadness = response['keywords'][0]['emotion']['sadness']
    disgust = response['keywords'][0]['emotion']['disgust']
    joy = response['keywords'][0]['emotion']['joy']
    mixedEmotion = disgust * 5 + sadness + anger * 3 + fear * 2 - joy
    warningRate = math.ceil(10 * math.log(mixedEmotion + 1, 11))

    return warningRate

# print(analyze('Joe Biden is a corrupt politician. He wants to send YOUR jobs to China, while his family rakes in millions from the Chinese Communist Party. '))

# print(json.dumps(response, indent=2))

# print(response['keywords'][0]['emotion']['joy'])

# Joe Biden is a corrupt politician. He wants to send YOUR jobs to China, while his family rakes in millions from the Chinese Communist Party. 