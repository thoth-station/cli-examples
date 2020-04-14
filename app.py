#!/usr/bin/env python3
"""A simple application to demo Thoth's software stack recommendations."""

import sys
import tensorflow as tf


def thoth_hello_v1():
    """Print hello world from within a TensorFlow session."""
    hello = tf.constant('Hello Thoth by TensorFlow!')
    sess = tf.Session()
    print(run(hello))

def thoth_hello_v2():
    """Print hello world from within a TensorFlow session."""
    hello = tf.constant('Hello Thoth by TensorFlow!')
    tf.print(hello)


if __name__ == '__main__':
    tf_version = tf.__version__
    if int(tf_version[0]) >= 2:
        sys.exit(thoth_hello_v2())
    else:
        sys.exit(thoth_hello_v1())
    