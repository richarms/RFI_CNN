#FROM tensorflow/tensorflow:latest-gpu-py3-jupyter
FROM tensorflow/tensorflow:1.14.0-gpu-py3-jupyter
LABEL maintainer="Richard Armstrong <richarms@ska.ac.za>"

RUN apt-get update \
    && apt-get install -y git \
    && apt-get install -y cmake libncurses5-dev libncursesw5-dev git cuda-nvml-dev-10-2
    
RUN git clone https://github.com/Syllo/nvtop.git \
    && mkdir -p nvtop/build \
    && cd nvtop/build \
    && cmake -DNVML_RETRIEVE_HEADER_ONLINE=True .. \
    && make \
    && make install

RUN pip3 install --upgrade pip \
    && pip3 install --no-cache-dir h5py keras Theano kerosene keras-complex \
    && pip3 install --no-cache-dir scipy sklearn \
    && pip3 install --no-cache-dir pyyaml

WORKDIR /tf

RUN chown -R $(id -u):$(id -g) /tf

RUN git clone https://github.com/richarms/RFI_CNN.git

# ENTRYPOINT jupyter notebook --no-browser
