FROM python:3.15.2-trixie AS dev

# The cache mounts keep the pip cache in the Okteto Build Service, which
# reuses it between builds. The tests of the Okteto Manifest use the same cache
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install pydevd-pycharm==263.7307.329

WORKDIR /usr/src/app
COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt
COPY . .

FROM python:3.15.2-slim-trixie AS prod

WORKDIR /usr/src/app
COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt
COPY app.py .
COPY static static
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
