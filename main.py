# imports
import os
from typing import Annotated
import autogen


# define the tasks
task1 = """
    Find arxiv papers that show how are people studying trust callibration in AI based systems
"""
task2 = """
    Analyze the above results to list the application domains studied by these papers.
"""
task3 = """
    Use this data to generate a bar chart of domains and number of papers in each domain and save the chart to a file.
"""
task4 = """
    Reflect on the sqeuence and create a recipe containing all the steps
    neccessar and name for it.  Suggest well-documentd, generalized python fuction(s)
    to perform similiar tasks for coding steps in the future.  Make sure coding steps and
    non-coding steps are never mixed in one fuction. In the docstr of the function(s)
    clarify the non-coding steps needed to use the language skill of the assistant.
"""

# create the the llm config
llm_config = {
    "timeout": 120,
    "cache_seed": 43,
    "config_list": autogen.config_list_from_json(
        env_or_file="OAI_CONFIG_LIST.json",
      filter_dict={"model": ["gpt-3.5-turbo"]},
    ),
    "temperature": 0,
}

# create the the agents


# create a simple fuction


# initiate the chats


# initiate chat with the recipe from the file
