from PyQt5.QtGui import QPixmap
from listing import *
__author__ = 'ayew'
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget, QApplication, QGroupBox, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, \
    QGridLayout, QFormLayout, QLineEdit, QTextEdit


class login(QWidget):
    def __init__(self):
        super(login, self).__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle("Amazon listing")
        layout = QGridLayout()
        self.setGeometry(600, 600, 400, 350)
        pix = QPixmap('./yi_go.jpeg')
        lb1 = QLabel(self)
        lb1.setGeometry(0, 0, 100, 100)
        lb1.setStyleSheet("border: 2px solid grey")
        lb1.setPixmap(pix)
        lb1.setFixedSize(100, 100)
        lb1.setScaledContents(True)
        siteLabel = QLabel("站点")
        self.siteLineEdit = QLineEdit(" ")
        asLabel = QLabel("ASIN")
        self.asLineEdit = QLineEdit(" ")
        emitLabel = QLabel("    敲黑板!!!\n        1.支持站点有:US/UK/ES/DE/CA/IT\n        2.建议开启小飞机使用\n        3.输入完成后点击启动即可\n        4.出错/卡死/找不到请检查重开Y!")
        self.phoneLineEdit = QLabel("/US")
        # timeLabel = QLabel("邮箱")
        # self.mailEdit = QLineEdit("")
        # layout.setSpacing(10)
        layout.addWidget(lb1, 1, 0)
        layout.addWidget(emitLabel, 1, 1)
        layout.addWidget(asLabel, 2, 0)
        layout.addWidget(self.asLineEdit, 2, 1)
        layout.addWidget(siteLabel, 3, 0)
        layout.addWidget(self.siteLineEdit, 3, 1)
        # layout.addWidget(timeLabel,4,0)
        # layout.addWidget(self.mailEdit,4,1)
        layout.setColumnStretch(1, 10)
        self.save_Btn = QPushButton('启动')
        self.cancle_Btn = QPushButton('退出')
        self.cancle_Btn.clicked.connect(QCoreApplication.quit)
        self.save_Btn.clicked.connect(self.addNum)
        layout.addWidget(self.save_Btn)
        layout.addWidget(self.cancle_Btn)
        self.setLayout(layout)

    def addNum(self):
        site = self.siteLineEdit.text().replace(" ",'')  # 获取文本框内容
        asin = self.asLineEdit.text().replace(" ",'')

        self.save_Btn.setText("正在启动中,请勿重复点击")
        # print('站点: %s ASIN: %s ' % (site, asin))
        print([site,asin],type(site),type(asin))
        url=get_base_url(site)
        # html = qt_mian(site, asin)

        print("正在启动浏览器...")
        driver = webdriver.Chrome(CHROM_PATH)
        driver.get(url[0])
        page = 1

        for i in range(30):
            print("\r倒计时%2s"%(30-i+1),end='')
            time.sleep(1)
            self.save_Btn.setText('剩余%2d s'%(30-i+1))
        print("")



        html = driver.page_source
        driver.quit()
        conti_main(site,html,page,asin,url)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    comboxDemo = login()
    comboxDemo.show()
    sys.exit(app.exec_())