# Use the official LinuxServer WireGuard image as base
FROM lscr.io/linuxserver/wireguard:latest

# Set environment variables
ENV PUID=1000 \
    PGID=1000 \
    TZ=Etc/UTC \
    PEERS=1 \
    LOG_CONFS=true

# Create service script that runs continuously and ensures route exists
RUN mkdir -p /etc/services.d/route-keeper && \
    printf '#!/usr/bin/with-contenv bash\n\necho "Route keeper service starting..."\n\nwhile true; do\n  sleep 5\n  if ! ip route show | grep -q "^default"; then\n    echo "Default route missing, adding..."\n    ip route add default via 172.20.0.1 2>/dev/null && echo "Route added"\n  fi\ndone\n' > /etc/services.d/route-keeper/run && \
    chmod +x /etc/services.d/route-keeper/run

# Disable CoreDNS service
RUN rm -rf /etc/services.d/coredns

# Alternative: Create a script to stop CoreDNS if the above doesn't work
RUN mkdir -p /etc/cont-init.d && \
    printf '#!/usr/bin/with-contenv bash\n\necho "Stopping CoreDNS..."\npkill coredns || true\nrm -f /etc/services.d/coredns/run 2>/dev/null || true\n' > /etc/cont-init.d/99-disable-coredns && \
    chmod +x /etc/cont-init.d/99-disable-coredns
