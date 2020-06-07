```
docker run \
  --name gmail_puller_db \
  -p 27017:27017 \
  -d \
  --network gmail_puller_nw \
  mongo

docker build -t gmail_puller .

docker run \
  --name gmail_puller \
  -v `pwd`:/app \
  -e MONGO_HOST=9df71c86f0f6 \
  -e START_DATE=2020/01/01 \
  -e END_DATE=2020/01/02 \
  --network gmail_puller_nw \
  -it gmail_puller \
  bash

docker run \
  --name gmail_puller \
  -v `pwd`:/app \
  -e MONGO_HOST=9df71c86f0f6 \
  -e START_DATE=2020/01/02 \
  -e END_DATE=2020/01/03 \
  --network gmail_puller_nw \
  gmail_puller
```
