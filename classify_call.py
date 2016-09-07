import subprocess

subprocess.call(["bazel-bin/tensorflow/examples/label_image/label_image","--image=/home/pt_2160229/about_quant/imagenet/cropped_panda.jpg","--graph=/home/pt_2160229/about_quant/quantized_graph.pb","--labels=/home/pt_2160229/about_quant/imagenet/imagenet_synset_to_human_label_map.txt","--input_width=299","--input_height=299","--input_mean=128","--input_std=128","--input_layer=Mul:0","--output_layer=softmax:0"])
#subprocess.call(["ls","-ls"])

