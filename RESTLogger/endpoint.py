import json

import flask
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/<path:path>', methods=['POST', 'PUT', 'GET', 'DELETE', 'PATCH'])
def main_entry_point(path):
    print(flush=True)
    print('#' * 80)
    print('#' * 80 + "\r## Init Petition ")
    print('#' * 80)
    print()

    print("Method: {} in Path: {}".format(request.method, request.path))

    print("From: {}".format(request.remote_addr))

    print('\n# Path params:')
    [print(' - {}: {}'.format(param, value)) for param, value in request.args.items()]

    print("\n# Headers:")
    [print(" - {}: {}".format(h, v)) for h, v in request.headers.items()]

    if request.is_json:
        print("\n# Body: json\n{}".format(json.dumps(request.json, indent=2, sort_keys=True)))
    else:
        print("\n# Body: {}".format(request.data))

    print()
    print('#' * 80)
    print(flush=True)

    status = request.args.get('status', default='200')

    return flask.Response(status=status, content_type='application/json')


if __name__ == '__main__':
    app.run(port=3000, debug=False)
