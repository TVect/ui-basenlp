from werobot import WeRoBot
from werobot.contrib.tornado import make_handler

robot = WeRoBot(token='VectorMachine')

@robot.text
def echo(message):
    return message.content

@robot.handler
def hello(message):
    return 'Hello World!'

WxMpHandler = make_handler(robot)

