import os
import csv

os.mkdir('output')
os.mkdir('output/train')
os.mkdir('output/test')

with open('output/train/train_labels.csv', mode='w') as train_labels_csv:
    with open('output/test/test_labels.csv', mode='w') as test_labels_csv:
        train_labels_writer = csv.writer(train_labels_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        test_labels_writer = csv.writer(test_labels_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        images_path = 'unprocessed_data_example\dataset2-master\dataset2-master\images'
        """
            EOSINOPHIL = 0
            LYMPHOCYTE = 1
            MONOCYTE = 2
            NEUTROPHIL = 3
        """
        labels = ['EOSINOPHIL', 'LYMPHOCYTE', 'MONOCYTE', 'NEUTROPHIL']

        for i, label in enumerate(labels):
            train_images = os.listdir(f'{images_path}\TRAIN\{label}')
            test_images = os.listdir(f'{images_path}\TEST\{label}')
            
            for train_image_name in train_images:
                train_labels_writer.writerow([f'/train/images/{train_image_name}', i])
            
            for test_image_name in test_images:
                test_labels_writer.writerow([f'/test/images/{test_image_name}', i])

            break