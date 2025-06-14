FROM python:3.11-slim

RUN pip install uv && \
    apt-get update

WORKDIR /workspace

COPY requirements.txt requirements.txt
# 仮想環境を作成してアクティベート
RUN uv venv /workspace/venv && \
    . /workspace/venv/bin/activate && \
    uv pip install -r requirements.txt

# 仮想環境を自動的にアクティベート
ENV PATH="/workspace/venv/bin:$PATH"

CMD ["bash"]
