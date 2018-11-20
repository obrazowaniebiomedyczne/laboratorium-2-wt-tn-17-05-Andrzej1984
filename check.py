import cv2

from solution import *
from obpng import read_png, write_png


print("- Ocena dostateczna")
renew_pictures()



print("- Ocena dobra")

image = cv2.imread("figures/crushed.png", 0)
erosion = own_simple_erosion(image)
write_png(erosion, "results/own_simple_erosion.png")



print("- Ocena bardzo dobra")

image = cv2.imread("figures/crushed.png", 0)
#read_png("figures/crushed.png")
kernel = np.array([[0, 1, 1, 1, 0],
                   [0, 1, 1, 1, 0],
                   [1, 1, 1, 1, 1],
                   [0, 1, 1, 1, 0],
                   [0, 1, 1, 1, 0]])

erosion = own_erosion(image, kernel)
write_png(erosion, "results/own_erosion.png")

