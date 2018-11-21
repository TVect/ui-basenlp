from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from dm.policies.rule_policy import RulePolicy

domain_file = "./dm/conf/domain-doctor.yml"

def test_dialog():
    agent = Agent(domain_file, 
                  policies=[RulePolicy()])

    agent.handle_channel(ConsoleInputChannel())

    return agent

if __name__ == "__main__":
    test_dialog()
