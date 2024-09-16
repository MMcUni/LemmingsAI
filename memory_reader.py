import pymem
import time
import psutil

class LemmingsMemoryReader:
    def __init__(self):
        self.pm = None
        self.base_address = None
        self.process_name = "LEMMINGS.EXE"
        self.important_addresses = [
            0x461360, 0x461364, 0x461368, 0x46136c, 0x461370,
            0x461420, 0x461424, 0x461428, 0x46142c, 0x4614ec,
            0x4157B0, 0x2E30DD4
        ]

    def find_lemmings_process(self):
        for proc in psutil.process_iter(['name']):
            if proc.info['name'].lower() == self.process_name.lower():
                return proc.pid
        return None

    def connect(self):
        pid = self.find_lemmings_process()
        if pid:
            try:
                self.pm = pymem.Pymem(pid)
                self.base_address = self.pm.base_address
                print(f"Connected to Lemmings process (PID: {pid})")
                return True
            except pymem.exception.CouldNotOpenProcess:
                print(f"Found Lemmings process, but couldn't open it. Try running the script as administrator.")
                return False
        else:
            print(f"Couldn't find {self.process_name}. Is the game running?")
            return False

    def read_memory(self):
        results = {}
        for address in self.important_addresses:
            try:
                value = self.pm.read_int(address)
                results[hex(address)] = value
            except Exception as e:
                results[hex(address)] = f"Error: {str(e)}"
        return results

    def write_memory(self, address, value):
        try:
            self.pm.write_int(address, value)
            return True
        except Exception as e:
            print(f"Error writing to address {hex(address)}: {str(e)}")
            return False

# Usage
reader = LemmingsMemoryReader()

while not reader.connect():
    print("Waiting for Lemmings to start...")
    time.sleep(5)  # Wait 5 seconds before trying again

print("Starting to monitor Lemmings memory...")
prev_results = None

try:
    while True:
        results = reader.read_memory()
        
        if results != prev_results:
            print("\nGame state changed:")
            for address, value in results.items():
                if prev_results is None or value != prev_results.get(address):
                    print(f"Address: {address}, Value: {value}")
            prev_results = results.copy()
        
        time.sleep(0.5)  # Update every half second
except KeyboardInterrupt:
    print("\nStopping memory reader.")