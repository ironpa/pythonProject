import copy

from PySide6 import QtWidgets as qtw
from Image_enhancement.UI.Image_enhancement import Ui_mw_enhance_image
from PIL import ImageEnhance, Image

class ImageEnhancer(qtw.QWidget, Ui_mw_enhance_image):

    image_to_enhance = None
    image_enhancer = None
    def __init__(self, window):

        super().__init__()

        self._window = window
        self.image_to_enhance = copy.deepcopy(window.image_to_edit)
        self.init_enhancers()
        self.setupUi(self)

        self.hs_color.valueChanged.connect(self.update_dsb_color)
        self.hs_contrast.valueChanged.connect(self.update_dsb_contrast)
        self.hs_brightness.valueChanged.connect(self.update_dsb_brightness)
        self.hs_sharpness.valueChanged.connect(self.update_dsb_sharpness)
        self.dsb_color.valueChanged.connect(self.update_hs_color)
        self.dsb_contrast.valueChanged.connect(self.update_hs_contrast)
        self.dsb_brightness.valueChanged.connect(self.update_hs_brightness)
        self.dsb_sharpness.valueChanged.connect(self.update_hs_sharpness)
        self.pb_color.clicked.connect(self.apply_color)
        self.pb_contrast.clicked.connect(self.apply_color)
        self.pb_sharpness.clicked.connect(self.apply_color)
        self.pb_brightness.clicked.connect(self.apply_color)

        self.show()
    def initial_values(self):
        self.dsb_color.setValue(1)
        self.dsb_contrast.setValue(1)
        self.dsb_brightness.setValue(1)
        self.dsb_sharpness.setValue(1)

    def init_enhancers(self):
        self.color_enhancer = ImageEnhance.Color(self._window.image_to_edit)
        self.contrast_enhancer = ImageEnhance.Contrast(self._window.image_to_edit)
        self.brightness_enhancer = ImageEnhance.Brightness(self._window.image_to_edit)
        self.sharpness_enhancer = ImageEnhance.Sharpness(self._window.image_to_edit)
    def apply_color(self):
        self._window.image_to_edit = self.image_to_enhance
        self.update_enhancers()
        self.initial_values()
    def update_enhancers(self):
        self.color_enhancer = ImageEnhance.Color(self.image_to_enhance)
        self.contrast_enhancer = ImageEnhance.Contrast(self.image_to_enhance)
        self.brightness_enhancer = ImageEnhance.Brightness(self.image_to_enhance)
        self.sharpness_enhancer = ImageEnhance.Sharpness(self.image_to_enhance)
    def enhance_color(self):

        self.image_to_enhance = self.color_enhancer.enhance(self.dsb_color.value())
        self._window.image_display(self.image_to_enhance)
    def enhance_contrast(self):

        self.image_to_enhance = self.contrast_enhancer.enhance(self.dsb_contrast.value())
        self._window.image_display(self.image_to_enhance)
    def enhance_brightness(self):

        self.image_to_enhance = self.brightness_enhancer.enhance(self.dsb_brightness.value())
        self._window.image_display(self.image_to_enhance)
    def enhance_sharpness(self):

        self.image_to_enhance = self.sharpness_enhancer.enhance(self.dsb_sharpness.value())
        self._window.image_display(self.image_to_enhance)
    def update_dsb_color(self):
        self.dsb_color.setValue(self.hs_color.value()/100)
        self.enhance_color()

    def update_hs_color(self):
        self.hs_color.setValue(self.dsb_color.value()*100)

    def update_dsb_contrast(self):
        self.dsb_contrast.setValue(self.hs_contrast.value()/100)
        self.enhance_contrast()

    def update_hs_contrast(self):
        self.hs_contrast.setValue(self.dsb_contrast.value()*100)

    def update_dsb_brightness(self):
        self.dsb_brightness.setValue(self.hs_brightness.value()/100)
        self.enhance_brightness()

    def update_hs_brightness(self):
        self.hs_brightness.setValue(self.dsb_brightness.value()*100)

    def update_dsb_sharpness(self):
        self.dsb_sharpness.setValue(self.hs_sharpness.value() / 100)
        self.enhance_sharpness()

    def update_hs_sharpness(self):
        self.hs_sharpness.setValue(self.dsb_sharpness.value() * 100)

    def closeEvent(self, event) -> None:
        if self._window.image_to_edit != None:
            self._window.pb_enhance.setEnabled(True)