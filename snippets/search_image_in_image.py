import cv2
import numpy as np

first_image = "image_2020_12_17T09_57_35_397Z.png"
second_image = "image_2020_12_17T09_59_40_825Z.png"
img_for_search = "image_must_be_in_first_img.png"


def image_search_in_image(base_image, looking_for_img):
    """Returns True if looking_for_img in base_image, else - False"""
    base_image = cv2.imread(base_image)
    looking_for_img = cv2.imread(looking_for_img)
    # result = cv2.matchTemplate(base_image, looking_for_img, cv2.TM_SQDIFF_NORMED)
    result = cv2.matchTemplate(base_image, looking_for_img, cv2.TM_CCOEFF)
    (_, _, minLoc, maxLoc) = cv2.minMaxLoc(result)
    print(result)
    (waldoHeight, waldoWidth) = looking_for_img.shape[:2]
    topLeft = maxLoc
    botRight = (topLeft[0] + waldoWidth, topLeft[1] + waldoHeight)
    roi = base_image[topLeft[1]:botRight[1], topLeft[0]:botRight[0]]
    mask = np.zeros(base_image.shape, dtype="uint8")
    puzzle = cv2.addWeighted(base_image, 0.25, mask, 0.75, 0)
    puzzle[topLeft[1]:botRight[1], topLeft[0]:botRight[0]] = roi
    cv2.imshow("Puzzle", puzzle)
    cv2.imshow("Waldo", looking_for_img)
    cv2.waitKey(0)


image_search_in_image(first_image, img_for_search)
