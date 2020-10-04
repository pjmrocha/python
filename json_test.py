#!/usr/bin/python

import json

resp = """{ "list": [ {"name": "john"}, {"name": "mike"} ] }"""

j = json.loads(resp)

print j
print j["list"]
print j["list"][0]
print j["list"][0]["name"]


resp2 = { "list": [ {"name": "anna"}, {"name": "susan"} ] }
j2 = json.dumps(resp2)
print j2

j3 = json.loads(j2)
print j3
