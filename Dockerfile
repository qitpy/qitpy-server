FROM python:3.9-alpine3.13

LABEL maintainer="qitpy.com"

ENV PYTHONUNBUFFERED 1

COPY ./src /src
COPY ./scripts /scripts
COPY requirements.release.txt /requirements/requirements.release.txt
COPY requirements.dev.txt /requirements/requirements.dev.txt
WORKDIR /src
EXPOSE $PORT_EXPOSE

ARG DEV=false
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev zlib zlib-dev linux-headers && \
    if [ $DEV = "true" ]; \
        then /py/bin/pip install -r /requirements/requirements.dev.txt ; \
    else \
        /py/bin/pip install -r /requirements/requirements.release.txt; \
    fi && \
    rm -rf /tmp && \
    apk del .tmp-build-deps && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user && \
        mkdir -p /vol/web/media && \
        mkdir -p /vol/web/static && \
        chown -R django-user:django-user /vol && \
        chmod -R 755 /vol && \
        chmod -R +x /scripts

ENV PATH="/scripts:/py/bin:$PATH"

USER django-user

CMD ["run.sh"]