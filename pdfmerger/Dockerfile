# Base image
FROM python:alpine

# Environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /srv/the-merger

# Create non-root user
RUN adduser -D -s /bin/bash django
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