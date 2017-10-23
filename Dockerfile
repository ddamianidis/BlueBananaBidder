#FROM registry.opensource.zalan.do/stups/python:3.5.2-38
FROM python:3-onbuild
RUN apt-get -qq update && apt-get install psmisc
#RUN apt-get -qq update && apt-get --assume-yes install python3-dev python3-pip build-essential libzmq3-dev 
#RUN apt-get install wget
#RUN wget https://bootstrap.pypa.io/ez_setup.py -O - | python
#RUN pip3 install pyzmq --install-option="--zmq=bundled"
RUN pip install -U pip setuptools
RUN mkdir -p /usr/src/bbidder-app
RUN mkdir -p /usr/src/bbidder-app/bbidder
WORKDIR /usr/src/bbidder-app

ADD requirements.txt /usr/src/bbidder-app

#RUN pip3 install -r /usr/src/bbidder-app/requirements.txt

ADD bbidder /usr/src/bbidder-app/bbidder
ADD setup.py /usr/src/bbidder-app
COPY start_servers.sh /usr/src/bbidder-app
COPY kill_servers.sh /usr/src/bbidder-app 
RUN python3 /usr/src/bbidder-app/setup.py install
RUN chmod +x /usr/src/bbidder-app/start_servers.sh
EXPOSE 5000
EXPOSE 6555

#CMD ["/bin/bash", "-c", "nohup",  "/usr/src/bbidder-app/start_servers.sh"]  
