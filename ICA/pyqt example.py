import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from random import choice

class CounterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle("Update the counter!")

        self.label = QLabel(self)
        self.label.setText("0")
        self.label.setFont(QFont("Arial", 40))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setGeometry(200, 100, 200, 100)

        self.button = QPushButton("Click me!", self)
        self.button.setGeometry(250, 200, 100, 50)
        self.button.clicked.connect(self.update_counter)

        self.show()

    def update_counter(self):
        self.count += 1
        self.label.setText(str(self.count))
        if self.count % 10 == 0:
            colours = ["red", "blue", "green", "yellow", "purple", "orange"]
            self.label.setStyleSheet(f"color: {choice(colours)}")
        self.label.setFont(QFont("Arial", 40 + self.count))

# Create a QApplication instance (required for PyQt)
# We pass the command line arguments to the QApplication constructor 
# through sys.argv. This is not necessary for this example, but it is good practice.
# Alternatively, you can use an empty list: app = QApplication([])
app = QApplication(sys.argv)
# Create an instance of the CounterApp class (our main window)
ex = CounterApp()
# Start the application event loop
app.exec_()