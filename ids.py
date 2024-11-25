import subprocess
import re

def start_snort(interface="eth0"):
    return subprocess.Popen(
        ["snort", "-i", interface, "-c", "/etc/snort/snort.conf", "-A", "console"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
def monitor_snort(snort_process):
    pattern = re.compile("ICMP")
    print("Monitoring for ICMP traffic alerts...")
    while True:
        line = snort_process.stdout.readline()
        if not line:
            break
        if pattern.search(line):
            print("Alert! Potential intrusion detected: ICMP packet identified.")
snort_process = start_snort()
monitor_snort(snort_process)
'''Steps to Resolve the Issue
Check if Snort is Installed: Make sure Snort is installed on your system. If it’s not installed, download and install it from the official Snort website.

Ensure Snort is Added to System PATH: If Snort is installed but you still face this issue, it’s likely that Snort's installation directory is not added to the system's PATH. Here's how you can check and fix it:

Go to System Properties → Advanced → Environment Variables.
Under System variables, find Path and click Edit.
Add the Snort installation directory to the Path. For example, if Snort is installed in C:\Snort, you should add C:\Snort\bin to the PATH.
After updating the PATH, close and reopen the command prompt or IDE (such as Visual Studio Code or PyCharm) to refresh the environment variables.'''
'''import subprocess
import re
def start_snort(interface="eth0"):
    print(f"Starting Snort on {interface}...")
    return subprocess.Popen(["snort", "-i", interface, "-c", "/etc/snort/snort.conf", "-A", "console"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
def monitor_snort(snort_process):
    pattern = re.compile("ICMP")
    print("Monitoring for ICMP traffic alerts...")
    while True:
        line = snort_process.stdout.readline()
        if not line:
            break
        if pattern.search(line):
            print("Alert! Potential intrusion detected: ICMP packet identified.")
snort_process = start_snort()
monitor_snort(snort_process)'''
