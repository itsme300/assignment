import os                                                                                                                                             
from flask import Flask, request, make_response, render_template, redirect
import plivo

auth_id='MAMWQYZJYWMGY0NZQ3MJ'
auth_token='NzhkMzYzNDhlOTcxMTQ2MDNkYjI0ZTdhNWQ4YWJi'

app=Flask(__name__)

ph=xxxxxxxxxx

@app.route('/outbound', methods=['POST','GET'])
def outcall():
    p=plivo.RestAPI(auth_id, auth_token)
    call_params={
            'to':'ph',
            'from':'xxxxxxxxxx',
            'answer_url':'https://www.dropbox.com/s/n76obusmwo64ttr/hangup.xml'
            }
    response = p.make_call(call_params)
   # if response['message']!='call fired':
    #    return 'call not made'
   # else:
    return 'call in progress'

if __name__=='__main__':
    app.run(debug=True)
