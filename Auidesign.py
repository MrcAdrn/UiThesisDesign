import sys
from PyQt5.QtWidgets import QMainWindow, QApplication , QPushButton , QLabel
from main_ui import Ui_MainWindow
from PyQt5.QtGui import QPixmap, QIcon



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.icon_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.dashboardbutton.setChecked(True)
        self.setWindowIcon(QIcon("C:/Users/4quin/OneDrive/Desktop/FinalThesisDesignShesh/LOGO/ACC_LOGO.jpg"))


      
      
    ##Qpush button chagne
    def on_stackedwidget_currentChanged(self, index):
        buttonlist = self.ui.icon_only_widget.findChildren(QPushButton) \
                     + self.ui.icons_details_widget.findChildren(QPushButton)
        
        
    ##funtion for changing  page
    def on_dashboardbutton_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_dashboardbutton_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    
    def on_peoplebutton_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_peoplebutton_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_acbutton_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)
    
    def on_acbutton_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)
    
    def on_electricfanbutton_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_electricfanbutton_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_lightsbutton_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def on_lightsbutton_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def on_ldoorbutton_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(5)

    def on_doorbutton_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(5)

    def on_powerconsumptionbutton_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(6)

    def on_powerconsumptionbutton_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(6)
    
    def on_infobutton_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(7)

    def on_infobutton_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(7)

              

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    window.setWindowTitle("Adaptive Classroom Control")
    
    sys.exit(app.exec())
