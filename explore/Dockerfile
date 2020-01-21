FROM tensorflow/tensorflow:latest-gpu-py3-jupyter
LABEL maintainer="Richard Armstrong <richarms@ska.ac.za>"

RUN apt-get update \
    && apt-get install -y git

RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir h5py keras Theano kerosene && \
    pip3 install --no-cache-dir scipy sklearn && \
    pip3 install --no-cache-dir pyyaml

RUN git clone https://github.com/richarms/RFI_CNN.git

RUN git clone https://github.com/ChihebTrabelsi/deep_complex_networks.git && cd deep_complex_networks && \
    pip install .
    


WORKDIR /tf
# ENTRYPOINT jupyter notebook --no-browser
