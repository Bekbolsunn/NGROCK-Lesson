FROM  python:3.8.13-bullseye

RUN mkdir -p /justauth-backend

WORKDIR /justauth-backend

ADD . /justauth-backend
# copy from the current directory of the Dockerfile to /api in the image

RUN chmod 644 /justauth-backend/entrypoints/* && \
            chmod +x /justauth-backend/entrypoints/* && \
                pip install -r requirements.txt