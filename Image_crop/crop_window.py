from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw

from Image_crop.UI.Image_crop import Ui_mw_image_crop


class CropTableModel(qtc.QAbstractTableModel):

    def __init__(self, window):
        super().__init__()
        self._window = window
        self.im_width , self.im_height = window.image_size
    def flags(self, index):
        return qtc.Qt.ItemFlag.ItemIsSelectable|qtc.Qt.ItemFlag.ItemIsEnabled|qtc.Qt.ItemFlag.ItemIsEditable
    def rowCount(self, parent=qtc.QModelIndex()):
        return 2

    def columnCount(self, parent=qtc.QModelIndex()):
        return 2


    def data(self, index, role=qtc.Qt.ItemDataRole.DisplayRole):

        if role == qtc.Qt.ItemDataRole.DisplayRole:
            try:
                if index.row() == 0 and index.column() == 0:

                    return "image height"
                elif index.row() == 0 and index.column() == 1:
                    return self.im_height
                elif index.row() == 1 and index.column() == 0:
                    return "image width"
                else:
                    return self.im_width


            except IndexError:
                print("Index Error!!")



class ImageCrop(qtw.QWidget, Ui_mw_image_crop):

    point1 = 0,0
    point2 = 0,0

    def __init__(self, window):
        super().__init__()
        self._window = window
        self.data_model = CropTableModel(window)
        self.setupUi(self)
        self.tv_crop_image.setModel(self.data_model)
        self.show()
        self.pb_crop.clicked.connect(self.crop_image)

    def closeEvent(self, event) -> None:
        if self._window.image_to_edit != None:
            self._window.pb_crop.setEnabled(True)
    def crop_image(self):
        if self.le_p1_y.text() != "0" and self.le_p1_x != "0" and self.le_p2_x != "0" and self.le_p2_y != "0":
            self._window.crop_image()



