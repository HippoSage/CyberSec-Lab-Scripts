print("Rogue Packet Watchdog is live. Monitoring network connections...\n")

while True:
    try:
        connections = psutil.net_connections(kind='inet')

        for conn in connections:
            laddr = conn.laddr if conn.laddr else ('', 0)
            raddr = conn.raddr if conn.raddr else ('', 0)
            proto = "TCP" if conn.type == socket.SOCK_STREAM else "UDP"

            remote_ip = raddr[0]
            remote_port = raddr[1]

            # Skip if there's no remote IP (local process)
            if not remote_ip or remote_ip in SAFE_IPS:
                continue

            ip_connection_count[remote_ip] += 1

            reason = None

            # Flag uncommon ports
            if remote_port not in SAFE_PORTS:
                reason = f"Unusual port: {remote_port}"

            # Flag IPs with high connection volume
            if ip_connection_count[remote_ip] > 10:
                reason = f"High connection count to {remote_ip}"

            # Only log once per reason
            if reason and (remote_ip, reason) not in logged_ips:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                geo = geo_lookup(remote_ip)

                print(f"[!] {timestamp} - Suspicious connection detected:")
                print(f"     Remote IP: {remote_ip} | Port: {remote_port} | Protocol: {proto}")
                print(f"     Reason: {reason}")
                print(f"     Geo: {geo}\n")

                with open(csv_file, mode='a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([timestamp, laddr[0], remote_ip, remote_port, proto, reason, geo])

                logged_ips.add((remote_ip, reason))

    except KeyboardInterrupt:
        print("\nStopping Rogue Packet Watchdog.")
        break
    except Exception as e:
        print(f"Error: {str(e)}")
