from PySide6 import QtWidgets as qtw
from Image_filter.UI.Image_filter import Ui_mw_filter_image

class Image_Filter(qtw.QWidget, Ui_mw_filter_image):

    def __init__(self, window):
        super().__init__()
        self._window = window
        self.setupUi(self)
        self.sb_box.valueChanged.connect(self.box_apply_button_enabler)
        self.sb_gaussian.valueChanged.connect(self.gaussian_apply_button_enabler)
        self.pb_apply_box.clicked.connect(self.blur_box_image)
        self.pb_apply_gaussian.clicked.connect(self.blur_gaussian_image)
        self.pb_apply_rank.clicked.connect(self.rank_image)
        self.rb_3x3.setChecked(True)
        self.rb_min.setChecked(True)
        self.show()

    def closeEvent(self, event) -> None:
        if self._window.image_to_edit != None:
            self._window.pb_blur.setEnabled(True)

    def blur_box_image(self):
        self._window.blur_image(self.sb_box.value(),0)
    def blur_gaussian_image(self):
        self._window.blur_image(self.sb_gaussian.value(),1)
    def rank_image(self):
        if self.rb_3x3.isChecked():
            size = 3
        else:
            size = 5
        if self.rb_min.isChecked():
            rank = 0
        elif self.rb_median.isChecked():
            rank = int((size*size)/2+1)
            print(rank)
        else:
            rank = (size*size)-1
        self._window.rank_image(size,rank)
    def box_apply_button_enabler(self):
        print(self.sb_box.value())
        if self.sb_box.value() != 0:
            self.pb_apply_box.setEnabled(True)
        else:
            self.pb_apply_box.setEnabled(False)

    def gaussian_apply_button_enabler(self):
        print(self.sb_gaussian.value())
        if self.sb_gaussian.value() != 0:
            self.pb_apply_gaussian.setEnabled(True)
        else:
            self.pb_apply_gaussian.setEnabled(False)


