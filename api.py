from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/device-status', methods=['GET'])
def device_status():
    return jsonify({"status": "Device is ready for migration", "code": 200})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
