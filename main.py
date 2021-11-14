from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFileDialog,QColorDialog,QApplication, \
 QTextEdit,QFontDialog,QDialog,QWidget,QPushButton, QLabel
from PyQt5.QtPrintSupport import QPageSetupDialog,QPrintDialog,QPrinter
from PyQt5.QtGui import QIcon

from cantonese import *
from setting import *
import sys

class Ui(object):
    def __init__(self):
        self.creat_info()
        self.printer = QPrinter()
        self.content = ""
        self.path = ""

    def creat_info(self):
        self.w = QWidget()
        self.w.setGeometry(0, 0, 2000, 2000)
        self.w.setWindowTitle('Cantonese IDE')
        self.w.setWindowIcon(QIcon('res/icon.ico'))
        self.w.setFixedSize(2000, 2000)
        self.creat_res()
        self.w.show()

    def creat_res(self):
        self.lang = LanguageSetter(LangType.CHINESE).data
        self.t1 = QTextEdit(self.w)
        self.t1.setGeometry(0,30,1980,1980)
        self.B_openfile = QPushButton(self.lang['openfile'], self.w)
        self.B_openfile.setGeometry(0,0,200,30)
        self.B_openmorefile = QPushButton(self.lang['openmorefile'], self.w)
        self.B_openmorefile.setGeometry(200,0,200,30)
        self.B_change_font = QPushButton(self.lang['change_font'], self.w)
        self.B_change_font.setGeometry(400,0,200,30)
        self.B_change_color = QPushButton(self.lang['change_color'], self.w)
        self.B_change_color.setGeometry(600,0,200,30)
        self.save_file = QPushButton(self.lang['save_file'], self.w)
        self.save_file.setGeometry(800,0,200,30)
        self.set_page = QPushButton(self.lang['set_page'], self.w)
        self.set_page.setGeometry(1000,0,200,30)
        self.print_file = QPushButton(self.lang['print_file'], self.w)
        self.print_file.setGeometry(1200,0,200,30)
        self.clear_file = QPushButton(self.lang['clear_file'],self.w)
        self.clear_file.setGeometry(1400,0,200,30)
        self.run_file = QPushButton(self.lang['run_file'], self.w)
        self.run_file.setGeometry(1600,0,200,30)
        self.exit_ = QPushButton(self.lang['exit_'], self.w)
        self.exit_.setGeometry(1800,0,200,30)
        self.config()

    def config(self):
        self.B_openfile.clicked.connect(self.open_file)
        self.B_openmorefile.clicked.connect(self.open_files)
        self.B_change_color.clicked.connect(self.change_color)
        self.B_change_font.clicked.connect(self.change_font)
        self.clear_file.clicked.connect(self.clear_all)
        self.save_file.clicked.connect(self.save_files)
        self.set_page.clicked.connect(self.page_config)
        self.print_file.clicked.connect(self.print_files)
        self.run_file.clicked.connect(self._run_file)
        self.exit_.clicked.connect(self.exit__)

    def clear_all(self):
        self.t1.clear()

    def open_file(self):
        files = QFileDialog.getOpenFileName(self.w,'打开本地文件')
        if files[0]:
            with open(files[0],mode = 'r', encoding = 'utf-8',errors='ignore') as f:
                c = f.read()
                self.content = c
                self.t1.setText(c)

    def open_files(self):
        files = QFileDialog.getOpenFileNames(self.w,'打开本地文件')
        print(files)
        if files[0]:
            for file in files[0]:
                with open(file,mode= 'r', encoding = 'utf-8',errors='ignore') as f:
                    c = f.read()
                    self.t1.append(c)

    def change_font(self):
        fo,b = QFontDialog.getFont()
        if b:
            self.t1.setCurrentFont(fo)

    def change_color(self):
        co = QColorDialog.getColor()
        if co.isValid():
            self.t1.setTextColor(co)

    def save_files(self):
        file = QFileDialog.getSaveFileName(self.w,'保存文件')
        if file[0]:
            with open(file[0],mode = 'r',encoding = 'utf-8',errors = 'ignore') as f:
                f.write(self.t1.toPlainText())

    def page_config(self):
        page_set = QPageSetupDialog(self.printer,self.w)
        page_set.exec_()

    def print_files(self):
        page_print = QPrintDialog(self.w)
        if QDialog.Accepted == page_print.exec_():
            self.t1.print(self.printer)

    def _run_file(self):
        cantonese_run(self.content, is_to_py = False, 
                    file = self.path, use_tradition = False)

    def exit__(self):
        exit(1)

app = QApplication(sys.argv)
ui = Ui()
sys.exit(app.exec_())