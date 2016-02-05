from . import app1

@app1.route('/app1')
def app1():
    return 'applicazione 1'

