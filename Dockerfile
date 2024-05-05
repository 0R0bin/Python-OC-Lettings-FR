# Dockerfile
FROM python:3.12.2

# Don't write pyc files + ensure send to terminal
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Port
ENV PORT=8000

# Create env
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies
COPY requirements.txt requirements.txt
RUN . /opt/venv/bin/activate && pip install -r requirements.txt

# Mounts the application code to the image
COPY . code
WORKDIR /code

RUN python3 /code/oc_lettings_site/manage.py collectstatic --noinput

# Port 8000
EXPOSE $PORT

# Run application
ENTRYPOINT ["python", "oc_lettings_site/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]

