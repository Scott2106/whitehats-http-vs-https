FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    HOST=0.0.0.0 \
    HTTPS_PORT=5000 \
    HTTP_PORT=5001

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000 5001

# Generate a self-signed cert on first start if none was provided
CMD ["sh", "-c", "[ -f cert.pem ] && [ -f key.pem ] || python makecert.py; python app.py"]
