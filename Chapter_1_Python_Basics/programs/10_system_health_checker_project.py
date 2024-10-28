# system_health_checker.py
# This script checks system resource usage (CPU, memory, and disk)
# and prints a warning if any resource exceeds a set threshold.

# Define current usage values (simulated)
cpu_usage = 65
memory_usage = 70
disk_usage = 80

# Define threshold limits
cpu_threshold = 75
memory_threshold = 75
disk_threshold = 85

# Check CPU usage
if cpu_usage > cpu_threshold:
    print("Warning: High CPU usage!")
else:
    print("CPU usage is normal.")

# Check memory usage
if memory_usage > memory_threshold:
    print("Warning: High Memory usage!")
else:
    print("Memory usage is normal.")

# Check disk usage
if disk_usage > disk_threshold:
    print("Warning: High Disk usage!")
else:
    print("Disk usage is normal.")

# Explanation:
# - The script checks three system resources (CPU, memory, and disk).
# - It compares each resource’s usage against a predefined threshold.
# - If any usage exceeds the threshold, a warning message is displayed.
# - Otherwise, it reports that the usage is normal.
# This project will help reinforce your understanding of variables, conditionals, and basic output statements.
