#!/usr/bin/env python3

import sys
import rospy
import cv2
import time
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class image_converter:

  def __init__(self):
    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("/cessna_0/camera/rgb", Image, self.callback)
    self.prev_time = time.time()

  def callback(self, data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
      print(e)
      return

    # FPS hesapla
    curr_time = time.time()
    fps = 1.0 / (curr_time - self.prev_time)
    self.prev_time = curr_time

    # FPS değerini görüntüye ekle
    cv2.putText(cv_image, f"FPS: {fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    height, width, _ = cv_image.shape

    # Dikdörtgenin köşe koordinatlarını hesapla
    top_left = (int(width * 0.25), int(height * 0.10))
    bottom_right = (int(width * 0.75), int(height * 0.90))

    # Dikdörtgeni çiz
    cv2.rectangle(cv_image, top_left, bottom_right, (0, 255, 0), 2)

    # Görüntüyü göster
    cv2.imshow("Image window", cv_image)
    cv2.waitKey(3)

def main(args):
  ic = image_converter()
  rospy.init_node('image_converter', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':
  main(sys.argv)