
# Copyright (C) 2005-2011 Splunk Inc. All Rights Reserved.  Version 4.0
import sys,splunk.Intersplunk

results,dummyresults,settings = splunk.Intersplunk.getOrganizedResults()
for result in results:
    Original_Value = result['Original_Value']
    New_Value = result['New_Value']
    Original_Value = Original_Value.split('|')
    New_Value = New_Value.split('|')
    Original_Value_list = list(set(Original_Value)^set(New_Value)&set(Original_Value))
    New_Value_list = list(set(New_Value)^set(Original_Value)&set(New_Value))
    result['Original_Value'] = "\n".join(Original_Value_list)
    result['New_Value'] = "\n".join(New_Value_list)

splunk.Intersplunk.outputResults(results)

