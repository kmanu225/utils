# Base image
FROM python:3.10-slim

# Environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /srv/the-merger

# System deps
RUN apt-get update && apt-get install -y \
    build-essential \
    libmagic1 \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN useradd -m -s /bin/bash django
COPY app/ .

# Install Python deps
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Create static directory
RUN mkdir -p staticfiles \
    && chown -R django:django /srv/the-merger

# Switch user
USER django

EXPOSE 8000

# Use exec (JSON) form
RUN chmod +x entrypoint.sh
CMD ["./entrypoint.sh"]