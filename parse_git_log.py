#!/usr/bin/env python

from datetime import datetime
import os
from subprocess import check_output


PROJECT_NAME = os.path.basename(
    os.path.dirname(os.path.abspath(__file__))).lower()
GIT_COMMAND = ["git", "log", "--pretty=format:{format}", "-n", "100"]
FORMATS = {
    "committer": "%cn <%ce>",
    "timestamp": "%ct",
    "hash": "%h",
    "message": "%s"
}
CHANGE_ENTRY = """{project} ({version}) UNRELEASED; urgency=low

  * {subject}

 -- {author}  {date}
"""


def build_commit(commit):
    date = datetime.fromtimestamp(int(commit["timestamp"]))
    version = date.strftime("%Y.%m%d.%H%M%S") + "-" + commit["hash"]

    commit_date = date.strftime("%a, %d %b %Y %H:%M:%S ") + "+0000"
    message = CHANGE_ENTRY.format(
        project=PROJECT_NAME, version=version, subject=commit["message"],
        author=commit["committer"], date=commit_date)
    return message


def main():
    commits = {}
    for attribute, format_string in FORMATS.items():
        command = [c.format(format=format_string) for c in GIT_COMMAND]
        commit_lines = [l.strip() for l in check_output(command).splitlines()]
        for i in range(len(commit_lines)):
            commits.setdefault(i, {})
            commits[i][attribute] = commit_lines[i]
    indexes = commits.keys()
    indexes.sort()
    commits = [build_commit(commits[i]) for i in indexes]
    print "\n".join(commits)


if __name__ == "__main__":
    main()
