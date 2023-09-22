from PySide6 import QtWidgets as qtw
from Image_threshold.UI.Image_threshold import Ui_mw_image_threshold

class ImageThreshold(qtw.QWidget, Ui_mw_image_threshold):

    def __init__(self, window):
        super().__init__()

        self._window = window
        self.minimum, self.maximum = window.image_extrema
        self.setupUi(self)
        self.hs_treshold.valueChanged.connect(self.update_sb)
        self.sb_treshold.valueChanged.connect(self.update_hs)
        self.pb_apply_treshold.clicked.connect(self.set_threshold)
        self.hs_treshold.setMinimum(self.minimum)
        self.hs_treshold.setMaximum(self.maximum)
        self.sb_treshold.setMinimum(self.minimum)
        self.sb_treshold.setValue(self.maximum)
        self.cut_treshold = self.maximum
        self.sb_treshold.setMaximum(self.maximum)

        self.show()
    def set_threshold(self):
        self._window.set_threshold(self.sb_treshold.value())

    def closeEvent(self, event) -> None:
        if self._window.image_to_edit != None and self._window.image_to_edit.getbands()==("L",):
            self._window.pb_threshold.setEnabled(True)
    def update_sb(self):
        self.cut_treshold = self.hs_treshold.value()
        self.sb_treshold.setValue(self.hs_treshold.value())
    def update_hs(self):
        self.cut_treshold = self.sb_treshold.value()
        self.hs_treshold.setValue(self.sb_treshold.value())
    def update_extrema(self,extrema):
        self.minimum, self.maximum = extrema
        self.hs_treshold.setMinimum(self.minimum)
        self.hs_treshold.setMaximum(self.maximum)
        self.sb_treshold.setMinimum(self.minimum)
        self.sb_treshold.setMaximum(self.maximum)
        self.sb_treshold.setValue(self.maximum)

