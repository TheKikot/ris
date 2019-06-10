# import the necessary packages
from scipy.spatial import distance as dist
#import numpy as np
import glob2 as glob
import cv2
import rospy



class Comparer:
    def __init__(self):
        self.bridge = CvBridge()


        # initialize the index dictionary to store the image name
        # and corresponding histograms and the images dictionary
        # to store the images themselves
        self.index = {}
        self.images = {}

        # loop over the image paths
        for imagePath in glob.glob("/ROS/images/*.jpeg"):
            # extract the image filename (assumed to be unique) and
            # load the image, updating the images dictionary
            filename = imagePath[imagePath.rfind("/") + 1:]
            image = cv2.imread(imagePath)
            self.images[filename] = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # extract a 3D RGB color histogram from the image,
            # using 8 bins per channel, normalize, and update
            # the index
            hist = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8],
                                [0, 256, 0, 256, 0, 256])
            hist = cv2.normalize(hist, hist).flatten()
            self.index[filename] = hist

    def compare(self, image):
        cv_image = self.bridge.imgmsg_to_cv2(data, 'bgr8')
        cv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)

        newHist = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8],
                                [0, 256, 0, 256, 0, 256])
        newHist = cv2.normalize(hist, hist).flatten()

        results = {}

        minD = 1000000000000
        name = ""
        for (key, hist) in self.index.items():
            # compute the distance between the two histograms
            # using the method and update the results dictionary
            d = cv2.compareHist(newHist, hist, cv2.HISTCMP_BHATTACHARYYA)
            if(d < minD)
                minD = d
                name = key




def main():

    comparer = Comparer()

    rospy.init_node("image_comparer")
    service = rospy.Service('compare_images', CompareImage, comparer.compare)
    

    try:
        rospy.spin()
    except KeyboardInterrupt:
        print('Shutting down')


if __name__ == '__main__':
    main()
