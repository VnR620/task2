from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add():
    a = request.form.get('a', 0, type=float)
    b = request.form.get('b', 0, type=float)
    result = a + b
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)