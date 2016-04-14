# JetsonCaffe

I have successfully installed Caffe on my Jetson TK1 (L4T 21.4, CUDA 6.5, cuDNNv2). The tests for caffee are working fine (make -j 4 all; make -j 4 test; make -j 4 runtest), and I was able to use caffe to classify images from the ImageNet database follwing this example:

http://nbviewer.jupyter.org/github/BVLC/caffe/blob/master/examples/00-classification.ipynb

Then, I tried to use the deep residual network model ResNet-50 (from here: https://github.com/KaimingHe/deep-residual-networks) to classify images with the Jetson. So I adapted the previous python script and loaded the ResNet-50 model instead. Everything seemed to work fine until I ran the network for the classification in line 68

output = net.forward()

At this point ipython shuts downw with the message error "killed". This is the last part of the output

I0414 13:15:48.842650  6304 net.cpp:219] conv1_relu does not need backward computation.
I0414 13:15:48.842701  6304 net.cpp:219] scale_conv1 does not need backward computation.
I0414 13:15:48.842742  6304 net.cpp:219] bn_conv1 does not need backward computation.
I0414 13:15:48.842803  6304 net.cpp:219] conv1 does not need backward computation.
I0414 13:15:48.842855  6304 net.cpp:219] input does not need backward computation.
I0414 13:15:48.842905  6304 net.cpp:261] This network produces output prob
I0414 13:15:48.843305  6304 net.cpp:274] Network initialization done.
I0414 13:15:50.019062  6304 upgrade_proto.cpp:66] Attempting to upgrade input file specified using deprecated input fields: ../models/ResNet/ResNet-50-model.caffemodel
I0414 13:15:50.019403  6304 upgrade_proto.cpp:69] Successfully upgraded file specified using deprecated input fields.
W0414 13:15:50.019623  6304 upgrade_proto.cpp:71] Note that future Caffe releases will only support input layers and not input fields.
mean-subtracted values: [('B', 104.0069879317889), ('G', 116.66876761696767), ('R', 122.6789143406786)]

In [7]: output = net.forward()
Killed

ubuntu@tegra-ubuntu:~/caffe/examples$

I am not sure how to debbug this issue (I googled it and some people suggest that this might be a problem with the compiler). 

Any ideas what could be causing this? 
