from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw

from Image_kernel.UI.Image_kernel import Ui_mw_kernel


class KernelTableModel3x3(qtc.QAbstractTableModel):

    matrix_3_3 = [0, -0.5, 0], [-0.5, 3, -0.5], [0, -0.5, 0]

    def __init__(self):
        super().__init__()

    def flags(self, index):
        return qtc.Qt.ItemFlag.ItemIsSelectable|qtc.Qt.ItemFlag.ItemIsEnabled|qtc.Qt.ItemFlag.ItemIsEditable
    def rowCount(self, parent=qtc.QModelIndex()):
        return 3

    def columnCount(self, parent=qtc.QModelIndex()):
        return 3
    def setData(self, index, value, role):

        if role == qtc.Qt.ItemDataRole.EditRole:
            try:
                self.entity = float(value)
                self.matrix_3_3[index.row()][index.column()] = self.entity
            except ValueError as valueError:
                pass
            except Exception as exception:
                pass

            return True

    def data(self, index, role=qtc.Qt.ItemDataRole.DisplayRole):

        if role == qtc.Qt.ItemDataRole.DisplayRole:
            try:
                return self.matrix_3_3[index.row()][index.column()]

            except IndexError:
                print("Index Error!!")
class KernelTableModel(qtc.QAbstractTableModel):

    def __init__(self,matrix):
        super().__init__()
        self.matrix = matrix

    def flags(self, index):
        return qtc.Qt.ItemFlag.ItemIsSelectable|qtc.Qt.ItemFlag.ItemIsEnabled|qtc.Qt.ItemFlag.ItemIsEditable
    def rowCount(self, parent=qtc.QModelIndex()):
        return len(self.matrix[0])

    def columnCount(self, parent=qtc.QModelIndex()):
        return len(self.matrix[0])
    def setData(self, index, value, role):

        if role == qtc.Qt.ItemDataRole.EditRole:
            try:
                self.entity = float(value)
                self.matrix[index.row()][index.column()] = self.entity
            except ValueError as valueError:
                pass
            except Exception as exception:
                pass

            return True

    def data(self, index, role=qtc.Qt.ItemDataRole.DisplayRole):

        if role == qtc.Qt.ItemDataRole.DisplayRole:
            try:
                return self.matrix[index.row()][index.column()]

            except IndexError:
                print("Index Error!!")

class FilterImageKernel(qtw.QWidget, Ui_mw_kernel):
    matrix_3_3 = [0, -0.5, 0], [-0.5, 3, -0.5], [0, -0.5, 0]
    matrix_5_5 = [[1 / 256, 4 / 256, 6 / 256, 4 / 256, 1 / 256],
                  [4 / 256, 16 / 256, 24 / 256, 16 / 256, 4 / 256],
                  [6 / 256, 24 / 256, 36 / 256, 24 / 256, 6 / 256],
                  [4 / 256, 16 / 256, 24 / 256, 16 / 256, 4 / 256],
                  [1 / 256, 4 / 256, 6 / 256, 4 / 256, 1 / 256]]
    tuple = None

    def __init__(self, window):
        super().__init__()
        self._window = window
        self.data_model1 = KernelTableModel(self.matrix_3_3)
        self.data_model2 = KernelTableModel(self.matrix_5_5)
        self.setupUi(self)
        self.tv_3x3.setModel(self.data_model1)
        self.tv_5x5.setModel(self.data_model2)
        self.pb_apply_kernel_3x3.clicked.connect(self.use_kernel_3x3_image)
        self.pb_apply_kernel_5x5.clicked.connect(self.use_kernel_5x5_image)

        self.show()


    def closeEvent(self, event) -> None:
        if self._window.image_to_edit != None:
            self._window.pb_kernel.setEnabled(True)

    def prepare_values(self,matrix):
        list = []
        for _ in matrix:
            for i in _:
                list.append(i)
        self.tuple = tuple(list)

    def use_kernel_5x5_image(self):
        self.prepare_values(self.data_model2.matrix)
        self._window.filter_kernel_image((5, 5), self.tuple, self.dsb_scale_kernel_5x5.value(),
                                         self.dsb_offset_kernel_5x5.value())
    def use_kernel_3x3_image(self):
            self.prepare_values(self.data_model1.matrix)
            self._window.filter_kernel_image((3,3),self.tuple, self.dsb_scale_kernel_3x3.value(), self.dsb_offset_kernel_3x3.value())

    # def kernel_3_3_apply_button_enabler(self):
    #     if self.dsb_scale_kernel_3x3.value() != 0 and self.dsb_offset_kernel_3x3 !=0:
    #         self.pb_apply_kernel_3x3.setEnabled(True)
    #     else:
    #         self.pb_apply_kernel_3x3.setEnabled(False)