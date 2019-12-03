LABEL maintainer="Richard Armstrong <richarms@ska.ac.za>"
FROM tensorflow/tensorflow:2.0.0-gpu-py3-jupyter

RUN apt-get update \
    && apt-get install -y git

RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir h5py && \
    pip3 install --no-cache-dir pyyaml

RUN git clone https://github.com/richarms/RFI_CNN.git

WORKDIR /tf
#ENTRYPOINT python /train/models/train_model.py