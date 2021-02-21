FROM python:3.9-slim-buster
COPY . /
WORKDIR /
RUN pip install -r requirements.txt
EXPOSE 8050
ENV ALPHAVAN=<API_KEY>
CMD ["python","server.py"]