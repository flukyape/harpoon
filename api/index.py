from flask import Flask, request, jsonify

app = Flask(__name__)

def find_hits(data):
    result = []
    transactions = data['block']['transactions']
    for transaction in transactions:
        created_contract = transaction.get('createdContract')
        if created_contract is not None:
            from_address = transaction['from']['address']
            contract_address = created_contract['address']
            result.append({
                'from_address': from_address,
                'contract_address': contract_address
            })
    return result

@app.route('/find_hits', methods=['POST'])
def find_hits_endpoint():
    data = request.json
    hits = find_hits(data)
    
    if not hits:
        message = "There's nothing in this block"
        print(message)
        return jsonify(message=message), 200

    response_message = f"{len(hits)} number of smart contracts"
    print(response_message)
    print('Contracts:', hits)
    response = {
        'message': response_message,
        'contracts': hits
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)