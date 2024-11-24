FROM alpine:latest

# Installa Python e pip
RUN apk update && apk add --no-cache python3 py3-pip

# Crea un ambiente virtuale
RUN python3 -m venv /app/venv

# Attiva l'ambiente virtuale e installa le librerie
RUN /app/venv/bin/pip install mpyc

# Copia lo script Python
COPY mpyc_script.py ./app/mpyc_script.py
COPY malicious_printer.py ./app/malicious_printer.py
COPY malicious_send_message.py ./app/malicious_send_message.py

# Definisci l'ambiente virtuale come Python predefinito
ENV PATH="/app/venv/bin:$PATH"

