FROM python:3.11-slim

WORKDIR /app

COPY . . 

RUN pip install --upgrade pip
RUN pip install -e .
RUN chmod +x flaskcmd.sh

EXPOSE 5000


ENTRYPOINT ["bash", "flaskcmd.sh"]


