FROM python:3.10

WORKDIR /app

RUN pip install django==4.0.8 django-tastypie==0.15.1

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]