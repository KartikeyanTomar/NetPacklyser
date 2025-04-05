

# 🧠 NetPacklyser – Real-Time Network Packet Analyzer

NetPacklyser is a command-line tool built in Python to analyze network traffic in real-time using deep packet inspection (DPI). It allows users to inspect various protocols, monitor top talkers, and analyze detailed statistics about network activity.

---

## ✨ Features

- 📡 Live packet sniffing on selected network interfaces
- 🔍 Deep Packet Inspection (HTTP, DNS, FTP)
- 📊 Real-time traffic stats (packet count, size, rate)
- 🌐 Top IP talkers and port usage monitoring
- 🎯 Optional IP-based filtering
- 🖥️ Hostname resolution for improved readability
- 🧩 Lightweight, fast, and fully terminal-based

---

## 🛠️ Tech Stack

| Tool/Library | Description |
|--------------|-------------|
| Python 3.x | Core programming language |
| Scapy       | Packet sniffing and protocol parsing |
| Netifaces   | Interface detection |
| Socket      | Hostname resolution and IP filtering |
| Datetime    | Timestamping and rate calculation |
| Pyfiglet    | Banner rendering for terminal aesthetics |

---

## ⚙️ Installation

> Make sure Python 3.6+ is installed.

### 🔧 Step 1: Clone the Repository
```bash
git clone https://github.com/KartikeyanTomar/NetPacklyser.git
cd netpacklyser
```

### 📦 Step 2: Install Dependencies
Use pip to install the required Python libraries:

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not provided, manually install:

```bash
pip install scapy netifaces pyfiglet
```

> You might need to run as `sudo` for packet sniffing capabilities depending on your OS.

---

## 🚀 Usage

```bash
sudo python3 netpacklyser.py
```

### 💡 Options:

- Select the desired network interface from the list.
- Choose to filter packets by specific IP (optional).
- View real-time logs and packet-level insights in the terminal.

---

## 🧪 Example Output

```
[+] Sniffing on interface: wlan0
[+] Captured Packet #12 - Protocol: TCP
    Source: 192.168.1.5:443 -> Destination: 192.168.1.7:50544
    Payload: HTTP GET /index.html
    Host: www.example.com
```

---

## 🔐 Permissions

- Linux/macOS users: Run as **sudo** to allow raw socket access.
- Windows users: Run with administrator privileges.

---

## 🧩 Future Scope

- Add more protocols (SMTP, POP3, Telnet)
- Export results to CSV/JSON
- Build a GUI version using PyQt or Tkinter
- Alert system for suspicious traffic (e.g., port scanning)

---

## 🙌 Acknowledgments

Thanks to the open-source Python networking community and contributors of Scapy and Netifaces for making network programming accessible and powerful!

---

## 🧑‍💻 Author

**Kartikeyan Singh Tomar**  
Cybersecurity Researcher | Python Developer | 

```
