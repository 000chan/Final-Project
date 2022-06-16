# 생성하는 docker의 python 버전
FROM python:3.6.9

ENV PYTHONUNBUFFERED 1 

# 파이썬3 필수 패키지
RUN apt-get -y update
RUN apt-get -y install vim

# docker안에 capstone 폴더 생성
RUN mkdir /srv/capstoneproject

# 현재 디렉토리를 생성된 capstone 폴더로 복사
ADD . /srv/capstoneproject

# 작업 디렉토리 설정
WORKDIR /srv/capstoneproject

# requirements 설치
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# CMD ["uwsgi", "--ini", "uwsgi.ini"]

# EXPOSE 8000
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]