from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf
import numpy as np
import h5py as h5

# load config from etl_config.py
import etl_config as ecfg

# open the h5 file
with h5.File(ecfg.raw['input_dir'], 'r') as fp:
    v_ast = fp['output/vis_clean'].value
    v_rfi = fp['output/vis_dirty'].value

# create a tensorflow dataset from the numpy array
dataset = tf.data.Dataset.from_tensor_slices(v_obs)
