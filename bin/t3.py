
# Copyright (C) 2005-2011 Splunk Inc. All Rights Reserved.  Version 4.0
import sys,splunk.Intersplunk
import socket

address = ('10.211.55.10', 514)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


results,dummyresults,settings = splunk.Intersplunk.getOrganizedResults()
for result in results:
    data = result['_raw']
    s.sendto( data,address)


s.close()

splunk.Intersplunk.outputResults(results)

