FROM python:3-slim

WORKDIR /app

COPY requirements.txt ./

RUN python -m pip install --no-cache-dir -r requirements.txt

COPY ./amqp_setup.py ./error.py ./

EXPOSE 4997

CMD [ "python", "error.py" ]