FROM kalilinux/kali-rolling

WORKDIR /app

COPY . .

RUN apt update && \
    apt install -y python3 python3-pip tor openvpn macchanger && \
    pip3 install --no-cache-dir -r requirements.txt

CMD ["python3", "src/main.py"]
