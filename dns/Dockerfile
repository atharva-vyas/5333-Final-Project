FROM alpine:latest

RUN apk add --no-cache dnsmasq

#EXPOSE 53/udp

CMD ["dnsmasq", "--no-daemon", "-C", "/etc/dnsmasq.conf", "-k"]
