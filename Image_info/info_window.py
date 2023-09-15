import pathlib
import sys

from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg
from PIL import Image, ImageQt

from Image_info.UI.Image_info import Ui_mw_image_info


class TableModel(qtc.QAbstractTableModel):
    i = 0
    im_data = []

    def __init__(self, data):
        super().__init__()
        self.image_data = data
        for key in data.keys():
            print("woow", data[key])
            self.im_data.append(str(key))
            self.im_data.append(str(data[key]))

    def rowCount(self, parent=qtc.QModelIndex()):
        print("policzyło", len(self.image_data))
        return len(self.image_data)

    def columnCount(self, parent=qtc.QModelIndex()):
        print("kolumny...")
        return 2

    def data(self, index, role=qtc.Qt.ItemDataRole.DisplayRole):
        print("jestem w data!")

        if role == qtc.Qt.ItemDataRole.DisplayRole:
            try:
                if index.row() == 0:

                    return self.im_data[index.row() + index.column()]
                else:
                    return self.im_data[index.row() * 2 + index.column()]
            except IndexError:
                print("Index Error!!")


class ImageInfo(qtw.QWidget, Ui_mw_image_info):

    def __init__(self, data):
        super().__init__()
        self.data_model = TableModel(data)
        self.setupUi(self)
        print("bbbbbbb")
        self.tableView.setModel(self.data_model)
        self.show()
        print("xoxoxoxo")


_data = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = ImageInfo(_data)
    window.show()

    sys.exit(app.exec())
