from github import Github
import os
import json


if __name__ == "__main__":

    ctx = json.loads(os.getenv("INPUT_CONTEXT_GITHUB"))

    token = ctx["token"]
    del ctx["token"]
    print(ctx)

    repo = ctx["repository"]
    e = ctx["event"]
    e_name = ctx["event_name"]

    # either pull_request
    if e_name == "issue_comment":
        print("EDITED issue!")

    review_state = e.get("review", {}).get("state", "")
    if review_state == "approved":
        print("APPROVED")

    # g = Github(token)
    # repo = g.get_repo(repo)
    # issue = repo.get_issue(number=pr_number)
    # title = issue.title
    # print(title)
