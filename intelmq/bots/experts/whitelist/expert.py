# -*- coding: utf-8 -*-
"""
Whitelist expert

Parameters:
whitelist_key: string
redis_cache_host: string
redis_cache_port: string
redis_cache_db: string
redis_cache_ttl: string

"""
import sys

from intelmq.lib.bot import Bot
from intelmq.lib.cache import Cache

class WhitelistExpertBot(Bot):

    def init(self):
        self.cache = Cache(self.parameters.redis_cache_host,
                           self.parameters.redis_cache_port,
                           self.parameters.redis_cache_db,
                           self.parameters.redis_cache_ttl,
                           )

    def process(self):
        event = self.receive_message()

        if event.contains(self.parameters.whitelist_key):
            value = event.get(self.parameters.whitelist_key)
            if self.cache.exists(value):
                accu = event.get("feed.accuracy")
                accu_white = int(self.cache.get(value))
                event.update("feed.accuracy", accu - accu_white
                    if accu >= accu_white else 0)

        self.send_message(event)
        self.acknowledge_message()


if __name__ == "__main__":
    bot = WhitelistExpertBot(sys.argv[1])
    bot.start()
