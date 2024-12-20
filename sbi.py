import threading
import nmap
import tkinter as tk
from tkinter import ttk, messagebox

# Nmap functions
def setup_nmap():
    nmScan = nmap.PortScanner()
    return nmScan

def scan_ports(nmScan, ip_address, port_range):
    nmScan.scan(ip_address, port_range)
    results = []
    for host in nmScan.all_hosts():
        for proto in nmScan[host].all_protocols():
            lport = nmScan[host][proto].keys()
            for port in lport:
                state = nmScan[host][proto][port]['state']
                results.append((ip_address, port, state))
    return results

def run_scanner(base_url):
    nmScan = setup_nmap()
    print(f"Starting scan on {base_url}")
    results = scan_ports(nmScan, base_url, "1-1024")  # Example port range
    for result in results:
        print(f"IP: {result[0]}, Port: {result[1]}, State: {result[2]}")
    print("Scan completed.")
    return results

# Tkinter GUI setup
def start_scan():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a URL")
        return
    results = run_scanner(url)
    show_results(results)
    messagebox.showinfo("Scan Completed", "Vulnerability scan completed.")

def show_results(results):
    result_window = tk.Toplevel(root)
    result_window.title("Scan Results")
    result_window.geometry("400x300")
    text = tk.Text(result_window)
    text.pack(fill=tk.BOTH, expand=1)
    for result in results:
        text.insert(tk.END, f"IP: {result[0]}, Port: {result[1]}, State: {result[2]}\n")

root = tk.Tk()
root.title("Vulnerability Scanner")
root.geometry("400x300")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(frame, text="Enter URL or IP Address:").grid(row=0, column=0, pady=10)
url_entry = ttk.Entry(frame, width=40)
url_entry.grid(row=0, column=1, pady=10)

scan_button = ttk.Button(frame, text="Start Scan", command=start_scan)
scan_button.grid(row=1, column=0, columnspan=2, pady=20)

root.mainloop()
