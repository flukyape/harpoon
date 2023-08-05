from flask import Flask, request
app = Flask(__name__)

@app.route("/api/python", methods=['POST'])
def hello_world():
    data = request.get_json()
    print('data is here')
    print(data.event)

    return {"message": "Received"}, 200

if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(debug=True)  # run the server in debug mode