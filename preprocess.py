from sys import argv
from os import error, mkdir, listdir, path
from shutil import copytree

try:
    input_folder_name = argv[1]
    output_folder_name = argv[2]

    print(f'\nProcessing from {input_folder_name} folder\n')
    mkdir(output_folder_name)
    mkdir(path.join(output_folder_name, 'data'))
    mkdir(path.join(output_folder_name, 'manual_test'))

    images_path = f'{input_folder_name}\dataset2-master\dataset2-master\images'

    labels = ['EOSINOPHIL', 'LYMPHOCYTE', 'MONOCYTE', 'NEUTROPHIL']

    for i, label in enumerate(labels):
        train_label_path = path.join(images_path, 'TRAIN', label)
        test_label_path = path.join(images_path, 'TEST', label)
        manual_test_label_path = path.join(images_path, 'TEST_SIMPLE', label)

        train_images = listdir(train_label_path)
        test_images = listdir(test_label_path)
        manual_test_images = listdir(manual_test_label_path)

        print(f'Copying {len(train_images)} train images and {len(test_images)} test images for {label}')

        copytree(train_label_path, path.join(f'{output_folder_name}', 'data', label), dirs_exist_ok=True)
        copytree(test_label_path, path.join(f'{output_folder_name}', 'data', label), dirs_exist_ok=True)
        copytree(manual_test_label_path, path.join(f'{output_folder_name}', 'manual_test', label), dirs_exist_ok=True)

    success_message = f'Successfuly processed data into {output_folder_name} folder'
    print(f'\n{"-" * len(success_message)}\n{success_message}\n{"-" * len(success_message)}')
except error:
    fail_message = 'Something failed'
    print(f'\n{"-" * len(fail_message)}\n{fail_message}\n{"-" * len(fail_message)}')
    print(error)