import PyQt5.QtWidgets as qtw
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
import tensorflow as tf
import numpy as np

IMG_HEIGHT = 224
IMG_WIDTH = 224

print(tf.__version__)
class_names = ['EOSINOPHIL', 'LYMPHOCYTE', 'MONOCYTE', 'NEUTROPHIL']
model = tf.keras.models.load_model('test_model.h5')

def prediction_from_path(model, path):
    img = tf.keras.utils.load_img(
        path, target_size=(IMG_HEIGHT, IMG_WIDTH)
    )

    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch

    predictions = model.predict(img_array)
    max_index = np.argmax(predictions[0])
    return (class_names[max_index], '{:.2f}'.format(predictions[0][max_index] * 100))

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('wbc-detection')
        self.setGeometry(0, 0, 500, 400)
        self.setLayout(qtw.QVBoxLayout())
        btn1 = qtw.QPushButton('Upload')
        btn1.clicked.connect(self.browseImage)
        btn1.setStyleSheet("""
        QWidget {
            border: 2px solid #fff;
            border-radius: 10px;
            width: 70%;
            height: 40%;
            }
        """)
        self.layout().addWidget(btn1)
        self.setStyleSheet("""text-align: center; width: 100%; height: 100%; background-color: #121212; color: #fff;""")
        self.label = qtw.QLabel('Upload image to check type')
        self.label.setStyleSheet("""
        QWidget {
            padding: 15px 0;
            width: 224px;
            height: 224px;
            }
        """)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.layout().addWidget(self.label)
        self.cellType = qtw.QLabel('')
        self.cellType.setAlignment(QtCore.Qt.AlignCenter)
        
        self.layout().addWidget(self.cellType)

        self.show()
    def browseImage(self):
        fname = qtw.QFileDialog.getOpenFileName(self, 'Opening file', 'c\\', 'JPEG File (*.jpeg)')
        imagePath = fname[0]
        pixmap = QPixmap(imagePath)
        self.label.setPixmap(QPixmap(pixmap))
        #self.resize(pixmap.width(), pixmap.height())
        cellType, confidence = prediction_from_path(model, imagePath)
        self.cellType.setText(f'{cellType} - {confidence}%')
        self.cellType.setStyleSheet("""
        QWidget {
            border: 2px solid #fff;
            border-radius: 10px;
            height: 40px;
            }
        """)

app = qtw.QApplication([])
mw = MainWindow()
app.exec_()