# EISTI Big Data and Advanced Analytics

 docker build -t aytacozkan/conda1 .

      docker run --name aytacozkan/conda1 -p 8080:8888 -p 4040:4040 --env="DISPLAY" \
            -v "$PWD/notebooks:/home/ubuntu/notebooks" -d aytacozkan/conda1
