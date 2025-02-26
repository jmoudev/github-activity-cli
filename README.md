Project url: https://roadmap.sh/projects/github-user-activity

# GitHub Activity CLI

This is a simple Command Line Interface (CLI) tool that fetches and displays the recent activity of a GitHub user directly in the terminal. It uses the GitHub API to retrieve user activity data and displays it in a human-readable format.

The purpose of this project is to practice working with APIs, handling JSON data, and building CLI applications without relying on external libraries for HTTP requests or JSON parsing.

## Features

- Accepts a GitHub username as a command-line argument.
- Fetches recent activity data of the specified GitHub user using the [GitHub Events API](https://api.github.com/users/<username>/events).
- Displays the activity in a simple, human-readable format, such as:
  - Pushed commits
  - Opened issues
  - Starred repositories
  - Other user events
- Gracefully handles errors like invalid usernames or API request failures.

## Installation

To use the GitHub Activity CLI, clone the repository to your local machine:

```bash
git clone https://github.com/your-username/github-activity-cli.git
cd github-activity-cli
```

## Usage

To run the GitHub Activity CLI, simply run the main.py python file with the username as arg:

```bash
python main.py myuser
```

The result will be the most recent user activity:
```bash
- Created an issue comment on myuser/myproject
- Created a pull request comment on myuser/myproject
- Reviewed a pull request on myuser/myproject
- Created a pull request comment on myuser/myproject
- Reviewed a pull request on myuser/myproject
```
