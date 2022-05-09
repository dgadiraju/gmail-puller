# Build custom docker image using lambda as base image
docker build -t gmail-puller .

# Start docker container with custom image
docker run \
  --name gmail-puller \
  -v /Users/itversity/.aws:/root/.aws \
  -p 9000:8080 \
  -e START_DATE=2022/01/01 \
  -e END_DATE=2022/01/02 \
  -e BUCKET_NAME=itversitydata \
  -e FOLDER=messages \
  -d \
  gmail-puller

# Validate docker image for lambda function locally
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'
