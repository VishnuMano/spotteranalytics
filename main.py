import easyocr
import torch
import cv2
import imutils
import numpy as np
from matplotlib import pyplot as plt


def read_plate(file):
    img = cv2.imread(file)

    # Convert Imgage to Greyscale (Not able to run on Collab)
    # grey = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # grey = cv2.bilateralFilter(grey, 13, 15, 15)

    # Finding Canny Edges (change img to grey once grey is working)
    edged = cv2.Canny(img, 30, 200)

    # Finding Contours
    contours = cv2.findContours(edged,
                                cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for c in contours:
        p = cv2.arcLength(c, True)
        con = cv2.approxPolyDP(c, 0.018 * p, True)

        if len(con) == 4:
            screenCnt = con
            break

    mask = np.zeros(img.shape, np.uint8)
    new_image = cv2.drawContours(mask, [screenCnt], 0, 255, -1, )
    new_image = cv2.bitwise_and(img, img, mask=mask)

    reader = easyocr.Reader(['en'])
    result = reader.readtext(img, paragraph=True, detail=0)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    read_plate('https://t3.ftcdn.net/jpg/04/21/63/30/360_F_421633077_ifam5iJ1NuqeO6kSvlg9jWsuSEAUyK6X.jpg')
