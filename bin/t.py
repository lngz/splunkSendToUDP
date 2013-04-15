
# Copyright (C) 2005-2011 Splunk Inc. All Rights Reserved.  Version 4.0
import sys,splunk.Intersplunk
import socket


results,dummyresults,settings = splunk.Intersplunk.getOrganizedResults()
#(isgetinfo, sys.argv) = splunk.Intersplunk.isGetInfo(sys.argv)
if len(sys.argv) < 2:
    splunk.Intersplunk.parseError("No arguments provided")
#address = ('10.211.55.10', 514)
address = (sys.argv[1], int(sys.argv[2]))

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


for result in results:
    data = result['_raw']
    s.sendto( data,address)


s.close()

splunk.Intersplunk.outputResults(results)

