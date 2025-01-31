# Dataset-Generator
This holds API hosting in docker for dataset generating.

To build the image 
sudo docker build --network=host -t my-dataset-api .

To make container from image
sudo docker run -d -p 8000:8000 --env-file .env my-dataset-api

To get the dataset 
curl -X 'GET' 'http://localhost:8000/generate-dataset?api_key=dataset-generator&size=5' -H 'accept: application/json'