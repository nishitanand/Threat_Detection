import cv2
import sys
import os
import numpy as np

#imagePath = sys.argv[1]

#image = cv2.imread(imagePath)
#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


cap = cv2.VideoCapture(0)
i=0
while True:
        ret,image = cap.read()

        if ret==False:
                continue
        i=i+1
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        faces = faceCascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=3, minSize=(30, 30))

        print("[INFO] Found {0} Faces.".format(len(faces)))

        #for (x, y, w, h) in faces:
                #cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                #roi_color = image[y:y + h, x:x + w]
                #print("[INFO] Object found. Saving locally.")
                #cv2.imwrite(str(w) + str(h) + '_faces.jpg', roi_color)

        #status = cv2.imwrite('faces_detected.jpg', image)
        #print("[INFO] Image faces_detected.jpg written to filesystem: ", status)
        for (x1, y1, w1, h1) in faces:
                #cv2.rectangle(image, (x1, y1), (x1 + w1, y1 + h1), (0, 255, 0), 2)
                cv2.imwrite("{0}.jpg".format(i),image)
                os.system("touch {0}.txt".format(i))
                string=str(i)+".txt"
                print(string)

                def convert(size, box):
                        dw = 1. / size[0]
                        dh = 1. / size[1]
                        x_new = (box[0] + box[1]) / 2.0
                        y_new = (box[2] + box[3]) / 2.0
                        w_new = box[1] - box[0]
                        h_new = box[3] - box[2]
                        x_new = x_new * dw
                        w_new = w_new * dw
                        y_new = y_new * dh
                        h_new = h_new * dh
                        return [x_new, y_new, w_new, h_new]

                def convert_to_yolo_label(x1,y1,w2,h2):
                            xmin = x1
                            xmax = x1+w1
                            ymin = y1
                            ymax = y1+h1
                            b = (float(xmin), float(xmax), float(ymin), float(ymax))
                            yolo_box = convert((w2, h2), b)
                            #print(yolo_box)
                            if np.max(yolo_box) > 1 or np.min(yolo_box) < 0: # Take this opportunity to check that conversion works
                                print("BOX HAS AN ISSUE")
                                print(x_new,y_new,w_new,h_new)
                                print(np.max(yolo_box),np.min(yolo_box))
                            else:
                                f=open(string,"w")
                                #f.write("0 "+str(x_new)+" "+str(y_new)+" "+str(w_new)+" "+str(h_new))
                                f.write("1 "+str(yolo_box[0])+" "+str(yolo_box[1])+" "+str(yolo_box[2])+" "+str(yolo_box[3]))
                                f.close()    
                h2,w2=image.shape[:2]
                convert_to_yolo_label(x1,y1,w2,h2)

                
                #f=open(string,"w")
                #f.write("0 "+str(x)+" "+str(y)+" "+str(w)+" "+str(h))
                #f.close()

                        
        key_pressed = cv2.waitKey(1) & 0xFF
        if key_pressed == ord('q'):
                breakpoint

