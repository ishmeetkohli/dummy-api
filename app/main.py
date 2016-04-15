#!/usr/bin/python
# -*- coding: utf-8 -*-
import bottle
import json
import heapq
import random
import copy
import os
import json

@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')

@bottle.get('/first')
def test():
    data = None
    with open('dataWithElevation.json') as data_file:
        data = json.load(data_file)
    return json.dumps(data)
    
@bottle.get('/later')
def test():
    data = None
    # with open('dataWithElevation.json') as data_file:
    #     data = json.load(data_file)
    return None
    
@bottle.get('/reset')
def test():
    data = None
    # with open('dataWithElevation.json') as data_file:
    #     data = json.load(data_file)
    return None

# Expose WSGI app (so gunicorn can find it)

application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'),
               port=os.getenv('PORT', '8080'))
