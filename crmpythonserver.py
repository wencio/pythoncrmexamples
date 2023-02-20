from flask import Flask, request

app = Flask(__name__)

@app.route('/api/crm', methods=['POST'])
def submit_form():
    data = request.json
    # do something with the data here
    return {'success': True}
