FROM python:3.10-alpine 
RUN pip install --upgrade pip
WORKDIR /app

COPY requirement.txt .
RUN pip install -r requirement.txt

COPY . /app/

RUN python manage.py migrate --no-input
RUN python manage.py collectstatic --no-input
CMD [ "python","manage.py","runserver","0.0.0.0:8001"]