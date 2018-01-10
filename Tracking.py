'''
Detect and show object.
From https://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/
'''
import cv2
import Sources
import sys


class Tracking:
    def __init__(self):
        self._colorUpper = Sources.colorUpper
        self._colorLower = Sources.colorLower
        self._camera = None
        self._frame = None
    
    def getVideo(self, adres):
        self._camera = cv2.VideoCapture(adres)
    
    def trackFrame(self):
        (grabbed, self._frame) = self._camera.read()
        
        if not grabbed:
            return -1
        
        hsv = cv2.cvtColor(self._frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, self._colorLower, self._colorUpper)
        
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)[-2]
        center = None
        if len(cnts) > 0:
            c = max(cnts, key=cv2.contourArea)
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            
#            YNormal[1] = Sources.LensResolutionScaled[1] - center[1]
            YNormal = Sources.LensResolution[1] - center[1]
            return [center[0], YNormal]
        return center
        
    def showFrame(self):
        cv2.imshow("Frame", self._frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            self.stop()
            sys.exit()
    
    def stop(self):
        self._camera.release()
        cv2.destroyAllWindows()
