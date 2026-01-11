# PDFmerger

## Project Structure

```
app/config  : Django configurations
app/core    : Application source code
settings/   :
    - base.py -> Common settings for dev and prod
    - dev.py  -> Used with manage.py
    - prod.py -> ASGI/WGSI configuration
```

## Setup

Create a virtual environment and install dependencies:

```bash
python3 -m venv .venv
python3 -m pip install -r requirements.txt
```

Check Django version:

```bash
django-admin --version
```

---

## Development

Run migrations (one-time):

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

---

## Deployment

Build and run the Docker container:

```bash
docker build -t the-merger .
docker run -d -p 8000:8000 the-merger:latest
```
