from . import app2

@app2.route('/app2')
def app2():
    return 'applicazione 2'

