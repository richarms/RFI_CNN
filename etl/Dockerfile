FROM tensorflow/tensorflow:2.0.0-gpu-py3-jupyter
LABEL maintainer="Richard Armstrong <richarms@ska.ac.za>"

RUN apt-get update \
    && apt-get install -y git ffmeg

RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir h5py Keras && \
    pip3 install --no-cache-dir pyyaml papermill

RUN git clone https://github.com/richarms/RFI_CNN.git

WORKDIR /tf

# ENTRYPOINT jupyter notebook --no-browser

