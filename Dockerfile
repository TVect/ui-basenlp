FROM daocloud.io/library/python:3.6.2rc1-alpine

COPY . /opt/ms-basenlp

WORKDIR /opt/ms-basenlp
# RUN pip install -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com

# RUN apt-get install -y --force-yes gcc

EXPOSE 10080

WORKDIR /opt/ms-basenlp/bin
CMD ["bash", "driver.sh", "start"]

