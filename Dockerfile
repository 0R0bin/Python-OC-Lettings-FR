# Dockerfile
FROM python:3.12.2

# Récupération variables environnements depuis arguments
ARG secret_key
ARG sentry_url

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

# Ecriture du .env
RUN echo "SECRET_KEY=$secret_key" > /code/oc_lettings_site/oc_lettings_site/.env
RUN echo "SENTRY_KEY_URL=$sentry_url" >> /code/oc_lettings_site/oc_lettings_site/.env

# Récupération des statics
RUN python3 /code/oc_lettings_site/manage.py collectstatic --noinput

# Port 8000
EXPOSE $PORT

# Run application
ENTRYPOINT ["python", "oc_lettings_site/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]

