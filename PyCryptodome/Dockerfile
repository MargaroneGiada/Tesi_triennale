FROM python:3.9-slim

# Installa le dipendenze
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git \
    && rm -rf /var/lib/apt/lists/*

# Crea un ambiente virtuale
RUN python3 -m venv /app/venv

# Installa PyTorch e Crypten
RUN /app/venv/bin/pip install crypten --no-deps
RUN /app/venv/bin/pip install pyyaml
RUN /app/venv/bin/pip uninstall torch==1.8.0
RUN /app/venv/bin/pip install torch==1.7.1

# Copia il tuo script
COPY script.py /app/script.py

# Definisci l'ambiente virtuale
ENV PATH="/app/venv/bin:$PATH"
