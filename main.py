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


def main(username):
    url = f"https://api.github.com/users/{username}/events"
    with urllib.request.urlopen(url) as f:
        events = json.load(f)

    event_messages = []
    for event in events:
        event_type = event["type"]

        try:
            event_message_callable = EVENT_TYPES[event_type]
        except KeyError as e:
            raise ValueError(f"{event_type} not in allowed event types.") from e
        
        event_messages.append(event_message_callable(event))
    
    print(event_messages)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="github-activity", description="Query GitHub activity from the command line")
    parser.add_argument("username", help="GitHub username")
    args = parser.parse_args()
    main(args.username)
