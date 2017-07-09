# coding=utf-8
import json
from os.path import join, dirname
from watson_developer_cloud import TextToSpeechV1

text_to_speech = TextToSpeechV1(
    username='f1a41b87-d977-4970-bd9a-96693a077c98',
    password='ADLADdfoxMsY',
    x_watson_learning_opt_out=True)  # Optional flag

print(json.dumps(text_to_speech.voices(), indent=2))

with open(join(dirname(__file__), 'output.ogg'),
          'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize('Hello world!', accept='audio/ogg',
                                  voice="en-US_MichaelVoice"))

print(
    json.dumps(text_to_speech.pronunciation(
        'Watson', pronunciation_format='spr'), indent=2))

print(json.dumps(text_to_speech.customizations(), indent=2))