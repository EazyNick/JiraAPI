from jira import JIRA, JIRAError, Issue
from pprint import pprint

# 기본 설정
mcols_id, mcols_pwd = "id", "password@"
jira_site = {'server': 'https://jira~~'}

# 로그인
Mcols = JIRA(jira_site, auth=(mcols_id, mcols_pwd))

issue_dict = {
            'project': {'key': ''}, # 프로젝트

            'summary': '', # 제목

            'issuetype': {"name": ""}, 
            "priority": {"name": ""}, 
            "customfield_10125": {"value": ""}, 
            "customfield_10137": {"value": ""}, 
            "customfield_16300": {"value" : ""}, 
            "customfield_10210": {"value": "","child": {"value": ""}}, 
            'components': [{"name": ""}], 
            "customfield_13100": [{"value": ""}], 

            "versions": [{"name": ""}],

            "assignee": {"name": ""},
            "customfield_10809": [""], 

            "environment": """""",

            "customfield_10900": {"value": ""}, 

            "description": "",
            "labels": ["",""],
            "customfield_11500": [{"value": ""}], 
            }

#안되는 것


Mcols_Issue = Mcols.create_issue(fields=issue_dict)


