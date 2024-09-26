from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QVBoxLayout, QVBoxLayout, QFrame, QSizePolicy
from PyQt5.QtGui import QPixmap, QIcon, QImage
from PyQt5.QtCore import Qt, QSize, QTimer
import cv2
import subprocess
from getmac import get_mac_address as gma

class Monitor(QWidget):
    def __init__(self, app_state):
        super().__init__()

        main_layout = QVBoxLayout()
        hbox_top = QHBoxLayout()

        hbox_top.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        logo_image_top_left = QLabel()
        logo_image_top_left.setPixmap(
            QPixmap("images/logo.png").scaledToWidth(40).scaledToHeight(40))
        logo_image_top_left.setScaledContents(True)

        logo_image_top_right = QLabel()
        logo_image_top_right.setPixmap(
            QPixmap("images/titulo.png").scaledToWidth(198))
        logo_image_top_right.setScaledContents(True)

        hbox_top.addWidget(logo_image_top_left)
        hbox_top.addWidget(logo_image_top_right)
        main_layout.addLayout(hbox_top)

        central_layout = QHBoxLayout()

        left_layout = QVBoxLayout()
        left_layout.setAlignment(Qt.AlignBottom | Qt.AlignLeft)
        central_layout.addLayout(left_layout)

        button_home = QPushButton()
        button_home.setIcon(QIcon("images/home.png"))
        button_home.setIconSize(QSize(50, 50))
        button_home.setStyleSheet("background-color: rgba(38,64,67,255);")
        button_home.clicked.connect(lambda: self.gotoHome(app_state))
        left_layout.addWidget(button_home)

        button_info = QPushButton()
        button_info.setIcon(QIcon("images/info.png"))
        button_info.setIconSize(QSize(50, 50))
        button_info.setStyleSheet("background-color: rgba(38,64,67,255);")
        button_info.clicked.connect(lambda: self.gotoInfo(app_state))
        left_layout.addWidget(button_info)

        center_layout = QVBoxLayout()

        center_layout.setAlignment(Qt.AlignCenter)
        central_layout.addLayout(center_layout)

        button_monitor_exterior = QPushButton("Monitor exterior")
        button_monitor_exterior.setIcon(QIcon("images/camara.png"))
        button_monitor_exterior.setIconSize(QSize(200, 200))
        button_monitor_exterior.setStyleSheet(
            "background-color: rgb(77, 128, 119); color: white;")
        button_monitor_exterior.clicked.connect(lambda: self.activeCamera())
        center_layout.addWidget(button_monitor_exterior)

        button_monitor_interior = QPushButton("Monitor interior")
        button_monitor_interior.setIcon(QIcon("images/camara_interior.png"))
        button_monitor_interior.setIconSize(QSize(200, 200))
        button_monitor_interior.setStyleSheet(
            "background-color: rgb(77, 128, 119); color: white;")
        button_monitor_exterior.clicked.connect(lambda: self.activeCamera2)
        center_layout.addWidget(button_monitor_interior)

        right_layout = QVBoxLayout()
        right_layout.setAlignment(Qt.AlignBottom | Qt.AlignLeft)
        central_layout.addLayout(right_layout)

        # Frame para representar el video
        self.video_frame = QFrame()
        self.video_frame.setStyleSheet("background-color: black;")
        self.video_frame.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding)
        right_layout.addWidget(self.video_frame)
        main_layout.addLayout(central_layout)
        self.setLayout(main_layout)

    def activeCamera(self):  # camara Exterior
        mac = gma()
        cap1 = cv2.VideoCapture(
            'rtsp://admin:eonboxseg1@192.168.1.98/H264?ch=1&subtype=0')
        command = [
            'ffmpeg',
            '-y',
            '-f', 'rawvideo',
            '-vcodec', 'rawvideo',
            '-pixel_format', 'bgr24',
            '-s', '640x480',
            '-framerate', '30',
            '-i', '-',
            '-map', '0:v',
            '-map', '1:a',
            '-c:v', 'libx264',
            '-c:a', 'aac',
            '-preset', 'ultrafast',
            '-tune', 'zerolatency',
            '-b:v', '1500k',
            '-maxrate', '1500k',
            '-bufsize', '512k',
            '-pix_fmt', 'yuv420p',
            '-r', '30',
            '-g', '60',
            '-f', 'flv'
            "rtmp://eonproduccion.net/live/interior/" + mac
        ]
        p = subprocess.Popen(command, stdin=subprocess.PIPE)
        ret1, frame1 = cap1.read()
        if ret1:
            frame1 = cv2.resize(frame1, (640, 350))
            img1 = QImage(
                frame1, frame1.shape[1], frame1.shape[0], QImage.Format_RGB888)
            pixmap1 = QPixmap.fromImage(img1)
            pixmap1 = pixmap1.scaled(
                self.video_frame.size(), Qt.KeepAspectRatio)
            
            p.stdin.write(frame1.tobytes())
            # cv2.imshow('Capturing',frame)

            label = QLabel(self.video_frame)
            label.setPixmap(pixmap1)
            label.setAlignment(Qt.AlignCenter)
            label.setGeometry(0, 0, self.video_frame.width(),
                              self.video_frame.height())
            label.show()

    def activeCamera2(self):
        mac = gma()
        cap = cv2.VideoCapture(
            'rtsp://admin:eonboxseg1@192.168.1.115/H264?ch=1&subtype=0')
        command = [
            'ffmpeg',
            '-y',
            '-f', 'rawvideo',
            '-vcodec', 'rawvideo',
            '-pixel_format', 'bgr24',
            '-s', '640x480',
            '-framerate', '30',
            '-i', '-',
            '-map', '0:v',
            '-map', '1:a',
            '-c:v', 'libx264',
            '-c:a', 'aac',
            '-preset', 'ultrafast',
            '-tune', 'zerolatency',
            '-b:v', '1500k',
            '-maxrate', '1500k',
            '-bufsize', '512k',
            '-pix_fmt', 'yuv420p',
            '-r', '30',
            '-g', '60',
            '-f', 'flv'
            "rtmp://eonproduccion.net/live/exterior/" + mac
        ]
        p = subprocess.Popen(command, stdin=subprocess.PIPE)
        ret, frame = cap.read()
        if ret:
            frame = cv2.resize(frame, (640, 350))
            img = QImage(frame, frame.shape[1],
                         frame.shape[0], QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(img)
            pixmap = pixmap.scaled(self.video_frame.size(), Qt.KeepAspectRatio)

            p.stdin.write(frame.tobytes())
            # cv2.imshow('Capturing',frame)

            label = QLabel(self.video_frame)
            label.setPixmap(pixmap)
            label.setAlignment(Qt.AlignCenter)
            label.setGeometry(0, 0, self.video_frame.width(),
                              self.video_frame.height())
            label.show()

    def gotoHome(self, app_state):
        app_state.set_stack(5)

    def gotoInfo(self, app_state):
        app_state.set_stack(8)