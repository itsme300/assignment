import os                                                                                                                                             
from flask import Flask, request, make_response, render_template, redirect
#from Wtforms import Form TextField, validators
import plivo

#class phoneno(Form):
#   phone number=Text.Field('Phone number',[validators.length(min=10, max=12)]

app=Flask(__name__)

ph=''

phoneno=''
auth_id = 'xxx'
auth_token = 'xxx'

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
        'from': 'xxxxxxxxxxxx',
        'to': ph,
        'answer_url':"https://dl-web.dropbox.com/get/Public/transfer2.xml?w=AABjZKrcXoysFZ9VNViu3EvPOnCdFeo6jVQuIP7t4slqUw"
        }
    response=p.make_call(params)
#    if response['message']!= 'call fired':

#    return 'call not made'
#    else:
    return transfer(ph)

#@app.route('/transfer/',methods=['GET','POST'])
def transfer(ph):
    p1=plivo.RestAPI(auth_id, auth_token)
    params={
        'from':ph,
        'to':'xxxxxxxxxxxx',
        'answer_url':"https://dl-web.dropbox.com/get/Public/transfer1.xml?w=AAA2sNSIdNTvs1jHMzV9FDz5sZI8mJ5GMX4LVQ9HgnJ-cw"
        }
    response=p1.make_call(params)
    
#    if response['message']!='call fired':
#        return 'call transfer failed'
#  else:

    return 'call in progress'

if __name__=='__main__':
    app.run(debug=True)                    
