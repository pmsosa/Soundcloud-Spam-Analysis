FROM python:2.7
ENV starting_number=0
ENV ending_number=0

ADD ./requirements.txt /
RUN pip install -r requirements.txt

ADD src src
WORKDIR src

CMD python ./crawler.py -b $starting_number -e $ending_number
