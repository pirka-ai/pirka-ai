#!/usr/bon/python3
#kanto kor pirka nociw AI system α0.0.0.0a source code
#apps.py:各種機能
#ハングリーであれ。愚かであれ。-スティーブ・ジョブズ
#©2019 Mamoru Itoi

#モジュール読み込み
import requests
from bs4 import BeautifulSoup

#pirka内部のモジュールを読み込み
import response
from data import *

triggers = {
	"いとっぴーはどこにいる" : "whereIsItoppy"
					}

def main(function):
	if function == "whereIsItoppy":
		whereIsItoppyGet()
	
def whereIsItoppyGet():
	html = requests.get("https://itoppy18.github.io/code/wii.html")
	soup = BeautifulSoup(html.text, "html.parser")
	place = soup.p.string
	print(place)
	response.response = "いとっぴーは" + str(place) + "にいる。"
