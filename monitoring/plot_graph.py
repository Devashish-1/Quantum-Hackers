import pandas as pd
import matplotlib.pyplot as plt

LOG_FILE = "logs/system_log.csv"

def plot_graph():
    df = pd.read_csv(LOG_FILE, parse_dates=['Timestamp'])

    plt.figure(figsize=(12, 8))

    # CPU Usage
    plt.subplot(2, 2, 1)
    plt.plot(df['Timestamp'], df['CPU%'], label='CPU%', color='blue')
    plt.xlabel('Time')
    plt.ylabel('CPU Usage (%)')
    plt.title('CPU Usage Over Time')
    plt.xticks(rotation=45)
    plt.grid()

    # Memory Usage
    plt.subplot(2, 2, 2)
    plt.plot(df['Timestamp'], df['Memory%'], label='Memory%', color='green')
    plt.xlabel('Time')
    plt.ylabel('Memory Usage (%)')
    plt.title('Memory Usage Over Time')
    plt.xticks(rotation=45)
    plt.grid()

    # Disk Usage
    plt.subplot(2, 2, 3)
    plt.plot(df['Timestamp'], df['Disk%'], label='Disk%', color='orange')
    plt.xlabel('Time')
    plt.ylabel('Disk Usage (%)')
    plt.title('Disk Usage Over Time')
    plt.xticks(rotation=45)
    plt.grid()

    # Network Usage (Sent/Received)
    plt.subplot(2, 2, 4)
    plt.plot(df['Timestamp'], df['Bytes_Sent(KB)'], label='Sent KB', color='purple')
    plt.plot(df['Timestamp'], df['Bytes_Recv(KB)'], label='Received KB', color='red')
    plt.xlabel('Time')
    plt.ylabel('Network Usage (KB)')
    plt.title('Network Usage Over Time')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_graph()
