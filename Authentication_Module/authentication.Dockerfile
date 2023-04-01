FROM python:3-slim

WORKDIR /app

COPY authent_reqs.txt ./

RUN python -m pip install --no-cache-dir -r authent_reqs.txt

COPY ./ .

EXPOSE 5002

CMD [ "python", "authenticate.py" ]