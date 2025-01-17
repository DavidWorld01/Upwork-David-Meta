from flask import request

from outside_apis.openai_api import generate_image, text_complition


def process_request(request: request) -> dict:
    '''
    Process the incoming data of the Telegram request

    Parameters:
        - request(falsk.request)

    Returns:
        - dict of these key and value 
        {
            'is_text': is_text,
            'is_chat_deleted': is_chat_deleted,
            'sender_id': sender_id,
            'message': message,
            'secret_token': secret_token,
            'first_name': first_name
        }
    '''
    body = request.get_json()
    print(body)
    headers = request.headers
    secret_token = headers['X-Telegram-Bot-Api-Secret-Token']

    message = ''
    is_bot = True
    is_text = False
    first_name = ''
    sender_id = None

    if 'message' in body.keys():
        sender_id = body['message']['from']['id']
        first_name = body['message']['from']['first_name']
        is_bot = body['message']['from']['is_bot']

        if 'text' in body['message'].keys():
            message += body['message']['text']
            is_text = True

    return {
        'is_text': is_text,
        'sender_id': sender_id,
        'message': message,
        'secret_token': secret_token,
        'first_name': first_name,
        'is_bot': is_bot
    }


def generate_response(message: str) -> str:
    '''
    Process the incoming message for different command and generate a response string

    Parameters:
        - message(str): incoming message from Telegram

    Returns:
        - str: formated response for the command
    '''
    if message == '/help':
        return {
            'message': 'Please use  /draw , /gen , /pixel , /emoji ,/anime ,/3d, /ask :-)',
            'isPhoto': False
        }
    elif message == '/start':
        return {
            'message': 'Hi, this is a chat-bot , developed by me with love. I will not spam you for sure.',
            'isPhoto': False
        }
    elif len(message) < 2:
        return {
            'message': 'Hey, it seems very few words, please write as much detail as you can, it will be always better with more words.',
            'isPhoto': False
        }
    else:
        words = message.split()
        print(words)
        if words[0] == '/ask':
            message = ' '.join(words[1:])
            result = text_complition(message)
            if result['status'] == 1:
                return {
                    'message': result['response'].strip(),
                    'isPhoto': False
                }
            else:
                return {
                    'message': 'Sorry, I did not unserstand you.',
                    'isPhoto': False
                }
        elif words[0] == '/draw':
            draw ='draw'
            message = ' '.join([draw] + words[1:])
            result = generate_image(message)
            if result['status'] == 1:
                return {
                    'message': result['url'],
                    'isPhoto': True
                }
            else:
                return {
                    'message': 'Sorry, I did not unserstand you.',
                    'isPhoto': False
                }
        elif words[0] == '/pixel':
            draw ='pixel art'
            message = ' '.join([draw] + words[1:])
            result = generate_image(message)
            if result['status'] == 1:
                return {
                    'message': result['url'],
                    'isPhoto': True
                }
            else:
                return {
                    'message': 'Sorry, I did not unserstand you.',
                    'isPhoto': False
                }
        elif words[0] == '/emoji':
            draw ='emoji'
            message = ' '.join([draw] + words[1:])
            result = generate_image(message)
            if result['status'] == 1:
                return {
                    'message': result['url'],
                    'isPhoto': True
                }
            else:
                return {
                    'message': 'Sorry, I did not unserstand you.',
                    'isPhoto': False
                }
        elif words[0] == '/anime':
            draw ='anime'
            message = ' '.join([draw] + words[1:])
            result = generate_image(message)
            if result['status'] == 1:
                return {
                    'message': result['url'],
                    'isPhoto': True
                }
            else:
                return {
                    'message': 'Sorry, I did not unserstand you.',
                    'isPhoto': False
                }
        elif words[0] == '/3d':
            draw ='3d render'
            message = ' '.join([draw] + words[1:])
            result = generate_image(message)
            if result['status'] == 1:
                return {
                    'message': result['url'],
                    'isPhoto': True
                }
            else:
                return {
                    'message': 'Sorry, I did not unserstand you.',
                    'isPhoto': False
                }
        elif words[0] == '/gen':
            message = ' '.join(words[1:])
            result = generate_image(message)
            if result['status'] == 1:
                return {
                    'message': result['url'],
                    'isPhoto': True
                }
            else:
                return {
                    'message': 'Sorry, I did not unserstand you.',
                    'isPhoto': False
                }
        else:
            return {
                'message': 'Please use /draw , /gen , /pixel , /emoji ,/anime ,/3d, /ask.',
                'isPhoto': False
            }
