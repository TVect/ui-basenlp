import aiml
import os
# os.chdir(os.path.dirname(os.path.abspath(__file__)) + "/botdata/alice")
# alice_aiml = os.path.dirname(os.path.abspath(__file__))+"/botdata/alice/startup.xml"
alice_dir = os.path.dirname(os.path.abspath(__file__)) + "/botdata/alice"

class AimlBot:

    def __init__(self):
        self.kernel = aiml.Kernel()
        for alice_aiml in os.listdir(alice_dir):
            if alice_aiml.endswith("aiml"):
                self.kernel.learn(os.path.join(alice_dir, alice_aiml))
        # self.kernel.learn("startup.xml")
        # self.kernel.respond("LOAD ALICE")

    def response(self, in_str):
        return self.kernel.respond(in_str)


if __name__ == "__main__":
    aiml_bot = AimlBot()
    while True:
        print(aiml_bot.response(input("> ")))
