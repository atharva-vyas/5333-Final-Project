FROM ghcr.io/blakeblackshear/frigate:stable

# Install WireGuard and required tools
RUN apt update && \
    apt install -y iproute2 wireguard-tools vim && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*

# Create entrypoint script to start WireGuard then Frigate
RUN echo '#!/bin/bash\n\
set -e\n\
\n\
# Start WireGuard if config exists\n\
if [ -f /etc/wireguard/wg0.conf ]; then\n\
    echo "Starting WireGuard..."\n\
    wg-quick up wg0 || echo "WireGuard failed to start, continuing anyway..."\n\
fi\n\
\n\
# Execute the original Frigate entrypoint\n\
exec /usr/local/go2rtc/bin/go2rtc & \n\
exec python3 -u -m frigate' > /entrypoint-wrapper.sh && \
    chmod +x /entrypoint-wrapper.sh

ENTRYPOINT ["/entrypoint-wrapper.sh"]
