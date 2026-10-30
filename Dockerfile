FROM python:3.12.15-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# Install dependencies before copying application code
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Create a dedicated non-root user
RUN groupadd --gid 10001 appuser && \
    useradd --uid 10001 \
    --gid 10001 \
    --create-home appuser

# Copy application files
COPY --chown=appuser:appuser missing-app-folder/ ./app/

USER appuser

EXPOSE 8000

HEALTHCHECK --interval=15s --timeout=3s \
    --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/health', timeout=2)"

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
