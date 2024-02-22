# import and setup
import os
import cv2
from paddleocr import PPStructure,save_structure_res

folder = "D:/Users/Davide/Documents/Scuola/Uni/Tirocinio/datasetImages/"
save_folder = "D:/Users/Davide/Documents/Scuola/Uni/Tirocinio/HTML/extracted/"

table_engine = PPStructure(layout=False, show_log=True)

# data extraction
files = os.listdir(folder)

for file in files:
    img_path = folder + file
    img = cv2.imread(img_path)
    result = table_engine(img)
    save_structure_res(result, save_folder, os.path.basename(img_path).split('.')[0])

    for line in result:
        line.pop('img')
        print(line)