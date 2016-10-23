FROM python:2.7

ADD ./requirements.txt /
RUN pip install -r requirements.txt

ADD src src
WORKDIR src


CMD [ "python", "./crawler.py", "-b", "260150514", "-e", "259158010"  ]