import cv2
import sys
import os.path

def detect(filename, cascade_file = "../lbpcascade_animeface.xml"):
    if not os.path.isfile(cascade_file):
        raise RuntimeError("%s: not found" % cascade_file)

    cascade = cv2.CascadeClassifier(cascade_file)
    image = cv2.imread(filename, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    faces = cascade.detectMultiScale(gray,
                                     # detector options
                                     scaleFactor = 1.01,
                                     minNeighbors = 30,
                                     minSize = (24, 24))
    ctr = 0
    for (x, y, w, h) in faces:
        crop_image=image[y:y+h,x:x+w]
        cv2.imwrite("face%d.png"%(ctr), crop_image)
        ctr += 1
    
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow("AnimeFaceDetect", image)
    cv2.waitKey(0)
    cv2.imwrite("out.png", image)

if len(sys.argv) != 2:
    sys.stderr.write("usage: detect.py <filename>\n")
    sys.exit(-1)

detect(sys.argv[1])
