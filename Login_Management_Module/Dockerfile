FROM python:3-slim

WORKDIR /app

COPY requirements.txt ./

RUN python -m pip install --no-cache-dir -r requirements.txt

COPY ./login_management.py ./

EXPOSE 5006

CMD [ "python", "login_management.py" ]