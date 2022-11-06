from github import Github
import os
import json


if __name__ == "__main__":

    ctx = json.loads(os.getenv("INPUT_CONTEXT_GITHUB"))

    token = ctx["token"]
    del ctx["token"]
    print(ctx)

    repo = ctx["repository"]
    pr_number = ctx["event"]["number"]

    g = Github(token)
    repo = g.get_repo(repo)
    issue = repo.get_issue(number=pr_number)
    title = issue.title
    print(title)
