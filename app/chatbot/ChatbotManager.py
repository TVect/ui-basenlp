from app.chatbot.aimlbot.AimlBot import AimlBot

class ChatbotManager:

    def __init__(self):
        self.bot = AimlBot()


    def response(self, in_str):
        return self.bot.response(in_str)


if __name__ == "__main__":
    chat_manager = ChatbotManager()
    while True:
        print(chat_manager.response(input("> ")))
