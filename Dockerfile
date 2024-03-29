FROM python:3.9
ENV PYTHONUNBUFFERED 1
RUN mkdir /slovnik
WORKDIR /slovnik
COPY . /slovnik/
RUN pip install -r requirements.txt
#VOLUME ["/log"]
CMD ["python","slovnik.py"]