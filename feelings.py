#!/usr/bin/python3
#kanto kor pirka nociw AI system
#feelings.py:4つの感情を計算し出力
#感情は魂の言語だ。 -ニール・ドナルド・ウォルシュ
#©2019 Mamoru Itoi

#モジュール読み込み
import pickle
import re

#pirka内部のモジュール読み込み
import analyzer
from data import *

match = None
nowFeelings = [0, 0, 0, 0]
allFeelings = [[], [], [], []]

#メイン
def main():
	move()
	adjustment()
	decay()
	rounding()

#感情変動
def move():
	global nowFeelings
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
		nowFeelings[0] += jot
		nowFeelings[1] += tot
		nowFeelings[2] += fot
		nowFeelings[3] += sot
	
#常に-1.00から1.00の間になるように調整
def adjustment():
	global nowFeelings
	if nowFeelings[0] > 1.00:
		nowFeelings[0] = 1.00
	if nowFeelings[0] < -1.00:
		nowFeelings[0] = -1.00
	if nowFeelings[1] > 1.00:
		nowFeelings[1] = 1.00
	if nowFeelings[1] < -1.00:
		nowFeelings[1] = -1.00
	if nowFeelings[2] > 1.00:
		nowFeelings[2] = 1.00
	if nowFeelings[2] < -1.00:
		nowFeelings[2] = -1.00
	if nowFeelings[3] > 1.00:
		nowFeelings[3] = 1.00
	if nowFeelings[3] < -1.00:
		nowFeelings[3] = -1.00
		
#感情を和らげ、0.00に戻していく
def decay():
	global nowFeelings
	if not match:
		if nowFeelings[0] > 0.00:
			nowFeelings[0] -= 0.02
		if nowFeelings[0] < 0.00:
			nowFeelings[0] += 0.02
		if nowFeelings[1] > 0.00:
			nowFeelings[1] -= 0.02
		if nowFeelings[1] < 0.00:
			nowFeelings[1] += 0.02
		if nowFeelings[2] > 0.00:
			nowFeelings[2] -= 0.02
		if nowFeelings[2] < 0.00:
			nowFeelings[2] += 0.02
		if nowFeelings[3] > 0.00:
			nowFeelings[3] -= 0.02
		if nowFeelings[3] < 0.00:
			nowFeelings[3] += 0.02
		
#小数点以下2桁までに丸める	
def rounding():
	global nowFeelings
	nowFeelings[0] = round(nowFeelings[0], 2)
	nowFeelings[1] = round(nowFeelings[1], 2)
	nowFeelings[2] = round(nowFeelings[2], 2)
	nowFeelings[3] = round(nowFeelings[3], 2)
		
#感情を表示
def display():
	print(nowFeelings[0])
	print(nowFeelings[1])
	print(nowFeelings[2])
	print(nowFeelings[3])
