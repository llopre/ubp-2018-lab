from bottle import Bottle, route, run, get, template, post, request
app = Bottle()



@app.route('/hello', method="GET")
def hello():
    return "Hello Wordl!"

@app.get('/')
@app.get('/hello/<name>', method="GET")
def greet(name='Stranger'):
    return template('Helloo{{name}}', name=name)


# @app.post('/param')
# def hello_json():
#     data =request.json
#     param =data ['param']
#     ret={"status": "OK","param":param}
#     return ret
# run(app,host='127.0.0.1', port =8081)


@app.post('/param')
def hello_json():
    data=request.json
    param=data['param']
    ret= {"status":"ok","param":param}
    return ret

@app.post("/login")
def login_json():
    users={}
    data = request.json
    if data in users:
        return {"status": "ok", "Description":"Bienvenido"}

    return {"status":"ERROR", "Description": "Se ingreso mal el usuario"}


@app.post('/register')
def register_json():
    users={}
    data= request.json 
    users.append(data)
    return{"status":"ok","Description":"Se registro correctamente el usuario"}

run(app,host='127.0.0.1', port =8081)


