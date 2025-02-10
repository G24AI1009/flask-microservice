from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/contribution', methods=['GET'])
def contribution():
    return jsonify({"VM": "VM-2", "Contribution": "Data Processing"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
