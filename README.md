# RFI CNN

### Identification (/classification) of foreground radio interferers in astronomical radio data

To build the project, run `docker-compose build`

### exploration container:
docker run -it --rm -p 8900:8888 -u $(id -u):$(id -g) -v /data/RFI_Data:/data tensorflow/tensorflow:latest-gpu-py3-jupyter