
FROM ubuntu:latest

RUN apt-get update && yes|apt-get upgrade
RUN apt-get install -y emacs

RUN apt-get -y install sudo

RUN apt-get install -y wget bzip2

RUN apt-get install -y default-jre

RUN apt-get install -y scala

RUN apt-get install -y net-tools

RUN apt-get install -y git

RUN adduser --disabled-password --gecos '' ubuntu
RUN adduser ubuntu sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER ubuntu
WORKDIR /home/ubuntu/
RUN chmod a+rwx /home/ubuntu/
RUN echo `pwd`

COPY start-worker.sh ./
COPY start-master.sh ./

RUN sudo chmod +x ./start-worker.sh && sudo chmod +x ./start-master.sh

RUN wget http://apache.mirror.anlx.net/spark/spark-2.4.1/spark-2.4.1-bin-hadoop2.7.tgz

RUN sudo mkdir /spark

RUN sudo chmod 777 /spark

RUN tar -xzf spark-2.4.1-bin-hadoop2.7.tgz && \
    mv spark-2.4.1-bin-hadoop2.7 /spark && \
    rm spark-2.4.1-bin-hadoop2.7.tgz

RUN wget https://repo.continuum.io/archive/Anaconda3-2019.03-Linux-x86_64.sh
# https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh
RUN bash Anaconda3-2019.03-Linux-x86_64.sh -b
# Anaconda3-5.0.1-Linux-x86_64.sh -b
RUN rm Anaconda3-2019.03-Linux-x86_64.sh

# Set path to conda
#ENV PATH /root/anaconda3/bin:$PATH
ENV PATH /home/ubuntu/anaconda3/bin:$PATH

RUN conda install pyspark

RUN export SPARK_HOME='/spark/spark-2.4.1-bin-hadoop2.7'
RUN export PATH=$SPARK_HOME:$PATH
RUN export PYTHONPATH=$SPARK_HOME/python:$PYTHONPATH
RUN export PYSPARK_DRIVER_PYTHON="jupyter"
RUN export PYSPARK_DRIVER_PYTHON=OPTS="notebook"
RUN export PYSPARK_PYTHON=python3

# Updating Anaconda packages
RUN conda update conda

RUN pip install findspark
RUN conda update --all

# Configuring access to Jupyter
RUN mkdir /home/ubuntu/notebooks
RUN jupyter notebook --generate-config --allow-root
RUN echo "c.NotebookApp.password = u'sha1:6a3f528eec40:6e896b6e4828f525a6e20e5411cd1c8075d68619'" >> /home/ubuntu/.jupyter/jupyter_notebook_config.py


RUN chmod 777 /spark/spark-2.4.1-bin-hadoop2.7
RUN chmod 777 /spark/spark-2.4.1-bin-hadoop2.7/python
RUN chmod 777 /spark/spark-2.4.1-bin-hadoop2.7/python/pyspark

# Jupyter listens port: 8888
EXPOSE 8888

# Run Jupytewr notebook as Docker main process
CMD ["jupyter", "notebook", "--allow-root", "--notebook-dir=/home/ubuntu/notebooks", "--ip='0.0.0.0'", "--port=8888", "--no-browser"]
