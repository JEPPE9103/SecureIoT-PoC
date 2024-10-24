SecureIoT PoC
Project Overview
SecureIoT PoC (Proof of Concept) demonstrates a secure and robust IoT solution. The project simulates an IoT environment where a sensor device sends data to a backend system using Docker containers. This setup is designed to be easily deployable, secure, and compliant with key aspects of the Cyber Resilience Act (CRA).

Components:
Sensor Device (Docker Container): Simulates a device that generates and sends sensor data.
InfluxDB (Database): Stores the sensor data received from the sensor device.
Grafana (Visualization): Visualizes the data from InfluxDB in real-time dashboards.
Docker Compose (Infrastructure): Manages the setup and connections between all components.
Features
Data Generation & Storage: Simulates sensor data and stores it in a time-series database.
Real-time Visualization: Displays data in a user-friendly Grafana dashboard.
Security: Incorporates Docker containerization and enables secure communication.
System Architecture
The system architecture comprises four main components:

Sensor Device (Python Script): Generates and sends temperature data to InfluxDB via HTTP POST requests.
InfluxDB: A time-series database to store the incoming sensor data.
Grafana: Retrieves data from InfluxDB and presents it visually in real-time dashboards.
Docker Compose: Simplifies deployment by orchestrating all components to run together seamlessly.
Refer to the System Specification PDF for more details.

Getting Started
Prerequisites
Docker and Docker Compose installed on your system.
Clone the repository:
bash
Kopiera kod
git clone https://github.com/JEPPER9103/SecureIoT-PoC.git
cd SecureIoT-PoC
Setup & Installation
Clone the Repository:

bash
Kopiera kod
git clone https://github.com/JEPPER9103/SecureIoT-PoC.git
cd SecureIoT-PoC
Run Docker Compose:

bash
Kopiera kod
docker-compose up -d
Access Grafana: Open a web browser and go to http://localhost:3000. Login with:

Username: admin
Password: admin (can be changed)
View Sensor Data: Create a new dashboard in Grafana and configure it to show data from InfluxDB.

Project Files
iot_client.py: Python script for the simulated sensor device.
docker-compose.yml: Configuration file to deploy the system using Docker.
Dockerfile: Builds the Docker image for the sensor device.
Secure_IoT_Solution_Specification.pdf: Detailed system architecture and CRA compliance explanation.
screenshots/: Contains images showing the working setup.
Security Measures
Container Isolation: Each component runs in its own Docker container to enhance security.
HTTPS and Authentication: Enables the use of TLS certificates for secure data transfer (recommended for production).
User Authentication: Grafana and InfluxDB require login credentials to access and configure the system.
Future Improvements
TLS Encryption: Secure communication by implementing HTTPS for data transmission.
Multi-Sensor Support: Expand the system to simulate and handle multiple sensors.
Advanced Dashboards: Create more complex visualizations for real-time analysis.
Cyber Resilience Act (CRA) Compliance
Security-by-Design: All components are isolated and can communicate securely within an internal network.
Update Mechanism: Each component can be updated independently through Docker, ensuring system security without downtime.
Vulnerability Management: The system can quickly adapt and redeploy updated containers when vulnerabilities are discovered.
Screenshots
Include relevant screenshots showing the working system setup and dashboards:

Grafana Dashboard - Real-time data visualization
InfluxDB Setup - Data storage configuration
Docker Status - Running containers
Author
Developed by Jesper Persson.

License
This project is licensed under the MIT License.
