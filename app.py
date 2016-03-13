import bottle
import json
import os



@route('/hello')
def hello():
    return template('<b>Hello {{name}}</b>!', name=name)

@route('/request', method = 'POST')
def request():
    return


application = bottle.default_app()
if __name__ == '__app__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'),
               port=os.getenv('PORT', '8080'))
