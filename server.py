from flask import Flask, request, jsonify

app = Flask(__name__)
need_data = False

@app.route('/')
def home():
    return "Flask server is running."

@app.route('/trigger', methods=['POST'])
def trigger():
    global need_data
    need_data = True
    return "Trigger received."

@app.route('/need_data', methods=['GET'])
def need_data_status():
    return jsonify({'need': need_data})

@app.route('/upload', methods=['POST'])
def upload():
    global need_data
    need_data = False
    data = request.get_json()
    print("✅ Data received:", data)
    return "Data received."

# 副程式接口
def run():
    app.run(host='0.0.0.0', port=5000)
