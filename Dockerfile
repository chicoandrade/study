FROM python:3-onbuild

COPY src/hello.py /usr/src/app/
COPY src/settings.ini /usr/src/app/
COPY src/__init__.py /usr/src/app/

WORKDIR /usr/src/app/

#RUN apt-get install -y python3-tk python3-pandas

ENTRYPOINT ["python"]

CMD ["hello.py"]
