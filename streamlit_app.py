import base64
import json
from flask import Flask, render_template, request
from worker import openai_process_message
from flask_cors import CORS
import os

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

from ibm_watson import SpeechToTextV1, TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


# Using get() method to get the value from dictionary
course={'result_index': 0, 'results': [{'final': True, 'alternatives': [{'transcript': 'hello how are you doing today ', 'confidence': 0.97}]}]}

print('language:', course.get('results'))
# language: python

print('fee:',course.get('fee'))


@app.route('/process-message', methods=['POST'])
def process_message_route():

    user_message = request.json['userMessage'] # Get user's message from their request
    print('user_message', user_message)

    # voice = request.json['voice'] # Get user's preferred voice from their request
    # print('voice in process-message', voice)

    # Call openai_process_message function to process the user's message and get a response back
    openai_response_text = openai_process_message(user_message)

    # Clean the response to remove any emptylines
    openai_response_text = os.linesep.join([s for s in openai_response_text.splitlines() if s])
    # print('<<<<<<<<<<<<<< in process-message >>>>>>>>>>>>>> ',openai_response_text)
    # Call our text_to_speech function to convert OpenAI Api's reponse to speech
    # openai_response_speech = text_to_speech(openai_response_text, voice)
    # print('openai_response_speech >>>>>>>>>  ',openai_response_speech)
    # convert openai_response_speech to base64 string so it can be sent back in the JSON response
    # openai_response_speech = base64.b64encode(openai_response_speech).decode('utf-8')

    # Send a JSON response back to the user containing their message's response both in text and speech formats
    # response = app.response_class(
    response=json.dumps({"openaiResponseText": openai_response_text})
        # status=200,
        # mimetype='application/json'
    # )

    print('from prossess-message >>>>> ',response)
    return response

@app.route('/process-avatar', methods=['POST'])
def process_avatar_route():

    user_message = request.json['userMessage'] # Get user's message from their request
    print('user_message', user_message)

    # voice = request.json['voice'] # Get user's preferred voice from their request
    # print('voice in process-message', voice)

    # Call did_process_avatar function to process the user's message and get a response back
    did_response_text = did_process_avatar(user_message)

    # Clean the response to remove any emptylines
    # openai_response_text = os.linesep.join([s for s in openai_response_text.splitlines() if s])
    # print('<<<<<<<<<<<<<< in process-message >>>>>>>>>>>>>> ',openai_response_text)
    # Call our text_to_speech function to convert OpenAI Api's reponse to speech
    # openai_response_speech = text_to_speech(openai_response_text, voice)
    # print('openai_response_speech >>>>>>>>>  ',openai_response_speech)
    # convert openai_response_speech to base64 string so it can be sent back in the JSON response
    # openai_response_speech = base64.b64encode(openai_response_speech).decode('utf-8')

    # Send a JSON response back to the user containing their message's response both in text and speech formats
    # response = app.response_class(
    response=json.dumps({"openaiResponseText": openai_response_text})
        # status=200,
        # mimetype='application/json'
    # )

    print('from prossess-avatar >>>>> ',response)
    return response



if __name__ == "__main__":
    # app.run(port=8000, host='0.0.0.0')
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)




