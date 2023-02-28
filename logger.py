import logging
from aws_lambda_powertools import Logger

logging.getLogger("requests").setLevel(logging.ERROR)

logger = Logger("simple_auth_crud")
