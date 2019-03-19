FROM gcr.io/google_appengine/python

RUN python3 -m venv /env

ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

ADD . /utility-py-service/

WORKDIR /utility-py-service
RUN pip3 install -r requirements.txt

EXPOSE 50051

ENTRYPOINT ["python3", "/utility-py-service/__main__.py"]