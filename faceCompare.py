import face_recognition

image_of_valentina = face_recognition.load_image_file('./img/known/valentina_test.jpg')
valentina_face_encoding = face_recognition.face_encodings(image_of_valentina)[0]

u_img = face_recognition.load_image_file('./img/unknown/pena_unknown.jpg')
u_img_enc = face_recognition.face_encodings(u_img)[0]

results = face_recognition.compare_faces([valentina_face_encoding], u_img_enc)

if results[0]:

    print("This is Valentina Schevchenko")

else:

    print("This is not Valentina Schevchenko")