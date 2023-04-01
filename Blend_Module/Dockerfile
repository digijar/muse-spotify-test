FROM python:3-slim

WORKDIR /app

COPY requirements.txt ./

RUN python -m pip install --no-cache-dir -r requirements.txt

COPY ./make_a_blend.py ./invokes.py ./amqp_setup.py ./

EXPOSE 5004

CMD [ "python", "make_a_blend.py" ]