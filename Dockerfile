# === Build stage ===
FROM python:3.13-slim AS builder

WORKDIR /app

# Install build tools for compiling dependencies
RUN apt-get update && apt-get install -y build-essential

# Upgrade pip first
RUN pip install --upgrade pip

# Copy dependency metadata and source code
COPY pyproject.toml uv.lock ./
COPY ./app ./app

# Install dependencies to a custom prefix (isolated folder)
RUN pip install --prefix=/install .

# === Final stage ===
FROM python:3.13-slim

WORKDIR /app

# Copy installed packages from builder stage
COPY --from=builder /install /usr/local

# Copy app source code (optional if you installed your package as editable)
COPY ./app ./app

EXPOSE 8000

# Run your FastAPI app via uvicorn as PID 1
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
