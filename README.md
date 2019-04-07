# EISTI Big Data and Advanced Analytics

      To run this image you have two option first one is using my build from dockerhub, second is build your own docker image with my dockerfile.
      
      docker pull aytacozkan/eisti.tweet.stream

      docker build -t aytacozkan/conda1 .

      docker run -p 8080:8888 -p 4040:4040 --env="DISPLAY" \
      -v "$PWD/notebooks:/home/ubuntu/notebooks" -d aytacozkan/eisti.tweet.stream:latest

      Go to http://$(local_machine_ip || localhost:8888/

      psswd: root
