import cv2


def compare_images(img, second_img):
    """Returns True if images is equal, else - False. Images expansion does not matter
    Details: https://www.bogotobogo.com/python/OpenCV_Python/python_opencv3_image_histogram_calcHist.php"""
    first_image = cv2.imread(img)
    second_image = cv2.imread(second_img)
    first_image_hist = cv2.calcHist([first_image], [0], None, [256], [0, 256])
    second_image_hist = cv2.calcHist([second_image], [0], None, [256], [0, 256])
    img_hist_diff = cv2.compareHist(first_image_hist, second_image_hist, cv2.HISTCMP_BHATTACHARYYA)
    if img_hist_diff == 0:
        return True
    else:
        return False


def image_search_in_image(base_image, looking_for_img):
    """Returns True if looking_for_img in base_image, else - False
    By default corellation coeffitient equal to 0.99"""
    base_image = cv2.imread(base_image)
    looking_for_img = cv2.imread(looking_for_img)
    result = cv2.matchTemplate(base_image, looking_for_img, cv2.TM_CCOEFF_NORMED)
    corellation_coeffitient = 0
    for i in result:
        if max(i) > corellation_coeffitient:
            corellation_coeffitient = max(i)
    if corellation_coeffitient >= 0.99:
        return True
    else:
        return False
