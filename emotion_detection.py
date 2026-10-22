""" This module helps detecting emotion in the input text.
"""
import json
import requests

def emotion_detector(text_to_analyze):
    """ This function is to run emotion detection using Emotion Predict
        Funciton of the Watson NLP Library
    """
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/" \
        "NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    my_obj = { "raw_document": { "text": text_to_analyze } }
    # get the response object from the input text
    response = requests.post(url, json=my_obj, headers=headers, timeout=30)
    # convert the response text into json dictionary
    json_response = json.loads(response.text)
    # strip the dictionary to get the part needed
    formatted_response = json_response["emotionPredictions"][0]["emotion"]
    # look for the emotion pair with the highest score
    dominant_emotion = max(formatted_response, key=formatted_response.get)
    # formatting output for final result
    final_response = {
        'anger': formatted_response.get('anger'),
        'disgust': formatted_response.get('disgust'),
        'fear': formatted_response.get('fear'),
        'joy': formatted_response.get('joy'),
        'sadness': formatted_response.get('sadness'),
        'dominant_emotion': dominant_emotion
    }

    return final_response
