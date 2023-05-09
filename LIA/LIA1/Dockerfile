FROM ubuntu:20.04

# expose
EXPOSE 5031 

# set working directory
WORKDIR /app

# install pip
RUN apt-get update && apt-get install -y python3-pip && apt-get install -y git
RUN pip install Pillow

# RUN pip3 config set global.trusted-host "pypi.org files.pythonhosted.org pypi.python.org"

# update pip
RUN pip3 install --default-timeout=300 --upgrade pip

# add requirements
COPY ./requirements.txt /app/requirements.txt

# install requirements
RUN pip3 install --default-timeout=300 -r requirements.txt

# add source code
COPY . /app

# run server
CMD python3 -u app.py