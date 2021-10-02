from sys import argv
from os import mkdir, listdir, path
from csv import writer, QUOTE_MINIMAL
from shutil import copytree

try:
    input_folder_name = argv[1]
    output_folder_name = argv[2]

    print(f'\nProcessing from {input_folder_name} folder\n')
    mkdir(output_folder_name)
    mkdir(f'{output_folder_name}/train')
    mkdir(f'{output_folder_name}/test')

    with open(f'{output_folder_name}/train/train_labels.csv', mode='w', newline='') as train_labels_csv:
        with open(f'{output_folder_name}/test/test_labels.csv', mode='w', newline='') as test_labels_csv:
            train_labels_writer = writer(train_labels_csv, delimiter=',', quotechar='"', quoting=QUOTE_MINIMAL)
            test_labels_writer = writer(test_labels_csv, delimiter=',', quotechar='"', quoting=QUOTE_MINIMAL)

            images_path = f'{input_folder_name}\dataset2-master\dataset2-master\images'

            labels = ['EOSINOPHIL', 'LYMPHOCYTE', 'MONOCYTE', 'NEUTROPHIL']
            """
                EOSINOPHIL = 0
                LYMPHOCYTE = 1
                MONOCYTE = 2
                NEUTROPHIL = 3
            """

            for i, label in enumerate(labels):
                train_label_path = path.join(images_path, 'TRAIN', label)
                test_label_path = path.join(images_path, 'TEST', label)

                train_images = listdir(train_label_path)
                test_images = listdir(test_label_path)
                print(f'Copying and Labelling {len(train_images)} train images and {len(test_images)} test images for {label}')

                for train_image_name in train_images:
                    train_labels_writer.writerow([f'/train/{train_image_name}', i])
                
                for test_image_name in test_images:
                    test_labels_writer.writerow([f'/test/{test_image_name}', i])
                
                copytree(train_label_path, path.join(f'{output_folder_name}', 'train', 'images'), dirs_exist_ok=True)
                copytree(test_label_path, path.join(f'{output_folder_name}', 'test', 'images'), dirs_exist_ok=True)

    success_message = f'Successfuly processed data into {output_folder_name} folder'
    print(f'\n{"-" * len(success_message)}\n{success_message}\n{"-" * len(success_message)}')
except:
    fail_message = 'Something failed'
    print(f'\n{"-" * len(fail_message)}\n{fail_message}\n{"-" * len(fail_message)}')