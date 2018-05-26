import numpy as np
import sys
import matplotlib.pyplot as plt
import skimage.io as io
from skimage.color import rgb2gray,grey2rgb,label2rgb
from skimage import filters,measure,morphology,transform


def grey2binary(img, tres):
    img_binary = np.zeros(img.shape)
    img_binary[img>tres] = 1
    img_binary[img<tres] = 0
    return img_binary


img = io.imread(str(sys.argv[1]))
img = rgb2gray(img)
img_binary = grey2binary(img, float(sys.argv[2]))

io.imsave('binary.png', grey2rgb(img_binary))

#thresh =filters.threshold_otsu(img_binary)
#img_binary =morphology.closing(img_binary > thresh, morphology.square(1))

#img_binary =morphology.closing(img_binary)
#img_binary =morphology.opening(img_binary)

plt.subplot(131)
io.imshow(img)
plt.title('draft')

labels = measure.label(img_binary)
dst = label2rgb(labels)
#io.imsave('labels.png',dst)

plt.subplot(132)
io.imshow(img_binary)
plt.title('binary')
io.imsave('b_'+str(sys.argv[1])[0:-4]+'.png', img_binary)

plt.subplot(133)
io.imshow(dst)
plt.title('labels')

plt.show()
