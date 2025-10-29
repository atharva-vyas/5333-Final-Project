#!/bin/bash
set -e

# Function to log messages
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Wait for system to be ready
log "Waiting for system initialization..."
sleep 3

# Check if config file exists
if [[ ! -f /etc/wireguard/wg0.conf ]]; then
    log "ERROR: WireGuard config file not found at /etc/wireguard/wg0.conf"
	exit 1
fi

# Fix file permissions
chmod 600 /etc/wireguard/wg0.conf

# Check if WireGuard is already running
if wg show wg0 >/dev/null 2>&1; then
    log "WireGuard interface wg0 already exists, bringing it down first..."
	wg-quick down wg0 || true
fi

# Start WireGuard
log "Starting WireGuard interface..."
wg-quick up /etc/wireguard/wg0.conf

log "WireGuard started successfully"

# Keep the container running - this is crucial!
log "WireGuard is running. Keeping container alive..."
while true; do
    if ! wg show wg0 >/dev/null 2>&1; then
	    log "ERROR: WireGuard interface down, exiting..."
	    exit 1
    fi
    sleep 30
done
