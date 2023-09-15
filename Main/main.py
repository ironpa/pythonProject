import pathlib
import sys

from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg
from PySide6.QtWidgets import QFileDialog
from PySide6.QtGui import QCursor
from PIL import Image,ImageQt, ImageChops, ImageFilter
from tr import tr


from Main.UI.main_window import Ui_mw_Main
from Image_filter.filter_window import Image_Filter
from Image_info.info_window import ImageInfo
from Image_resize.resize_window import ImageResize
from Image_crop.crop_window import ImageCrop
from Image_kernel.filter_kernel_window import FilterImageKernel

class MainWindow(qtw.QMainWindow, Ui_mw_Main):

    filename = ""
    point1 = (0,0)
    point2 = (0,0)
    point = (0,0)
    points = ""
    file_info = ""
    image_to_edit = None
    image_size = ""
    imageCropUI = None
    imageResizeUI = None
    imageFilterUI = None
    _data = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setMouseTracking(True)

        self.ql_coordinates.setAlignment(qtc.Qt.AlignmentFlag.AlignRight | qtc.Qt.AlignmentFlag.AlignBottom)

        self.action_Quit.triggered.connect(self.close)
        self.action_Open_file.triggered.connect(self.openFile)
        self.pb_open_file.clicked.connect(self.openFile)
        self.pb_image_description.clicked.connect(self.image_info_open)
        self.pb_rotate_right.clicked.connect(self.rotate_right)
        self.pb_rotate_left.clicked.connect(self.rotate_left)
        self.pb_flip.clicked.connect(self.flip_left_right)
        self.pb_clear.clicked.connect(self.remove_image)
        self.pb_invert_colors.clicked.connect(self.invert_colors)
        self.pb_resize.clicked.connect(self.resize_image_open)
        self.pb_crop.clicked.connect(self.crop_image_open)
        self.pb_blur.clicked.connect(self.filter_image_open)
        self.pb_sharpen.clicked.connect(self.sharpen_image)
        self.pb_grayscale.clicked.connect(self.to_grayscale)
        self.pb_smooth.clicked.connect(self.smooth_image)
        self.pb_find_edges.clicked.connect(self.find_edges)
        self.pb_emboss.clicked.connect(self.emboss)
        self.pb_kernel.clicked.connect(self.kernel_image_open)

    def kernel_image_open(self):
        self.pb_kernel.setEnabled(False)
        self.imageFilterKernelUI = FilterImageKernel(self)
    def resize_image_open(self):
        self.pb_resize.setEnabled(False)
        self.imageResizeUI = ImageResize(self)
    def crop_image_open(self):
        # self.crop_image()
        self.pb_crop.setEnabled(False)
        self.imageCropUI = ImageCrop(self)
    def filter_image_open(self):
        self.pb_blur.setEnabled(False)
        self.imageFilterUI = Image_Filter(self)
    def filter_kernel_image(self,size,kernel,scale,offset):
        if scale==0 and offset==0:
            self.image_to_edit = self.image_to_edit.filter(ImageFilter.Kernel(size,kernel))
        elif scale == 0:
            self.image_to_edit = self.image_to_edit.filter(ImageFilter.Kernel(size,kernel,None,offset))
        else:
            self.image_to_edit = self.image_to_edit.filter(ImageFilter.Kernel(size, kernel, scale, offset))
        self.image_display(self.image_to_edit)
    def blur_image(self, radius, type):
        if type == 0:
            self.image_to_edit = self.image_to_edit.filter(ImageFilter.BoxBlur(radius))
            self.update_values()
            print("box")
        else:
            self.image_to_edit = self.image_to_edit.filter(ImageFilter.GaussianBlur(radius))
            self.update_values()
            print("gaussian")
    def crop_image(self):
        self.points = self.point1 + self.point2
        self.image_to_edit = self.image_to_edit.crop(self.points)
        self.update_values()
    def rank_image(self, size, rank):
        self.image_to_edit = self.image_to_edit.filter(ImageFilter.RankFilter(size, rank))
        self.image_display(self.image_to_edit)
    def to_grayscale(self):
        self.image_to_edit = self.image_to_edit.convert("L")
        self.image_display(self.image_to_edit)
    def smooth_image(self):
        self.image_to_edit = self.image_to_edit.filter(ImageFilter.SMOOTH)
        self.image_display(self.image_to_edit)
    def find_edges(self):
        self.image_to_edit = self.image_to_edit.filter(ImageFilter.FIND_EDGES)
        self.image_display(self.image_to_edit)
    def emboss(self):
        self.image_to_edit = self.image_to_edit.filter(ImageFilter.EMBOSS)
        self.image_display(self.image_to_edit)
    # , point1, point2
    def change_image_size(self, size):

        self.image_to_edit = self.image_to_edit.resize(size, 1)
        self.update_values()
    def update_values(self):
        self.image_size = self.image_to_edit.size
        self.image_display(self.image_to_edit)
        self.updateViews()
    def sharpen_image(self):
        self.image_to_edit = self.image_to_edit.filter(ImageFilter.SHARPEN)
        self.image_display(self.image_to_edit)
    def flip_left_right(self):
        self.image_to_edit = self.image_to_edit.transpose(Image.FLIP_LEFT_RIGHT)
        self.image_display(self.image_to_edit)
    # funkcjonalnosc resize - dorobic resampling i resize region
    def updateViews(self):
        if self.imageResizeUI != None and self.imageResizeUI.isVisible():
            self.imageResizeUI.data_model.im_width, self.imageResizeUI.data_model.im_height = self.image_to_edit.size
            self.imageResizeUI.data_model.layoutChanged.emit()
        if self.imageCropUI != None and self.imageCropUI.isVisible():
            self.imageCropUI.data_model.im_width, self.imageCropUI.data_model.im_height  = self.image_to_edit.size
            self.imageCropUI.data_model.layoutChanged.emit()

    def print_to_dialog(self, window_size):
        print(window_size)
    def invert_colors(self):
        #self.image_to_edit = self.image_to_edit.convert("L")
        self.image_to_edit = ImageChops.invert(self.image_to_edit)
        self.image_display(self.image_to_edit)
    def remove_image(self):
        self.image_to_edit = None
        self.point = (0,0)
        self.ql_coordinates.setText("(%d,%d)" % self.point)
        self.qt_label.clear()
        self.clearUp_menu()

        # self.closeWindows((self.imageResizeUI,self.imageCropUI,self.imageBlurUI))

        if self.imageCropUI != None:
            if self.imageCropUI.isVisible():
                self.imageCropUI.close()
        if self.imageResizeUI != None:
            if self.imageResizeUI.isVisible():
                self.imageResizeUI.close()
        if self.imageFilterUI != None:
            if self.imageFilterUI.isVisible():
                self.imageFilterUI.close()


    # def closeWindows(self, *qwidgets):
    #     for i in qwidgets:
    #         if i != None:
    #             if i.isVisible():
    #                 i.close()


    def clearUp_menu(self):
        self.pb_rotate_left.setEnabled(False)
        self.pb_rotate_right.setEnabled(False)
        self.pb_image_description.setEnabled(False)
        self.pb_flip.setEnabled(False)
        self.pb_clear.setEnabled(False)
        self.pb_clear.setEnabled(False)
        self.pb_invert_colors.setEnabled(False)
        self.pb_resize.setEnabled(False)
        self.pb_crop.setEnabled(False)
        self.pb_blur.setEnabled(False)
        self.pb_sharpen.setEnabled(False)
        self.pb_grayscale.setEnabled(False)
        self.pb_smooth.setEnabled(False)
        self.pb_find_edges.setEnabled(False)
        self.pb_emboss.setEnabled(False)
        self.pb_kernel.setEnabled(False)
        self.qt_image_description.setText("No image opened...")
    def set_editing_menu(self):
        self.pb_rotate_left.setEnabled(True)
        self.pb_rotate_right.setEnabled(True)
        self.pb_image_description.setEnabled(True)
        self.pb_flip.setEnabled(True)
        self.pb_clear.setEnabled(True)
        self.pb_clear.setEnabled(True)
        self.pb_invert_colors.setEnabled(True)
        self.pb_resize.setEnabled(True)
        self.pb_crop.setEnabled(True)
        self.pb_blur.setEnabled(True)
        self.pb_sharpen.setEnabled(True)
        self.pb_grayscale.setEnabled(True)
        self.pb_smooth.setEnabled(True)
        self.pb_find_edges.setEnabled(True)
        self.pb_emboss.setEnabled(True)
        self.pb_kernel.setEnabled(True)

    def closeEvent(self, event) -> None:
        try:
            if isinstance(self.image_to_edit, Image):
                print("just about to close:", self.filename)
                self.image_to_edit.close()
        except (RuntimeError, TypeError, NameError):
            print("Oh no... Image not closed...")



    def setMouseTracking(self, enable: bool) -> None:
        def recursive_set(parent):
            for child in parent.findChildren(qtc.QObject):
                try:
                    child.setMouseTracking(enable)
                except:
                    pass
                recursive_set(child)
        qtw.QWidget.setMouseTracking(self, enable)
        recursive_set(self)
    def rotate_right(self):
        self.image_to_edit = self.image_to_edit.transpose(Image.ROTATE_270)
        self.image_display(self.image_to_edit)
        self.update_values()

    def rotate_left(self):
        self.image_to_edit = self.image_to_edit.transpose(Image.ROTATE_90)
        self.image_display(self.image_to_edit)
        self.update_values()

    def mouseMoveEvent(self, event):
        if self.image_to_edit != None:
            point = (event.position().x()-self.scrollArea.geometry().x(), event.position().y()-self.scrollArea.geometry().y())
            if point[0]>0 and point[1]>0 and point[0]<=self.image_size[0] and point[1]<=self.image_size[1]:
                self.point = point
                self.ql_coordinates.setText("(%d,%d)" % self.point)
    def mouseDoubleClickEvent(self, event):
        if self.imageCropUI != None and self.imageCropUI.isVisible():
            print("self.point")
            if self.imageCropUI.rb_upper_left.isChecked()==True:
                self.point1 = self.point
                self.imageCropUI.le_p1_x.setText(str(self.point[0]))
                self.imageCropUI.le_p1_y.setText(str(self.point[1]))
            if self.imageCropUI.rb_lower_right.isChecked() == True:
                self.point2 = self.point
                self.imageCropUI.le_p2_x.setText(str(self.point[0]))
                self.imageCropUI.le_p2_y.setText(str(self.point[1]))

    def image_info_open(self):
        self.showInfoWindow = qtw.QWidget()
        self.ui = ImageInfo(self.image_to_edit.info)
        #self.showInfoWindow.show()


    def openFile(self):
        file_Dialog = QFileDialog()
        #file_Dialog.setNameFilters("Images (*.png *.jpg *.tiff")
        file_Dialog.setNameFilters(["Images (*.png *.jpg *.tiff *.tif)"])
        file_Dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        is_File_Selected = file_Dialog.exec()

        if is_File_Selected:
            if self.image_to_edit != None:
                print("just about to close:",self.filename)
                self.image_to_edit.close()

            self.filename = file_Dialog.selectedFiles().pop(0)
            path = pathlib.Path(self.filename)
            self.image_to_edit = Image.open(path)
            self.set_editing_menu()
            self.image_size = self.image_to_edit.size
            print(self.image_size)
            bands = self.image_to_edit.getbands()
            self.file_info = ""
            self.image_display(self.image_to_edit)
            print(type(self.image_to_edit.info))
            for k, v in self.image_to_edit.info.items():
                print(k, v)
                self.file_info += str(k) +": "+ str(v)+"\n"

            print(self.file_info)
            self.qt_image_description.setText(self.file_info+self.image_to_edit.format +" "+ self.image_to_edit.mode)
            print(self.image_to_edit.format, self.image_to_edit.mode)
            print(path)
        else:
            print("No file selected")
    def image_display(self, image):
        pixel_map = qtg.QPixmap(image.toqimage())
        self.qt_label.setPixmap(pixel_map)



if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())