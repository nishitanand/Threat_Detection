Public safety in public areas is nowadays one of the main concerns for governments and companies around the world. There are CCTV cameras everywhere these days- public places, shops, malls, schools etc. But still people are able to commit crimes. **Guns and knives are the most common weapon used in committing crimes.** 

It is estimated that the **concentration of a security guard watching a camera panel decreases catastrophically after 20 minutes**. So many precious lives are lost every year due to crimes using guns and knives. This is because the police or authorities in charge come to the scene of the crime only after the crime has been done and by then it is too late. This is because they are notified very late. 

Surveillance systems still require human supervision and intervention. Video surveillance systems can take advantage from the merging techniques of deep learning to improve their performance and accuracy detecting possible threats. We aim to develop a system which can **detect guns and knives** in real time and thus notify the authorities instantly, so that they can come at the right moment and save lives. 

For object detection we chose **YOLOv4** as compared to other object detection models like Faster R-CNN because it is **very fast and has high Mean Average Precision**.  We then downloaded Training and Validation images and their labels for guns and knives from **Google Open Images Dataset version 6.**

We also changed the **obj.data file, obj.names file and yolov4-obj.cfg file** according to our dataset and classes. Then we trained it on Google Colab for 6000 iterations. Weights were saved after every 100 iterations in the backup folder in google drive and after every 1000 iterations.

Then we checked the mAP and Average IOU of all the saved weight to find which one was the best. The highest Average IOU was achieved in **5500th iteration** weight file and was **73.39%.** So we have used that weight file for all detections and it provided the best results out of all.

Our model is able to successfully find and draw bounding boxes for guns and knives. It also has a high confidence percentage for these bounding boxes. Further we did more tests by varying the height and width and the confidence threshold. We found out these following observations - 

We tried different tests on video clips by varying the height and width. We set width and height to (416,416) and to (608,608) and to (832,832). We observed that the best results were achieved when **height and width were (416,416)**. And also Average FPS (Speed) was fastest for this height and weight.

We also varied the threshold percentage and tested it on more videos. We set the threshold to 0% and 25% and 30% and 40%. We observed and learnt that best results are achieved when confidence **threshold is set to 0.3 or 30%**.
