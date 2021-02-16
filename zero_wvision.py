import numpy as np
import cv2
import time
while True:
    filename = str(time.strftime('%S')) + '.png'
    blank_image = np.zeros(shape=[512, 512, 3], dtype=np.uint8)
    white_image = 255 * np.ones(shape=[512, 512, 3], dtype=np.uint8)

    cv2.line(blank_image, (5, 5), (512, 5), (150 + 2 * int(time.strftime("%S")), 0, 0), thickness=5)
    cv2.rectangle(blank_image, (10, 10), (75, 60), (0, 255, 0), thickness=1)
    cv2.putText(blank_image, str(time.strftime("%S")), (10, 50), 1, cv2.FONT_HERSHEY_COMPLEX, (0, 0, 255), thickness=2)
    cv2.imshow("Black Blank", blank_image)
    cv2.imshow("White Blank", white_image)
    cv2.imwrite(filename, white_image)
    if cv2.waitKey(30) & 0xFF == ord('q'):

        cv2.destroyAllwindows()
        break
