#!/usr/bin/python3
#kanto kor pirka nociw AI system α0.0.0.0a source code
#feelings.py:４つの感情を計算し出力
#感情は魂の言語だ。 -ニール・ドナルド・ウォルシュ
#©2019 Mamoru Itoi

#モジュール読み込み
import pickle
import re

#pirka内部のモジュール読み込み
import analyzer
from data import *

match = None
joy = 0
trust = 0
fear = 0
surprise = 0
flist = [[], [], [], []]

#メイン
def main():
	move()
	adjustment()
	decay()
	rounding()
	
#初期化
def start():
	global joy
	global trust
	global fear
	global surprise
	joy = 0
	trust = 0
	fear = 0
	surprise = 0
	
#感情変動
def move():
	global joy
	global trust
	global fear
	global surprise
	tokens = analyzer.tokens
	nociwTokens = []
	#感情変動用辞書「nociw」を開く
	with open("nociw.pickle", "rb") as f:
		Nociw.nociw = pickle.load(f)
	nociw = Nociw.nociw
	for token in tokens:
		for key, value in nociw.items():
			k = key
			v = value
			match = re.search(k, token[0])
			if match:
				tf = analyzer.tf(k)
				if v[0] == "plus":
					v[0] = 1 - tf
				else:
					v[0] = tf -1
				if v[1] == "plus":
					v[1] = 1 - tf
				else:
					v[1] = tf -1
				if v[2] == "plus":
					v[2] = 1 - tf
				else:
					v[2] = tf -1
				if v[3] == "plus":
					v[3] = 1 - tf
				else:
					v[3] = tf -1	
				nociwTokens.append(v)
	if len(tokens) != 0:
		jot = 0
		tot = 0
		fot = 0
		sot = 0
		for item in nociwTokens:
			jot += item[0]
			tot += item[1]
			fot += item[2]
			sot += item[3]
		joy += jot
		trust += tot
		fear += fot
		surprise += sot
	
#常に-1.00から1.00の間になるように調整
def adjustment():
	global joy
	global trust
	global fear
	global surprise
	if joy > 1.00:
		joy = 1.00
	if joy < -1.00:
		joy = -1.00
	if trust > 1.00:
		trust = 1.00
	if trust < -1.00:
		trust = -1.00
	if fear > 1.00:
		fear = 1.00
	if fear < -1.00:
		fear = -1.00
	if surprise > 1.00:
		surprise = 1.00
	if surprise < -1.00:
		surprise = -1.00
		
#感情を和らげ、0.00に戻していく
def decay():
	global joy
	global trust
	global fear
	global surprise
	if not match:
		if joy > 0.00:
			joy -= 0.02
		if joy < 0.00:
			joy += 0.02
		if trust > 0.00:
			trust -= 0.02
		if trust < 0.00:
			trust += 0.02
		if fear > 0.00:
			fear -= 0.02
		if fear < 0.00:
			fear += 0.02
		if surprise > 0.00:
			surprise -= 0.02
		if surprise < 0.00:
			surprise += 0.02
		
#小数点以下2桁までに丸める	
def rounding():
	global joy
	global trust
	global fear
	global surprise
	joy = round(joy, 2)
	trust = round(trust, 2)
	fear = round(fear, 2)
	surprise = round(surprise, 2)
		
#感情を表示
def display():
	print(joy)
	print(trust)
	print(fear)
	print(surprise)
