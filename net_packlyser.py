import scapy.all as scapy
from scapy.all import get_if_list

def list_interfaces():
  """Prints available network interfaces"""
  print("Available interfaces:")
  for i, iface in enumerate(get_if_list()):
    print(f"{i+1}. {iface.name}")

def choose_interface():
  """Prompts user to select an interface and returns its name"""
  list_interfaces()
  while True:
    try:
      choice = int(input("Enter your choice (1-N): "))
      if 1 <= choice <= len(get_if_list()):
        return get_if_list()[choice-1].name
      else:
        print("Invalid choice. Please select a valid number.")
    except ValueError:
      print("Invalid input. Please enter a number.")

def capture_packets(interface, duration=None):
  """Captures packets for the specified duration (optional)"""
  try:
    print(f"Capturing packets on {interface}...")
    if duration:
      scapy.sniff(iface=interface, prn=lambda p: print(p.summary()), timeout=duration)
    else:
      scapy.sniff(iface=interface, prn=lambda p: print(p.summary()))
  except KeyboardInterrupt:
    print("Capture interrupted.")

if __name__ == "__main__":
  interface = choose_interface()
  duration = input("Enter capture duration (seconds, leave empty for continuous): ")
  try:
    duration = int(duration)
  except ValueError:
    duration = None
  capture_packets(interface, duration)
