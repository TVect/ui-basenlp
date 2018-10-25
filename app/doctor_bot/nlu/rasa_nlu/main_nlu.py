import os
import logging
import argparse
import pprint
from rasa_nlu import config
from rasa_nlu.model import Interpreter
from rasa_nlu.training_data import load_data
from rasa_nlu.model import Trainer

logger = logging.getLogger(__name__)

##################  nlu_mitie_pipeline ##################
# data_location = "./data/nlu.json"
# nlu_config_file = "./conf/nlu_mitie_pipeline.yaml"
# fixed_model_name = "nlu_mitie_pipeline"
# model_path = "./models"
# project_name = "doctor_bot"

##################  nlu_spacy_pipeline ##################
# data_location = "./data/nlu.json"
# nlu_config_file = "./conf/nlu_spacy_pipeline.yaml"
# fixed_model_name = "nlu_spacy_pipeline"
# model_path = "./models"
# project_name = "doctor_bot"

##################  nlu_spacy_pipeline ##################
data_location = "./data/nlu.json"
nlu_config_file = "./conf/nlu_tfembed_pipeline.yaml"
fixed_model_name = "nlu_tfembed_pipeline"
model_path = "./models"
project_name = "doctor_bot"

def train_nlu():
    '''
    python -m rasa_nlu.train -c nlu_model_config.yaml -d nlu.json --fixed_model_name current -o models
    '''
    training_data = load_data(data_location)
    trainer = Trainer(config.load(nlu_config_file))
    trainer.train(training_data)
    model_directory = trainer.persist(path=model_path, 
                                      project_name=project_name,
                                      fixed_model_name=fixed_model_name)

def test_nlu():
    '''
    '''
    interpreter = Interpreter.load(os.path.join(model_path, project_name, fixed_model_name))
    while True:
        message = input(" >>> input: ")
        result = interpreter.parse(message)
        pprint.pprint(result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mode', default='test', help="mode: train | test")
    cmdline_args = parser.parse_args()
    if cmdline_args.mode == "train":
        logger.info("=== train mode ===")
        train_nlu()
    elif cmdline_args.mode == "test":
        logger.info("=== test mode ===")
        test_nlu()
