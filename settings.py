"""
    Interface between os(serverless) and the application.
    New environment in the serverless should have a new additions in the settings
"""

import os

STAGE = os.environ.get("STAGE")

MONGO_URI = os.environ.get("MONGO_URI")
MONGO_DBNAME = os.environ.get("MONGO_DBNAME")
