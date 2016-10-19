# -*- coding: utf-8 -*-
"""
Generic CSV Whitelist parser

Parameters:
columns: string
delimiter: string
skip_header: boolean

"""
import csv
import io
import json
import re
import sys

from dateutil.parser import parse

from intelmq.lib import utils
from intelmq.lib.bot import ParserBot
from intelmq.lib.message import Event
from intelmq.lib.cache import Cache

class GenericCsvWhitelistParserBot(ParserBot):

    def init(self):
        self.cache = Cache(self.parameters.redis_cache_host,
                           self.parameters.redis_cache_port,
                           self.parameters.redis_cache_db,
                           self.parameters.redis_cache_ttl,
                           )

    def parse(self, report):
        self.type_translation = None

        self.columns = self.parameters.columns
        # convert columns to an array
        if type(self.parameters.columns) is str:
            self.columns = map(str.strip, self.columns.split(","))

        if hasattr(self.parameters, 'type_translation'):
            self.type_translation = json.loads(self.parameters.type_translation)

        raw_report = utils.base64_decode(report.get("raw"))
        # ignore lines starting with #
        raw_report = re.sub(r'(?m)^#.*\n?', '', raw_report)
        # ignore null bytes
        raw_report = re.sub(r'(?m)\0', '', raw_report)
        # skip header
        if hasattr(self.parameters, 'skip_header') and self.parameters.skip_header:
            raw_report = raw_report[raw_report.find('\n') + 1:]
        for row in csv.reader(io.StringIO(raw_report),
                              delimiter=str(self.parameters.delimiter)):
            yield row

    def parse_line(self, row, report):
        event = Event(report)

        for key, value in zip(self.columns, row):
            if key in ["__IGNORE__", ""]:
                continue
            event.add(key, value)

        fqdn = event.get("source.fqdn")
        accu = event.get("feed.accuracy")
        if self.cache.exists(fqdn):
            accu_old = int(self.cache.get(fqdn))
            if accu_old < accu:
                self.cache.set(fqdn, str(int(accu)), 864000)
        else:
            self.cache.set(fqdn, str(int(accu)), 864000)
        yield event

    recover_line = ParserBot.recover_line_csv

if __name__ == "__main__":
    bot = GenericCsvWhitelistParserBot(sys.argv[1])
    bot.start()
