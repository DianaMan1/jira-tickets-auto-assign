from requests import get, post, put
from json import loads, dumps

from helpers.check_for_debug_level import isDebugLevelOne, isDebugLevelTwo
from helpers.conditionally_print import conditionally_print
from helpers.config_values import JIRA_AUTH, JIRA_DATA_INITIATIVE_TYPE_FIELD_ID, JIRA_SOURCE_URL_CUSTOM_FIELD_ID, JIRA_URL, JIRA_USERNAME
from helpers.get_maximum_number_of_tickets_to_be_assigned import get_maximum_number_of_tickets_to_be_assigned
from helpers.get_my_account_id import get_my_account_id
from helpers.get_test_label_value import TEST_LABEL_VALUE
from helpers.jira_headers import JIRA_HEADERS


jql = 'assignee in (EMPTY) AND status="Selected for development" AND issuetype = Sub-Task'
maxResults = 500

get_free_tickets_url = f"{JIRA_URL}/rest/agile/1.0/board/297/issue?maxResults={maxResults}&jql={jql}"

conditionally_print("Executing:" + get_free_tickets_url + "...")

response = get(get_free_tickets_url, auth=JIRA_AUTH)

if response.status_code == 200:
    conditionally_print("JIRA call was successful.")
else:
    conditionally_print("JIRA call failed.")

response_data = loads(response.text)
issues = sorted(response_data['issues'], key= lambda item:item['fields']['created'])

assignable_issues: "dict[str, object]" = {}

for issue in issues:
    fields = issue["fields"]
    if (fields[JIRA_SOURCE_URL_CUSTOM_FIELD_ID] is None):
        continue
    if (fields[JIRA_DATA_INITIATIVE_TYPE_FIELD_ID]['value'] != 'New Source'):
        continue
    if (isDebugLevelTwo()):
        if (TEST_LABEL_VALUE not in fields['labels']):
            continue
    assignable_issues[issue['key']] = issue

if (isDebugLevelOne()):
    output = open("output.json", "w")
    output.write(dumps(assignable_issues))
    output.close()


my_account_id = get_my_account_id()

max_number_of_tickets_to_be_assigned = get_maximum_number_of_tickets_to_be_assigned(len(assignable_issues.keys()))
number_of_assigned_tickets = 0

print('Available tickets are: ', list(assignable_issues.keys()), '.')

for issue_key in assignable_issues:
    assign_ticket_url = f"{JIRA_URL}/rest/api/3/issue/{issue_key}/assignee"
    payload = dumps({"accountId": my_account_id})
    if number_of_assigned_tickets >= int(max_number_of_tickets_to_be_assigned):
        break
    response = put(url=assign_ticket_url, data=payload,
                   headers=JIRA_HEADERS, auth=JIRA_AUTH)

    if response.status_code == 204:
        print(f'We have assigned to you the ticket {issue_key}.')
        number_of_assigned_tickets+=1

    comment_text = f"This issue has been automatically assigned. [{issue_key} :: {JIRA_USERNAME}]"
    comment_payload = dumps({
        "body": {
            "content": [
                {
                    "content": [
                        {
                            "text": comment_text,
                            "type": "text"
                        }
                    ],
                    "type": "paragraph"
                }
            ],
            "type": "doc",
            "version": 1
        }})
    comment_on_ticket_url = f"{JIRA_URL}/rest/api/3/issue/{issue_key}/comment"
    post(comment_on_ticket_url, data=comment_payload, headers=JIRA_HEADERS, auth=JIRA_AUTH)
