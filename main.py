import os


if __name__ == "__main__":
    gh_token = os.environ["INPUT_GITHUB_TOKEN"]
    print(gh_token[:10])
