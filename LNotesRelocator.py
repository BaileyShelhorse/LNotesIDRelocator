import psutil
import subprocess

# get system information
cpu_count = psutil.cpu_count()
cpu_freq = psutil.cpu_freq()
memory = psutil.virtual_memory()
disk_usage = psutil.disk_usage('/')

# print system information
print(f"CPU count: {cpu_count}")
print(f"CPU frequency: {cpu_freq.current:.1f} MHz")
print(f"Memory: {memory.total/(1024**2):.2f} MB")
print(f"Disk usage: {disk_usage.used/(1024**3):.2f} GB / {disk_usage.total/(1024**3):.2f} GB ({disk_usage.percent}%)")

# get process information
processes = []
for proc in psutil.process_iter(['pid', 'name', 'username']):
    try:
        pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
    except psutil.NoSuchProcess:
        pass
    else:
        processes.append(pinfo)

# print process information
print("\nRunning processes:")
for process in processes:
    print(f"PID: {process['pid']}, Name: {process['name']}, User: {process['username']}")

# Run the systeminfo command and capture its output
result = subprocess.run(['systeminfo'], capture_output=True, text=True)

# Print the output
print(result.stdout)

# Wait for user input before exiting
input("Press Enter to exit.")
