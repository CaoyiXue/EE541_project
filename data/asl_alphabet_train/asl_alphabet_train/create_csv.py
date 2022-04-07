"""
create csv for asl_alphabet_train data
"""
import glob
import csv
import os

classes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
           'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z', 'nothing', 'space', 'del']
label_map = {}
for id, cl in enumerate(classes):
    label_map[cl] = id
with open('asl_alphabet_train.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    header = ['image_relative_path', 'label']
    csv_writer.writerow(header)

    for cl in classes:
        for f in glob.glob(os.path.join(cl, '*.jpg')):
            row = [f, label_map[cl]]
            csv_writer.writerow(row)
