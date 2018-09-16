import random
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware

class RandomUserAgentMiddleware(UserAgentMiddleware):
    
    def __init__(self, user_agent):
        self.user_agent = user_agent
    
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            user_agent=crawler.settings.get('USER_AGENT_LIST')
        )
    
    
    def process_request(self, request, spider):
        agent = random.choice(self.user_agent)
        if agent:
            request.headers.setdefault("User-Agent", agent)
