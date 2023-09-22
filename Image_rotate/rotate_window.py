from PySide6 import QtWidgets as qtw
from Image_rotate.UI.Image_rotate import Ui_mw_rotate
from PIL import Image

class ImageRotate(qtw.QWidget, Ui_mw_rotate):

    def __init__(self, window):
        super().__init__()
        self._window = window
        self.resample = Image.NEAREST

        self.size_y, self.size_x = self._window.image_size
        self.setupUi(self)
        self.expand = self.cb_expand.isChecked()
        self.sb_x.setMinimum(0)
        self.sb_x.setMaximum(self.size_x)
        self.sb_y.setMinimum(0)
        self.sb_y.setMaximum(self.size_y)
        self.center_x = int(self.size_x/2)
        self.sb_x.setValue(self.center_x)
        self.center_y = int(self.size_y/2)
        self.sb_y.setValue(self.center_y)
        self.hs_rotate.valueChanged.connect(self.update_sb)
        self.sb_rotate.valueChanged.connect(self.update_hs)
        self.pb_apply_rotation.clicked.connect(self.apply_rotation)
        self.show()

    def update_sb(self):
        self.sb_rotate.setValue(self.hs_rotate.value())
    def update_hs(self):
        self.hs_rotate.setValue(self.sb_rotate.value())
    def rotate_image(self, angle, resample, expand, center=None):
        self._window.image_to_edit = self._window.image_to_edit.rotate(angle,resample,expand,center)
        self._window.image_display(self._window.image_to_edit)

    def apply_rotation(self):

        if self.rb_bicubic.isChecked():
            self.resample = Image.BICUBIC
        if self.rb_nearest.isChecked():
            self.resample = Image.NEAREST
        if self.rb_bilinear.isChecked():
            self.resample = Image.BILINEAR
        if self.ch_rotation_center.isChecked():
            self.center_x = self.sb_x.value()
            self.center_y = self.sb_y.value()
        if self.ch_rotation_center.isChecked():
            self.rotate_image(self.sb_rotate.value(), self.resample,self.cb_expand.isChecked(),(self.sb_y.value(),self.sb_x.value()))
        else:
            self.rotate_image(self.sb_rotate.value(), self.resample, self.cb_expand.isChecked())
    def update_point(self):
        self.center_y, self.center_x =self._window.point
        self.sb_x.setValue(self.center_x)
        self.sb_y.setValue(self.center_y)