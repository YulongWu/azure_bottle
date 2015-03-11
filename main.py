from bottle import route, static_file, run

@route('/<filename:path>')
def send_static(filename):
    return static_file(filename, root='./')
@route('/')
def main_static():
    return static_file('index.html', root='./')
@get('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='./')

run(host='localhost', port=8080, debug=True)
