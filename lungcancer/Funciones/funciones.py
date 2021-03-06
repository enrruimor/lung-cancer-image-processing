import os
from glob import glob

import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage
import SimpleITK as sitk
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from plotly.graph_objs import *
from plotly.offline import  iplot
from plotly.tools import FigureFactory as FF
from skimage import measure


def lung_segmentation(img_original, seedList):
    """Este método recibe una array N-dimensional con valores de intensidad en 
    escala HU (imagen) y dos puntos (x,y,z) que son las semillas del crecimiento de regiones"""

    # Aplicamos el filtro de suavizado gaussiano
    img = sitk.DiscreteGaussian(img_original, 10)
    # Obtenemos el crecimiento de regiones partiendo de la lista de semillas
    # El resultado es una imagen binarizada.

    img = sitk.ConnectedThreshold(img, seedList, lower=-1000.0, upper=-200.0)

    # Realizamos un cierre morfológico para unir pequeñas regiones separadas
    img = sitk.BinaryMorphologicalClosing(img, 12, sitk.sitkBall)

    #Convertimos la imagen binaria en el mismo tipo que la imagen original
    img = sitk.Cast(img, sitk.sitkInt16)

    #Como dentro de la escala HU etá incluido el 0, vamos a sumar 1024 para que al multiplicar, el menor valor de la nueva
    #escala sea 0
    img_original = img_original + 1024

    #Realizamos la segmentación de los pulmones
    img_segmentada = sitk.Multiply(img, img_original)

    #Reescalamos a HU
    img_segmentada = img_segmentada-1024

    # Devolvemos la imagen de los pulmones segmentados
    return img_segmentada





def mostrar_slice(image, n_slice=None):
    if not isinstance(image, np.ndarray):
        img = sitk.GetArrayFromImage(image)
        new_array = np.array(np.swapaxes(img, 0, 2))
        new_array = np.array(np.swapaxes(new_array, 0, 1))

    else:
        new_array = image

    #Para encontrar el nodulo mostrar aquellas slices que tengan
    #un valor maximo mayor que 0

    if n_slice == None:
        n_slice = new_array.shape[2]//2

    plt.imshow(new_array[:, :, n_slice], cmap="gray")
    #plt.imshow(new_array[new_array.shape[0]//2, :, :], cmap="gray")

    plt.show()


def obtener_array(imagen_sitk):
    """Dada una imagen itk la transformamos a np array y colocamos
    las componentes de manera adecuada. """
    img = sitk.GetArrayFromImage(imagen_sitk)
    new_array = np.array(np.swapaxes(img, 0, 2))
    new_array = np.array(np.swapaxes(new_array, 0, 1))

    return new_array




def resample(image, dim,  new_spacing=[1, 1, 1]):
    # Determine current pixel spacing
    spac = list(image.GetSpacing()[:2])
    spacing = map(float, (dim + spac))
    spacing = np.array(list(spacing))

    img_arr = sitk.GetArrayFromImage(image)
    resize_factor = spacing / new_spacing
    new_real_shape = img_arr.shape * resize_factor
    new_shape = np.round(new_real_shape)
    real_resize_factor = new_shape / img_arr.shape
    new_spacing = spacing / real_resize_factor

    image = scipy.ndimage.interpolation.zoom(img_arr, real_resize_factor)

    return image, new_spacing


def make_mesh(image, level=None, step_size=1):
    print("Transposing surface")
    p = image.transpose(2, 1, 0)

    print("Calculating surface")
    verts, faces, norm, val = measure.marching_cubes_lewiner(
        p, level, step_size=step_size, allow_degenerate=True)
    return verts, faces


def plotly_3d(verts, faces):
    x, y, z = zip(*verts)

    print("Drawing")

    # Make the colormap single color since the axes are positional not intensity.
    #    colormap=['rgb(255,105,180)','rgb(255,255,51)','rgb(0,191,255)']
    colormap = ['rgb(236, 236, 212)', 'rgb(236, 236, 212)']

    fig = FF.create_trisurf(x=x,
                            y=y,
                            z=z,
                            plot_edges=False,
                            colormap=colormap,
                            simplices=faces,
                            backgroundcolor='rgb(64, 64, 64)',
                            title="Interactive Visualization")
    iplot(fig)


def plt_3d(verts, faces):
    print("Drawing")
    x, y, z = zip(*verts)
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')

    # Fancy indexing: `verts[faces]` to generate a collection of triangles
    mesh = Poly3DCollection(verts[faces], linewidths=0.05, alpha=1)
    face_color = [1, 1, 0.9]
    mesh.set_facecolor(face_color)
    ax.add_collection3d(mesh)

    ax.set_xlim(0, max(x))
    ax.set_ylim(0, max(y))
    ax.set_zlim(0, max(z))
    ax.set_facecolor((0.7, 0.7, 0.7))
    plt.show()


def obterner_array_overlay(pulmones_sitk, nodulo_sitk):
    """pulmones_sitk es la segmentación de los pulmones, nodulo_sitk es una
    mascara del nodulo cancerigeno """
    nodulo_sitk.CopyInformation(pulmones_sitk)
    pulmones_sitk = sitk.RescaleIntensity(pulmones_sitk, 0, 255)
    pulmones_sitk = sitk.Cast(pulmones_sitk, sitk.sitkUInt8)
    nodulo_sitk = sitk.Cast(nodulo_sitk, sitk.sitkUInt8)
    overlay = sitk.LabelOverlay(
        pulmones_sitk, nodulo_sitk, opacity=0.3, backgroundValue=0)

    return obtener_array(overlay)


def obtener_slice_nodulo(nodulo_sitk):
    nodulo_array = obtener_array(nodulo_sitk)
    pixeles_mayor, indice_mayor = 0, 0

    for i in range(nodulo_array.shape[2]):
        pixeles_actual = np.sum(nodulo_array[:, :, i])
        if pixeles_actual > pixeles_mayor:
            pixeles_mayor = pixeles_actual
            indice_mayor = i
        if pixeles_actual < pixeles_mayor:
            break

    return indice_mayor
