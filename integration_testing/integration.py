import requests
import time

# Service URLs
CUSTOMER_SERVICE_URL = 'http://localhost:8000'
ORDER_SERVICE_URL = 'http://localhost:8080'

def test_customer_registration_and_order_placement():
    # Step 1: Register a new customer
    customer_data = {
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    response = requests.post(f"{CUSTOMER_SERVICE_URL}/register", json=customer_data)
    assert response.status_code == 200, f"Customer registration failed: {response.text}"
    print("Customer registered successfully")

    # Step 2: Retrieve the customer
    response = requests.get(f"{CUSTOMER_SERVICE_URL}/customers/{customer_data['name']}")
    assert response.status_code == 200, f"Failed to retrieve customer: {response.text}"
    customer = response.json()
    print("Customer retrieved successfully")

    # Step 3: Place an order
    order_data = {
        "customer_name": customer['name'],
        "coffee_details": "Latte, Large"
    }
    response = requests.post(f"{ORDER_SERVICE_URL}/order", json=order_data)
    assert response.status_code == 200, f"Order placement failed: {response.text}"
    order = response.json()
    print("Order placed successfully")
    print(f"Order ID: {order['order_id']}")

    print("Integration test passed successfully!")

if __name__ == "__main__":
    # Wait for services to be ready
    time.sleep(30)
    test_customer_registration_and_order_placement()
