import sys
import pyshark

# Default packet count
packet_count = 10

# Read packet count from dashboard
if len(sys.argv) > 1:
    try:
        packet_count = int(sys.argv[1])
    except ValueError:
        packet_count = 10

print("Starting packet capture...")
print(f"Capturing {packet_count} packets on any...")

capture = pyshark.LiveCapture(
    interface="any",
    output_file="capture.pcap"
)

capture.sniff(packet_count=packet_count)

print(f"{packet_count} packets captured successfully.")
print("Capture saved as: capture.pcap")
