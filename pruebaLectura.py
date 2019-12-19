import pydicom
import numpy as np
import matplotlib.pyplot as plt
import SimpleITK as sitk
import funciones

import sys
import os

# load the DICOM files
files = []
directorio = "./database/0/"
for fname in os.listdir(directorio):

    if fname[-3::] == "dcm":
        print("loading: {}".format(directorio+"/"+fname))
        files.append(pydicom.read_file(directorio+"/"+fname))

print("file count: {}".format(len(files)))

# skip files with no SliceLocation (eg scout views)
slices = []
skipcount = 0
for f in files:
    if hasattr(f, 'SliceLocation'):
        slices.append(f)
    else:
        skipcount = skipcount + 1


# ensure they are in the correct order
slices = sorted(slices, key=lambda s: s.SliceLocation)

print("skipped, no SliceLocation: {}".format(skipcount))


# pixel aspects, assuming all slices are the same
ps = slices[0].PixelSpacing
ss = slices[0].SliceThickness
ax_aspect = ps[1]/ps[0]
sag_aspect = ps[1]/ss
cor_aspect = ss/ps[0]

# create 3D array
img_shape = list(slices[0].pixel_array.shape)
img_shape.append(len(slices))
img3d = np.zeros(img_shape)

# fill 3D array with the images from the files
for i, s in enumerate(slices):
    img2d = s.pixel_array
    img3d[:, :, i] = img2d


# plot 3 orthogonal slices
a1 = plt.subplot(2, 2, 1)
plt.imshow(img3d[:, :, img_shape[2]//2], cmap="gray")
a1.set_aspect(ax_aspect)

# a2 = plt.subplot(2, 2, 2)
# plt.imshow(img3d[:, img_shape[1]//2, :], cmap="gray")
# a2.set_aspect(sag_aspect)

# a3 = plt.subplot(2, 2, 3)
# plt.imshow(img3d[img_shape[0]//2, :, :].T, cmap="gray")
# a3.set_aspect(cor_aspect)

# plt.show()

img_3d_hu = funciones.get_pixels_hu(slices)

s1 = (150, 250, img_shape[2]//2)
img_binaria = funciones.lung_segmentation(img_3d_hu, s1, s1)


plt.imshow(img_binaria[:, :, img_shape[2]//2], cmap="gray")
plt.imshow(img_3d_hu[:, :, img_shape[2]//2], cmap="gray")
