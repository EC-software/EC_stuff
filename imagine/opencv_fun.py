import cv2
import numpy as np
from matplotlib import pyplot as plt

# inpired by: http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_canny/py_canny.html


def show_colour_transforms():
    for flag in [i for i in dir(cv2) if i.startswith('COLOR_')]:
        if flag.startswith('COLOR_BGR'):
            print flag
    return 0

def treshold_test(str_fn):
    img = cv2.imread(str_fn, 0)
    low, hig = 96,255
    ret, thresh1 = cv2.threshold(img, low, hig, cv2.THRESH_BINARY)
    ret, thresh2 = cv2.threshold(img, low, hig, cv2.THRESH_BINARY_INV)
    ret, thresh3 = cv2.threshold(img, low, hig, cv2.THRESH_TRUNC)
    ret, thresh4 = cv2.threshold(img, low, hig, cv2.THRESH_TOZERO)
    ret, thresh5 = cv2.threshold(img, low, hig, cv2.THRESH_TOZERO_INV)

    titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
    images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

    for i in xrange(6):
        plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])

    plt.show()

def treshold_adaptive_test(str_fn):
    img = cv2.imread(str_fn, 0)

    # global thresholding
    ret1, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    # Otsu's thresholding
    ret2, th2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Otsu's thresholding after Gaussian filtering
    blur = cv2.GaussianBlur(img, (5, 5), 0)
    ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # plot all the images and their histograms
    images = [img, 0, th1,
              img, 0, th2,
              blur, 0, th3]
    titles = ['Original Noisy Image', 'Histogram', 'Global Thresholding (v=127)',
              'Original Noisy Image', 'Histogram', "Otsu's Thresholding",
              'Gaussian filtered Image', 'Histogram', "Otsu's Thresholding"]

    for i in xrange(3):
        plt.subplot(3, 3, i * 3 + 1), plt.imshow(images[i * 3], 'gray')
        plt.title(titles[i * 3]), plt.xticks([]), plt.yticks([])
        plt.subplot(3, 3, i * 3 + 2), plt.hist(images[i * 3].ravel(), 256)
        plt.title(titles[i * 3 + 1]), plt.xticks([]), plt.yticks([])
        plt.subplot(3, 3, i * 3 + 3), plt.imshow(images[i * 3 + 2], 'gray')
        plt.title(titles[i * 3 + 2]), plt.xticks([]), plt.yticks([])
    plt.show()

def highpass_test(str_fn):
    img = cv2.imread(str_fn, 0)

    laplacian = cv2.Laplacian(img, cv2.CV_64F)
    #ret1, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    #ret2, th2 = cv2.threshold(laplacian, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=-1)
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=-1)

    plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
    plt.title('Original'), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 2, 2), plt.imshow(laplacian, cmap='gray') # laplacian, cmap='gray')
    plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 2, 3), plt.imshow(sobelx, cmap='gray')
    plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 2, 4), plt.imshow(sobely, cmap='gray')
    plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

    plt.show()

def canny_test(str_fn):
    img = cv2.imread(str_fn, 0)
    edges = cv2.Canny(img, 100, 200)
    plt.subplot(121), plt.imshow(img, cmap='gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(edges, cmap='gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    plt.show()

def houghlines_test(str_fn):
    img = cv2.imread(str_fn)
    img_org = img
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)
    for rho, theta in lines[0]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
    cv2.imwrite('h'+str_fn, img)

    plt.subplot(121), plt.imshow(img_org, cmap='gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(img, cmap='gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    plt.show()


def houghlines2_test(str_fn):
    img = cv2.imread(str_fn)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    minLineLength = 100
    maxLineGap = 10
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength, maxLineGap)
    for x1, y1, x2, y2 in lines[0]:
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

    cv2.imwrite('houghlines2.jpg', img)


if __name__ == "__main__":

    ## images
    str_fn = r"/home/martin/PycharmProjects/sudoku/data/images/pol20171201.jpg" # rather nice
    #str_fn = r"/home/martin/PycharmProjects/sudoku/data/images/pol20170825.jpg" # cener fold
    #str_fn = r"/home/martin/PycharmProjects/sudoku/data/images/pol20170909.jpg" # mixed light
    str_fn = r"/home/martin/PycharmProjects/sudoku/data/images/pol20170917.jpg" # super nice
    #str_fn = r"/home/martin/PycharmProjects/sudoku/data/images/gradients01.jpg" # super nice

    ## routines
    #canny_test(str_fn)
    #show_colour_transforms()
    #treshold_test(str_fn)
    #treshold_adaptive_test(str_fn)  # Gaussian + Otsu give good results for (no shadow) Sudoku :-)
    #highpass_test(str_fn)
    #canny_test(str_fn)
    #houghlines_test(str_fn)
    houghlines2_test(str_fn)

# Later :
# Perspective transform:
#   Then transformation matrix can be found by the function cv2.getPerspectiveTransform. Then apply cv2.warpPerspective with this 3x3 transformation matrix.
# Consider Open and Close, before identifying numbers
# Template matching for number recognition
#   http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_template_matching/py_template_matching.html
