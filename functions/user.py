"""
    TO DO...method having the validation about the input informations.
    If is valid, will validate the saved informations on the database 
"""

from aws_lambda_powertools import Logger
import json
from utils.user import JSONEncoder, email_validation
from database import user_db

logging = Logger()

def create_user(event,context):
    logging.info(event)
    #event_body = json.loads(event.get('body'))
    #logging.info(f'{event_body}')
    invalid_response = {
                "statusCode": 400,
                "body": 'Invalid body'
            }
    recheck_body = {
                "statusCode": 404,
                "body": 'Invalid body values'
            }

    try:
        #event_body = json.loads(event.get('body'))
        event_body = json.loads(event['body'])
    except Exception as ex:
        logging.error(f'Error during event body validation {ex}')
        return invalid_response

    if event_body.get('email', None):
        user_email = event_body.get('email')
        user_password = event_body.get('password')
    else:
        logging.info(f'Body has none email or password user')
        return invalid_response
             
    user_valid_email = email_validation(user_email)
    if user_valid_email:
        mongo_return_user = user_db.MongoDbUser().insert_user(user_email,user_password)
        mongo_user_full = user_db.MongoDbUser().get_user_id(mongo_return_user)
        if mongo_user_full:
            response = {'id': mongo_user_full.get('_id'),
                        'email': mongo_user_full.get('email')
                        }
            logging.info(f'response eh {response}')
            return {"statusCode": 200,"body": json.dumps(response, cls=JSONEncoder)}
    else:
        logging.info('Invalid email')
        return invalid_response