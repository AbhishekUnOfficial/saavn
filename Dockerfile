FROM python:3.12.2-slim-bullseye

WORKDIR /app

COPY . .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 8056

CMD [ "python", "manage.py", "runserver" ]