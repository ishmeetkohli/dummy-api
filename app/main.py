#!/usr/bin/python
# -*- coding: utf-8 -*-
import bottle
import json
import heapq
import random
import copy
import os
import json

with open('data.json') as data_file:
    data = json.load(data_file)
pprint(data)


###### server shit down here
@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')

@bottle.get('/test')
def test():
    with open('../app.json') as data_file:
    data = json.load(data_file)
    return data

# Expose WSGI app (so gunicorn can find it)

application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'),
               port=os.getenv('PORT', '8080'))
