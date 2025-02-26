def get_push_message(push_event):
    return f"Pushed {push_event['payload']['size']} commits to {push_event['repo']['name']}"


def get_pull_request_review_message(pull_request_review_event):
    return f"Reviewed a pull request on {pull_request_review_event['repo']['name']}"


def get_delete_message(delete_event):
    return f"Deleted {delete_event["payload"]["ref_type"]} {delete_event["payload"]["ref"]} from {delete_event["repo"]["name"]}"


def get_issue_comment_message(issue_comment_event):
    return f"{issue_comment_event["payload"]["action"].capitalize()} an issue comment on {issue_comment_event["repo"]["name"]}"


def get_pull_request_review_comment_message(pull_request_comment_event):
    return f"{pull_request_comment_event["payload"]["action"].capitalize()} a pull request comment on {pull_request_comment_event["repo"]["name"]}"


def get_pull_request_message(pull_request_event):
    return f"{pull_request_event["payload"]["action"].capitalize().replace("_", " ")} a pull request on {pull_request_event["repo"]["name"]}"
