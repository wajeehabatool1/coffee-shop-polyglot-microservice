# coffee-shop-polyglot-microservice
![image](https://github.com/user-attachments/assets/f7f96881-eaa9-407f-9398-f704265c7972)

## Overview
Coffee Shop Polyglot Microservice is a project designed to showcase a microservices architecture built using **Python**, **Node.js**, and **GoLang**, containerized for scalable deployment. The project demonstrates the fundamentals of microservices, inter-service communication, and containerization while serving as a codebase to practice DevOps concepts or implement CI/CD pipelines.

This system simulates a coffee shop environment, where users can register, place orders, and receive notifications about their orders. The services are implemented in different languages to highlight the polyglot aspect of the architecture.

---
## User Interface of the Coffee Shop Application

![image](https://github.com/user-attachments/assets/34d804f8-e481-42b1-8aa7-d799d53b4986)

![image](https://github.com/user-attachments/assets/281e1b25-d6cd-4043-8e27-bc3a322819b7)


---
## Technologies Used
- **Python**: For the Customer Registration service.
- **Node.js**: For the Order Taking/Processing service.
- **GoLang**: For the Notification service.
- **MongoDB**: For data storage (customer and order data).
- **Docker**: For containerizing the services.
- **Docker Compose**: For service orchestration and networking.
---
## Service Interaction
1. **Customer Registration**:
   - A user registers their details via the Python-based Customer Registration service.
   - This service stores the customer data in **MongoDB** and confirms registration.

2. **Order Taking/Processing**:
   - A registered user places an order via the Node.js-based Order Processing service.
   - The order details are stored in **MongoDB**.
   - The service ensures inter-service communication by interacting with the Customer Registration and Notification service.

3. **Notification Service**:
   - The GoLang-based Notification service handles sending order notifications to users via email.
   - It receives order details from the Order Processing service and sends real-time email updates.

---
## Usage
To run the project:
1. clone the git repository
   ```bash
   git clone https://github.com/wajeehabatool1/coffee-shop-polyglot-microservice.git
   ```
2. navigate to coffee-shop-polyglot-microservice
   ```bash
   cd coffee-shop-polyglot-microservice
   ```
3. Make sure you have Docker and Docker Compose installed.
4. run the follwing docker-compose command
   ```bash
   docker-compose up
   ```
   **NOTE**: change the frontend env url  to localhost if you are running this project on local machine, but to run this project on cloud replace the the customer_service and order_service url in frontend enviroment variable to public ip of the  cloud compute instance
   





