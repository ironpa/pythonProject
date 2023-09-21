# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Image_filter.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QDoubleSpinBox, QFrame,
    QHBoxLayout, QLabel, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_mw_filter_image(object):
    def setupUi(self, mw_filter_image):
        if not mw_filter_image.objectName():
            mw_filter_image.setObjectName(u"mw_filter_image")
        mw_filter_image.resize(273, 403)
        self.verticalLayout_5 = QVBoxLayout(mw_filter_image)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(mw_filter_image)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(mw_filter_image)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.sb_box = QSpinBox(mw_filter_image)
        self.sb_box.setObjectName(u"sb_box")
        self.sb_box.setMaximumSize(QSize(40, 16777215))
        self.sb_box.setMaximum(50)

        self.horizontalLayout.addWidget(self.sb_box)

        self.pb_apply_box = QPushButton(mw_filter_image)
        self.pb_apply_box.setObjectName(u"pb_apply_box")
        self.pb_apply_box.setEnabled(False)
        self.pb_apply_box.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout.addWidget(self.pb_apply_box)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_5.addLayout(self.verticalLayout)

        self.line = QFrame(mw_filter_image)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(mw_filter_image)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(mw_filter_image)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.dsb_gaussian = QDoubleSpinBox(mw_filter_image)
        self.dsb_gaussian.setObjectName(u"dsb_gaussian")
        self.dsb_gaussian.setDecimals(3)

        self.horizontalLayout_2.addWidget(self.dsb_gaussian)

        self.pb_apply_gaussian = QPushButton(mw_filter_image)
        self.pb_apply_gaussian.setObjectName(u"pb_apply_gaussian")
        self.pb_apply_gaussian.setEnabled(False)
        self.pb_apply_gaussian.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_2.addWidget(self.pb_apply_gaussian)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout_5.addLayout(self.verticalLayout_2)

        self.line_2 = QFrame(mw_filter_image)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_5 = QLabel(mw_filter_image)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_3.addWidget(self.label_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_9 = QLabel(mw_filter_image)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_4.addWidget(self.label_9)

        self.rb_3x3 = QRadioButton(mw_filter_image)
        self.rbg_kernel_size = QButtonGroup(mw_filter_image)
        self.rbg_kernel_size.setObjectName(u"rbg_kernel_size")
        self.rbg_kernel_size.addButton(self.rb_3x3)
        self.rb_3x3.setObjectName(u"rb_3x3")

        self.horizontalLayout_4.addWidget(self.rb_3x3)

        self.rb_5x5 = QRadioButton(mw_filter_image)
        self.rbg_kernel_size.addButton(self.rb_5x5)
        self.rb_5x5.setObjectName(u"rb_5x5")

        self.horizontalLayout_4.addWidget(self.rb_5x5)

        self.horizontalSpacer = QSpacerItem(50, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.rb_min = QRadioButton(mw_filter_image)
        self.rbg_filter = QButtonGroup(mw_filter_image)
        self.rbg_filter.setObjectName(u"rbg_filter")
        self.rbg_filter.addButton(self.rb_min)
        self.rb_min.setObjectName(u"rb_min")
        self.rb_min.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_3.addWidget(self.rb_min)

        self.rb_max = QRadioButton(mw_filter_image)
        self.rbg_filter.addButton(self.rb_max)
        self.rb_max.setObjectName(u"rb_max")
        self.rb_max.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_3.addWidget(self.rb_max)

        self.rb_median = QRadioButton(mw_filter_image)
        self.rbg_filter.addButton(self.rb_median)
        self.rb_median.setObjectName(u"rb_median")
        self.rb_median.setEnabled(True)
        self.rb_median.setMaximumSize(QSize(65, 16777215))

        self.horizontalLayout_3.addWidget(self.rb_median)

        self.pb_apply_rank = QPushButton(mw_filter_image)
        self.pb_apply_rank.setObjectName(u"pb_apply_rank")
        self.pb_apply_rank.setEnabled(True)
        self.pb_apply_rank.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_3.addWidget(self.pb_apply_rank)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)

        self.line_4 = QFrame(mw_filter_image)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line_4)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_6 = QLabel(mw_filter_image)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_4.addWidget(self.label_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_7 = QLabel(mw_filter_image)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_5.addWidget(self.label_7)

        self.sb_unsharp_radius = QSpinBox(mw_filter_image)
        self.sb_unsharp_radius.setObjectName(u"sb_unsharp_radius")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sb_unsharp_radius.sizePolicy().hasHeightForWidth())
        self.sb_unsharp_radius.setSizePolicy(sizePolicy)
        self.sb_unsharp_radius.setMinimumSize(QSize(0, 0))
        self.sb_unsharp_radius.setMaximumSize(QSize(40, 16777215))
        self.sb_unsharp_radius.setMaximum(50)
        self.sb_unsharp_radius.setValue(2)

        self.horizontalLayout_5.addWidget(self.sb_unsharp_radius)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.label_8 = QLabel(mw_filter_image)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_5.addWidget(self.label_8)

        self.sb_un_procent = QSpinBox(mw_filter_image)
        self.sb_un_procent.setObjectName(u"sb_un_procent")
        sizePolicy.setHeightForWidth(self.sb_un_procent.sizePolicy().hasHeightForWidth())
        self.sb_un_procent.setSizePolicy(sizePolicy)
        self.sb_un_procent.setMinimumSize(QSize(50, 0))
        self.sb_un_procent.setMaximumSize(QSize(100, 16777215))
        self.sb_un_procent.setMaximum(1000)
        self.sb_un_procent.setValue(150)

        self.horizontalLayout_5.addWidget(self.sb_un_procent)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_10 = QLabel(mw_filter_image)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_6.addWidget(self.label_10)

        self.sb_unsharp_threshold = QSpinBox(mw_filter_image)
        self.sb_unsharp_threshold.setObjectName(u"sb_unsharp_threshold")
        sizePolicy.setHeightForWidth(self.sb_unsharp_threshold.sizePolicy().hasHeightForWidth())
        self.sb_unsharp_threshold.setSizePolicy(sizePolicy)
        self.sb_unsharp_threshold.setMinimumSize(QSize(40, 0))
        self.sb_unsharp_threshold.setMaximumSize(QSize(30, 16777215))
        self.sb_unsharp_threshold.setMaximum(255)
        self.sb_unsharp_threshold.setValue(3)

        self.horizontalLayout_6.addWidget(self.sb_unsharp_threshold)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.pb_apply_unsharp = QPushButton(mw_filter_image)
        self.pb_apply_unsharp.setObjectName(u"pb_apply_unsharp")
        self.pb_apply_unsharp.setEnabled(True)
        self.pb_apply_unsharp.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_6.addWidget(self.pb_apply_unsharp)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)


        self.retranslateUi(mw_filter_image)

        QMetaObject.connectSlotsByName(mw_filter_image)
    # setupUi

    def retranslateUi(self, mw_filter_image):
        mw_filter_image.setWindowTitle(QCoreApplication.translate("mw_filter_image", u"Filter", None))
        self.label.setText(QCoreApplication.translate("mw_filter_image", u"Box Blur", None))
        self.label_3.setText(QCoreApplication.translate("mw_filter_image", u"radius:", None))
        self.pb_apply_box.setText(QCoreApplication.translate("mw_filter_image", u"Apply", None))
        self.label_2.setText(QCoreApplication.translate("mw_filter_image", u"Gaussian Blur", None))
        self.label_4.setText(QCoreApplication.translate("mw_filter_image", u"radius:", None))
        self.pb_apply_gaussian.setText(QCoreApplication.translate("mw_filter_image", u"Apply", None))
        self.label_5.setText(QCoreApplication.translate("mw_filter_image", u"Rank Filter", None))
        self.label_9.setText(QCoreApplication.translate("mw_filter_image", u"kernel size:", None))
        self.rb_3x3.setText(QCoreApplication.translate("mw_filter_image", u"(3x3)", None))
        self.rb_5x5.setText(QCoreApplication.translate("mw_filter_image", u"(5x5)", None))
        self.rb_min.setText(QCoreApplication.translate("mw_filter_image", u"min", None))
        self.rb_max.setText(QCoreApplication.translate("mw_filter_image", u"max", None))
        self.rb_median.setText(QCoreApplication.translate("mw_filter_image", u"median", None))
        self.pb_apply_rank.setText(QCoreApplication.translate("mw_filter_image", u"Apply", None))
        self.label_6.setText(QCoreApplication.translate("mw_filter_image", u"UnsharpMask", None))
        self.label_7.setText(QCoreApplication.translate("mw_filter_image", u"radius:", None))
        self.label_8.setText(QCoreApplication.translate("mw_filter_image", u"%:", None))
        self.label_10.setText(QCoreApplication.translate("mw_filter_image", u"treshold:", None))
        self.pb_apply_unsharp.setText(QCoreApplication.translate("mw_filter_image", u"Apply", None))
    # retranslateUi

