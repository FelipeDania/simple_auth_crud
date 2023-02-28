"""
    TO DO...method having the validation about the input informations.
    If is valid, will validate the saved informations on the database 
"""
from aws_lambda_powertools import Logger
import json
from utils import user
from database import user_db

logging = Logger()


def read(event,context):
    logging.info(event)
    invalid_response = {
                "statusCode": 400,
                "body": 'Invalid body'
            }
    recheck_body = {
                "statusCode": 404,
                "body": 'Invalid body values'
            }

    try:
        event_body = json.loads(event["body"])
    except Exception as ex:
        logging.error(f'Error during event body validation {ex}')
        return invalid_response

    if event_body.get('email', None) or event_body.get('password', None):
        user_email = event_body.get('email')
        user_password = event_body.get('password')
    else:
        logging.info(f'Body has none email or password user')
        return invalid_response
             
    user_valid_email = user.email_validation(user_email)
    if user_valid_email:
        mongo_return_user = user_db.MongoDbUser().get_user_email(user_email)
    else:
        logging.info('Invalid email')
        return invalid_response
    if mongo_return_user is not None:
        if mongo_return_user.get('password') == user_password:
            logging.info('User with correct data, will autenticate')
            token_generated = user.token_gen(
                mongo_return_user.get('_id'),
                mongo_return_user.get('email')
                )
        return {"statusCode": 200,
                "body": token_generated
                }
    else:
        logging.info('User not exist in the database')
        return recheck_body
    