# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
import sys

from intelmq.lib import utils
from intelmq.lib.bot import Bot
from intelmq.lib.message import Event


def is_valid_date(strd):
    try:
        datetime.datetime.strptime(strd, '%Y%m%d')
        return True
    except Exception:
        return False


class UniversalLinesParserBot(Bot):

    def process(self):
        report = self.receive_message()

        if report is None or not report.contains("raw"):
            self.acknowledge_message()
            return

        raw_report = utils.base64_decode(report.value("raw"))

        for row in raw_report.split('\n'):
            row = row.rstrip()
            if row.startswith("#") or len(row) == 0:
                continue

            values = row.split(self.parameters.delimiter)
            event = Event(report)

            for value in values:


            event.add('source.fqdn', values[1], sanitize=True)
            event.add('event_description.text', values[2], sanitize=True)

            for i in range(4, len(values)):
                if is_valid_date(values[i]):
                    event.add('time.source',  # TODO: verify timezone
                              values[i] + "T00:00:00+00:00", sanitize=True, force=True)
                    break

            event.add('classification.type', self.parameters.type)
            event.add('raw', row, sanitize=True)

            self.send_message(event)
        self.acknowledge_message()

if __name__ == "__main__":
    bot = UniversalLinesParserBot(sys.argv[1])
    bot.start()
