"""
This sample demonstrates a simple skill built with the Amazon Alexa Skills Kit.
The Intent Schema, Custom Slots, and Sample Utterances for this skill, as well
as testing instructions are located at http://amzn.to/1LzFrj6

For additional samples, visit the Alexa Skills Kit Getting Started guide at
http://amzn.to/1LGWsLG
"""

from __future__ import print_function
import urllib, urllib2, json;

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])


def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "GetRoomTemperature":
        return getroomTemperature(intent, session)
    elif intent_name == "StartLight":
        return startLight(intent, session)
    elif intent_name == "StopLight":
        return stopLight(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    else:
        raise ValueError("Invalid intent")

def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here

# --------------- Functions that control the skill's behavior ------------------


def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome to Alexa. Sometimes I don't make sense but I'm the closest thing to Jarvis."
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "I can tell the current temperature."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def getroomTemperature(intent, session):
    card_title = '';
    
    session_attributes = {}
    reprompt_text = None

    rooms = {
        'garage' : 'https://api.particle.io/v1/devices/laser_aardvark/temperature?access_token=3b0183aac1a6233abc2cee57eb57d4299f6cf7d2', # blue
        'living room' : 'https://api.particle.io/v1/devices/badger_vampire/temperature?access_token=3b0183aac1a6233abc2cee57eb57d4299f6cf7d2' # green
    };
    
    if 'value' in intent['slots']['Room']:
        room = intent['slots']['Room']['value'];
        response = urllib2.urlopen(rooms[room]);
        value = json.loads(response.read());
        data = 'result'
        
        if value[data.decode('unicode-escape')]:
            value = value[data.decode('unicode-escape')]
            speech_output = "Temperature in " + room + " is " + str(value);
            should_end_session = False;
    else:
        speech_output = "What room do you want to check with";
        should_end_session = False;
    
    return build_response(session_attributes, build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))

def startLight(intent, session):
    card_title = '';
    session_attributes = {}
    reprompt_text = None
    rooms = {'garage' : 'https://api.particle.io/v1/devices/laser_aardvark/powerleds?access_token=3b0183aac1a6233abc2cee57eb57d4299f6cf7d2', 'living room' : 'https://api.particle.io/v1/devices/badger_vampire/powerleds?access_token=3b0183aac1a6233abc2cee57eb57d4299f6cf7d2'};

    if 'value' in intent['slots']['Room']:
        room = intent['slots']['Room']['value'];        # Get the room
        datasend = urllib.urlencode({'args':'on'})      # Append ON argument to be sent with the POST request
        req = urllib2.Request(rooms[room], datasend);   # Build the POST request with the ON argument
        response = urllib2.urlopen(req);                # Send the POST request with the ON argument
        value = json.loads(response.read());            # Parse the JSON response and get the whole thing
        data = 'connected'                              # We will use this to extract the data in the 'connected' field from the JSON response

        if value[data.decode('unicode-escape')]:        # If the value 'connected' is true (which it will be)
            value = value[data.decode('unicode-escape')]# Just store it
            speech_output = room + "Lights are now on"; # Force Alexa to say this
            should_end_session = False;

    else:                                               # Alexa says this crap when it can't match a probability to an intent
        speech_output = "What do you want to do with the lights";
        should_end_session = False;

    return build_response(session_attributes,build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))

def stopLight(intent, session):
    card_title = '';
    
    session_attributes = {}
    reprompt_text = None

    rooms = {'garage' : 'https://api.particle.io/v1/devices/laser_aardvark/powerleds?access_token=3b0183aac1a6233abc2cee57eb57d4299f6cf7d2','living room' : 'https://api.particle.io/v1/devices/badger_vampire/powerleds?access_token=3b0183aac1a6233abc2cee57eb57d4299f6cf7d2'};

    if 'value' in intent['slots']['Room']:
        room = intent['slots']['Room']['value'];
        datasend = urllib.urlencode({'args':'off'})
        req = urllib2.Request(rooms[room], datasend);
        response = urllib2.urlopen(req);
        value = json.loads(response.read());
        data = 'connected'

        if value[data.decode('unicode-escape')]:
            value = value[data.decode('unicode-escape')]
            speech_output = room + "Lights are now off";
            should_end_session = False;

    else:
        speech_output = "What do you want to do with the lights";
        should_end_session = False;

    return build_response(session_attributes,build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))	

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': 'SessionSpeechlet - ' + title,
            'content': 'SessionSpeechlet - ' + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }