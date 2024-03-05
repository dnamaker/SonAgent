
#to do: move this one to langchain 


def summary_doc(text: str) -> str:
    SUMMARY_DOC = f"""
    You are an expert software engineer with expertise in summarizing and pulling out important sections of a text. 
    The following text is from discussions and is about Software Development. 
    Follow these steps: read the text, summarize the text, and identify key issues can be planned for implementation. 
    In your response include the summary and bullet points for the main ideas, steps, and key vocabulary.
    ### Text
    {text}
    """
    return SUMMARY_DOC


def create_git_pull_request_param(sumary_text):

    GITHUB_PULL_REQUEST = f"""
    You are a software engineer working on a python project.
    You have been asked to create a pull request for the following changes.
    The changes are to the codebase of a project. 
    Based on the content provided below. Let's create a json file, ouput is json.

    For example:

    Example 1:
    ### SUMMARY
    SonAgent (to assistant):
    create a python class that have function to plot apple stock price in from 1 year ago to now user yahoo finance data 
    that class need extend from 
    ```python
    from pydantic import BaseModel
    ```
    --------------------------------------------------------------------------------
    assistant (to SonAgent):

    To accomplish this task, we will create a Python class that extends from `BaseModel` provided by `pydantic`. This class will have a function to plot the Apple stock price from 1 year ago to the current date using Yahoo Finance data. We will use the `yfinance` library to fetch the stock data and `matplotlib` for plotting. If you don't have `yfinance` and `matplotlib` installed, you will need to install them using pip.

    Here's the plan:
    1. Import necessary libraries.
    2. Extend the class from `BaseModel`.
    3. Implement a function within the class to fetch and plot the Apple stock price data.

    First, ensure you have `pydantic`, `yfinance`, and `matplotlib` installed. You can install them using pip. Execute the following command in your shell:

    ### OUTPUT
    {
        "branch_name": "feature/sonagent-plot-apple-stock",
        "commit_message": "add new feature to plot apple stock price",
        "pull_request_title": "Add new skill to agent to plot Apple stock price",
        "pull_request_body": "This pull request adds a new skill to the agent to plot the Apple stock price using Yahoo Finance data.",
        "source_code_file_name": "skill_plot_apple_stock.py",
    }

    Example 2:
    ### SUMMARY
    Certainly! The following is a summary of the Python function for performing a Google search using the googlesearch-python library:
    Install the googlesearch-python library using pip install googlesearch-python.
    Create a function called google_search that takes a search query and an optional parameter for the number of results to fetch.
    Inside the function, use the search function from the library to perform the Google search with the given query and retrieve the specified number of results.
    Iterate through the search results and print the title and URL of each result.
    Handle exceptions gracefully in case of errors during the search process.
    Remember to use this functionality responsibly and be aware of potential legal and ethical considerations when interacting with external APIs or web services.

    ### OUTPUT
    {
        "branch_name": "feature/sonagent-google-search",
        "commit_message": "add new feature to perform Google search",
        "pull_request_title": "Add new skill to agent to perform Google search",
        "pull_request_body": "This pull request adds a new skill to the agent to perform a Google search using the googlesearch-python library.",
        "source_code_file_name": "skill_google_search.py",
    }


    ### SUMMARY
    {sumary_text}

    ### OUTPUT

    """

    return GITHUB_PULL_REQUEST



GITHUB_PULL_REQUEST_PROMPT = """
You are a software engineer working on a python project.
You have been asked to create a pull request for the following changes.
The changes are to the codebase of a project. 
Based on the content provided below. Let's create a json file, ouput is json that format can load by json.loads.

For example:

Example 1:
[SUMMARY]
SonAgent (to assistant):
create a python class that have function to plot apple stock price in from 1 year ago to now user yahoo finance data 
that class need extend from 
```python
from pydantic import BaseModel
```
--------------------------------------------------------------------------------
assistant (to SonAgent):

To accomplish this task, we will create a Python class `PlotAppleStock` that extends from `BaseModel` provided by `pydantic`. 
This class will have a function to plot the Apple stock price from 1 year ago to the current date using Yahoo Finance data. 
We will use the `yfinance` library to fetch the stock data and `matplotlib` for plotting. 
If you don't have `yfinance` and `matplotlib` installed, you will need to install them using pip.

Here's the plan:
1. Import necessary libraries.
2. Extend the class from `BaseModel`.
3. Implement a function within the class to fetch and plot the Apple stock price data.

First, ensure you have `pydantic`, `yfinance`, and `matplotlib` installed. You can install them using pip. Execute the following command in your shell:

[OUTPUT]
```json
{{
    "branch_name": "feature/sonagent-plot-apple-stock",
    "commit_message": "add new feature to plot apple stock price",
    "pull_request_title": "Add new skill to agent to plot Apple stock price",
    "pull_request_body": "This pull request adds a new skill to the agent to plot the Apple stock price using Yahoo Finance data.",
    "source_code_file_name": "skill_plot_apple_stock.py",
    "class_name": "PlotAppleStock"
}}
```

Example 2:
[SUMMARY]
Certainly! The following is a summary of the Python function for performing a Google search using the googlesearch-python library:
Install the googlesearch-python library using pip install googlesearch-python.
Create a class called `GooleSearch` have a function called google_search that takes a search query and an optional parameter for the number of results to fetch.
Inside the function, use the search function from the library to perform the Google search with the given query and retrieve the specified number of results.
Iterate through the search results and print the title and URL of each result.
Handle exceptions gracefully in case of errors during the search process.
Remember to use this functionality responsibly and be aware of potential legal and ethical considerations when interacting with external APIs or web services.

[OUTPUT]
```json
{{
    "branch_name": "feature/sonagent-google-search",
    "commit_message": "add new feature to perform Google search",
    "pull_request_title": "Add new skill to agent to perform Google search",
    "pull_request_body": "This pull request adds a new skill to the agent to perform a Google search using the googlesearch-python library.",
    "source_code_file_name": "skill_google_search.py",
    "class_name": "GooleSearch"
}}
```

[SUMMARY]
{sumary_text}

[OUTPUT]

"""