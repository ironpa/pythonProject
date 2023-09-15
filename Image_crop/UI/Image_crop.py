# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Image_crop.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)

class Ui_mw_image_crop(object):
    def setupUi(self, mw_image_crop):
        if not mw_image_crop.objectName():
            mw_image_crop.setObjectName(u"mw_image_crop")
        mw_image_crop.resize(321, 326)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mw_image_crop.sizePolicy().hasHeightForWidth())
        mw_image_crop.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(mw_image_crop)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tv_crop_image = QTableView(mw_image_crop)
        self.tv_crop_image.setObjectName(u"tv_crop_image")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tv_crop_image.sizePolicy().hasHeightForWidth())
        self.tv_crop_image.setSizePolicy(sizePolicy1)
        self.tv_crop_image.horizontalHeader().setVisible(False)
        self.tv_crop_image.horizontalHeader().setHighlightSections(True)
        self.tv_crop_image.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.tv_crop_image)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.rb_upper_left = QRadioButton(mw_image_crop)
        self.rb_upper_left.setObjectName(u"rb_upper_left")

        self.horizontalLayout.addWidget(self.rb_upper_left)

        self.label = QLabel(mw_image_crop)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label)

        self.le_p1_x = QLineEdit(mw_image_crop)
        self.le_p1_x.setObjectName(u"le_p1_x")
        self.le_p1_x.setReadOnly(True)

        self.horizontalLayout.addWidget(self.le_p1_x)

        self.le_p1_y = QLineEdit(mw_image_crop)
        self.le_p1_y.setObjectName(u"le_p1_y")
        self.le_p1_y.setReadOnly(True)

        self.horizontalLayout.addWidget(self.le_p1_y)

        self.horizontalLayout.setStretch(1, 30)
        self.horizontalLayout.setStretch(2, 30)
        self.horizontalLayout.setStretch(3, 30)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.rb_lower_right = QRadioButton(mw_image_crop)
        self.rb_lower_right.setObjectName(u"rb_lower_right")

        self.horizontalLayout_2.addWidget(self.rb_lower_right)

        self.label_2 = QLabel(mw_image_crop)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.le_p2_x = QLineEdit(mw_image_crop)
        self.le_p2_x.setObjectName(u"le_p2_x")

        self.horizontalLayout_2.addWidget(self.le_p2_x)

        self.le_p2_y = QLineEdit(mw_image_crop)
        self.le_p2_y.setObjectName(u"le_p2_y")

        self.horizontalLayout_2.addWidget(self.le_p2_y)

        self.horizontalLayout_2.setStretch(1, 30)
        self.horizontalLayout_2.setStretch(2, 30)
        self.horizontalLayout_2.setStretch(3, 30)

        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.pb_crop = QPushButton(mw_image_crop)
        self.pb_crop.setObjectName(u"pb_crop")
        self.pb_crop.setEnabled(True)

        self.verticalLayout_2.addWidget(self.pb_crop)


        self.retranslateUi(mw_image_crop)

        QMetaObject.connectSlotsByName(mw_image_crop)
    # setupUi

    def retranslateUi(self, mw_image_crop):
        mw_image_crop.setWindowTitle(QCoreApplication.translate("mw_image_crop", u"Image crop", None))
        self.rb_upper_left.setText("")
        self.label.setText(QCoreApplication.translate("mw_image_crop", u"First point:", None))
        self.le_p1_x.setText(QCoreApplication.translate("mw_image_crop", u"0", None))
        self.le_p1_y.setText(QCoreApplication.translate("mw_image_crop", u"0", None))
        self.rb_lower_right.setText("")
        self.label_2.setText(QCoreApplication.translate("mw_image_crop", u"Second point:", None))
        self.le_p2_x.setText(QCoreApplication.translate("mw_image_crop", u"0", None))
        self.le_p2_y.setText(QCoreApplication.translate("mw_image_crop", u"0", None))
        self.pb_crop.setText(QCoreApplication.translate("mw_image_crop", u"Crop", None))
    # retranslateUi

