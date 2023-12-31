# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QMenu, QMenuBar,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)
import icons_rc

class Ui_mw_Main(object):
    def setupUi(self, mw_Main):
        if not mw_Main.objectName():
            mw_Main.setObjectName(u"mw_Main")
        mw_Main.resize(881, 700)
        icon = QIcon()
        icon.addFile(u":/menu/icons8-exit-sign-64.png", QSize(), QIcon.Normal, QIcon.Off)
        mw_Main.setWindowIcon(icon)
        self.action_Quit = QAction(mw_Main)
        self.action_Quit.setObjectName(u"action_Quit")
        self.action_Quit.setIcon(icon)
        self.action_Open_file = QAction(mw_Main)
        self.action_Open_file.setObjectName(u"action_Open_file")
        icon1 = QIcon()
        icon1.addFile(u":/menu/icons8-image-file-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Open_file.setIcon(icon1)
        self.actionRotate = QAction(mw_Main)
        self.actionRotate.setObjectName(u"actionRotate")
        icon2 = QIcon()
        icon2.addFile(u":/editors/icons8-rotate-right-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionRotate.setIcon(icon2)
        self.action_save = QAction(mw_Main)
        self.action_save.setObjectName(u"action_save")
        self.centralwidget = QWidget(mw_Main)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.fb_group_box = QGroupBox(self.centralwidget)
        self.fb_group_box.setObjectName(u"fb_group_box")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(50)
        sizePolicy1.setVerticalStretch(50)
        sizePolicy1.setHeightForWidth(self.fb_group_box.sizePolicy().hasHeightForWidth())
        self.fb_group_box.setSizePolicy(sizePolicy1)
        self.fb_group_box.setMinimumSize(QSize(0, 40))
        self.verticalLayout_3 = QVBoxLayout(self.fb_group_box)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(5, -1, -1, -1)
        self.pb_open_file = QPushButton(self.fb_group_box)
        self.pb_open_file.setObjectName(u"pb_open_file")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(32)
        sizePolicy2.setVerticalStretch(32)
        sizePolicy2.setHeightForWidth(self.pb_open_file.sizePolicy().hasHeightForWidth())
        self.pb_open_file.setSizePolicy(sizePolicy2)
        self.pb_open_file.setMinimumSize(QSize(30, 35))
        self.pb_open_file.setMaximumSize(QSize(30, 35))
        icon3 = QIcon()
        icon3.addFile(u":/menu/icons8-opened-folder-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_open_file.setIcon(icon3)
        self.pb_open_file.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.pb_open_file)

        self.pb_save = QPushButton(self.fb_group_box)
        self.pb_save.setObjectName(u"pb_save")
        self.pb_save.setEnabled(False)
        self.pb_save.setMinimumSize(QSize(30, 35))
        self.pb_save.setMaximumSize(QSize(30, 35))
        icon4 = QIcon()
        icon4.addFile(u":/editors/icons8-save-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_save.setIcon(icon4)
        self.pb_save.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.pb_save)

        self.pb_image_description = QPushButton(self.fb_group_box)
        self.pb_image_description.setObjectName(u"pb_image_description")
        self.pb_image_description.setEnabled(False)
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(30)
        sizePolicy3.setVerticalStretch(25)
        sizePolicy3.setHeightForWidth(self.pb_image_description.sizePolicy().hasHeightForWidth())
        self.pb_image_description.setSizePolicy(sizePolicy3)
        self.pb_image_description.setMinimumSize(QSize(30, 35))
        self.pb_image_description.setMaximumSize(QSize(30, 35))
        icon5 = QIcon()
        icon5.addFile(u":/menu/icons8-information-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_image_description.setIcon(icon5)
        self.pb_image_description.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.pb_image_description)

        self.pb_rotate = QPushButton(self.fb_group_box)
        self.pb_rotate.setObjectName(u"pb_rotate")
        self.pb_rotate.setEnabled(False)
        self.pb_rotate.setMinimumSize(QSize(30, 35))
        self.pb_rotate.setMaximumSize(QSize(30, 35))
        icon6 = QIcon()
        icon6.addFile(u":/editors/icons8-rotate-80.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_rotate.setIcon(icon6)
        self.pb_rotate.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.pb_rotate)

        self.pb_rotate_right = QPushButton(self.fb_group_box)
        self.pb_rotate_right.setObjectName(u"pb_rotate_right")
        self.pb_rotate_right.setEnabled(False)
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(50)
        sizePolicy4.setVerticalStretch(50)
        sizePolicy4.setHeightForWidth(self.pb_rotate_right.sizePolicy().hasHeightForWidth())
        self.pb_rotate_right.setSizePolicy(sizePolicy4)
        self.pb_rotate_right.setMinimumSize(QSize(30, 35))
        self.pb_rotate_right.setMaximumSize(QSize(30, 35))
        self.pb_rotate_right.setIcon(icon2)
        self.pb_rotate_right.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.pb_rotate_right)

        self.pb_rotate_left = QPushButton(self.fb_group_box)
        self.pb_rotate_left.setObjectName(u"pb_rotate_left")
        self.pb_rotate_left.setEnabled(False)
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.pb_rotate_left.sizePolicy().hasHeightForWidth())
        self.pb_rotate_left.setSizePolicy(sizePolicy5)
        self.pb_rotate_left.setMinimumSize(QSize(30, 35))
        self.pb_rotate_left.setMaximumSize(QSize(30, 35))
        icon7 = QIcon()
        icon7.addFile(u":/editors/icons8-rotate-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_rotate_left.setIcon(icon7)
        self.pb_rotate_left.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.pb_rotate_left)

        self.pb_flip = QPushButton(self.fb_group_box)
        self.pb_flip.setObjectName(u"pb_flip")
        self.pb_flip.setEnabled(False)
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.pb_flip.sizePolicy().hasHeightForWidth())
        self.pb_flip.setSizePolicy(sizePolicy6)
        self.pb_flip.setMinimumSize(QSize(30, 35))
        self.pb_flip.setMaximumSize(QSize(30, 35))
        icon8 = QIcon()
        icon8.addFile(u":/editors/icons8-flip-vertical-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_flip.setIcon(icon8)
        self.pb_flip.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.pb_flip)

        self.pb_enhance = QPushButton(self.fb_group_box)
        self.pb_enhance.setObjectName(u"pb_enhance")
        self.pb_enhance.setEnabled(False)
        self.pb_enhance.setMinimumSize(QSize(30, 35))
        self.pb_enhance.setMaximumSize(QSize(30, 35))
        icon9 = QIcon()
        icon9.addFile(u":/editors/icons8-wand-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_enhance.setIcon(icon9)
        self.pb_enhance.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.pb_enhance)

        self.pb_detail = QPushButton(self.fb_group_box)
        self.pb_detail.setObjectName(u"pb_detail")
        self.pb_detail.setEnabled(False)
        self.pb_detail.setMinimumSize(QSize(30, 35))
        self.pb_detail.setMaximumSize(QSize(30, 35))
        icon10 = QIcon()
        icon10.addFile(u":/editors/icons8-detail-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_detail.setIcon(icon10)
        self.pb_detail.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.pb_detail)

        self.pb_grayscale = QPushButton(self.fb_group_box)
        self.pb_grayscale.setObjectName(u"pb_grayscale")
        self.pb_grayscale.setEnabled(False)
        self.pb_grayscale.setMinimumSize(QSize(30, 35))
        self.pb_grayscale.setMaximumSize(QSize(30, 35))
        icon11 = QIcon()
        icon11.addFile(u":/editors/icons8-grayscale-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_grayscale.setIcon(icon11)
        self.pb_grayscale.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.pb_grayscale)

        self.pb_smooth = QPushButton(self.fb_group_box)
        self.pb_smooth.setObjectName(u"pb_smooth")
        self.pb_smooth.setEnabled(False)
        self.pb_smooth.setMinimumSize(QSize(30, 35))
        self.pb_smooth.setMaximumSize(QSize(30, 35))
        icon12 = QIcon()
        icon12.addFile(u":/editors/icons8-cleanup-noise-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_smooth.setIcon(icon12)
        self.pb_smooth.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.pb_smooth)

        self.pb_invert_colors = QPushButton(self.fb_group_box)
        self.pb_invert_colors.setObjectName(u"pb_invert_colors")
        self.pb_invert_colors.setEnabled(False)
        self.pb_invert_colors.setMinimumSize(QSize(30, 35))
        self.pb_invert_colors.setMaximumSize(QSize(30, 35))
        icon13 = QIcon()
        icon13.addFile(u":/editors/icons8-invert-colors-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_invert_colors.setIcon(icon13)
        self.pb_invert_colors.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.pb_invert_colors)

        self.pb_sharpen = QPushButton(self.fb_group_box)
        self.pb_sharpen.setObjectName(u"pb_sharpen")
        self.pb_sharpen.setEnabled(False)
        self.pb_sharpen.setMinimumSize(QSize(30, 35))
        self.pb_sharpen.setMaximumSize(QSize(30, 35))
        icon14 = QIcon()
        icon14.addFile(u":/editors/icons8-sharp-80.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_sharpen.setIcon(icon14)
        self.pb_sharpen.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.pb_sharpen)

        self.pb_find_edges = QPushButton(self.fb_group_box)
        self.pb_find_edges.setObjectName(u"pb_find_edges")
        self.pb_find_edges.setEnabled(False)
        self.pb_find_edges.setMinimumSize(QSize(30, 35))
        self.pb_find_edges.setMaximumSize(QSize(30, 35))
        icon15 = QIcon()
        icon15.addFile(u":/editors/icons8-broken-bottle-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_find_edges.setIcon(icon15)
        self.pb_find_edges.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.pb_find_edges)

        self.pb_emboss = QPushButton(self.fb_group_box)
        self.pb_emboss.setObjectName(u"pb_emboss")
        self.pb_emboss.setEnabled(False)
        self.pb_emboss.setMinimumSize(QSize(30, 35))
        self.pb_emboss.setMaximumSize(QSize(30, 35))
        icon16 = QIcon()
        icon16.addFile(u":/editors/icons8-3d-touch-80.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_emboss.setIcon(icon16)
        self.pb_emboss.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.pb_emboss)

        self.pb_blur = QPushButton(self.fb_group_box)
        self.pb_blur.setObjectName(u"pb_blur")
        self.pb_blur.setEnabled(False)
        self.pb_blur.setMinimumSize(QSize(30, 35))
        self.pb_blur.setMaximumSize(QSize(30, 35))
        icon17 = QIcon()
        icon17.addFile(u":/editors/icons8-filter-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_blur.setIcon(icon17)
        self.pb_blur.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.pb_blur)

        self.pb_kernel = QPushButton(self.fb_group_box)
        self.pb_kernel.setObjectName(u"pb_kernel")
        self.pb_kernel.setEnabled(False)
        self.pb_kernel.setMinimumSize(QSize(30, 35))
        self.pb_kernel.setMaximumSize(QSize(30, 35))
        icon18 = QIcon()
        icon18.addFile(u":/editors/icons8-kernel-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_kernel.setIcon(icon18)
        self.pb_kernel.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.pb_kernel)

        self.pb_resize = QPushButton(self.fb_group_box)
        self.pb_resize.setObjectName(u"pb_resize")
        self.pb_resize.setEnabled(False)
        self.pb_resize.setMinimumSize(QSize(30, 35))
        self.pb_resize.setMaximumSize(QSize(30, 35))
        icon19 = QIcon()
        icon19.addFile(u":/editors/icons8-crop-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_resize.setIcon(icon19)
        self.pb_resize.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.pb_resize)

        self.pb_crop = QPushButton(self.fb_group_box)
        self.pb_crop.setObjectName(u"pb_crop")
        self.pb_crop.setEnabled(False)
        self.pb_crop.setMinimumSize(QSize(30, 35))
        self.pb_crop.setMaximumSize(QSize(30, 35))
        icon20 = QIcon()
        icon20.addFile(u":/editors/icons8-cut-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_crop.setIcon(icon20)
        self.pb_crop.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.pb_crop)

        self.pb_showRGB = QPushButton(self.fb_group_box)
        self.pb_showRGB.setObjectName(u"pb_showRGB")
        self.pb_showRGB.setEnabled(False)
        self.pb_showRGB.setMinimumSize(QSize(30, 35))
        self.pb_showRGB.setMaximumSize(QSize(30, 35))
        icon21 = QIcon()
        icon21.addFile(u":/editors/icons8-rgb-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_showRGB.setIcon(icon21)
        self.pb_showRGB.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.pb_showRGB)

        self.pb_threshold = QPushButton(self.fb_group_box)
        self.pb_threshold.setObjectName(u"pb_threshold")
        self.pb_threshold.setEnabled(False)
        self.pb_threshold.setMinimumSize(QSize(30, 35))
        self.pb_threshold.setMaximumSize(QSize(30, 35))
        icon22 = QIcon()
        icon22.addFile(u":/editors/icons8-electrical-threshold-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_threshold.setIcon(icon22)
        self.pb_threshold.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.pb_threshold)

        self.pb_revert = QPushButton(self.fb_group_box)
        self.pb_revert.setObjectName(u"pb_revert")
        self.pb_revert.setEnabled(False)
        self.pb_revert.setMinimumSize(QSize(30, 35))
        self.pb_revert.setMaximumSize(QSize(30, 35))
        icon23 = QIcon()
        icon23.addFile(u":/main/icons8-revert-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_revert.setIcon(icon23)
        self.pb_revert.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.pb_revert)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pb_clear = QPushButton(self.fb_group_box)
        self.pb_clear.setObjectName(u"pb_clear")
        self.pb_clear.setEnabled(False)
        self.pb_clear.setMinimumSize(QSize(30, 35))
        self.pb_clear.setMaximumSize(QSize(30, 35))
        icon24 = QIcon()
        icon24.addFile(u":/editors/icons8-trash-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_clear.setIcon(icon24)
        self.pb_clear.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.pb_clear)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.fb_group_box)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy7)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 855, 533))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.qt_label = QLabel(self.scrollAreaWidgetContents)
        self.qt_label.setObjectName(u"qt_label")
        self.qt_label.setMouseTracking(True)
        self.qt_label.setMidLineWidth(-5)
        self.qt_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_2.addWidget(self.qt_label)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy8)
        self.groupBox.setMinimumSize(QSize(0, 30))
        self.groupBox.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox.setBaseSize(QSize(0, 30))
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.qt_image_description = QLabel(self.groupBox)
        self.qt_image_description.setObjectName(u"qt_image_description")
        sizePolicy9 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.qt_image_description.sizePolicy().hasHeightForWidth())
        self.qt_image_description.setSizePolicy(sizePolicy9)
        self.qt_image_description.setMinimumSize(QSize(0, 20))
        self.qt_image_description.setMaximumSize(QSize(16777215, 200))
        self.qt_image_description.setBaseSize(QSize(0, 20))

        self.horizontalLayout_2.addWidget(self.qt_image_description)

        self.ql_coordinates = QLabel(self.groupBox)
        self.ql_coordinates.setObjectName(u"ql_coordinates")
        sizePolicy9.setHeightForWidth(self.ql_coordinates.sizePolicy().hasHeightForWidth())
        self.ql_coordinates.setSizePolicy(sizePolicy9)
        self.ql_coordinates.setMinimumSize(QSize(0, 20))
        self.ql_coordinates.setMaximumSize(QSize(16777215, 100))
        self.ql_coordinates.setBaseSize(QSize(0, 20))
        self.ql_coordinates.setLayoutDirection(Qt.LeftToRight)
        self.ql_coordinates.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_2.addWidget(self.ql_coordinates)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.groupBox)

        mw_Main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mw_Main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 881, 24))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        mw_Main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mw_Main)
        self.statusbar.setObjectName(u"statusbar")
        mw_Main.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.action_Open_file)
        self.menuFile.addAction(self.action_Quit)
        self.menuFile.addAction(self.action_save)

        self.retranslateUi(mw_Main)

        QMetaObject.connectSlotsByName(mw_Main)
    # setupUi

    def retranslateUi(self, mw_Main):
        mw_Main.setWindowTitle(QCoreApplication.translate("mw_Main", u"ImageEditor Application", None))
        self.action_Quit.setText(QCoreApplication.translate("mw_Main", u"Quit", None))
        self.action_Open_file.setText(QCoreApplication.translate("mw_Main", u"Open file...", None))
        self.actionRotate.setText(QCoreApplication.translate("mw_Main", u"Rotate", None))
#if QT_CONFIG(shortcut)
        self.actionRotate.setShortcut(QCoreApplication.translate("mw_Main", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.action_save.setText(QCoreApplication.translate("mw_Main", u"Save file", None))
        self.fb_group_box.setTitle("")
#if QT_CONFIG(tooltip)
        self.pb_open_file.setToolTip(QCoreApplication.translate("mw_Main", u"Browse an image...", None))
#endif // QT_CONFIG(tooltip)
        self.pb_open_file.setText("")
#if QT_CONFIG(tooltip)
        self.pb_save.setToolTip(QCoreApplication.translate("mw_Main", u"Save an image...", None))
#endif // QT_CONFIG(tooltip)
        self.pb_save.setText("")
#if QT_CONFIG(tooltip)
        self.pb_image_description.setToolTip(QCoreApplication.translate("mw_Main", u"Image Info", None))
#endif // QT_CONFIG(tooltip)
        self.pb_image_description.setText("")
#if QT_CONFIG(tooltip)
        self.pb_rotate.setToolTip(QCoreApplication.translate("mw_Main", u"Rotation window...", None))
#endif // QT_CONFIG(tooltip)
        self.pb_rotate.setText("")
#if QT_CONFIG(tooltip)
        self.pb_rotate_right.setToolTip(QCoreApplication.translate("mw_Main", u"Rotate right", None))
#endif // QT_CONFIG(tooltip)
        self.pb_rotate_right.setText("")
#if QT_CONFIG(shortcut)
        self.pb_rotate_right.setShortcut(QCoreApplication.translate("mw_Main", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.pb_rotate_left.setToolTip(QCoreApplication.translate("mw_Main", u"Rotate left", None))
#endif // QT_CONFIG(tooltip)
        self.pb_rotate_left.setText("")
#if QT_CONFIG(shortcut)
        self.pb_rotate_left.setShortcut(QCoreApplication.translate("mw_Main", u"Ctrl+L", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.pb_flip.setToolTip(QCoreApplication.translate("mw_Main", u"Flip", None))
#endif // QT_CONFIG(tooltip)
        self.pb_flip.setText("")
#if QT_CONFIG(tooltip)
        self.pb_enhance.setToolTip(QCoreApplication.translate("mw_Main", u"Enhance Image", None))
#endif // QT_CONFIG(tooltip)
        self.pb_enhance.setText("")
#if QT_CONFIG(tooltip)
        self.pb_detail.setToolTip(QCoreApplication.translate("mw_Main", u"Detail", None))
#endif // QT_CONFIG(tooltip)
        self.pb_detail.setText("")
#if QT_CONFIG(tooltip)
        self.pb_grayscale.setToolTip(QCoreApplication.translate("mw_Main", u"Grayscale", None))
#endif // QT_CONFIG(tooltip)
        self.pb_grayscale.setText("")
#if QT_CONFIG(tooltip)
        self.pb_smooth.setToolTip(QCoreApplication.translate("mw_Main", u"Smooth", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pb_smooth.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.pb_smooth.setText("")
#if QT_CONFIG(tooltip)
        self.pb_invert_colors.setToolTip(QCoreApplication.translate("mw_Main", u"Invert colors", None))
#endif // QT_CONFIG(tooltip)
        self.pb_invert_colors.setText("")
#if QT_CONFIG(tooltip)
        self.pb_sharpen.setToolTip(QCoreApplication.translate("mw_Main", u" Sharpen image", None))
#endif // QT_CONFIG(tooltip)
        self.pb_sharpen.setText("")
#if QT_CONFIG(tooltip)
        self.pb_find_edges.setToolTip(QCoreApplication.translate("mw_Main", u"Find edges", None))
#endif // QT_CONFIG(tooltip)
        self.pb_find_edges.setText("")
#if QT_CONFIG(tooltip)
        self.pb_emboss.setToolTip(QCoreApplication.translate("mw_Main", u"Emboss", None))
#endif // QT_CONFIG(tooltip)
        self.pb_emboss.setText("")
#if QT_CONFIG(tooltip)
        self.pb_blur.setToolTip(QCoreApplication.translate("mw_Main", u"Additional filters", None))
#endif // QT_CONFIG(tooltip)
        self.pb_blur.setText("")
#if QT_CONFIG(tooltip)
        self.pb_kernel.setToolTip(QCoreApplication.translate("mw_Main", u"Write your own kernel", None))
#endif // QT_CONFIG(tooltip)
        self.pb_kernel.setText("")
#if QT_CONFIG(tooltip)
        self.pb_resize.setToolTip(QCoreApplication.translate("mw_Main", u"Resize image", None))
#endif // QT_CONFIG(tooltip)
        self.pb_resize.setText("")
#if QT_CONFIG(tooltip)
        self.pb_crop.setToolTip(QCoreApplication.translate("mw_Main", u"Crop image", None))
#endif // QT_CONFIG(tooltip)
        self.pb_crop.setText("")
#if QT_CONFIG(tooltip)
        self.pb_showRGB.setToolTip(QCoreApplication.translate("mw_Main", u"Pixel values", None))
#endif // QT_CONFIG(tooltip)
        self.pb_showRGB.setText("")
#if QT_CONFIG(tooltip)
        self.pb_threshold.setToolTip(QCoreApplication.translate("mw_Main", u"Threshold", None))
#endif // QT_CONFIG(tooltip)
        self.pb_threshold.setText("")
#if QT_CONFIG(tooltip)
        self.pb_revert.setToolTip(QCoreApplication.translate("mw_Main", u"Revert changes", None))
#endif // QT_CONFIG(tooltip)
        self.pb_revert.setText("")
#if QT_CONFIG(tooltip)
        self.pb_clear.setToolTip(QCoreApplication.translate("mw_Main", u"Remove image", None))
#endif // QT_CONFIG(tooltip)
        self.pb_clear.setText("")
        self.qt_label.setText("")
        self.groupBox.setTitle("")
        self.qt_image_description.setText(QCoreApplication.translate("mw_Main", u"No image opened...", None))
        self.ql_coordinates.setText(QCoreApplication.translate("mw_Main", u"(0,0)", None))
        self.menuFile.setTitle(QCoreApplication.translate("mw_Main", u"File", None))
    # retranslateUi

