#!/usr/bin/python3
#kanto kor pirka nociw AI system
#gui.py:GUIを生成
#もし今日が人生最後の日なら、やろうとしていることは本当に自分のやりたいことだろうか？-スティーブ・ジョブズ
#©2019 Mamoru Itoi

#モジュール読み込み
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pickle
import sys
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QBrush, QColor, QIcon, QPainter, QPixmap
from PyQt5.QtWidgets import QAction, QApplication, QCheckBox, QGridLayout, QLabel, QLineEdit, QMainWindow, QMessageBox, QPushButton, QTextEdit, QWidget

#pirka内部のモジュール読み込み
import analyzer
import apps
import feelings
import learn
import response
import switch
from data import *

count = 0
nowLog = """kanto kor pirka nociw AI system α0.0.0.0a\n\n"""
text = None

class Pirka(QWidget):

	def __init__(self):
		super().__init__()
		self.title = "pirka AI α0.0"
		self.left = 100
		self.top = 100
		self.width = 1000
		self.height = 600
		self.initUI()
	
	def initUI(self):
		analyzer.start()
		learn.start()
		with open("log.pickle", "rb") as f:
			Log.log = pickle.load(f)
		#タイトル設定
		self.setWindowTitle(self.title)
		#位置・サイズ設定
		self.setGeometry(self.left, self.top, self.width, self.height)
		#アイコン設定
		self.setWindowIcon(QIcon("img/pirka.png"))
		#最大化できないようにする
		self.setMaximumHeight(self.height)
		self.setMaximumWidth(self.width)
		self.setMinimumHeight(self.height)
		self.setMinimumWidth(self.width)
		#入力欄
		self.textbox = QLineEdit(self)
		self.textbox.move(5, 560)
		self.textbox.resize(350,30)
		#ログ領域
		self.responselbl = QTextEdit(self)
		self.responselbl.move(505, 10)
		self.responselbl.resize(460, 580)
		self.responselbl.setText(nowLog)
		#送信ボタン
		self.sendButton = QPushButton("送信", self)
		self.sendButton.move(380,560)
		self.sendButton.clicked.connect(self.sendButtonClick)
		#顔
		self.face = QLabel(self)
		self.faceimg = QPixmap("img/zero.jpg")
		self.face.setPixmap(self.faceimg)
		self.face.move(10, 5)
		self.face.resize(460, 300)
		#グラフ
		self.graph = QLabel(self)
		plt.savefig("img/graph.png", figsize=(9, 6), dpi=50)
		self.graphImg = QPixmap("img/graph.png")
		self.graph.setPixmap(self.graphImg)
		self.graph.move(10, 310)
		#実行
		self.show()
		
	@pyqtSlot()
	def sendButtonClick(self):
		global text
		global nowLog
		text = self.textbox.text()
		#終了処理
		if text == "":
			Log.log += nowLog
			with open("log.pickle", "wb") as f:
				pickle.dump(Log.log, f)
			analyzer.end()
			learn.end()	
			quit()
		#メイン処理
		else:
			analyzer.main(text, "gui")
			s = switch.main()
			#会話モード
			if not s:
				feelings.main()
				learn.main()
				response.main()
			#機能モード
			else:
				apps.main(s)
			#感情により顔を変える
			joy = feelings.joy
			trust = feelings.trust
			fear = feelings.fear
			surprise = feelings.surprise
			if joy > 0.2:
				self.pixmap = QPixmap('img/plus.jpg')
				self.face.setPixmap(self.pixmap)
			elif joy < -0.2:
				self.pixmap = QPixmap('img/minus.jpg')
				self.face.setPixmap(self.pixmap)
			else:
				self.pixmap = QPixmap('img/zero.jpg')
				self.face.setPixmap(self.pixmap)
			self.textbox.setText("")
			#感情グラフを表示
			global count
			count += 1
			flist = feelings.flist
			flist[0].append(joy)
			flist[1].append(trust)
			flist[2].append(fear)
			flist[3].append(surprise)
			if len(flist[0]) > 10:
				plt.xlim([count - 9, count + 1])
			else:
				plt.xlim([0, 10])
			plt.ylim([-1, 1])
			plt.plot(flist[0], "b")
			plt.plot(flist[1], "g")
			plt.plot(flist[2], "r")
			plt.plot(flist[3], "y")
			plt.savefig("img/graph.png", figsize=(9, 6), dpi=50)
			self.graphimg = QPixmap("img/graph.png")
			self.graph.setPixmap(self.graphimg)
			#ログを表示
			diff = "In[" + str(count) + "] " + User.username + ":\n" + text + "\n" + "Out[" + str(count) + "] " + "pirka:\n" + response.response + "\n\n"
			nowLog = diff + nowLog
			self.responselbl.setText(nowLog )
			self.show()
			
app = QApplication(sys.argv)
ex = Pirka()
sys.exit(app.exec_())
