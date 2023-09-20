from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw

from Image_resize.UI.Image_resize import Ui_mw_image_resize


class ResizeTableModel(qtc.QAbstractTableModel):

    def __init__(self, window):
        super().__init__()
        self._window = window
        self.im_width, self.im_height = window.image_size
    def flags(self, index):
        return qtc.Qt.ItemFlag.ItemIsSelectable|qtc.Qt.ItemFlag.ItemIsEnabled|qtc.Qt.ItemFlag.ItemIsEditable
    def rowCount(self, parent=qtc.QModelIndex()):
        return 2

    def columnCount(self, parent=qtc.QModelIndex()):
        return 2
    def setData(self, index, value, role):

        if role ==qtc.Qt.ItemDataRole.EditRole:
            if index.row() == 0 and index.column() == 1:
                try:
                    self.im_height = int(value)
                    size = self.im_width, self.im_height
                    self._window.change_image_size(size)
                except ValueError as valueError:
                    pass
                except Exception as exception:
                    pass

                return True
            elif index.row() == 1 and index.column() == 1:

                try:
                    self.im_width = int(value)
                    size = self.im_width, self.im_height
                    self._window.change_image_size(size)
                except ValueError as valueError:
                    pass
                except Exception as exception:
                    pass
                return True
            else:
                return False


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

class ImageResize(qtw.QWidget, Ui_mw_image_resize):

    def __init__(self, window):
        super().__init__()
        self._window = window
        self.data_model = ResizeTableModel(window)
        self.setupUi(self)
        self.tv_image_resize.setModel(self.data_model)
        self.show()
    def closeEvent(self, event) -> None:
        if self._window.image_to_edit != None:
            self._window.pb_resize.setEnabled(True)