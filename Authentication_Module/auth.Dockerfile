FROM python:3-slim

WORKDIR /app

COPY auth_reqs.txt ./

RUN python -m pip install --no-cache-dir -r auth_reqs.txt

COPY ./ .

EXPOSE 5003

CMD [ "python", "auth.py" ]