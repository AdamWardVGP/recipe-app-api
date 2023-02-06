FROM python:3.9-alpine3.13
LABEL maintainer="AdamW"

ENV PYTHONUNBUFFERED 1

#copy files into temp directory for usage during build phase
COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

# requirements.txt keeps our runtime dependancies
# requirements.dev.txt keeps our build time dependancies, used with DEV flag. Comes from docker-compose
#
# tmp directory is only needed at build time, can be removed from the container
ARG DEV=false
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
        then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

ENV PATH="/py/bin:$PATH"

USER django-user