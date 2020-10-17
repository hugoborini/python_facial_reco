import face_recognition
from PIL import Image, ImageDraw
from lib import *



def img_reco(folder, unKnown):

    tab_img = folderToTab(folder)
    
    image_load_tab = []

    for img in tab_img:
        image_load_tab.append(face_recognition.load_image_file(img))

    known_face_encodings = []
    
    for img_load in image_load_tab:
        img = img_load[0]
        known_face_encodings.append(face_recognition.face_encodings(img_load)[0])
    
    
    known_face_names = folderToTabFront(folder)

    test_image = face_recognition.load_image_file(unKnown)

    face_locations = face_recognition.face_locations(test_image)
    face_encodings = face_recognition.face_encodings(test_image)


    pil_image = Image.fromarray(test_image)

    draw = ImageDraw.Draw(pil_image)

    for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "unknown person"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]


        draw.rectangle(((left, top),(right, bottom)), outline=(0,0,0))
        text_width, text_height = draw.textsize(name)
        draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0,0,0), outline=(0,0,0))
        draw.text((left + 6, bottom - text_height - 5), name, fill=(255,255,255,255))
        del draw
        
        pil_image.show()


