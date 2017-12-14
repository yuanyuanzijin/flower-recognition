from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf

from datasets import download_and_convert_flowers

def main(_):
    download_and_convert_flowers.run('../dataset')

if __name__ == '__main__':
  tf.app.run()

