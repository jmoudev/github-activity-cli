import argparse
import json
import urllib.request

import messages


EVENT_TYPES = {
    # "CommitCommentEvent",
    # "CreateEvent",
    "DeleteEvent": messages.get_delete_message,
    # "ForkEvent",
    # "GollumEvent",
    "IssueCommentEvent": messages.get_issue_comment_message,
    # "IssuesEvent",
    # "MemberEvent",
    # "PublicEvent",
    "PullRequestEvent": messages.get_pull_request_message,
    "PullRequestReviewEvent": messages.get_pull_request_review_message,
    "PullRequestReviewCommentEvent": messages.get_pull_request_review_comment_message,
    # "PullRequestReviewThreadEvent",
    "PushEvent": messages.get_push_message
    # "ReleaseEvent",
    # "SponsorshipEvent",
    # "WatchEvent"
}


def main(username, limit=5):
    url = f"https://api.github.com/users/{username}/events"
    with urllib.request.urlopen(url) as f:
        events = json.load(f)

    # Events in descending order of created_at
    for i, event in enumerate(events):
        if i >= limit:
            break

        event_type = event["type"]
        try:
            event_message_callable = EVENT_TYPES[event_type]
        except KeyError as e:
            raise ValueError(f"{event_type} not in allowed event types.") from e
        
        print(f"- {event_message_callable(event)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="github-activity", description="Query GitHub activity from the command line")
    parser.add_argument("username", help="GitHub username")
    args = parser.parse_args()
    main(args.username)
