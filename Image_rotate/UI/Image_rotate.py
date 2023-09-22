# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Image_rotate.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QFrame,
    QHBoxLayout, QLabel, QPushButton, QRadioButton,
    QSizePolicy, QSlider, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_mw_rotate(object):
    def setupUi(self, mw_rotate):
        if not mw_rotate.objectName():
            mw_rotate.setObjectName(u"mw_rotate")
        mw_rotate.resize(420, 207)
        self.verticalLayout_2 = QVBoxLayout(mw_rotate)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.hs_rotate = QSlider(mw_rotate)
        self.hs_rotate.setObjectName(u"hs_rotate")
        self.hs_rotate.setMinimum(-360)
        self.hs_rotate.setMaximum(360)
        self.hs_rotate.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.hs_rotate)

        self.sb_rotate = QSpinBox(mw_rotate)
        self.sb_rotate.setObjectName(u"sb_rotate")
        self.sb_rotate.setMinimum(-360)
        self.sb_rotate.setMaximum(360)

        self.horizontalLayout.addWidget(self.sb_rotate)

        self.cb_expand = QCheckBox(mw_rotate)
        self.cb_expand.setObjectName(u"cb_expand")

        self.horizontalLayout.addWidget(self.cb_expand)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.line = QFrame(mw_rotate)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.label = QLabel(mw_rotate)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.rb_nearest = QRadioButton(mw_rotate)
        self.bG_resample = QButtonGroup(mw_rotate)
        self.bG_resample.setObjectName(u"bG_resample")
        self.bG_resample.addButton(self.rb_nearest)
        self.rb_nearest.setObjectName(u"rb_nearest")
        self.rb_nearest.setChecked(True)

        self.horizontalLayout_2.addWidget(self.rb_nearest)

        self.rb_bicubic = QRadioButton(mw_rotate)
        self.bG_resample.addButton(self.rb_bicubic)
        self.rb_bicubic.setObjectName(u"rb_bicubic")
        self.rb_bicubic.setChecked(False)

        self.horizontalLayout_2.addWidget(self.rb_bicubic)

        self.rb_bilinear = QRadioButton(mw_rotate)
        self.bG_resample.addButton(self.rb_bilinear)
        self.rb_bilinear.setObjectName(u"rb_bilinear")

        self.horizontalLayout_2.addWidget(self.rb_bilinear)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.line_2 = QFrame(mw_rotate)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.ch_rotation_center = QCheckBox(mw_rotate)
        self.ch_rotation_center.setObjectName(u"ch_rotation_center")

        self.horizontalLayout_3.addWidget(self.ch_rotation_center)

        self.x_label = QLabel(mw_rotate)
        self.x_label.setObjectName(u"x_label")
        self.x_label.setMaximumSize(QSize(20, 16777215))

        self.horizontalLayout_3.addWidget(self.x_label)

        self.sb_x = QSpinBox(mw_rotate)
        self.sb_x.setObjectName(u"sb_x")

        self.horizontalLayout_3.addWidget(self.sb_x)

        self.y_label = QLabel(mw_rotate)
        self.y_label.setObjectName(u"y_label")
        self.y_label.setMaximumSize(QSize(20, 16777215))

        self.horizontalLayout_3.addWidget(self.y_label)

        self.sb_y = QSpinBox(mw_rotate)
        self.sb_y.setObjectName(u"sb_y")

        self.horizontalLayout_3.addWidget(self.sb_y)

        self.pb_apply_rotation = QPushButton(mw_rotate)
        self.pb_apply_rotation.setObjectName(u"pb_apply_rotation")
        self.pb_apply_rotation.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_3.addWidget(self.pb_apply_rotation)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.retranslateUi(mw_rotate)

        QMetaObject.connectSlotsByName(mw_rotate)
    # setupUi

    def retranslateUi(self, mw_rotate):
        mw_rotate.setWindowTitle(QCoreApplication.translate("mw_rotate", u"Rotate", None))
        self.cb_expand.setText(QCoreApplication.translate("mw_rotate", u"expand", None))
        self.label.setText(QCoreApplication.translate("mw_rotate", u"Resample", None))
        self.rb_nearest.setText(QCoreApplication.translate("mw_rotate", u"Nearest", None))
        self.rb_bicubic.setText(QCoreApplication.translate("mw_rotate", u"Bicubic", None))
        self.rb_bilinear.setText(QCoreApplication.translate("mw_rotate", u"Bilinear", None))
        self.ch_rotation_center.setText(QCoreApplication.translate("mw_rotate", u"Rotation center:", None))
        self.x_label.setText(QCoreApplication.translate("mw_rotate", u"x:", None))
        self.y_label.setText(QCoreApplication.translate("mw_rotate", u"y:", None))
        self.pb_apply_rotation.setText(QCoreApplication.translate("mw_rotate", u"Apply", None))
    # retranslateUi

