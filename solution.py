import numpy as np
import obpng
import cv2




# Zadanie na ocenę dostateczną
def renew_pictures():

    image1 = cv2.imread("figures/crushed.png",0)
    image2 = cv2.imread("figures/crushed2.png", 0)
    image3 = cv2.imread("figures/crushed3.png", 0)
    image4 = cv2.imread("figures/crushed4.png", 0)

    kernel = np.ones((3, 3), np.uint8)

    image1 = cv2.morphologyEx(image1, cv2.MORPH_OPEN, kernel)

    image2 = cv2.morphologyEx(image2, cv2.MORPH_CLOSE, kernel)
    image2 = cv2.morphologyEx(image2, cv2.MORPH_OPEN, kernel)

    kernel = np.ones((5, 5), np.uint8)
    image3 = cv2.morphologyEx(image3, cv2.MORPH_CLOSE, kernel)
    image3 = cv2.morphologyEx(image3, cv2.MORPH_OPEN, kernel)

    image4 = cv2.morphologyEx(image4, cv2.MORPH_CLOSE, kernel)
    image4 = cv2.morphologyEx(image4, cv2.MORPH_OPEN, kernel)


    obpng.write_png(image1,"results/crushed.png")
    obpng.write_png(image2, "results/crushed2.png")
    obpng.write_png(image3, "results/crushed3.png")
    obpng.write_png(image4, "results/crushed4.png")

    kernel = np.ones((6, 6), np.uint8)# test z większą maską
    image4 = cv2.morphologyEx(image4, cv2.MORPH_CLOSE, kernel)
    image4 = cv2.morphologyEx(image4, cv2.MORPH_OPEN, kernel)
    obpng.write_png(image4, "results/crushed4maska6px.png")



    pass


# Zadanie na ocenę dobrą
def own_simple_erosion(image):

   new_image = np.zeros(image.shape, dtype=image.dtype)
   for i in range (image.shape[0]-1):
       for j in range (image.shape[1]-1):
           if image[i, j]==0 or image[i-1,j]==0 or image[i+1, j]==0 or image[i, j+1]==0 or image[i, j-1] == 0:

                new_image[i, j] = 0
           else:
               new_image[i, j] = image[i,j]


   return new_image


# Zadanie na ocenę bardzo dobrą
def own_erosion(image, kernel=None):
    new_image = np.zeros(image.shape, dtype=image.dtype)
    if kernel is None:
        kernel = np.array([[0, 1, 0],
                           [1, 1, 1],
                           [0, 1, 0]])


    print (kernel)
    size = kernel.shape
    central = []
    central.append((size[0]/2))
    central.append((size[1]/2))
    central[0] = int (central[0])
    central[1] = int(central[1])
    print(central)

    for x in range(image.shape[0] - 2):
         for y in range(image.shape[1] - 2):  # sprawdzamy po polei pixele obrazu

             for kerX in range(kernel.shape[0]):
                 for kerY in range (kernel.shape[1]):  # i porównanie z wszystkimi elementami jądra
                     if kernel[kerX, kerY] == 1:
                         if image[x-central[0]+kerX, y-central[1]+kerY]==0:
                            new_image[x, y] = 0


                     else :
                         new_image[x, y]= image[x, y]




    # ---------------
    # Do uzupełnienia
    # ---------------

    return new_image
