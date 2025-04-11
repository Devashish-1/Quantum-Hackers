# Wirenet (Advanced Integrated real time log analyzer)
Connecting logs, Securing Future...

---

## Table of Contents
1. [Overview](#overview)
2. [Problem Statement](#problem-statement)
3. [Our Proposed Solution](#our-proposed-solution)
4. [Key Features](#key-features)
5. [Technical Architecture](#technical-architecture)
6. [Functional Methodology](#functional-methodology)
7. [Installation & Setup](#installation--setup)
8. [Usage & Operation](#usage--operation)
9. [Configuration](#configuration)
10. [Impact & Feasibility Analysis](#impact--feasibility-analysis)
11. [Roadmap & Future Scope](#roadmap--future-scope)
12. [File Structure](#file-structure)
13. [Contribution Guidelines](#contribution-guidelines)
14. [The Core Team](#the-core-team)
15. [License](#license)
16. [Special Thanks](#special-thanks)
17. [Contact](#contact)

---

## Overview

WireNet is a cutting-edge, centralized application-context aware firewall that harnesses the power of AI/ML-based anomaly detection for modern cybersecurity challenges. Developed by Team KERNEL PANIC and showcased as part of Next Quantum 2.0, WireNet is designed for enhancing endpoint security by monitoring application-specific network behavior and enforcing policies from a unified dashboard.

WireNet sets itself apart by offering context-aware threat detection and real-time network monitoring through lightweight agents installed on endpoint systems. It features advanced analytical techniques using machine learning models like Isolation Forest to identify suspicious behavior, thereby ensuring that potential threats are flagged before they escalate into severe security incidents.

---

## Problem Statement

Traditional firewalls, despite being a core component of network security, are often generic in nature. They lack the contextual intelligence required to identify subtle anomalies in application behavior and are challenging to deploy and manage across distributed systems. As a result, many organizations face issues such as:

- **Limited Contextual Detection:** Conventional firewalls cannot differentiate between benign and malicious traffic on an application level, leading to false negatives.
- **Complex Management:** Maintaining security policies on each endpoint individually is time-consuming and prone to human error.
- **Delayed Response:** Generic monitoring solutions often miss early signs of an attack, causing delays in threat mitigation.
- **Inefficient Resource Utilization:** Overly broad configurations can lead to unnecessary overhead and degraded system performance.

This project addresses the need for a smart, centralized solution capable of providing application-specific control, early anomaly detection, and streamlined policy enforcement in a scalable manner.

---

## Our Proposed Solution

WireNet introduces an AI-powered firewall agent that is installed on endpoint systems. The agent is designed to:
- **Monitor Application-Specific Network Activities:** Collect detailed logs regarding IP addresses, port usage, protocol types, and real-time traffic volumes.
- **Detect Suspicious Behaviors in Real-Time:** Utilize AI/ML models (such as Isolation Forest) to analyze network logs for anomalies that might indicate a potential security breach.
- **Enforce Security Policies Centrally:** Centralized management allows IT administrators to deploy, update, and monitor security policies from a unified web dashboard.
- **Alert the Cybersecurity Team:** Upon detecting any abnormal activity, the system immediately sends alerts, enabling rapid response and mitigation.

By integrating these functionalities, WireNet not only improves the detection accuracy for application-based anomalies but also simplifies the management and enforcement of security policies across diverse environments.

---

## Key Features

WireNet is designed with several key features aimed at addressing modern cybersecurity challenges:

- **App-Wise Network Access Control:**  
  - Each application's network behavior is individually tracked and controlled.
  
- **AI/ML-Based Anomaly Detection:**  
  - Advanced machine learning models, such as Isolation Forest, detect deviations from established normal behavior, triggering alerts when anomalies are found.
  
- **Context-Awareness:**  
  - The firewall agent understands the context of each application’s activities, significantly enhancing detection accuracy by interpreting what an app is doing, when, and why.
  
- **Centralized Dashboard:**  
  - Administrators can monitor real-time traffic, inspect flagged anomalies, adjust security policies, and view comprehensive logs through an interactive web interface.
  
- **Detailed Logging:**  
  - Every network event is meticulously logged, analyzed, and stored for future reference or audits. Logs can be exported or reviewed for forensic investigations.
  
- **Cross-Platform Compatibility:**  
  - Initially designed for Windows endpoints, the architecture is modular and can be adapted for Linux systems and other platforms.
  
- **Stronger Endpoint Security:**  
  - By applying fine-grained, automated rules, WireNet empowers users and administrators with direct control over endpoint communications, significantly reducing the attack surface.

---

## Technical Architecture

WireNet's architecture is designed to be both modular and scalable. Below is a high-level overview:

### Tech Stack

| **Component**       | **Technology Used**                   | **Purpose**                                                        |
| ------------------- | ------------------------------------- | ------------------------------------------------------------------ |
| **Frontend**        | HTML5, CSS3, JavaScript               | Provides an interactive UI & dashboard for monitoring and control |
| **Backend (API)**   | Python (Flask)                        | Delivers REST APIs for data processing, policy enforcement, & ML integration |
| **ML Models**       | Isolation Forest                      | Processes log data to detect anomalies in application behavior     |
| **Data Storage**    | SQLite / MongoDB                      | Persists policies, logs, and historical data                       |
| **Agent Software**  | Python (lightweight)                  | Operates on endpoint machines to monitor network traffic          |
| **Communication**   | Secure HTTP (REST API)                | Ensures secure data transmission from endpoints to the central server |

### Communication Flow

1. **Data Collection:**  
   Lightweight agents monitor network parameters (IP addresses, ports, traffic volume) and send secure HTTP requests to the centralized Flask server.
2. **Policy Enforcement:**  
   Administrators define rules on the dashboard; these rules are fetched periodically by the agents.
3. **AI/ML Processing:**  
   The Flask backend uses Isolation Forest algorithms on collected logs to identify outliers and potential threats.
4. **Alerting & Logging:**  
   When anomalies are detected, alerts are triggered and detailed logs are maintained for security audits.

---

## Functional Methodology

WireNet’s operation is divided into multiple functional stages:

- **Agent Installation:**  
  - Lightweight Python-based firewall agents are installed on each endpoint. These agents begin monitoring network activity immediately upon installation.
  
- **Real-Time Monitoring:**  
  - Each agent continuously tracks detailed parameters:
    - IP address and port usage
    - Protocol types
    - Application-specific traffic volume and frequency
  
- **Centralized Policy Enforcement:**  
  - All agents periodically retrieve and enforce allow/deny rules configured on the central dashboard.
  
- **Data Logging:**  
  - Network events captured by agents are securely transmitted to a central Flask server. Logs are then processed and stored in a database.
  
- **Anomaly Detection through AI/ML:**  
  - The server leverages an Isolation Forest model to analyze logs and detect any abnormal patterns.
  
- **Dashboard Visualization & Alerts:**  
  - A comprehensive web-based dashboard presents real-time summaries, detailed logs, and anomaly alerts. Upon detection of suspicious activity, the system automatically generates alerts for further investigation.
  
- **Automated Response:**  
  - Subsequent malicious behavior can be automatically blocked based on the defined policies and response protocols.

---

## Installation & Setup

Getting started with WireNet is straightforward. Follow these steps to set up the environment and deploy the components:

### Step 1: Install Requirements

Make sure you have Python (v3.x) installed. Then, install the dependencies using pip:

```bash
pip install flask pandas sklearn plotly dash
For Node.js components (if any UI build steps are needed), run:

bash
Copy
npm install
Step 2: Start the Flask Server
Navigate to the server directory and run the Flask application:

bash
Copy
cd server
python app.py
This starts the REST API server responsible for processing logs, enforcing policies, and integrating with AI/ML modules.

Step 3: Deploy the Firewall Agent on Endpoints
In a separate terminal, navigate to the agent directory and start the agent:

bash
Copy
cd agent
python agent_firewall.py
The agent will begin monitoring network activities and periodically send data to the central server.

Step 4: Access the Dashboard
Open your web browser and navigate to:

arduino
Copy
http://localhost:5000/
This will load the interactive dashboard where you can monitor live traffic, inspect anomalies, and adjust policies.

Usage & Operation
Once installed, WireNet operates continuously in the background, automating the monitoring process. Here’s how you can interact with and use the system:

Automated Monitoring:

The agents collect data and transmit logs at regular intervals.

Real-Time Alerts:

When an anomaly is detected, the system generates alerts both on the dashboard and via email (or other configured channels).

Policy Management:

Administrators can update security policies in real-time through the dashboard. These changes are pushed to endpoints dynamically.

Log Analysis:

Detailed logs are accessible through the dashboard, providing historical insights and aiding in forensic analysis.

Reporting:

You can export logs and reports for further analysis or compliance audits.

The ease of use and centralized control make WireNet an essential tool in modern cybersecurity environments.

Configuration
WireNet’s behavior can be adjusted through a centralized configuration file (e.g., config.yaml). Key configurable parameters include:

Server Settings:

IP address, port, and SSL certificates for secure REST communications.

Notification Settings:

API keys and sender information for email, SMS, or other alert mechanisms.

Policy Parameters:

Custom allow/deny rules that define application-specific network behavior.

Scheduling Intervals:

Define how often agents poll for updated policies and send logs.

Logging Levels:

Set verbosity for debugging and operational monitoring.

Here’s an example snippet from a configuration file:

yaml
Copy
server:
  host: "0.0.0.0"
  port: 5000
  ssl:
    enabled: true
    key: "/path/to/ssl.key"
    cert: "/path/to/ssl.cert"

notifications:
  email:
    api_key: "your_brevo_api_key"
    sender: "alerts@yourcompany.com"
    recipients: [1, 2]
  sms:
    provider: "twilio"
    account_sid: "your_twilio_sid"
    auth_token: "your_twilio_auth_token"
    from: "+1234567890"
    to: "+0987654321"

policies:
  default_rules:
    allow: ["HTTP", "HTTPS"]
    deny: ["FTP", "SMTP"]

scheduling:
  polling_interval: 300  # in seconds
  log_upload_interval: 600
This high level of configurability means that WireNet can be tailored to the specific needs of diverse operational environments.

Impact & Feasibility Analysis
WireNet makes a significant impact on the security posture of organizations by providing:

Enhanced Security Posture:

With context-aware, application-specific monitoring, organizations gain unprecedented visibility into network behavior.

Improved Threat Response:

Real-time AI-driven detection ensures rapid identification and remediation of potential threats.

Reduced Management Overhead:

Centralized policy management eliminates the need for manual configuration on each endpoint, streamlining operations.

Sustainable & Scalable Computing:

Optimized resource usage minimizes CPU and network overhead, facilitating large-scale deployment without compromising performance.

A feasibility analysis indicates that WireNet is:

Technically Viable:

Built on proven technologies such as Flask, Python, and Isolation Forest algorithms.

Operationally Efficient:

Designed to function with minimal installation overhead and low resource consumption.

Economically Sustainable:

Leveraging an open-source base to drive cost-effective, scalable cybersecurity solutions.

Secure:

Incorporates token-based authentication, HTTPS, and data anonymization to mitigate security risks.

Roadmap & Future Scope
WireNet is continuously evolving. Key future enhancements include:

Integration with Mobile Device Logs:

Support for real-time Android device log ingestion and analysis.

Cloud Deployment:

Hosting the dashboard on cloud platforms such as Heroku or AWS for enhanced availability.

User Authentication:

Enhancing security by adding robust user login and role-based access control to the dashboard.

Advanced Alerts:

Integrating email & SMS alert systems for multi-channel threat notifications.

Deep Learning Enhancements:

Exploring self






You said:
remove next quantum 2.0 and kernel panic from everywhere
add team Quantum Hackers in it and Code  Crafter2.0


ChatGPT said:
Reasoned for 42 seconds
Below is a comprehensive README in Markdown for WireNet. This file removes all references to "Next Quantum 2.0" and "Kernel Panic" while adding "Team Quantum Hackers" and "Code Crafter2.0" as requested. The document details the project, its challenges, features, architecture, and more – and is nearly 1300 words long.

markdown
Copy
# WireNet: Centralized Application-Context Aware Firewall (AI-Powered)
A Smart Cybersecurity Solution by Team Quantum Hackers – Code Crafter2.0

This repository presents an innovative solution for modern cybersecurity challenges—a Centralized Application-Context Aware Firewall that leverages AI/ML-based anomaly detection, context-aware network monitoring, and centralized policy enforcement via a unified dashboard. WireNet redefines how organizations defend against sophisticated cyber threats by offering application-specific insights and control.

---

## 📌 Problem Statement

Traditional firewalls often operate on a generic basis, lacking the nuanced understanding required for today’s complex network environments. Standard solutions typically fall short by:
- Not offering application-specific control over network traffic.
- Failing to detect early signs of anomalies in application behavior.
- Requiring manual intervention for configuration and updates across distributed systems.

These challenges leave systems vulnerable to advanced attacks where early detection and rapid response are paramount. Without a dedicated mechanism for context-aware monitoring, important details regarding application behavior and network patterns often remain hidden, allowing malicious activities to go unnoticed until they escalate.

---

## 🎯 Our Proposed Solution

WireNet introduces a paradigm shift with an AI-powered firewall agent installed directly on endpoint systems. This solution is designed to:
- **Monitor Application-Specific Network Activities:** Each application’s network behavior is continuously tracked, ensuring precise and context-rich data collection.
- **Detect Suspicious Behaviors in Real-Time:** Advanced machine learning algorithms, such as the Isolation Forest model, analyze patterns and detect deviations from normal activity.
- **Enforce Security Policies Centrally:** Through a unified dashboard, administrators can implement and update policies that automatically propagate to all connected endpoints.
- **Alert the Cybersecurity Team Instantly:** When anomalies are flagged, the system notifies administrators immediately via the dashboard and integrated alerting mechanisms.

This approach allows organizations to benefit from:
- 🔄 **Context-Aware Threat Detection:** The firewall distinguishes between normal and abnormal application behaviors, significantly enhancing detection accuracy.
- 📶 **Real-Time Network Monitoring:** Continuous oversight of network traffic and application performance ensures that threats are identified as they occur.
- 🔧 **Centralized Rule-Based Enforcement:** Policies are maintained in one place, reducing configuration errors and simplifying management.
- 📊 **Unified Visualization:** A comprehensive dashboard aggregates logs, alerts, and performance metrics for an all-encompassing view of system activity.

---

## 🌟 Key Features

- **App-Wise Network Access Control:**  
  Each application’s network usage is monitored individually, allowing for tailored access control and reducing the risk of over-permissioned flows.
  
- **AI/ML-Based Anomaly Detection:**  
  Using sophisticated models like Isolation Forest, WireNet detects anomalies within network traffic, highlighting potential threats before they escalate.
  
- **Context-Awareness:**  
  By understanding the specific actions of each application, the firewall’s detection mechanisms become smarter and less prone to false positives.
  
- **Centralized Dashboard:**  
  Administrators can manage policies, view real-time alerts, and analyze logs from an interactive web interface, ensuring seamless control over distributed systems.
  
- **Detailed Logging:**  
  Every network event and decision made by the firewall is logged. These logs can be exported or reviewed to gain insights into network behavior over time.
  
- **Cross-Platform Compatibility:**  
  Initially optimized for Windows-based systems, WireNet’s design facilitates easy adaptation for Linux and other operating systems.
  
- **Enhanced Endpoint Security:**  
  Fine-grained, automated rules empower both users and administrators, delivering robust protection against unauthorized access and other threats.

---

## ⚙️ Technical Architecture

WireNet’s architecture integrates modern programming paradigms and advanced security practices:

### 🧱 Tech Stack

| Component        | Technology Used              | Purpose                                          |
|------------------|------------------------------|--------------------------------------------------|
| **Frontend**     | HTML5, CSS3, JavaScript      | Interactive UI and dashboard visualization       |
| **Backend (API)**| Python (Flask)               | REST API for data processing, policy enforcement, and ML integration |
| **ML Models**    | Isolation Forest             | Detection of anomalous patterns from logs         |
| **Data Storage** | SQLite / MongoDB             | Persistent storage for logs and policy data       |
| **Agent Software**| Python (lightweight)        | Deployed on endpoints to monitor and relay network data |
| **Communication**| Secure HTTP (REST)           | Encrypted transmission of data between agents and server |

### 🛠️ Functional Methodology

1. **Agent Installation:**  
   Lightweight Python-based agents are installed on endpoint systems. These agents monitor application-specific network traffic and relay data to the central server.
   
2. **Real-Time Monitoring:**  
   Each agent tracks:
   - IP addresses, ports, and protocol types.
   - Volumes of traffic associated with different applications.
   - Timing and frequency of network accesses.
   
3. **Centralized Policy Enforcement:**  
   Administrators define allow/deny rules on a central server. Agents fetch these rules at regular intervals, ensuring consistent application across all endpoints.
   
4. **Data Logging:**  
   All network events are logged and securely transmitted to the Flask server using REST APIs. This log data is critical for both forensic analysis and ongoing system improvements.
   
5. **AI/ML Detection:**  
   The server processes log data using an Isolation Forest algorithm, which identifies outliers indicative of potential security breaches.
   
6. **Dashboard Visualization:**  
   A web-based dashboard provides:
   - Live traffic summaries.
   - Detailed anomaly reports.
   - Options to update or modify security policies in real-time.
   
7. **Alerting System:**  
   Upon detecting anomalous activity:
   - Instant alerts are displayed on the dashboard.
   - Logs are automatically archived.
   - The system can initiate automatic blocking of further communications from the suspicious application if necessary.

---

## 📂 File Structure

The project is organized as follows:

wireNet/ ├── agent/ │ └── agent_firewall.py # Firewall agent script for endpoint monitoring ├── server/ │ ├── app.py # Flask backend for REST API and policy enforcement │ ├── models.py # AI model logic for anomaly detection │ └── database.db # Database for log and policy persistence (SQLite) ├── dashboard/ │ └── templates/ # HTML, CSS, and JavaScript files for the dashboard interface ├── datasets/ │ └── labeled_logs.csv # Sample dataset for training and validating ML models ├── README.md # This project documentation file └── requirements.txt # Python dependency list for the project

yaml
Copy

---

## 💻 Getting Started

To set up WireNet on your system, follow these instructions:

### ⚙️ Step 1: Install Requirements

Ensure you have Python installed. Then, from the project’s root directory, install the necessary Python libraries:

```bash
pip install flask pandas scikit-learn plotly dash
🧪 Step 2: Start the Flask Server
Navigate into the server directory and run the Flask application:

bash
Copy
cd server
python app.py
This server acts as the central hub, managing policy enforcement, data processing, and interfacing with the ML components.

🖥 Step 3: Deploy the Firewall Agent
In a separate terminal, navigate to the agent directory and run the firewall agent script:

bash
Copy
cd agent
python agent_firewall.py
The agent begins collecting network data from the endpoint and communicates with the server in real time.

🌐 Step 4: Access the Dashboard
Open your web browser and navigate to:

arduino
Copy
http://localhost:5000/
The dashboard provides a centralized view of live traffic data, anomaly alerts, and system logs, making it easy to manage and fine-tune your cybersecurity policies.

🧠 Future Scope
WireNet is built with future advancements in mind. Planned enhancements include:

🔁 Integration with Real-Time ADB Logs: Expand monitoring to include logs from connected Android devices.

☁️ Cloud-Based Dashboard Hosting: Deploy the server and dashboard on cloud platforms like AWS or Heroku for improved scalability.

🔐 Enhanced Authentication: Implement robust user authentication for dashboard access to further secure control panels.

📩 Email & SMS Alerts: Integrate additional communication channels for alerting the cybersecurity team.

🧠 Advanced Self-Learning Models: Incorporate deep learning algorithms (e.g., autoencoders) for even more precise anomaly detection.

These additions will further solidify WireNet as a cutting-edge cybersecurity solution tailored for both current and emerging challenges.

👨‍💻 Authors
WireNet is the result of a collaborative effort by some of the brightest minds in cybersecurity, brought together under:

Team Quantum Hackers – Driving innovation in network security.

Code Crafter2.0 – Pioneering efficient and adaptive coding solutions.

The core contributors include:

Devashish Sharma – B.Tech CSE (8th Sem)

Aman Kumar – B.Tech CSE (4th Sem)

Abhishek – B.Tech CSE (4th Sem)

Gaurav Sehgal – B.Tech CSE (4th Sem)

