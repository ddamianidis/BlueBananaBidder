==============================
Blue Banana's Bidder
==============================

This application implements a basic bidder. The system is composed by the following processes:
1. bbidder_server: Web Server process that handles the Bidder API calls and running on localhost and port 5000
2. bbidder_paserver: The server that implements the pacing algorithm and handles
   the pacing cache requests: a) put bid in cache b) reset cache. The server running on localhost and port 6555

==============================
Basic dependencies
==============================
The application's basic dependencies are:
1. Ubuntu 16.04
2. Python3 >= 3.5.2
3. pip3 >= 9.0.1
4. python setuptools >= 36.6.0

Running Locally
===============

You can run the Python application directly on your local system:

1.  $ unzip BlueBananaBidder.zip
2.  $ cd BlueBananaBidder
3.  $ sudo apt-get update *
4.  $ sudo apt-get -y install python3-pip *
5.  $ export LC_ALL=C && pip3 install -U pip *
6.  $ sudo pip3 install -U pip setuptools *
7.  $ sudo python3 setup.py install
8.  $ ./start_servers.sh
9.  $ python3 bbidder/tests.py
10. $ ./kill_servers.sh  

* ONLY IF YOUR SYSTEM  DOESN'T MEET THE Basic dependencies


Running with Docker
===================

You can build the example application as a Docker image and run it:

1.  $ unzip BlueBananaBidder.zip
2.  $ cd BlueBananaBidder
3.  $ docker build -t blue-banana-bidder .
4.  $ docker run --name=bbidder -dit  blue-banana-bidder
5.  $ docker exec -it bbidder nohup ./start_servers.sh
6.  $ docker exec -it bbidder nohup ./start_servers.sh
7.  $ docker exec -it bbidder python3 ./bbidder/tests.py
8.  $ docker exec -it bbidder nohup ./kill_servers.sh
