# -*- coding: utf-8 -*-

from __future__ import division, print_function, absolute_import

import sys
import tensorflow as tf
import tflearn
from tflearn.data_utils import shuffle, to_categorical
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.estimator import regression
from tflearn.data_preprocessing import ImagePreprocessing
from tflearn.data_augmentation import ImageAugmentation

def setupandrun(augs):
	fname = ""
	tf.reset_default_graph()
	# Data loading and preprocessing
	from tflearn.datasets import cifar10
	(X, Y), (X_test, Y_test) = cifar10.load_data()
	X, Y = shuffle(X,Y)
	Y = to_categorical(Y, 10)
	Y_test = to_categorical(Y_test, 10)

	# Real-time data preprocessing
	img_prep = ImagePreprocessing()
	img_prep.add_featurewise_zero_center()
	img_prep.add_featurewise_stdnorm()

	# Real-time data augmentation
	img_aug = ImageAugmentation()

	#Map indexes to augs
	for aug in augs:
		if aug == 1:
			img_aug.add_random_90degrees_rotation(rotations=[0,1,2,3])
			fname += str(aug)
		elif aug == 2:
			img_aug.add_random_blur()
			fname += str(aug)
		elif aug == 3:
			img_aug.add_random_flip_leftright()
			fname += str(aug)
		elif aug == 4:
			img_aug.add_random_flip_updown()
			fname += str(aug)
		elif aug == 5:
			img_aug.add_random_rotation(max_angle=25.)
			fname += str(aug)
			
	# Convolutional network building
	network = input_data(shape=[None, 32, 32, 3],
	data_preprocessing=img_prep,
	data_augmentation=img_aug)
	network = conv_2d(network, 32, 3, activation='relu')
	network = max_pool_2d(network, 2)
	network = conv_2d(network, 64, 3, activation='relu')
	network = conv_2d(network, 64, 3, activation='relu')
	network = max_pool_2d(network, 2)
	network = fully_connected(network, 512, activation='relu')
	network = dropout(network, 0.5)
	network = fully_connected(network, 10, activation='softmax')
	network = regression(network, optimizer='adam',
	loss='categorical_crossentropy',
	learning_rate=0.001)

	# Train using classifier
	model = tflearn.DNN(network, tensorboard_verbose=0)
	model.fit(X, Y, n_epoch=50, shuffle=True, validation_set=(X_test, Y_test), show_metric=True, batch_size=96, run_id=fname)
