# -*- coding: utf-8 -*-

import os
import unittest

import intelmq.lib.test as test
import intelmq.lib.utils as utils
from intelmq.bots.parsers.shadowserver.microsoft_sinkhole_parser import \
    ShadowServerMicrosoftSinkholeParserBot

with open(os.path.join(os.path.dirname(__file__),
                       'microsoft-sinkhole.csv')) as handle:
    EXAMPLE_FILE = handle.read()

EXAMPLE_REPORT = {"feed.name": "ShadowServer QOTD",
                  "raw": utils.base64_encode(EXAMPLE_FILE),
                  "__type": "Report",
                  "time.observation": "2015-01-01T00:00:00+00:00",
                  }
EVENTS = [{'__type': 'Event',
           'classification.type': 'botnet drone',
           'destination.asn': 8075,
           'destination.geolocation.cc': 'SG',
           'destination.ip': '168.63.184.224',
           'destination.port': 16470,
           'feed.name': 'ShadowServer QOTD',
           'malware.name': 'b68-zeroaccess-1-64bit',
           'protocol.application': 'http',
           'raw': 'Iih1J2lwJywgdSc3Ny4xMi43My4xMzgnKSwodSdkc3RfYXNuJywgdSc4MDc1JyksKHUnaHR0cF9yZWZlcmVyX2FzbicsIHUnJyksKHUnc3JjX3BvcnQnLCB1JzY0NzQyJyksKHUnaHR0cF9yZWZlcmVyJywgdScnKSwodSd0b3InLCB1JycpLCh1J2hvc3RuYW1lJywgdScnKSwodSdzaWMnLCB1JzAnKSwodSd0eXBlJywgdSdiNjgtemVyb2FjY2Vzcy0xLTY0Yml0JyksKHUncDBmX2dlbnJlJywgdScnKSwodSdodHRwX3JlZmVyZXJfZ2VvJywgdScnKSwodSdodHRwX3JlZmVyZXJfaXAnLCB1JycpLCh1J3AwZl9kZXRhaWwnLCB1JycpLCh1J3RpbWVzdGFtcCcsIHUnMjAxNC0wOS0xMiAwMDowMDowMCcpLCh1J2h0dHBfYWdlbnQnLCB1JycpLCh1J2h0dHBfaG9zdCcsIHUnJyksKHUnZHN0X2dlbycsIHUnU0cnKSwodSdnZW8nLCB1J0RFJyksKHUnYXNuJywgdSc2ODA1JyksKHUnbmFpY3MnLCB1JzAnKSwodSd1cmwnLCB1JycpLCh1J2RzdF9wb3J0JywgdScxNjQ3MCcpLCh1J2RzdF9pcCcsIHUnMTY4LjYzLjE4NC4yMjQnKSI=',
           'source.asn': 6805,
           'source.geolocation.cc': 'DE',
           'source.ip': '77.12.73.138',
           'source.port': 64742,
           'time.observation': '2015-01-01T00:00:00+00:00',
           'time.source': '2014-09-12T00:00:00+00:00'},
          {'__type': 'Event',
           'classification.type': 'botnet drone',
           'destination.asn': 8075,
           'destination.geolocation.cc': 'HK',
           'destination.ip': '168.63.202.23',
           'destination.port': 16470,
           'feed.name': 'ShadowServer QOTD',
           'malware.name': 'b68-zeroaccess-1-64bit',
           'protocol.application': 'http',
           'raw': 'Iih1J2lwJywgdScxMDkuNjQuMTMzLjE4NycpLCh1J2RzdF9hc24nLCB1JzgwNzUnKSwodSdodHRwX3JlZmVyZXJfYXNuJywgdScnKSwodSdzcmNfcG9ydCcsIHUnNjI0NzMnKSwodSdodHRwX3JlZmVyZXInLCB1JycpLCh1J3RvcicsIHUnJyksKHUnaG9zdG5hbWUnLCB1JycpLCh1J3NpYycsIHUnMCcpLCh1J3R5cGUnLCB1J2I2OC16ZXJvYWNjZXNzLTEtNjRiaXQnKSwodSdwMGZfZ2VucmUnLCB1JycpLCh1J2h0dHBfcmVmZXJlcl9nZW8nLCB1JycpLCh1J2h0dHBfcmVmZXJlcl9pcCcsIHUnJyksKHUncDBmX2RldGFpbCcsIHUnJyksKHUndGltZXN0YW1wJywgdScyMDE0LTA5LTEyIDAwOjAwOjAwJyksKHUnaHR0cF9hZ2VudCcsIHUnJyksKHUnaHR0cF9ob3N0JywgdScnKSwodSdkc3RfZ2VvJywgdSdISycpLCh1J2dlbycsIHUnSUwnKSwodSdhc24nLCB1Jzg1NTEnKSwodSduYWljcycsIHUnMCcpLCh1J3VybCcsIHUnJyksKHUnZHN0X3BvcnQnLCB1JzE2NDcwJyksKHUnZHN0X2lwJywgdScxNjguNjMuMjAyLjIzJyki',
           'source.asn': 8551,
           'source.geolocation.cc': 'IL',
           'source.ip': '109.64.133.187',
           'source.port': 62473,
           'time.observation': '2015-01-01T00:00:00+00:00',
           'time.source': '2014-09-12T00:00:00+00:00'},
          {'__type': 'Event',
           'classification.type': 'botnet drone',
           'destination.asn': 16265,
           'destination.geolocation.cc': 'NL',
           'destination.ip': '82.192.70.219',
           'destination.port': 16471,
           'feed.name': 'ShadowServer QOTD',
           'malware.name': 'b68-zeroaccess-1-32bit',
           'protocol.application': 'http',
           'raw': 'Iih1J2lwJywgdScxODcuMjQuMjIuOTAnKSwodSdkc3RfYXNuJywgdScxNjI2NScpLCh1J2h0dHBfcmVmZXJlcl9hc24nLCB1JycpLCh1J3NyY19wb3J0JywgdScxMDMwJyksKHUnaHR0cF9yZWZlcmVyJywgdScnKSwodSd0b3InLCB1JycpLCh1J2hvc3RuYW1lJywgdScnKSwodSdzaWMnLCB1JzAnKSwodSd0eXBlJywgdSdiNjgtemVyb2FjY2Vzcy0xLTMyYml0JyksKHUncDBmX2dlbnJlJywgdScnKSwodSdodHRwX3JlZmVyZXJfZ2VvJywgdScnKSwodSdodHRwX3JlZmVyZXJfaXAnLCB1JycpLCh1J3AwZl9kZXRhaWwnLCB1JycpLCh1J3RpbWVzdGFtcCcsIHUnMjAxNC0wOS0xMiAwMDowMDowMCcpLCh1J2h0dHBfYWdlbnQnLCB1JycpLCh1J2h0dHBfaG9zdCcsIHUnJyksKHUnZHN0X2dlbycsIHUnTkwnKSwodSdnZW8nLCB1J0JSJyksKHUnYXNuJywgdScyMjA4NScpLCh1J25haWNzJywgdScwJyksKHUndXJsJywgdScnKSwodSdkc3RfcG9ydCcsIHUnMTY0NzEnKSwodSdkc3RfaXAnLCB1JzgyLjE5Mi43MC4yMTknKSI=',
           'source.asn': 22085,
           'source.geolocation.cc': 'BR',
           'source.ip': '187.24.22.90',
           'source.port': 1030,
           'time.observation': '2015-01-01T00:00:00+00:00',
           'time.source': '2014-09-12T00:00:00+00:00'},
          {'__type': 'Event',
           'classification.type': 'botnet drone',
           'destination.asn': 8075,
           'destination.geolocation.cc': 'SG',
           'destination.ip': '168.63.184.224',
           'destination.port': 16470,
           'feed.name': 'ShadowServer QOTD',
           'malware.name': 'b68-zeroaccess-1-64bit',
           'protocol.application': 'http',
           'raw': 'Iih1J2lwJywgdScxMTguMTU4LjIyNi4xMDUnKSwodSdkc3RfYXNuJywgdSc4MDc1JyksKHUnaHR0cF9yZWZlcmVyX2FzbicsIHUnJyksKHUnc3JjX3BvcnQnLCB1JzQ5MTUyJyksKHUnaHR0cF9yZWZlcmVyJywgdScnKSwodSd0b3InLCB1JycpLCh1J2hvc3RuYW1lJywgdScnKSwodSdzaWMnLCB1JzAnKSwodSd0eXBlJywgdSdiNjgtemVyb2FjY2Vzcy0xLTY0Yml0JyksKHUncDBmX2dlbnJlJywgdScnKSwodSdodHRwX3JlZmVyZXJfZ2VvJywgdScnKSwodSdodHRwX3JlZmVyZXJfaXAnLCB1JycpLCh1J3AwZl9kZXRhaWwnLCB1JycpLCh1J3RpbWVzdGFtcCcsIHUnMjAxNC0wOS0xMiAwMDowMDowMCcpLCh1J2h0dHBfYWdlbnQnLCB1JycpLCh1J2h0dHBfaG9zdCcsIHUnJyksKHUnZHN0X2dlbycsIHUnU0cnKSwodSdnZW8nLCB1J0pQJyksKHUnYXNuJywgdScyNTE2JyksKHUnbmFpY3MnLCB1JzAnKSwodSd1cmwnLCB1JycpLCh1J2RzdF9wb3J0JywgdScxNjQ3MCcpLCh1J2RzdF9pcCcsIHUnMTY4LjYzLjE4NC4yMjQnKSI=',
           'source.asn': 2516,
           'source.geolocation.cc': 'JP',
           'source.ip': '118.158.226.105',
           'source.port': 49152,
           'time.observation': '2015-01-01T00:00:00+00:00',
           'time.source': '2014-09-12T00:00:00+00:00'},
          {'__type': 'Event',
           'classification.type': 'botnet drone',
           'destination.asn': 8075,
           'destination.geolocation.cc': 'HK',
           'destination.ip': '207.46.138.117',
           'destination.port': 16464,
           'feed.name': 'ShadowServer QOTD',
           'malware.name': 'b68-zeroaccess-2-32bit',
           'protocol.application': 'http',
           'raw': 'Iih1J2lwJywgdScxNzMuMTk2LjkuMjIyJyksKHUnZHN0X2FzbicsIHUnODA3NScpLCh1J2h0dHBfcmVmZXJlcl9hc24nLCB1JycpLCh1J3NyY19wb3J0JywgdSc1NTI1MycpLCh1J2h0dHBfcmVmZXJlcicsIHUnJyksKHUndG9yJywgdScnKSwodSdob3N0bmFtZScsIHUnJyksKHUnc2ljJywgdScwJyksKHUndHlwZScsIHUnYjY4LXplcm9hY2Nlc3MtMi0zMmJpdCcpLCh1J3AwZl9nZW5yZScsIHUnJyksKHUnaHR0cF9yZWZlcmVyX2dlbycsIHUnJyksKHUnaHR0cF9yZWZlcmVyX2lwJywgdScnKSwodSdwMGZfZGV0YWlsJywgdScnKSwodSd0aW1lc3RhbXAnLCB1JzIwMTQtMDktMTIgMDA6MDA6MDAnKSwodSdodHRwX2FnZW50JywgdScnKSwodSdodHRwX2hvc3QnLCB1JycpLCh1J2RzdF9nZW8nLCB1J0hLJyksKHUnZ2VvJywgdSdVUycpLCh1J2FzbicsIHUnMjAwMDEnKSwodSduYWljcycsIHUnMCcpLCh1J3VybCcsIHUnJyksKHUnZHN0X3BvcnQnLCB1JzE2NDY0JyksKHUnZHN0X2lwJywgdScyMDcuNDYuMTM4LjExNycpIg==',
           'source.asn': 20001,
           'source.geolocation.cc': 'US',
           'source.ip': '173.196.9.222',
           'source.port': 55253,
           'time.observation': '2015-01-01T00:00:00+00:00',
           'time.source': '2014-09-12T00:00:00+00:00'},
          {'__type': 'Event',
           'classification.type': 'botnet drone',
           'destination.asn': 8075,
           'destination.geolocation.cc': 'SG',
           'destination.ip': '168.63.240.164',
           'destination.port': 16464,
           'feed.name': 'ShadowServer QOTD',
           'malware.name': 'b68-zeroaccess-2-32bit',
           'protocol.application': 'http',
           'raw': 'Iih1J2lwJywgdSc0Mi4xMTIuMTQxLjE1NCcpLCh1J2RzdF9hc24nLCB1JzgwNzUnKSwodSdodHRwX3JlZmVyZXJfYXNuJywgdScnKSwodSdzcmNfcG9ydCcsIHUnMjk1NTQnKSwodSdodHRwX3JlZmVyZXInLCB1JycpLCh1J3RvcicsIHUnJyksKHUnaG9zdG5hbWUnLCB1JycpLCh1J3NpYycsIHUnMCcpLCh1J3R5cGUnLCB1J2I2OC16ZXJvYWNjZXNzLTItMzJiaXQnKSwodSdwMGZfZ2VucmUnLCB1JycpLCh1J2h0dHBfcmVmZXJlcl9nZW8nLCB1JycpLCh1J2h0dHBfcmVmZXJlcl9pcCcsIHUnJyksKHUncDBmX2RldGFpbCcsIHUnJyksKHUndGltZXN0YW1wJywgdScyMDE0LTA5LTEyIDAwOjAwOjAwJyksKHUnaHR0cF9hZ2VudCcsIHUnJyksKHUnaHR0cF9ob3N0JywgdScnKSwodSdkc3RfZ2VvJywgdSdTRycpLCh1J2dlbycsIHUnVk4nKSwodSdhc24nLCB1JzE4NDAzJyksKHUnbmFpY3MnLCB1JzAnKSwodSd1cmwnLCB1JycpLCh1J2RzdF9wb3J0JywgdScxNjQ2NCcpLCh1J2RzdF9pcCcsIHUnMTY4LjYzLjI0MC4xNjQnKSI=',
           'source.asn': 18403,
           'source.geolocation.cc': 'VN',
           'source.ip': '42.112.141.154',
           'source.port': 29554,
           'time.observation': '2015-01-01T00:00:00+00:00',
           'time.source': '2014-09-12T00:00:00+00:00'},
          {'__type': 'Event',
           'classification.type': 'botnet drone',
           'destination.asn': 8075,
           'destination.geolocation.cc': 'US',
           'destination.ip': '204.95.99.205',
           'destination.port': 443,
           'destination.url': 'http://204.95.99.205/index.php',
           'extra': '{"http_agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.0.8077)", "http_host": "204.95.99.205", "http_referer": "0"}',
           'feed.name': 'ShadowServer QOTD',
           'malware.name': 'caphaw',
           'protocol.application': 'http',
           'raw': 'Iih1J2lwJywgdScxMi4xNzkuMTEyLjE1NScpLCh1J2RzdF9hc24nLCB1JzgwNzUnKSwodSdodHRwX3JlZmVyZXJfYXNuJywgdScnKSwodSdzcmNfcG9ydCcsIHUnNTcwNjcnKSwodSdodHRwX3JlZmVyZXInLCB1JzAnKSwodSd0b3InLCB1JycpLCh1J2hvc3RuYW1lJywgdScnKSwodSdzaWMnLCB1JzAnKSwodSd0eXBlJywgdSdjYXBoYXcnKSwodSdwMGZfZ2VucmUnLCB1JycpLCh1J2h0dHBfcmVmZXJlcl9nZW8nLCB1JycpLCh1J2h0dHBfcmVmZXJlcl9pcCcsIHUnJyksKHUncDBmX2RldGFpbCcsIHUnJyksKHUndGltZXN0YW1wJywgdScyMDE0LTA5LTEyIDAwOjAwOjAwJyksKHUnaHR0cF9hZ2VudCcsIHUnTW96aWxsYS80LjAgKGNvbXBhdGlibGU7IE1TSUUgNi4wOyBXaW5kb3dzIE5UIDUuMTsgU1YxOyAuTkVUIENMUiAxLjAuODA3NyknKSwodSdodHRwX2hvc3QnLCB1JzIwNC45NS45OS4yMDUnKSwodSdkc3RfZ2VvJywgdSdVUycpLCh1J2dlbycsIHUnVVMnKSwodSdhc24nLCB1JzcwMTgnKSwodSduYWljcycsIHUnMCcpLCh1J3VybCcsIHUnL2luZGV4LnBocCcpLCh1J2RzdF9wb3J0JywgdSc0NDMnKSwodSdkc3RfaXAnLCB1JzIwNC45NS45OS4yMDUnKSI=',
           'source.asn': 7018,
           'source.geolocation.cc': 'US',
           'source.ip': '12.179.112.155',
           'source.port': 57067,
           'time.observation': '2015-01-01T00:00:00+00:00',
           'time.source': '2014-09-12T00:00:00+00:00'},
          {'__type': 'Event',
           'classification.type': 'botnet drone',
           'destination.asn': 8075,
           'destination.geolocation.cc': 'US',
           'destination.ip': '204.95.99.204',
           'destination.port': 443,
           'destination.url': 'http://xf5wau9lcpf5.oonucoog.cc/ping.html',
           'extra': '{"http_agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.0.7357)", "http_host": "xf5wau9lcpf5.oonucoog.cc", "http_referer": "0"}',
           'feed.name': 'ShadowServer QOTD',
           'malware.name': 'caphaw',
           'protocol.application': 'http',
           'raw': 'Iih1J2lwJywgdSc3MC42MC40My4xMDInKSwodSdkc3RfYXNuJywgdSc4MDc1JyksKHUnaHR0cF9yZWZlcmVyX2FzbicsIHUnJyksKHUnc3JjX3BvcnQnLCB1JzIyNjYnKSwodSdodHRwX3JlZmVyZXInLCB1JzAnKSwodSd0b3InLCB1JycpLCh1J2hvc3RuYW1lJywgdScnKSwodSdzaWMnLCB1JzAnKSwodSd0eXBlJywgdSdjYXBoYXcnKSwodSdwMGZfZ2VucmUnLCB1JycpLCh1J2h0dHBfcmVmZXJlcl9nZW8nLCB1JycpLCh1J2h0dHBfcmVmZXJlcl9pcCcsIHUnJyksKHUncDBmX2RldGFpbCcsIHUnJyksKHUndGltZXN0YW1wJywgdScyMDE0LTA5LTEyIDAwOjAwOjAwJyksKHUnaHR0cF9hZ2VudCcsIHUnTW96aWxsYS80LjAgKGNvbXBhdGlibGU7IE1TSUUgNi4wOyBXaW5kb3dzIE5UIDUuMTsgU1YxOyAuTkVUIENMUiAxLjAuNzM1NyknKSwodSdodHRwX2hvc3QnLCB1J3hmNXdhdTlsY3BmNS5vb251Y29vZy5jYycpLCh1J2RzdF9nZW8nLCB1J1VTJyksKHUnZ2VvJywgdSdVUycpLCh1J2FzbicsIHUnMTA3OTYnKSwodSduYWljcycsIHUnMCcpLCh1J3VybCcsIHUnL3BpbmcuaHRtbCcpLCh1J2RzdF9wb3J0JywgdSc0NDMnKSwodSdkc3RfaXAnLCB1JzIwNC45NS45OS4yMDQnKSI=',
           'source.asn': 10796,
           'source.geolocation.cc': 'US',
           'source.ip': '70.60.43.102',
           'source.port': 2266,
           'time.observation': '2015-01-01T00:00:00+00:00',
           'time.source': '2014-09-12T00:00:00+00:00'},
          {'__type': 'Event',
           'classification.type': 'botnet drone',
           'destination.asn': 8075,
           'destination.geolocation.cc': 'US',
           'destination.ip': '204.95.99.204',
           'destination.port': 443,
           'destination.url': 'http://3k3kwrnj.rgk.cc/index.php',
           'extra': '{"http_agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.0.9121)", "http_host": "3k3kwrnj.rgk.cc", "http_referer": "0"}',
           'feed.name': 'ShadowServer QOTD',
           'malware.name': 'caphaw',
           'protocol.application': 'http',
           'raw': 'Iih1J2lwJywgdScxODkuMTA4LjI1LjI2JyksKHUnZHN0X2FzbicsIHUnODA3NScpLCh1J2h0dHBfcmVmZXJlcl9hc24nLCB1JycpLCh1J3NyY19wb3J0JywgdSc1MDYzNCcpLCh1J2h0dHBfcmVmZXJlcicsIHUnMCcpLCh1J3RvcicsIHUnJyksKHUnaG9zdG5hbWUnLCB1JycpLCh1J3NpYycsIHUnMCcpLCh1J3R5cGUnLCB1J2NhcGhhdycpLCh1J3AwZl9nZW5yZScsIHUnJyksKHUnaHR0cF9yZWZlcmVyX2dlbycsIHUnJyksKHUnaHR0cF9yZWZlcmVyX2lwJywgdScnKSwodSdwMGZfZGV0YWlsJywgdScnKSwodSd0aW1lc3RhbXAnLCB1JzIwMTQtMDktMTIgMDA6MDA6MDAnKSwodSdodHRwX2FnZW50JywgdSdNb3ppbGxhLzQuMCAoY29tcGF0aWJsZTsgTVNJRSA2LjA7IFdpbmRvd3MgTlQgNS4xOyBTVjE7IC5ORVQgQ0xSIDEuMC45MTIxKScpLCh1J2h0dHBfaG9zdCcsIHUnM2sza3dybmoucmdrLmNjJyksKHUnZHN0X2dlbycsIHUnVVMnKSwodSdnZW8nLCB1J0JSJyksKHUnYXNuJywgdScxMDQyOScpLCh1J25haWNzJywgdScwJyksKHUndXJsJywgdScvaW5kZXgucGhwJyksKHUnZHN0X3BvcnQnLCB1JzQ0MycpLCh1J2RzdF9pcCcsIHUnMjA0Ljk1Ljk5LjIwNCcpIg==',
           'source.asn': 10429,
           'source.geolocation.cc': 'BR',
           'source.ip': '189.108.25.26',
           'source.port': 50634,
           'time.observation': '2015-01-01T00:00:00+00:00',
           'time.source': '2014-09-12T00:00:00+00:00'},
          {'__type': 'Event',
           'classification.type': 'botnet drone',
           'destination.asn': 3598,
           'destination.geolocation.cc': 'US',
           'destination.ip': '199.2.137.201',
           'destination.port': 80,
           'destination.url': 'http://ultimaresource.com/wild/live/file.php',
           'extra': '{"http_agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; BRI/1)", "http_host": "ultimaresource.com", "http_referer": "0"}',
           'feed.name': 'ShadowServer QOTD',
           'malware.name': 'citadel-b54',
           'protocol.application': 'http',
           'raw': 'Iih1J2lwJywgdSc2Ni4yNDUuNjkuMTI0JyksKHUnZHN0X2FzbicsIHUnMzU5OCcpLCh1J2h0dHBfcmVmZXJlcl9hc24nLCB1JycpLCh1J3NyY19wb3J0JywgdSczMTMwJyksKHUnaHR0cF9yZWZlcmVyJywgdScwJyksKHUndG9yJywgdScnKSwodSdob3N0bmFtZScsIHUnJyksKHUnc2ljJywgdScwJyksKHUndHlwZScsIHUnY2l0YWRlbC1iNTQnKSwodSdwMGZfZ2VucmUnLCB1JycpLCh1J2h0dHBfcmVmZXJlcl9nZW8nLCB1JycpLCh1J2h0dHBfcmVmZXJlcl9pcCcsIHUnJyksKHUncDBmX2RldGFpbCcsIHUnJyksKHUndGltZXN0YW1wJywgdScyMDE0LTA5LTEyIDAwOjAwOjAxJyksKHUnaHR0cF9hZ2VudCcsIHUnTW96aWxsYS80LjAgKGNvbXBhdGlibGU7IE1TSUUgNy4wOyBXaW5kb3dzIE5UIDUuMTsgQlJJLzEpJyksKHUnaHR0cF9ob3N0JywgdSd1bHRpbWFyZXNvdXJjZS5jb20nKSwodSdkc3RfZ2VvJywgdSdVUycpLCh1J2dlbycsIHUnVVMnKSwodSdhc24nLCB1JzY5ODMnKSwodSduYWljcycsIHUnMCcpLCh1J3VybCcsIHUnL3dpbGQvbGl2ZS9maWxlLnBocCcpLCh1J2RzdF9wb3J0JywgdSc4MCcpLCh1J2RzdF9pcCcsIHUnMTk5LjIuMTM3LjIwMScpIg==',
           'source.asn': 6983,
           'source.geolocation.cc': 'US',
           'source.ip': '66.245.69.124',
           'source.port': 3130,
           'time.observation': '2015-01-01T00:00:00+00:00',
           'time.source': '2014-09-12T00:00:01+00:00'},
          {'__type': 'Event',
           'classification.type': 'botnet drone',
           'destination.asn': 3598,
           'destination.geolocation.cc': 'US',
           'destination.ip': '199.2.137.202',
           'destination.port': 80,
           'destination.url': 'http://199.2.137.202/file-b29d40.php',
           'extra': '{"http_agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; WOW64; .NET CLR 3.5.21022)", "http_host": "199.2.137.202", "http_referer": "0"}',
           'feed.name': 'ShadowServer QOTD',
           'malware.name': 'citadel-b54',
           'protocol.application': 'http',
           'raw': 'Iih1J2lwJywgdSc1MC41Mi4xOS4xODAnKSwodSdkc3RfYXNuJywgdSczNTk4JyksKHUnaHR0cF9yZWZlcmVyX2FzbicsIHUnJyksKHUnc3JjX3BvcnQnLCB1JzUyMTc2JyksKHUnaHR0cF9yZWZlcmVyJywgdScwJyksKHUndG9yJywgdScnKSwodSdob3N0bmFtZScsIHUnJyksKHUnc2ljJywgdScwJyksKHUndHlwZScsIHUnY2l0YWRlbC1iNTQnKSwodSdwMGZfZ2VucmUnLCB1JycpLCh1J2h0dHBfcmVmZXJlcl9nZW8nLCB1JycpLCh1J2h0dHBfcmVmZXJlcl9pcCcsIHUnJyksKHUncDBmX2RldGFpbCcsIHUnJyksKHUndGltZXN0YW1wJywgdScyMDE0LTA5LTEyIDAwOjAwOjAxJyksKHUnaHR0cF9hZ2VudCcsIHUnTW96aWxsYS80LjAgKGNvbXBhdGlibGU7IE1TSUUgNy4wOyBXaW5kb3dzIE5UIDYuMDsgV09XNjQ7IC5ORVQgQ0xSIDMuNS4yMTAyMiknKSwodSdodHRwX2hvc3QnLCB1JzE5OS4yLjEzNy4yMDInKSwodSdkc3RfZ2VvJywgdSdVUycpLCh1J2dlbycsIHUnVVMnKSwodSdhc24nLCB1JzU2NTAnKSwodSduYWljcycsIHUnMCcpLCh1J3VybCcsIHUnL2ZpbGUtYjI5ZDQwLnBocCcpLCh1J2RzdF9wb3J0JywgdSc4MCcpLCh1J2RzdF9pcCcsIHUnMTk5LjIuMTM3LjIwMicpIg==',
           'source.asn': 5650,
           'source.geolocation.cc': 'US',
           'source.ip': '50.52.19.180',
           'source.port': 52176,
           'time.observation': '2015-01-01T00:00:00+00:00',
           'time.source': '2014-09-12T00:00:01+00:00'},
          {'__type': 'Event',
           'classification.type': 'botnet drone',
           'destination.asn': 3598,
           'destination.geolocation.cc': 'US',
           'destination.ip': '199.2.137.201',
           'destination.port': 80,
           'destination.url': 'http://prohomemain.com/367601b6737825deb58a244576e4f098/file.php',
           'extra': '{"http_agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; AskTB5.6)", "http_host": "prohomemain.com", "http_referer": "0"}',
           'feed.name': 'ShadowServer QOTD',
           'malware.name': 'citadel-b54',
           'protocol.application': 'http',
           'raw': 'Iih1J2lwJywgdSc5OS4yNDMuMzIuNDgnKSwodSdkc3RfYXNuJywgdSczNTk4JyksKHUnaHR0cF9yZWZlcmVyX2FzbicsIHUnJyksKHUnc3JjX3BvcnQnLCB1JzQ5NzI1JyksKHUnaHR0cF9yZWZlcmVyJywgdScwJyksKHUndG9yJywgdScnKSwodSdob3N0bmFtZScsIHUnJyksKHUnc2ljJywgdScwJyksKHUndHlwZScsIHUnY2l0YWRlbC1iNTQnKSwodSdwMGZfZ2VucmUnLCB1JycpLCh1J2h0dHBfcmVmZXJlcl9nZW8nLCB1JycpLCh1J2h0dHBfcmVmZXJlcl9pcCcsIHUnJyksKHUncDBmX2RldGFpbCcsIHUnJyksKHUndGltZXN0YW1wJywgdScyMDE0LTA5LTEyIDAwOjAwOjAxJyksKHUnaHR0cF9hZ2VudCcsIHUnTW96aWxsYS80LjAgKGNvbXBhdGlibGU7IE1TSUUgNy4wOyBXaW5kb3dzIE5UIDYuMDsgQXNrVEI1LjYpJyksKHUnaHR0cF9ob3N0JywgdSdwcm9ob21lbWFpbi5jb20nKSwodSdkc3RfZ2VvJywgdSdVUycpLCh1J2dlbycsIHUnQ0EnKSwodSdhc24nLCB1JzgxMicpLCh1J25haWNzJywgdScwJyksKHUndXJsJywgdScvMzY3NjAxYjY3Mzc4MjVkZWI1OGEyNDQ1NzZlNGYwOTgvZmlsZS5waHAnKSwodSdkc3RfcG9ydCcsIHUnODAnKSwodSdkc3RfaXAnLCB1JzE5OS4yLjEzNy4yMDEnKSI=',
           'source.asn': 812,
           'source.geolocation.cc': 'CA',
           'source.ip': '99.243.32.48',
           'source.port': 49725,
           'time.observation': '2015-01-01T00:00:00+00:00',
           'time.source': '2014-09-12T00:00:01+00:00'},
          {'__type': 'Event',
           'classification.type': 'botnet drone',
           'destination.asn': 3598,
           'destination.geolocation.cc': 'US',
           'destination.ip': '199.2.137.202',
           'destination.port': 80,
           'destination.url': 'http://ronapri.com/view/file.php',
           'extra': '{"http_agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; AskTbFWV5/5.11.3.15590)", "http_host": "ronapri.com", "http_referer": "0"}',
           'feed.name': 'ShadowServer QOTD',
           'malware.name': 'citadel-b54',
           'protocol.application': 'http',
           'raw': 'Iih1J2lwJywgdScxMDYuMTU2LjIxMC4xOTcnKSwodSdkc3RfYXNuJywgdSczNTk4JyksKHUnaHR0cF9yZWZlcmVyX2FzbicsIHUnJyksKHUnc3JjX3BvcnQnLCB1JzU1NDAwJyksKHUnaHR0cF9yZWZlcmVyJywgdScwJyksKHUndG9yJywgdScnKSwodSdob3N0bmFtZScsIHUnJyksKHUnc2ljJywgdScwJyksKHUndHlwZScsIHUnY2l0YWRlbC1iNTQnKSwodSdwMGZfZ2VucmUnLCB1JycpLCh1J2h0dHBfcmVmZXJlcl9nZW8nLCB1JycpLCh1J2h0dHBfcmVmZXJlcl9pcCcsIHUnJyksKHUncDBmX2RldGFpbCcsIHUnJyksKHUndGltZXN0YW1wJywgdScyMDE0LTA5LTEyIDAwOjAwOjAxJyksKHUnaHR0cF9hZ2VudCcsIHUnTW96aWxsYS80LjAgKGNvbXBhdGlibGU7IE1TSUUgNy4wOyBXaW5kb3dzIE5UIDYuMDsgQXNrVGJGV1Y1LzUuMTEuMy4xNTU5MCknKSwodSdodHRwX2hvc3QnLCB1J3JvbmFwcmkuY29tJyksKHUnZHN0X2dlbycsIHUnVVMnKSwodSdnZW8nLCB1J0pQJyksKHUnYXNuJywgdScyNTE2JyksKHUnbmFpY3MnLCB1JzAnKSwodSd1cmwnLCB1Jy92aWV3L2ZpbGUucGhwJyksKHUnZHN0X3BvcnQnLCB1JzgwJyksKHUnZHN0X2lwJywgdScxOTkuMi4xMzcuMjAyJyki',
           'source.asn': 2516,
           'source.geolocation.cc': 'JP',
           'source.ip': '106.156.210.197',
           'source.port': 55400,
           'time.observation': '2015-01-01T00:00:00+00:00',
           'time.source': '2014-09-12T00:00:01+00:00'},
          {'__type': 'Event',
           'classification.type': 'botnet drone',
           'destination.asn': 3598,
           'destination.geolocation.cc': 'US',
           'destination.ip': '199.2.137.201',
           'destination.port': 80,
           'destination.url': 'http://9A5BB34EEDE4B85B9E81F40D530B68FF.co.cc/message.php',
           'extra': '{"http_agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; .NET4.0C)", "http_host": "9A5BB34EEDE4B85B9E81F40D530B68FF.co.cc", "http_referer": "0"}',
           'feed.name': 'ShadowServer QOTD',
           'malware.name': 'bamital-b58',
           'protocol.application': 'http',
           'raw': 'Iih1J2lwJywgdScxMzguMjE3Ljg5LjI1JyksKHUnZHN0X2FzbicsIHUnMzU5OCcpLCh1J2h0dHBfcmVmZXJlcl9hc24nLCB1JycpLCh1J3NyY19wb3J0JywgdSc2MjI1NCcpLCh1J2h0dHBfcmVmZXJlcicsIHUnMCcpLCh1J3RvcicsIHUnJyksKHUnaG9zdG5hbWUnLCB1JycpLCh1J3NpYycsIHUnMCcpLCh1J3R5cGUnLCB1J2JhbWl0YWwtYjU4JyksKHUncDBmX2dlbnJlJywgdScnKSwodSdodHRwX3JlZmVyZXJfZ2VvJywgdScnKSwodSdodHRwX3JlZmVyZXJfaXAnLCB1JycpLCh1J3AwZl9kZXRhaWwnLCB1JycpLCh1J3RpbWVzdGFtcCcsIHUnMjAxNC0wOS0xMiAwMDowMDowMScpLCh1J2h0dHBfYWdlbnQnLCB1J01vemlsbGEvNC4wIChjb21wYXRpYmxlOyBNU0lFIDguMDsgV2luZG93cyBOVCA2LjE7IC5ORVQ0LjBDKScpLCh1J2h0dHBfaG9zdCcsIHUnOUE1QkIzNEVFREU0Qjg1QjlFODFGNDBENTMwQjY4RkYuY28uY2MnKSwodSdkc3RfZ2VvJywgdSdVUycpLCh1J2dlbycsIHUnQVUnKSwodSdhc24nLCB1JzEyMjEnKSwodSduYWljcycsIHUnMCcpLCh1J3VybCcsIHUnL21lc3NhZ2UucGhwJyksKHUnZHN0X3BvcnQnLCB1JzgwJyksKHUnZHN0X2lwJywgdScxOTkuMi4xMzcuMjAxJyki',
           'source.asn': 1221,
           'source.geolocation.cc': 'AU',
           'source.ip': '138.217.89.25',
           'source.port': 62254,
           'time.observation': '2015-01-01T00:00:00+00:00',
           'time.source': '2014-09-12T00:00:01+00:00'}]


class TestShadowServerMicrosoftSinkholeParserBot(test.BotTestCase,
                                                 unittest.TestCase):
    """
    A TestCase for a ShadowServerMicrosoftSinkholeParserBot.
    """

    @classmethod
    def set_bot(cls):
        cls.bot_reference = ShadowServerMicrosoftSinkholeParserBot
        cls.default_input_message = EXAMPLE_REPORT

    def test_event(self):
        """ Test if correct Event has been produced. """
        self.run_bot()
        for i, EVENT in enumerate(EVENTS):
            self.assertMessageEqual(i, EVENT)


if __name__ == '__main__':
    unittest.main()
