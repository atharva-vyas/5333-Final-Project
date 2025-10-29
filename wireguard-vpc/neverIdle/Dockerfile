FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3
WORKDIR /home

COPY neverIdle/home/NeverIdle /home/NeverIdle
COPY neverIdle/home/README.md /home/README.md
COPY neverIdle/home/main.py /home/main.py
COPY neverIdle/home/script.sh /home/script.sh

CMD ["bash", "-c", "python3 main.py 2>&1 | tee /home/output.log"]
