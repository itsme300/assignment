import json
from flask import Flask, request, Response
import subprocess

app = Flask(__name__)

@app.route("/<table>/chain:<chain>/append", methods=['POST'])
def append(table, chain):
    rule_spec = request.args.get('rule_spec')
    return run_iptables(['-t', table, '--append', chain, rule_spec])

@app.route("/<table>/chain:<chain>/delete", methods=['POST'])
def delete(table, chain):
    rule_spec = request.args.get('rule_spec', None)
    rule_num = request.args.get('rule_num', None)
    if rule_spec is None and rule_num is None:
        return client_error("must specify one of 'rule_spec' or 'rule_num'")
    if rule_spec is not None and rule_num is not None:
        return client_error("can't specify both 'rule_spec' or 'rule_num'")

    if rule_spec is not None:
        return run_iptables(['-t', table, '--delete', chain, rule_spec])
    else:
        try:
            rule_num = int(rule_num)
        except ValueError:
            return client_error("'rule_num' is not an integer or is out of range")
        return run_iptables(['-t', table, '--delete', chain, str(rule_num)])

# Runs the 'iptables' command with the given arguments and returns an HTTP
# response with the command's output.  The HTTP status code depends on whether
# the command succeeded or not.
def run_iptables(args):
    command = ['echo'] + args

    try:
        output = subprocess.check_output(command)
        status = 200
    except subprocess.CalledProcessError, e:
        output = e.output
        if e.returncode == 2:
            # Incorrect command usage.
            status = 400
        else:
            # Some other failure.  Use a generic HTTP 409 "Conflict" response,
            # though we could parse the output and try and pick a more specific
            # HTTP code.
            status = 409

    return make_response(status, {'output': output})

# Utility function to create an HTTP 400 with a JSON-wrapped error string.
def client_error(message):
    return make_response(400, {'message': message})

# Utility function to create an HTTP response with a JSON-encoded body.
def make_response(status, data):
    data_json = json.dumps(data)
    return Response(data_json, status, mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True)
