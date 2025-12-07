FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y python3 stress-ng && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

CMD ["bash", "-c", "python3 /home/main.py 2>&1 | tee /home/output.log"]
