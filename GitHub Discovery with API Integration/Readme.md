# **Project Name: GitHub Discovery with API Integration**

**Project Description:**

The GitHub Discovery with API Integration project is a Python program that utilizes the GitHub API to retrieve and display information about a specified user. The program fetches details about the user's repositories and pull requests authored by the user. It leverages the `requests` library for API interaction.

**Key Features:**

**1. User Repositories:**
   - Fetches and displays a list of repositories owned by the specified GitHub user.

**2. Pull Requests by User:**
   - Retrieves and presents information about pull requests authored by the user.
   - Displays the repository name and pull request title for each pull request.

**How It Works:**

1. The program prompts the user to input a GitHub username.

2. Constructs two URLs for GitHub API requests:
   - `url_1` for fetching user repositories.
   - `url_2` for searching pull requests authored by the user.

3. Sends HTTP GET requests to the GitHub API using the constructed URLs.

4. Processes the API responses:
   - If successful (HTTP status code 200), extracts and displays repository names for user-owned repositories.
   - If unsuccessful, provides an error message indicating the failure and the corresponding HTTP status code.

5. Similarly, for pull requests:
   - If successful, extracts and displays repository names and pull request titles for pull requests authored by the user.
   - If unsuccessful, provides an error message.

**Usage:**

- Run the program.
- Input the GitHub username when prompted.
- View the console output for a list of user repositories and pull requests.

**Project Benefits:**

- **GitHub User Overview:** Provides a quick overview of a user's GitHub activity.
- **Repository Information:** Retrieves and displays repositories owned by the user.
- **Pull Request Details:** Presents information about pull requests created by the user.
- **API Interaction:** Demonstrates practical use of the GitHub API and the `requests` library.
