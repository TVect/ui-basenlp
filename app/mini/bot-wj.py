from rasa_core.train import train_dialogue_model
from rasa_core.agent import Agent
from rasa_core.run import main
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.interpreter import NaturalLanguageInterpreter

domain_file = "./conf/domain-wj.yml"
stories_file = "./data/stories-exported"
output_path = "./models/dialogue-wj"


def train_dialog(use_online_learning=False):
    train_dialogue_model(domain_file, stories_file, output_path, 
                         use_online_learning=use_online_learning,
                         kwargs={"epochs": 200})


def test_dialog():
    agent = Agent.load(output_path, interpreter=NaturalLanguageInterpreter.create(None))

    agent.handle_channel(ConsoleInputChannel())

    return agent

if __name__ == "__main__":
    # test_dialog()
    train_dialog(use_online_learning=False)
