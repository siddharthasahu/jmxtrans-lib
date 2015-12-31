#!/usr/bin/python2

import os
import sys
from config import *

template_data = open('templates/template.json', 'r').read()

for server in servers:
    print "generating template for %(host)s:%(port)s" % { 'host': server["host"], 'port': server["port"]}
    output_file = open("%(output_dir)s/%(server_alias)s-%(host)s-%(port)s.json" % { 'host': server["host"], 'port': server["port"], 'server_alias': server["server_alias"], 'output_dir': output_dir}, "w")
    server.update(graphite_data)
    output_file.write(template_data % server)
    output_file.close()
