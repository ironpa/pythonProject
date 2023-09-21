from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw

from Image_pixel_info.UI.Image_pixel_info import Ui_mw_image_pixel_info


class ImagePixelInfoModel(qtc.QAbstractTableModel):
    position = ["X", "Y"]

    def __init__(self, mode, values, pos, img_mode):
        super().__init__()
        self._mode = mode
        self._values = values
        self._pos = pos
        self._img_mode = img_mode


    def rowCount(self, parent=qtc.QModelIndex()):
        return len(self._mode)+2

    def columnCount(self, parent=qtc.QModelIndex()):
        return 2

    def data(self, index, role=qtc.Qt.ItemDataRole.DisplayRole):

        if role == qtc.Qt.ItemDataRole.DisplayRole:
            try:
                if index.column() == 0:
                    if index.row()<len(self._mode):

                        return self._mode[index.row()]

                    else:
                        return self.position[index.row()-len(self._mode)]
                else:
                    if index.row() < len(self._mode):
                        if isinstance(self._values,int):
                            return self._values
                        else:
                            if self._img_mode != "CMYK":
                                return self._values[index.row()]
                            else:
                                return int(self._values[index.row()]/255*100)
                    else:
                        return self._pos[index.row() - len(self._mode)]

            except IndexError:
                print("Index Error!!")


class ImagePixelInfo(qtw.QWidget, Ui_mw_image_pixel_info):

    def __init__(self, window, mode, values, pos):
        super().__init__()
        self._window = window
        self._mode = mode
        self._values = values
        self._pos = pos
        self.data_model = ImagePixelInfoModel(self._mode, self._values, self._pos, self._window.image_to_edit.mode)
        self.setupUi(self)
        self.tv_image_pixel_info.setModel(self.data_model)
        self.show()

    def closeEvent(self, event) -> None:
        if self._window.image_to_edit != None:
            self._window.pb_showRGB.setEnabled(True)
