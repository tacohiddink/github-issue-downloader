# Export github issues using https://pygithub.readthedocs.io/en/latest/
from github import Github


repo_owner = "<owner>"
repo_name = "<reponame>"

# first create a token, see:
# https://docs.github.com/en/enterprise-server@3.4/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token
access_token = "<token>"

if __name__ == '__main__':

    # using an access token
    g = Github(access_token)

    repo = g.get_repo(f"{repo_owner}/{repo_name}")
    open_issues = repo.get_issues()
    for issue in open_issues[:10]:
        iss = {
            'title': issue.title,
            'status': issue.state,
            'labels': [o.name for o in issue.labels],
            'assignees':[o.login for o in issue.assignees],
            'closed_at': issue.closed_at,
            'created_at': issue.created_at,
        }
        print(iss)

