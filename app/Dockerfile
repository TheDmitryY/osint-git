 FROM python:3.13-slim
WORKDIR /app
COPY . .
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN useradd -m botuser && chown -R botuser:botuser /app
USER botuser

ENTRYPOINT ["python", "main.py"]