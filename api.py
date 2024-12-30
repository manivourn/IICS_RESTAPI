from flask import Flask, jsonify
from faker import Faker

app = Flask(__name__)
fake = Faker()

# Test route returning JSON
@app.route('/')
def hello_world():
    return jsonify({"message": "neang ban sok hz"})

# Get a list of fake products
@app.route('/api/products')
def get_products():
    products = []
    for _ in range(50):  
        product = {
            "id": fake.uuid4(),
            "name": fake.company(),
            "description": fake.text(max_nb_chars=100),
            "price": round(fake.random_number(digits=2) + fake.random.random(), 2),
            "category": fake.word()
        }
        products.append(product)
    
    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Explicitly define the port here
