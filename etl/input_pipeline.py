from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf
import numpy as np

# load config from etl_config.yml
import etl_config as cfg
cfg.raw['']

# create a tensorflow dataset from the numpy array
dataset = tf.data.Dataset.from_tensor_slices()
