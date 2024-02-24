# import scapy.all as scapy
# from scapy.all import get_if_list

# def list_interfaces():
#   """Prints available network interfaces"""
#   print("Available interfaces:")
#   for i, iface in enumerate(get_if_list()):
#     print(f"{i+1}. {iface.name}")

# def choose_interface():
#   """Prompts user to select an interface and returns its name"""
#   list_interfaces()
#   while True:
#     try:
#       choice = int(input("Enter your choice (1-N): "))
#       if 1 <= choice <= len(get_if_list()):
#         return get_if_list()[choice-1].name
#       else:
#         print("Invalid choice. Please select a valid number.")
#     except ValueError:
#       print("Invalid input. Please enter a number.")

# def capture_packets(interface, duration=None):
#   """Captures packets for the specified duration (optional)"""
#   try:
#     print(f"Capturing packets on {interface}...")
#     if duration:
#       scapy.sniff(iface=interface, prn=lambda p: print(p.summary()), timeout=duration)
#     else:
#       scapy.sniff(iface=interface, prn=lambda p: print(p.summary()))
#   except KeyboardInterrupt:
#     print("Capture interrupted.")

# if __name__ == "__main__":
#   interface = choose_interface()
#   duration = input("Enter capture duration (seconds, leave empty for continuous): ")
#   try:
#     duration = int(duration)
#   except ValueError:
#     duration = None
#   capture_packets(interface, duration)


import scapy.all as scapy
import netifaces

def get_interface_names():
    interfaces = netifaces.interfaces()
    return interfaces

def print_available_interfaces(interfaces):
    print("Available interfaces:")
    for i, interface in enumerate(interfaces, start=1):
        print(f"{i}. {interface}")

def packet_callback(packet):
    if packet.haslayer(scapy.IP):
        ip_src = packet[scapy.IP].src
        ip_dst = packet[scapy.IP].dst
        protocol = packet[scapy.IP].proto

        print(f"\nPacket: {ip_src} -> {ip_dst}, Protocol: {protocol}")

        if packet.haslayer(scapy.TCP):
            src_port = packet[scapy.TCP].sport
            dst_port = packet[scapy.TCP].dport
            print(f"TCP Port: {src_port} -> {dst_port}")

        elif packet.haslayer(scapy.UDP):
            src_port = packet[scapy.UDP].sport
            dst_port = packet[scapy.UDP].dport
            print(f"UDP Port: {src_port} -> {dst_port}")

# Get a list of available network interfaces
interfaces = get_interface_names()

# Print available interfaces
print_available_interfaces(interfaces)

# Prompt the user to select a network interface
try:
    selected_interface_index = int(input("Enter the number of the interface to capture packets: "))
    selected_interface = interfaces[selected_interface_index - 1]
except (ValueError, IndexError):
    print("Invalid input. Please enter a valid interface number.")
    exit(1)

print(f"\nSelected interface: {selected_interface}")

# Start sniffing packets on the selected interface and apply the callback function
scapy.sniff(iface=selected_interface, store=False, prn=packet_callback)
