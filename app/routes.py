from app import app
@app.route ('/')
@app.route ('/index')
def index():
    return'<html><head><title>what is management</title></head><body>'
