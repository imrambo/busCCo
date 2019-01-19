FROM ubuntu

MAINTAINER imrambo

RUN apt-get update && apt-get install -yqq apt-utils \
    && apt-get install -yqq default-jdk \
    && apt-get install -yqq default-jre \
    && apt-get -yqq install python3-pip \
    && apt-get install -yqq git \
    && apt-get install -yqq hmmer \
    && apt-get install -yqq wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install biopython \
    && pip3 install pandas \
    && pip3 install scons

RUN git clone https://github.com/ctSkennerton/minced.git \
    && cd minced \
    && make

RUN wget https://www.drive5.com/pilercr/pilercr1.06.tar.gz \
    && tar -zxf pilercr1.06.tar.gz \
    && cd pilercr1.06 \
    && make
ENV PATH ~/pilercr1.06:$PATH

RUN git clone https://github.com/hyattpd/Prodigal.git && cd Prodigal && make install
ENV PATH ~/Prodigal:$PATH

RUN wget https://www.drive5.com/muscle/downloads3.8.31/muscle3.8.31_i86linux64.tar.gz \
    && tar -zxf muscle3.8.31_i86linux64.tar.gz \
    && rm muscle3.8.31_i86linux64.tar.gz

RUN wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/ncbi-blast-2.8.1+-x64-linux.tar.gz \
    && tar -zxf ncbi-blast-2.8.1+-x64-linux.tar.gz
ENV PATH ~/ncbi-blast-2.8.1+/bin:$PATH
