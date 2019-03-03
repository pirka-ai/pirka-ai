#!/usr/bin/python3
#kanto kor pirka nociw AI system
#analyzer.py:MeCabによる形態素解析を行う
#単純であることは、究極の洗練だ。 -レオナルド・ダ・ヴィンチ
#©2019 Mamoru Itoi

#モジュール読み込み
import CaboCha
import MeCab
import pickle
import re

#pirka内部のモジュール読み込み
from data import *

tokens = []
chunks = []

#メイン処理
def tokenizer(text, mode = "normal"):
	t = MeCab.Tagger("")
	t.parse("")
	m = t.parseToNode(text)
	if mode == "gui":
		global tokens
	tokens = []
	while m:
		tokenData = m.feature.split(",")
		token = [m.surface]
		for data in tokenData:
			token.append(data)
		tokens.append(token)
		m = m.next
		if mode == "gui":
			Log.tokenLog.append(token)
	return tokens

def dependencyAnalyzer(text, mode="nomal"):
	c = CaboCha.Parser()
	tree = c.parse(text)
	chunks = []
	t = ""
	toChunkId = -1
	if mode == "gui":
		global chunks
	for i in range(0, tree.size()):
		token = tree.token(i)
		t = token.surface if token.chunk else (t + token.surface)
		toChunkId = token.chunk.link if token.chunk else toChunkId
		if i == tree.size() - 1 or tree.token(i+1).chunk:
			chunks.append({"c" : text, "to" : toChunkId})
	return chunks
	
#起動時に実行する処理
def start():
	with open("tokenLog.pickle", "rb") as f:
		Log.tokenLog = pickle.load(f)
		
#終了時に実行する処理
def end():
	with open("tokenLog.pickle", "wb") as f:
		pickle.dump(Log.tokenLog, f)

#TF(単語頻度)を計算
def tf(word):
	tokenLog = Log.tokenLog
	count = 0
	for token in tokenLog:
		surface = token[0]
		match = re.search(word, surface)
		if match:
			count += 1
	tf = round(count / len(tokenLog), 2)
	return tf
	
#リセット
def reset():
	with open("tokenLog.pickle", "wb") as f:
		pickle.dump(Log.tokenLog, f)
