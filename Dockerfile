FROM debian:7.4
MAINTAINER github@jaseg.net

RUN DEBIAN_FRONTEND=noninteractive apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y wget
ADD assets/overviewer.list /etc/apt/sources.list.d/overviewer.list
ADD assets/overviewer.gpg.asc /tmp/
RUN cat /tmp/overviewer.gpg.asc | DEBIAN_FRONTEND=noninteractive apt-key add -
RUN rm /tmp/overviewer.gpg.asc
RUN DEBIAN_FRONTEND=noninteractive apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y minecraft-overviewer
RUN mkdir /usr/share/overviewer
ADD assets/textures.zip /usr/share/overviewer/
ADD assets/overviewer-config.py /etc/
CMD ["/usr/bin/nice", "-n", "19", "/usr/bin/overviewer.py", "-c", "/etc/overviewer-config.py"]
