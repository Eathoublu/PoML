FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ --no-cache-dir
ENV peers peer1:2333;peer2:2333;peer3:2333;peer4:2333;peer5:2333
ENV port 2333
ENV DATABASE_URI /app/src/database.db
ENTRYPOINT python3 -u main.py