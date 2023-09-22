import openai
import requests

openai.api_key = "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"

import json

# from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# from ibm_watson import SpeechToTextV1
# from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# authenticator = IAMAuthenticator('H8MapKpf8g6RSqV_RK47ddon8mt3NvLG3GcDbluKYlev')
# speech_to_text = SpeechToTextV1(
#     authenticator=authenticator
# )

# speech_to_text.set_service_url('https://api.us-east.speech-to-text.watson.cloud.ibm.com/instances/3911f3fd-e098-4576-8720-20c11b32135f')

# speech_models = speech_to_text.list_models().get_result()

# print(json.dumps(speech_models, indent=2))

# speech_model = speech_to_text.get_model('en-US_BroadbandModel').get_result()
# print(json.dumps(speech_model, indent=2))

# def speech_to_text(audio_binary):
    
#     # Set up Watson Speech to Text HTTP Api url
#     base_url = 'https://api.us-east.speech-to-text.watson.cloud.ibm.com'
#     api_url = base_url+'/speech-to-text/api/v1/recognize'

#     # Set up parameters for our HTTP reqeust
#     params = {
#         'model': 'en-US_Multimedia',
#     }

#     # Set up the body of our HTTP request
#     body = audio_binary

#     # Send a HTTP Post request
#     response = requests.post(api_url, params=params, data=audio_binary).json()
#     print('in worker >>>>>>>  ',response)
#     # Parse the response to get our transcribed text
#     text = 'null'
#     while bool(response.get('results')):
#         print('speech to text response:', response)
#         text = response.get('results').pop().get('alternatives').pop().get('transcript')
#         print('recognised text: ', text)
#         return text


# def text_to_speech(text, voice):

#     print('voice in text_to_speech --------------- >>>> ', voice) 
#     # Adding voice parameter in api_url if the user has selected a preferred voice
#     # if voice != "" and voice != "default":
#     #     api_url += "&voice=" + voice

#     # Set the headers for our HTTP request
#     headers = {
#         'Accept': 'audio/wav',
#         'Content-Type': 'application/json',
#     }

#     # Set the body of our HTTP request
#     json_data = {
#         'text': text,
#     }
#     print('text from cGPT >>>>>>:', text)
    
#     authenticator = IAMAuthenticator('8LaQASnSw8fYtIkpe3UVxG_tzvd3pujg48I6uh3ttINo')
#     text_to_speech = TextToSpeechV1(
#         authenticator=authenticator
#     )

#     text_to_speech.set_service_url('https://api.us-east.text-to-speech.watson.cloud.ibm.com/instances/4e1f09ee-b08f-4833-8541-821cf2ed81d0')
#     voices = text_to_speech.list_voices().get_result()
#     print(json.dumps(voices, indent=2))


#     # pronunciation = text_to_speech.get_pronunciation(
#     #     text='Sridhar Naidu',
#     #     voice='en-US_AllisonV3Voice',
#     #     format='ibm'
#     #     ).get_result()
    
#     # print(json.dumps(pronunciation, indent=2))
#     file_name = 'output_text.wav'
#     response = text_to_speech.synthesize(text,voice=voice,accept='audio/wav').get_result()
#     # print('text to speech response:', response)
    
#     print(response.status_code)

#     with open(file_name, mode='wb') as f:
#         f.write(response.content)

#     # with open('output_text.wav', 'wb') as audio_file:
#     #     audio_file.write(
#     #         text_to_speech.synthesize(
#     #             text,
#     #             voice='en-US_AllisonV3Voice',
#     #             accept='audio/wav'        
#     #         ).get_result().content)

#     # # Set up Watson Text to Speech HTTP Api url
#     # base_url = 'https://api.us-east.text-to-speech.watson.cloud.ibm.com/instances/805e1e90-5cef-451b-8d5b-9131e10adfa1'
#     # api_url = base_url + '/v1/synthesize?output=output_text.wav'

#     # + '?access_token=' + access_token
#     # + '&voice=en-US_AllisonV3Voice';

    
#     # Send a HTTP Post reqeust to Watson Text to Speech Service
#     # response = requests.post(api_url, headers=headers, json=json_data)
#     print('text to speech response:', response)
#     return response.content


def openai_process_message(user_message):
    # Set the prompt for OpenAI Api
    prompt = "\"Act like a personal assistant. You can respond to questions, translate sentences, summarize news, and give recommendations. " + user_message + "\""
    # Call the OpenAI Api to process our prompt
    # openai_response = openai.Completion.create(model="text-davinci-003", prompt=prompt, max_tokens=4000)
    openai_response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=4000)

    print("openai response:", openai_response)
    # Parse the response to get the response text for our prompt
    response_text = openai_response.choices[0].text
    return response_text


    
def did_process_avatar(user_message):
    # Set the prompt for OpenAI Api
    prompt = "\"Act like a personal assistant. You can respond to questions, translate sentences, summarize news, and give recommendations. " + user_message + "\""
    # Call the OpenAI Api to process our prompt
    # openai_response = openai.Completion.create(model="text-davinci-003", prompt=prompt, max_tokens=4000)
    did_response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=4000)

    print("openai response:", openai_response)
    # Parse the response to get the response text for our prompt
    response_text = openai_response.choices[0].text
    return response_text

# def getSpeechFromText(headers,params,data,file_name):
#     request =requests.post(text_to_speech_url,headers=headers,params =params,data=data)
#     print(request.status_code)
#     with open(file_name, mode='bx') as f:
#         f.write(request.content)


# file_name = 'text_to_speech_sample1.wav'
# result = getSpeechFromText(headers, params, data, file_name)
# print_plot_play(file_name)

