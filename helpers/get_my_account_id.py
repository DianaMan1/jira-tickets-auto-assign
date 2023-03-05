from json import  loads
from requests import get
from helpers.config_values import JIRA_URL, JIRA_USER_TOKEN, JIRA_USERNAME

def get_my_account_id():
    url = f"{JIRA_URL}/rest/api/3/user/search?query={JIRA_USERNAME}"
    response = get(url, auth=(JIRA_USERNAME, JIRA_USER_TOKEN))
    if(response.status_code != 200):
        return None
    decoded_response = loads(response.text)
    accountId = None
    for user in decoded_response:
        if(user['emailAddress'] == JIRA_USERNAME):
            accountId = user['accountId']
    return accountId
