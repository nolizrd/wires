import numpy as np 
import matplotlib.pyplot as plt
from skimage.morphology import (binary_erosion, binary_dilation, binary_closing, binary_opening)

from skimage.measure import label 

wires=np.load("wires5.npy")
labeled=label(wires)

struct=np.ones((3,1))
for lb in range(1, np.max(labeled)+1):
    new_image=np.zeros_like(wires) #переносим провод в новый массив, один провод с меткой 2
    new_image[labeled==lb] = 1
    new_er=(binary_erosion(new_image,struct))
    new_labeled=label(new_er)
    print (new_labeled.max())

plt.subplot(121)
plt.imshow(label(wires))
plt.imshow(wires)
plt.subplot(122)
plt.imshow (binary_erosion(wires, struct))
#plt.imshow(new_labeled)
plt.show()


#маркировка отделить
#морфология 