import os
import sys
import json
import logging
logging.getLogger().addHandler(logging.StreamHandler())

from github import Github
import prtime


def validate(repo_name: str, pr_number: int):
    """
        Validate PR ETA table if present.
    """
    pr = repo.get_issue(number=pr_number)
    pr_id = prtime.get_pr_id(repo_name, pr)

    # get labels but without ETA related errors
    labels = pr.get_labels()
    label_names = [x.name for x in labels if not x.name.startswith(
        prtime.eta_table.label_prefix)]
    print("Current labels: [%s]" % label_names)

    # parse eta
    eta = prtime.parse_eta(pr, pr_id)
    print("ETA: [%s]" % str(eta.d))

    exit = 0

    # validate
    if eta is None:
        exit = 1
    else:
        valid, err_labels = eta.validate_hours()
        label_names += err_labels
        if not valid:
            exit = 2

    # set new labels
    print("Current labels: [%s]" % label_names)
    pr.set_labels(*label_names)

    print("Exit code: [%s]" % exit)
    sys.exit(exit)


if __name__ == "__main__":

    ctx = json.loads(os.getenv("INPUT_CONTEXT_GITHUB"))

    token = ctx["token"]
    del ctx["token"]

    e = ctx["event"]
    # print("event:\n%s" % json.dumps(e, indent=2))

    e_name = ctx["event_name"]
    e_action = e.get("action", "")
    e_number = e.get("number", -1)
    repo_name = ctx["repository"]

    g = Github(token)
    repo = g.get_repo(repo_name)

    # review_state = e.get("review", {}).get("state", "")
    # if review_state == "approved":
    #     print("APPROVED")

    if e_name == "pull_request" and e_action == "edited":
        print("PR edited!")
        validate(repo_name, e_number)

    if e_action == "review_requested":
        print("REVIEW requested!")
        validate(repo_name, e_number)
