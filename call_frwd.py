import os                                                                                                                                             
from flask import Flask, request, make_response, render_template, redirect
#from Wtforms import Form TextField, validators
import plivo

#class phoneno(Form):
#   phone number=Text.Field('Phone number',[validators.length(min=10, max=12)]

app=Flask(__name__)


phoneno=''
auth_id = 'MAMWQYZJYWMGY0NZQ3MJ'
auth_token = 'NzhkMzYzNDhlOTcxMTQ2MDNkYjI0ZTdhNWQ4YWJi'

@app.route('/', methods=['POST', 'GET'])
def index():
        return 'call a number'

@app.route('/call/')
def call_arg():
    return render_template("phoneno.html")

@app.route('/call/', methods=['GET','POST'])
def call():
    ph=request.form['phonenumber']
    p=plivo.RestAPI(auth_id, auth_token)
    params={
        'from': '919941975713',
        'to': 'ph',
        'answer_url':"https://www.dropbox.com/s/9nhoxcku1b8ij3o/transfer2.xml"
        }
    response=p.make_call(params)
if response['message']!='call fired':
        return 'call not made'
#    else:
        return transfer()

#@app.route('/transfer/',methods=['GET','POST'])
def transfer():
    p1=plivo.RestAPI(auth_id, auth_token)
    params={
        'from':'ph',
        'to':'919043836911',
        'answer_url':"https://www.dropbox.com/s/q012vu3pl0c8n71/transfer1.xml"
        }
    response=p1.make_call(params)
    if response['message']!='call fired':
        return 'call transfer failed'
    else:
        return 'call in progress'

if __name__=='__main__':
    app.run(debug=True)                                                                                                                               
                                                   
