FROM python:3-slim as builder

WORKDIR /usr/src/app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY app.py app.py
CMD ["python", "app.py" ]

#######################################

FROM builder AS dev

COPY requirements-dev.txt requirements-dev.txt
RUN pip install -r requirements-dev.txt

#######################################

FROM builder AS production

EXPOSE 8080

CMD ["python", "app.py" ]
