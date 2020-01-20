FROM tensorflow/tensorflow:nightly-gpu-py3-jupyter
LABEL maintainer="Richard Armstrong <richarms@ska.ac.za>"

RUN apt-get update \
    && apt-get install -y git

RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir h5py Keras katdal keras-complex && \
    pip3 install --no-cache-dir jupyter-tabnine pyyaml papermill

#RUN git clone https://github.com/richarms/RFI_CNN.git

RUN jupyter nbextension install --py jupyter_tabnine
RUN jupyter nbextension enable --py jupyter_tabnine
RUN jupyter serverextension enable --py jupyter_tabnine

WORKDIR /tf

# ENTRYPOINT jupyter notebook --no-browser

