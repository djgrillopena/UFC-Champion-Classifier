import face_recognition
from PIL import Image, ImageDraw
from matplotlib.pyplot import fill
import os

testpath = "./img/fights"

image_of_adesanya = face_recognition.load_image_file('./img/known/Adesanya.jpg')
adesanya_face_encoding = face_recognition.face_encodings(image_of_adesanya)[0]

image_of_figueredo = face_recognition.load_image_file('./img/known/Figueredo.jpg')
figueredo_face_encoding = face_recognition.face_encodings(image_of_figueredo)[0]

image_of_namajunas = face_recognition.load_image_file('./img/known/Namajunas.jpg')
namajunas_face_encoding = face_recognition.face_encodings(image_of_namajunas)[0]

image_of_ngannou = face_recognition.load_image_file('./img/known/Ngannou.jpg')
ngannou_face_encoding = face_recognition.face_encodings(image_of_ngannou)[0]

image_of_nunes = face_recognition.load_image_file('./img/known/Nunes.jpg')
nunes_face_encoding = face_recognition.face_encodings(image_of_nunes)[0]

image_of_oliveira = face_recognition.load_image_file('./img/known/Oliveira.jpg')
oliveira_face_encoding = face_recognition.face_encodings(image_of_oliveira)[0]

image_of_pena = face_recognition.load_image_file('./img/known/Pena.jpg')
pena_face_encoding = face_recognition.face_encodings(image_of_pena)[0]

image_of_schevchenko = face_recognition.load_image_file('./img/known/Schevchenko.jpg')
schevchenko_face_encoding = face_recognition.face_encodings(image_of_schevchenko)[0]

image_of_sterling = face_recognition.load_image_file('./img/known/Sterling.jpg')
sterling_face_encoding = face_recognition.face_encodings(image_of_sterling)[0]

image_of_texeira = face_recognition.load_image_file('./img/known/Texeira.jpg')
texeira_face_encoding = face_recognition.face_encodings(image_of_texeira)[0]

image_of_usman = face_recognition.load_image_file('./img/known/Usman.jpg')
usman_face_encoding = face_recognition.face_encodings(image_of_usman)[0]

image_of_volkanovski = face_recognition.load_image_file('./img/known/Volkanovski.jpg')
volkanovski_face_encoding = face_recognition.face_encodings(image_of_volkanovski)[0]

known_face_encodings = [
    adesanya_face_encoding,
    figueredo_face_encoding,
    namajunas_face_encoding,
    ngannou_face_encoding,
    nunes_face_encoding,
    oliveira_face_encoding,
    pena_face_encoding,
    schevchenko_face_encoding,
    sterling_face_encoding,
    texeira_face_encoding,
    usman_face_encoding,
    volkanovski_face_encoding,
]

known_face_names = [
    "MiddleW_Champ:Israel Adesanya",
    "FlyW_Champ:Davidson Figueredo",
    "W_StrawW_Champ:Rose Namajunas",
    "HeavyW_Champ:Francis Ngannou",
    "W_FeatherW_Champ:Amanda Nunes",
    "LightW_Champ:Charles Oliveira",
    "W_BantamW_Champ:Julianna Peña",
    "W_FlyW_Champ:Valentina Schevchenko",
    "BantamW_Champ:Aljamain Sterling",
    "LightHeavyW_Champ:Glover Texeira",
    "WelterW_Champ:Kumaru Usman",
    "FeatherW_Champ:Alexander Volkanovski"
]

testfiles = [testpath+"/"+ file for file in os.listdir(testpath)]

for testfile in testfiles:

    #test_image = face_recognition.load_image_file('./img/groups/group6.jpg')
    test_image = face_recognition.load_image_file(testfile)

    face_locations = face_recognition.face_locations(test_image)
    face_encodings = face_recognition.face_encodings(test_image, face_locations)

    pil_image = Image.fromarray(test_image)

    draw = ImageDraw.Draw(pil_image)

    for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):

        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "NotChamp"

        if True in matches:

            first_match_index = matches.index(True)
            #name = "known_face_names[first_match_index]"
            name = "UFCChamp"

        draw.rectangle(((left, top), (right, bottom)), outline = "#d4af37")

        text_width, text_height = draw.textsize(name)
        draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0,0,0), outline="#d4af37")
        draw.text((left + 6, bottom - text_height - 5), name, fill = (255, 255, 255, 255))

    del draw

    pil_image.save(f"./img/results/{testfile.split('/')[-1]}_detected.jpg")
    print(f"Detection for {testfile.split('/')[-1]} completed")