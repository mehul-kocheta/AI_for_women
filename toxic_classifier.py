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
    system_message="""You are an expert in classifying toxic comments.
    You will be given a comment and it's parent thread, and you need to determine if it is toxic or non-toxis or neutral.
    It the comment is toxic, you need to suggest an alternative non-toxic comment.
    
    ** DONOT PUT ANY OTHER TEXT ASIDE FROM THE FORMAT MENTIONED BELOW **
    ** DONOT Give reason for your classification **
    ** After classification retun "TERMINATE" **
    
    Output:
    
    Classifications: Toxic or Non-Toxic or Neutral
    Suggested Comment: ....
    """,
    llm_config=llm_config,
)

def get_toxic_classification(parents, comment):
    response = ClassifierAgent.run("Parent Thread : \n" + parents + "\n Comment :\n" + comment, user_input=False, max_turns=1)
    response_message = response.chat_history[1]['content']
    return response_message