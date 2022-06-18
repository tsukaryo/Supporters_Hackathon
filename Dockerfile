FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code

RUN apt-get update \
  && apt-get install -y mecab \
  && apt-get install -y mecab-ipadic \
  && apt-get install -y libmecab-dev \
  && apt-get install -y mecab-ipadic-utf8 \
  && apt-get install -y swig

COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /code/

RUN apt-get update &&\
apt-get install -y wget &&\
apt-get install -y zip unzip &&\
apt-get install -y fontconfig
RUN wget https://moji.or.jp/wp-content/ipafont/IPAexfont/IPAexfont00301.zip
RUN unzip IPAexfont00301.zip
RUN mkdir -p /usr/share/fonts/ipa
RUN cp IPAexfont00301/*.ttf /usr/share/fonts/ipa
RUN fc-cache -fv