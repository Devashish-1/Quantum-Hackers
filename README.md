# WireNet: Centralized Application-Context Aware Firewall (AI-Powered)
A Smart Cybersecurity Solution by Team Quantum Hackers – Code Crafter2.0

This repository presents an innovative solution for modern cybersecurity challenges—a Centralized Application-Context Aware Firewall that leverages AI/ML-based anomaly detection, context-aware network monitoring, and centralized policy enforcement via a unified dashboard. WireNet redefines how organizations defend against sophisticated cyber threats by offering application-specific insights and granular control.

---

## 📌 Problem Statement

Traditional firewalls often operate on a generic basis, lacking the nuanced understanding required for today’s complex network environments. Standard solutions typically fall short by:
- Not offering application-specific control over network traffic.
- Failing to detect early signs of anomalies in application behavior.
- Requiring manual intervention for configuration and updates across distributed systems.

These limitations render networks vulnerable to advanced attacks—when early detection and rapid response are crucial. Without dedicated, context-aware monitoring, critical details about application behavior and network patterns remain obscured, allowing malicious activity to go unnoticed until significant damage occurs.

---

## 🎯 Our Proposed Solution

WireNet introduces a paradigm shift with an AI-powered firewall agent installed directly on endpoint systems. This solution is designed to:

- **Monitor Application-Specific Network Activities:**  
  Continuously tracking each application’s network behavior to gather rich, context-aware data.
  
- **Detect Suspicious Behaviors in Real-Time:**  
  Leveraging advanced machine learning algorithms (e.g., Isolation Forest) to analyze data and detect deviations from established patterns.
  
- **Enforce Security Policies Centrally:**  
  Using a unified dashboard, administrators can implement and update policies that automatically propagate to all endpoints.
  
- **Alert the Cybersecurity Team Instantly:**  
  Anomalies trigger immediate alerts on the dashboard and via integrated communication channels, ensuring rapid incident response.

This approach enables organizations to benefit from:
- 🔄 **Context-Aware Threat Detection:** Sophisticated mechanisms differentiate between normal and abnormal application behaviors.
- 📶 **Real-Time Monitoring:** Continuous oversight of network activity allows potential threats to be identified as they occur.
- 🔧 **Centralized Rule Enforcement:** Unified configuration reduces human error and simplifies network management.
- 📊 **Comprehensive Visualization:** Aggregated logs, alerts, and performance metrics are available in a single interactive dashboard.

---

## 🌟 Key Features

- **App-Wise Network Access Control:**  
  Each application's network usage is individually monitored, allowing for precise access control and reducing the risk of excessive permissions.
  
- **AI/ML-Based Anomaly Detection:**  
  Advanced models like Isolation Forest automatically identify outliers and deviations indicative of potential threats.
  
- **Context-Awareness:**  
  The system understands what each application is doing, when, and why—leading to fewer false alarms and more accurate threat detections.
  
- **Centralized Dashboard:**  
  An intuitive web interface provides real-time monitoring, historical log access, and policy management capabilities.
  
- **Detailed Logging:**  
  Every event and decision is recorded, ensuring traceability and facilitating forensic analysis.
  
- **Cross-Platform Compatibility:**  
  Although optimized for Windows initially, WireNet can be adapted for Linux-based systems and beyond.
  
- **Enhanced Endpoint Security:**  
  Fine-tuned, automated rules empower users and administrators to maintain tight control over network traffic.

---

## ⚙️ Technical Architecture

WireNet leverages modern programming paradigms and state-of-the-art security practices to deliver a robust and scalable solution.

### 🧱 Tech Stack

| Component           | Technology Used             | Purpose                                                  |
|---------------------|-----------------------------|----------------------------------------------------------|
| **Frontend**        | HTML5, CSS3, JavaScript     | Interactive UI and dashboard visualization               |
| **Backend (API)**   | Python (Flask)              | REST API for data processing, policy enforcement, and AI/ML integration |
| **ML Models**       | Isolation Forest            | Anomaly detection from logs and network patterns            |
| **Data Storage**    | SQLite / MongoDB            | Persistence storage for logs and policy data             |
| **Agent Software**  | Python (lightweight)        | Deployed on endpoints to monitor application-specific traffic |
| **Communication**   | Secure HTTP (REST)          | Encrypted data transmission between agents and the server    |

### 🛠️ Functional Methodology

1. **Agent Installation:**  
   Lightweight Python agents are deployed on each endpoint to track network activity with application-specific insights.
   
2. **Real-Time Monitoring:**  
   Agents capture details including IP addresses, ports, protocols, traffic volume per application, and timing of network events.
   
3. **Centralized Policy Enforcement:**  
   Administrators define comprehensive allow/deny rules on a centralized server. Agents periodically synchronize with this server to maintain consistent policy application.
   
4. **Data Logging:**  
   All monitored network activities are logged and sent securely to the central Flask server for real-time analysis and historical review.
   
5. **AI/ML Detection:**  
   The central server processes received log data using an Isolation Forest algorithm, detecting anomalies and potential security threats.
   
6. **Dashboard Visualization:**  
   A web-based dashboard offers live traffic summaries, detailed anomaly reports, and real-time policy management capabilities.
   
7. **Alerting System:**  
   When an anomaly is detected:
   - Immediate alerts are displayed on the dashboard.
   - Incident logs are archived for subsequent analysis.
   - Automatic blocks may be initiated for suspicious network traffic.

---

## 🔌 Hardware Requirements

In addition to the software components, WireNet employs specialized hardware to enhance its monitoring and enforcement capabilities. The hardware components include:

- **WiFi Deauthor Hardware:**  
  Utilized to simulate deauthentication attacks to test the firewall’s resilience. Typical setups may include ESP8266-based boards equipped with WiFi deauthorization tools for controlled experiments.
  
- **Bluetooth Jammer:**  
  A dedicated hardware module employed to simulate and analyze interference in Bluetooth communications. This assists in evaluating how well the system copes with wireless disruptions and unauthorized Bluetooth communications.
  
- **ESP32 Marouder:**  
  A versatile microcontroller used to gather and relay network data across endpoints. This device aids in real-time monitoring and serves as a bridge between multiple hardware components and the central server.

These devices are selected for their cost-effectiveness, power efficiency, and ease of integration with the WireNet environment. Proper calibration and secure handling of these components are essential for ensuring that experimental setups do not unintentionally impact legitimate network operations.

---

## 📂 File Structure

The project is organized in a structured manner to promote modularity and ease of management:

wireNet/ ├── agent/ │ └── agent_firewall.py # Endpoint agent script for network monitoring ├── server/ │ ├── app.py # Flask backend for REST API and policy enforcement │ ├── models.py # AI/ML model logic for anomaly detection │ └── database.db # Database for logging and policy persistence (SQLite) ├── dashboard/ │ └── templates/ # HTML, CSS, and JS files for the dashboard interface ├── datasets/ │ └── labeled_logs.csv # Labeled dataset for training the ML models ├── README.md # Project documentation (this file) └── requirements.txt # Python dependencies list for the project

yaml
Copy

---

## 💻 Getting Started

To set up WireNet on your system, follow these steps:

### ⚙️ Step 1: Install Requirements

Ensure you have Python installed. From the project’s root directory, install the necessary Python libraries:

```bash
pip install flask pandas scikit-learn plotly dash
🧪 Step 2: Start the Flask Server
Navigate into the server directory and run the Flask application:

bash
Copy
cd server
python app.py
This server acts as the central hub for policy enforcement, data processing, and AI/ML integration.

🖥 Step 3: Deploy the Firewall Agent
Open a new terminal, navigate to the agent directory, and execute the firewall agent script:

bash
Copy
cd agent
python agent_firewall.py
The agent begins monitoring network activity on the endpoint and transmits data to the server.

🌐 Step 4: Access the Dashboard
Launch your web browser and access the dashboard at:

arduino
Copy
http://localhost:5000/
The dashboard provides a centralized view of live traffic, anomaly alerts, and logs, empowering administrators to manage network security effectively.

🧠 Future Scope
WireNet is designed with scalability and future advancements in mind. Planned enhancements include:

🔁 Integration with Real-Time ADB Logs:
Extend monitoring capabilities to include logs from connected Android devices.

☁️ Cloud-Based Dashboard Hosting:
Deploy the server and dashboard on cloud platforms such as AWS or Heroku to enhance scalability.

🔐 Enhanced User Authentication:
Implement robust authentication mechanisms to secure dashboard access.

📩 Additional Alerting Channels:
Integrate email and SMS alerts to complement existing notification systems.

🧠 Advanced Self-Learning Models:
Research and implement deep learning techniques (e.g., autoencoders) for more precise anomaly detection.

These future enhancements aim to further fortify WireNet as a cutting-edge, adaptive cybersecurity solution.

## 👨‍💻 Authors
WireNet is a collaborative effort by a group of passionate cybersecurity innovators brought together under:

Team Quantum Hackers – Driving innovation in network security.

Code Crafter2.0 – Pioneering efficient and adaptive coding solutions.

The core contributors include:

Devashish Sharma 

Subhampreet Singh

Priyanka Janjua

Pratiksha Thakur


📬 Contact
For further information, inquiries, or collaboration opportunities, please reach out:

## Email: devashishsharma5000@gmail.com

Location: India
