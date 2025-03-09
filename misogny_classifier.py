import autogen
from autogen import AfterWorkOption, ConversableAgent, OnCondition, initiate_swarm_chat, register_hand_off
from autogen import UserProxyAgent
import os

config_list = [
    {
        "model": 'llama3.2:latest',
        "api_type": "ollama",
    }
]

llm_config = {
    "cache_seed": 42,
    "temperature": 0.7,
    "config_list": config_list,
    "timeout": 120,
    "tools": [],  # Add function calling tools if needed
}


# Classifier agent: Checks if a comment is toxic
ClassifierAgent = ConversableAgent(
    name="ClassifierAgent",
    system_message="""You are an expert in classifying comments for the saftery of women.
    You will be given a comment and it's parent thread, and you need to determine if it is contains misogny or not.
    It the comment contains misogny, you need to point out specific word for your conclusion.
    
    ** DONOT Give reason for your classification **
    ** After classification return "TERMINATE" **
    ** DONOT PUT ANY OTHER TEXT ASIDE FROM THE FORMAT MENTIONED BELOW AND REPLACE WITH THE ACTUAL VALUES**
    
    Output:
    
    Classifications: Misogny or Non-Misogny
    Highlighted Words: ....
    """,
    llm_config=llm_config,
)

def get_misogny_classification(parents, comment):
    response = ClassifierAgent.run("Parent Thread : \n" + parents + "\n Comment :\n" + comment, user_input=False, max_turns=1)
    response_message = response.chat_history[1]['content']
    return response_message