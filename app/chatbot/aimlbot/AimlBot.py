import aiml
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)) + "/botdata/alice")
# alice_aiml = os.path.dirname(os.path.abspath(__file__))+"/botdata/alice/startup.xml"

class AimlBot:

    def __init__(self):
        self.kernel = aiml.Kernel()
        self.kernel.learn("startup.xml")
        self.kernel.respond("LOAD ALICE")

    def response(self, in_str):
        return self.kernel.respond(in_str)


if __name__ == "__main__":
    aiml_bot = AimlBot()
    while True:
        print(aiml_bot.response(input("> ")))
