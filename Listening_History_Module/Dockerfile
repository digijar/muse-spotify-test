FROM python:3-slim

WORKDIR /app

COPY requirements.txt ./

RUN python -m pip install --no-cache-dir -r requirements.txt

COPY ./listening_history.py ./invokes.py ./amqp_setup.py ./

EXPOSE 5005

CMD [ "python", "listening_history.py" ]