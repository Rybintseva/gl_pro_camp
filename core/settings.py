import os

from utils import utils

ENV = os.environ.get('ENV')
BROWSER = os.environ.get('BROWSER')

BASE_FE_URL = 'https://www.cosmosid.com/'
BASE_API_URL = 'https://app.cosmosid.com/api/'

USER_NAME = 'gl-procamp-2021@globallogic.com'
PASSWORD = 'DXdUVEFNpHA8LXm'
PASSWORD_INVALID = '1DXdUVEFNpHA8LXm'

HEADERS = {"Authorization": f"Basic {utils.get_base64_encoded_string(f'{USER_NAME}:{PASSWORD}')}"}
HEADERS_INVALID = {"Authorization": f"Basic {utils.get_base64_encoded_string(f'{USER_NAME}:{PASSWORD_INVALID}')}"}

# RESPONSE STATUS CODES
OK = 200
UN_AUTH = 401
FORBIDDEN = 403
NOT_FOUND = 404

# ACCOUNT
ROOT_FOLDER_NAME = 'ROOT'
ROOT_FOLDER_LOCATION = 'metagenid/v2/files?_=1622700773180'
ROOT_FOLDER_NUMBER_FILES = 1
SPECIFIC_FOLDER_NAME = 'Example_Datasets'
SPECIFIC_FOLDER_LOCATION = f'{ROOT_FOLDER_LOCATION}&folder_id=84c966d5-8dce-429d-8f92-44d5e28b1581'
SPECIFIC_FOLDER_NUMBER_FILES = 58

RUNS = 'metagenid/v1/files/7f4c7326-0a4e-4b56-a8d0-8ce002191672/runs?_=1622700773181'
ANALYSIS = 'metagenid/v1/runs/437ef8e4-b595-4fd8-a2f5-64221831e925/analysis?filter=total&_=1622700773184'
ARTIFACTS = 'metagenid/v1/runs/437ef8e4-b595-4fd8-a2f5-64221831e925/artifacts?_=1622700773185'
