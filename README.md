# jira-tickets-auto-assign

1. you have to edit ./config/jira_username and set your username there, eg: 'firstname.surname@organization.com'

2. you have to grab your jira user token from jira interface and set it it ./config/jira_user_token

    2.1 https://id.atlassian.com/manage-profile/security/api-tokens

4. you have to ask your TL for jira URL and set it within ./config/jira_url

5. you should not set debug_level above '1' while you're not properly debugging the app

    5.1 output.json may log json structured information within itself if debug_level is set above 0

5. for running the script you have to "Run with Powershell" './execute-auto-assign.ps1' command, windows only for the moment

6. while running the app, the interface will guide you through its functionality

    6.1 you have to set a number of tickets to be assigned to yourself, the max number being 5 if there are 5 or more available