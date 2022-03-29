# UFC-Champion-Classifier
Created a UFC champion classifier using Python face_recognition library. Able to determine through face encodings whether a given individual is a current UFC champion in any of the 12 different weight divisions.

Steps:

1. Created an environment in Anaconda Navigator, with a donwgraded Python 3.6 version.
2. Installed all the required libraries, including numpy, dlib, and face_recognition.
3. Created a Python file called findFaces.py, which looks at an image of people, recognizes the faces, and counts the number of faces in the image.
4. Created a Python file called faceCompare.py, which compares images and determines whether the same person is in both the images or not.
5. Created a Python file called faceExtract.py, which takes a picture as input, extracts detected faces as output and saves them.
6. Created a Python file called detect.py, which takes a picture as input, detects the faces present in the input image and labels them as UFC Champion or Not UFC Champion.

This is a work in progress, the system currently works with images, however, the end goal is to have a fully functioning system able to detect UFC Champions in video data, or image data.
