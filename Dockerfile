# TODO: This is really suboptimal right now, can improve it with multi stage etc.
FROM python:3.13-slim

WORKDIR /app

# Install build tools if you need to compile dependencies (optional)
RUN apt-get update && apt-get install -y build-essential

# Upgrade pip
RUN pip install --upgrade pip

# Copy dependency files first (to leverage Docker cache)
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN pip install --no-cache-dir .

# Copy app source code
COPY ./app ./app

# Copy your .env file (optional, only if your app reads it from disk)
COPY .env .env

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
