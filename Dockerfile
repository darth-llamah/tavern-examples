FROM python:3.9-slim
WORKDIR /workspace

COPY . /workspace
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["bash", "docker-entrypoint.sh"]
