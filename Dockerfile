FROM python:3.10

WORKDIR /code

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY . /code

EXPOSE 8000 

RUN ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]