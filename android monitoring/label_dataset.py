import pandas as pd

INPUT_FILE = "device_monitor_log.csv"
OUTPUT_FILE = "labeled_device_data.csv"

def assign_label(row):
    cpu = row["CPU%"]
    ram = row["RAM_MB"]
    battery = row["Battery%"]

    if battery < 15:
        return "Low_Battery"
    elif ram > 500 and cpu > 70:
        return "Overloaded"
    elif ram > 500:
        return "High_RAM_Usage"
    elif cpu > 70:
        return "High_CPU_Usage"
    else:
        return "Normal"

def label_dataset():
    try:
        df = pd.read_csv(INPUT_FILE)
        df["Label"] = df.apply(assign_label, axis=1)
        df.to_csv(OUTPUT_FILE, index=False)
        print(f"✅ Labeled dataset saved as '{OUTPUT_FILE}'")
    except Exception as e:
        print(f"❌ Error processing file: {e}")

if __name__ == "__main__":
    label_dataset()
