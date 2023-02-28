"""
    Possible common methods can be used in the other controllers.
"""

import re
import jwt
from aws_lambda_powertools import Logger
from datetime import datetime, timedelta, date, time
import json
import decimal
from bson.objectid import ObjectId
import bcrypt

logging = Logger()

def email_validation(s):
   pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
   if re.match(pat,s):
      return True
   return False

#def token_gen(id_user,email_user):
#   #https://pyjwt.readthedocs.io/en/latest/
#   try:
#      user_info = {
#            "exp": datetime.utcnow() + timedelta(days=0, seconds=720),
#            "initial": datetime.utcnow(),
#            "usr": str(id_user),
#            "email":str(email_user)
#      }
#      encoded_jwt = jwt.encode({user_info}, "secret", algorithm="HS256")
#   except Exception as ex:
#      logging.error(f'Error during payload to token gen {ex}')
#   
#   return encoded_jwt

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        elif isinstance(o, (datetime, date, time)):
            return o.isoformat()
        elif isinstance(o, timedelta):
            return (datetime.min + o).time().isoformat()
        elif isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        elif isinstance(o, set):
            return list(o)
        return json.JSONEncoder.default(self, o)

def encrypted_password(pwd):
    '''
         Receive the raw password and change to encrypted password
    '''
 
    ## Adding the salt to password
    #salt = bcrypt.gensalt()
    ## Hashing the password
    #hashed = bcrypt.hashpw(pwd, salt)
    #
    ## printing the salt
    #print("Salt :")
    #print(salt)
    #
    ## printing the hashed
    #print("Hashed")
    #print(hashed)
    #return hashed
    return ''

def decrypted_password(pwd):
    '''
         Receive the encrypted password and decode, to raw value.
    '''
    return ''