from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample in-memory storage
data_store = {}

# GET request to fetch data
@app.route('/items/<string:item_id>', methods=['GET'])
def get_item(item_id):
    item = data_store.get(item_id)
    if item:
        return jsonify({"item_id": item_id, "data": item}), 200
    return jsonify({"error": "Item not found"}), 404

# POST request to create data
@app.route('/items', methods=['POST'])
def create_item():
    item_data = request.json
    item_id = item_data.get("item_id")
    
    if not item_id:
        return jsonify({"error": "Item ID is required"}), 400
    
    data_store[item_id] = item_data.get("data", {})
    return jsonify({"message": "Item created", "item": data_store[item_id]}), 201

# PUT request to update data
@app.route('/items/<string:item_id>', methods=['PUT'])
def update_item(item_id):
    if item_id not in data_store:
        return jsonify({"error": "Item not found"}), 404

    item_data = request.json
    data_store[item_id] = item_data.get("data", {})
    return jsonify({"message": "Item updated", "item": data_store[item_id]}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
