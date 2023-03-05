from helpers.conditionally_print import conditionally_print
from requests.auth import HTTPBasicAuth


def __get_jira_url():
    with open('.config/jira_url') as file:
        url = file.read()
        file.close()
        return url
    
JIRA_URL = __get_jira_url()

def __get_jira_username():
    with open('.config/jira_username') as file:
        username = file.read()
        file.close()
        conditionally_print(
            "You are now executing the script as " + username + ".")
        return username
    
JIRA_USERNAME = __get_jira_username()

def __get_jira_user_token():
    with open('.config/jira_user_token', 'r+') as file:
        user_token = file.read()
        file.close()
        conditionally_print("Your user token is:" + user_token)
        return user_token
    
__JIRA_USER_TOKEN = __get_jira_user_token()


def __get_jira_source_url_custom_field_id():
    with open('.config/jira_source_url_custom_field_id') as file:
        source_url_custom_field_id = file.read()
        file.close()
        return source_url_custom_field_id
    
JIRA_SOURCE_URL_CUSTOM_FIELD_ID = __get_jira_source_url_custom_field_id()

    
def __get_jira_data_initiative_type_field_id():
    with open('.config/jira_data_initiative_type_field_id') as file:
        data_initiative_type_field_id = file.read()
        file.close()
        return data_initiative_type_field_id

JIRA_DATA_INITIATIVE_TYPE_FIELD_ID = __get_jira_data_initiative_type_field_id()

JIRA_AUTH = HTTPBasicAuth(JIRA_USERNAME, __JIRA_USER_TOKEN)
