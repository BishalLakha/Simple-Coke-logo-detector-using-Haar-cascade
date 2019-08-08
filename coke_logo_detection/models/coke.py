import numpy as np
import cv2
from coke_logo_detection.definitions import *
from colorthief import ColorThief


class CokeModel:
    def __init__(self):
        self.coke_model = cv2.CascadeClassifier(MODEL_PATH)
        self.image_path = IMAGE_PATH
        self.width = 640
        self.height = 480

    def _convert_cordinate_to_original(self,coordinate):
        """

        :return:
        """
        (x, y, w, h) = coordinate
        x = int(self.rx * x)
        y = int(self.ry * y)
        w = int(self.rx * w)
        h = int(self.ry * h)

        return (x, y, w, h)

    def detect_coke_logo(self):
        """

        :return:
        """
        self.image_org = cv2.imread(self.image_path)

        height, width, _ = self.image_org.shape
        self.ry = height/self.height
        self.rx = width/self.width

        self.image = cv2.resize(self.image_org, (self.width, self.height))

        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        self.coke_logos = self.coke_model.detectMultiScale(gray,
                                             scaleFactor=1.5,
                                             minNeighbors=10,
                                             minSize=(30, 30),  # (60, 20),
                                             flags=cv2.CASCADE_SCALE_IMAGE
                                             )

        self.valid_logo = []

        for (x, y, w, h) in self.coke_logos:
            cropped_image = self.image[y:y+h, x:x+w]
            cv2.imwrite(CROPPED_IMAGE,cropped_image)
            if self._validate_logo_by_color():
                x,y,w,h = self._convert_cordinate_to_original((x, y, w, h))

                self.valid_logo.append((x,y,w,h))

        if DEBUG:
            for (x, y, w, h) in self.valid_logo:
                cv2.rectangle(self.image_org, (x, y), (x + w, y + h), (0, 255, 0), 2)

            result = cv2.resize(self.image_org, (640,480))
            cv2.imshow("image",result)
            cv2.waitKey(1000)
            cv2.destroyAllWindows()

    @staticmethod
    def _detect_dominant_colors():
        """

        :return:
        """
        color_thief = ColorThief(CROPPED_IMAGE)
        return color_thief.get_palette(color_count=2)

    def _validate_logo_by_color(self):
        """

        :return:
        """
        colors = self._detect_dominant_colors()
        red_count = 0
        white_count = 0
        for r,g,b in colors:
            if r > 180 and g < 50 and b < 50:
                red_count += 1

            if r > 150 and g > 150 and b > 150:
                white_count += 1

        return True if (white_count >= 1 or red_count >= 1) else False

    def json(self):
       """

       :return:
       """
       return {
            "total_coke_logo": len(self.valid_logo),
            "logo_coordinates": self.valid_logo
        }


if __name__ == "__main__":
    a = CokeModel()
    cord = a.detect_coke_logo()



