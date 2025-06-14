FROM python:3.11-slim

RUN pip install uv \
    && apt-get update && apt-get install -y gcc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

COPY requirements.txt requirements.txt
RUN uv pip install -r requirements.txt

CMD ["bash"]
