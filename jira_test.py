from jira.client import JIRA

jira_options={'server': 'https://xamplify.atlassian.net/', 'headers': {'content-type': 'application/json', 'Authorization': 'Basic ZHRlamFzaHdpbmlAc3RyYXRhcHBzLmNvbTpPVXlrQ21KODZIMFpEeXIwU2RjYUEzMkI='}}
jira=JIRA(options=jira_options)

# print("**************" , jira.my_permissions(projectKey='XBI'))
#Creating an issue:

new_issue = jira.create_issue(project={'key': 'XBI'}, summary= 'New issue from jira-python', description=  'Look into this one' , issuetype={'name': 'Bug'})


# or creating issues using dict:

# issue_dict = {
#     'project': {'key': 'XBI'},
#     'summary': 'New issue from jira-python',
#     'description': 'Look into this one',
#     'issuetype': {'name': 'Bug'},
# }
# new_issue = jira.create_issue(fields=issue_dict)
print(new_issue)