# ! /usr/bin/env python

import cv2 as cv
import numpy as np

img1 = cv.imread('image/woods3.jpg')
img2 = cv.imread('image/woods1.jpg')
gray1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY,0)
gray2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY,0)
print("Image Read Complete")

# ORB, FLANN
# https://docs.opencv.org/3.4/db/d95/classcv_1_1ORB.html#adc371099dc902a9674bd98936e79739c
detector = cv.ORB_create(nfeatures=500)
kp1, desc1 = detector.detectAndCompute(gray1, None)
kp2, desc2 = detector.detectAndCompute(gray2, None)

index_params= dict(algorithm = 6, table_number = 6, key_size = 12, multi_probe_level = 1)
search_params = dict(checks=10)

matcher = cv.FlannBasedMatcher(index_params,search_params)
matches = matcher.knnMatch(desc1,desc2,k=2)

print("Keypoint and Description and Macthing Complete")

# Good Matching Point
ratio_thresh = 0.75
good_matches = [m for m,n in matches if m.distance < ratio_thresh * n.distance]

result = cv.drawMatches(img1, kp1, img2, kp2, good_matches, None, flags=2)

cv.imshow("ORB+FLANN",result)
cv.waitKey()
cv.destroyAllWindows()

if __name__ == "__main__":
    