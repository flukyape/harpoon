from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/python", methods=['POST'])
def process_data():
    data = request.get_json()
    transactions = data.get('event', {}).get('data', {}).get('block', {}).get('transactions', [])
    
    # Extracting smart contract addresses
    smart_contract_addresses = [tx['from']['address'] for tx in transactions if tx.get('createdContract')]

    print('Smart contract addresses:')
    print(smart_contract_addresses)

    return jsonify({"message": "Received", "smart_contract_addresses": smart_contract_addresses}), 200

if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(debug=True)  # run the server in debug mode