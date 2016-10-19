# -*- coding: utf-8 -*-
import csv
import io
import sys

from intelmq.lib import utils
from intelmq.lib.bot import Bot
from intelmq.lib.message import Event
from intelmq.lib.cache import Cache

class AlexaWhitelistParserBot(Bot):

    def init(self):
        self.cache = Cache(self.parameters.redis_cache_host,
                           self.parameters.redis_cache_port,
                           self.parameters.redis_cache_db,
                           self.parameters.redis_cache_ttl,
                           )

    def process(self):
        report = self.receive_message()

        raw_report = utils.base64_decode(report.get("raw"))
        report_accu = report.get("feed.accuracy")
        for row in csv.reader(io.StringIO(raw_report)):

            if not len(row):  # csv module can give empty lists
                self.acknowledge_message()
                return

            fqdn = row[1]
            accu = report_accu - int(int(row[0])/10000)

            if self.cache.exists(fqdn):
                accu_old = int(self.cache.get(fqdn))
                if accu_old < accu:
                    self.cache.set(fqdn, str(int(accu)), 864000)
            else:
                self.cache.set(fqdn, str(int(accu)), 864000)

        self.acknowledge_message()


if __name__ == "__main__":
    bot = AlexaWhitelistParserBot(sys.argv[1])
    bot.start()
