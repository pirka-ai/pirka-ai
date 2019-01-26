#!/usr/bin/python3
#kanto kor pirka nociw AI system
#learn.py:応答の学習
#学習:経験を通じて行動に持続的な変化が生じる、ないし行動パターンが変化する現象のこと。 -Wikipedia
#©2019 Mamoru Itoi

#モジュール読み込み
import math
import pickle
import re
import time

#pirka内部のモジュールを読み込み
import analyzer
from data import *

#常識学習が行われたかのフラグ
did = None
#今までにない常識が登録されたかのフラグ
notFound = None

start = None
end = None

#メイン処理
def main():
	withdrawn()
	makeNounTemp()
	makeProperNounTemp()
	makeNumberNounTemp()
	makeProNounTemp()
	makeVerbTemp()
	makeVerbMizenTemp()
	makeVerbRennyoTemp()
	makeVerbRentaiTemp()
	makeVerbKateiTemp()
	makeVerbMeireiTemp()
	makeAdjTemp()
	makeAdjMizenTemp()
	makeAdjRennyoTemp()
	makeAdjRentaiTemp()
	makeAdjKateiTemp()
	makeAdjVerbTemp()
	commonSense()
	
#起動時に実行
def start():
	with open("noun.pickle", "rb") as f:
		Learn.noun = pickle.load(f)
	with open("properNoun.pickle", "rb") as f:
		Learn.properNoun = pickle.load(f)
	with open("numberNoun.pickle", "rb") as f:
		Learn.numberNoun = pickle.load(f)
	with open("proNoun.pickle", "rb") as f:
		Learn.proNoun = pickle.load(f)
	with open("verb.pickle", "rb") as f:
		Learn.verb = pickle.load(f)
	with open("verbMizen.pickle", "rb") as f:
		Learn.verbMizen = pickle.load(f)
	with open("verbRennyo.pickle", "rb") as f:
		Learn.verbRennyo = pickle.load(f)
	with open("verbRentai.pickle", "rb") as f:
		Learn.verbRentai = pickle.load(f)
	with open("verbKatei.pickle", "rb") as f:
		Learn.verbKatei = pickle.load(f)
	with open("verbMeirei.pickle", "rb") as f:
		Learn.verbMeirei = pickle.load(f)
	with open("adj.pickle", "rb") as f:
		Learn.adj = pickle.load(f)
	with open("adjMizen.pickle", "rb") as f:
		Learn.adjMizen = pickle.load(f)
	with open("adjRennyo.pickle", "rb") as f:
		Learn.adjRennyo = pickle.load(f)
	with open("adjRentai.pickle", "rb") as f:
		Learn.adjRentai = pickle.load(f)
	with open("adjKatei.pickle", "rb") as f:
		Learn.adjKatei = pickle.load(f)
	with open("adjVerb.pickle",  "rb") as f:
		Learn.adjVerb = pickle.load(f)
	with open("definition.pickle", "rb") as f:
		Learn.definition = pickle.load(f)

#tokensの両端の空白を削除
def withdrawn():
	tokens = analyzer.tokens
	tokens.pop(0)
	tokens.pop(-1)

#名詞を使ったテンプレートを生成
def makeNounTemp():
	tokens = analyzer.tokens
	nowTemp = []
	count = 0
	for token in tokens:
		surface = token[0]
		part = token[1]
		typeOfPart = token[2]
		if part == "名詞" and typeOfPart == "一般":
			count += 1
			surface = "%pat%"
		nowTemp.append(surface)
		join = "".join(nowTemp)
	noun = Learn.noun
	if count != 0 and not join in noun[count]:
		if not count in noun:
			noun[count] = []
		noun[count].append(join)

#固有名詞を使ったテンプレートを生成
def makeProperNounTemp():
	tokens = analyzer.tokens
	nowTemp = []
	count = 0
	appearance = False
	for token in tokens:
		surface = token[0]
		part = token[1]
		typeOfPart = token[2]
		if part == "名詞" and typeOfPart == "固有名詞":
			appearance = True
			count += 1
			surface = "%pat%"
		nowTemp.append(surface)
		join = "".join(nowTemp)
	properNoun = Learn.properNoun
	if count != 0 and not join in properNoun[count]:
		if not count in properNoun:
			properoun[count] = []
		properNoun[count].append(join)

#数詞を使ったテンプレートを生成	
def makeNumberNounTemp():
	tokens = analyzer.tokens
	nowTemp = []
	count = 0
	appearance = False
	for token in tokens:
		surface = token[0]
		part = token[1]
		typeOfPart = token[2]
		if part == "名詞" and typeOfPart == "数":
			appearance = True
			count += 1
			surface = "%pat%"
		nowTemp.append(surface)
		join = "".join(nowTemp)
	numberNoun = Learn.numberNoun
	if count != 0 and not join in numberNoun[count]:
		if not count in numberNoun:
			numberNoun[count] = []
		numberNoun[count].append(join)

#代名詞を使ったテンプレートを生成
def makeProNounTemp():
	tokens = analyzer.tokens
	nowTemp = []
	count = 0
	appearance = False
	for token in tokens:
		surface = token[0]
		part = token[1]
		typeOfPart = token[2]
		if part == "名詞" and typeOfPart == "代名詞":
			appearance = True
			count += 1
			surface = "%pat%"
		nowTemp.append(surface)
		join = "".join(nowTemp)
	proNoun = Learn.proNoun
	if count != 0 and not join in proNoun[count]:
		if not count in proNoun:
			proNoun[count] = []
		proNoun[count].append(join)
		
#動詞を使ったテンプレートを生成
def makeVerbTemp():
	tokens = analyzer.tokens
	nowTemp = []
	count = 0
	appearance = False
	for token in tokens:
		surface = token[0]
		part = token[1]
		inflection = token[6]
		if part == "動詞" and inflection == "基本形":
			appearance = True
			count += 1
			surface = "%pat%"
		nowTemp.append(surface)
		join = "".join(nowTemp)
	verb = Learn.verb
	if count != 0 and not join in verb[count]:
		if not count in verb:
			verb[count] = []
		verb[count].append(join)

def makeVerbMizenTemp():
	tokens = analyzer.tokens
	nowTemp = []
	count = 0
	appearance = False
	for token in tokens:
		surface = token[0]
		part = token[1]
		inflection = token[6]
		if part == "動詞" and inflection == "未然形":
			appearance = True
			count += 1
			surface = "%pat%"
		nowTemp.append(surface)
		join = "".join(nowTemp)
	verbMizen = Learn.verbMizen
	if count != 0 and not join in verbMizen[count]:
		if not count in verbMizen:
			verbMizen[count] = []
		verbMizen[count].append(join)
		
def makeVerbRennyoTemp():
	tokens = analyzer.tokens
	nowTemp = []
	count = 0
	appearance = False
	for token in tokens:
		surface = token[0]
		part = token[1]
		inflection = token[6]
		if part == "動詞" and inflection == "連用タ連続":
			appearance = True
			count += 1
			surface = "%pat%"
		nowTemp.append(surface)
		join = "".join(nowTemp)
	verbRennyo = Learn.verbRennyo
	if count != 0 and not join in verbRennyo[count]:
		if not count in verbRennyo:
			verbRennyo[count] = []
		verbRennyo[count].append(join)
		
def makeVerbRentaiTemp():
	tokens = analyzer.tokens
	nowTemp = []
	count = 0
	appearance = False
	for token in tokens:
		surface = token[0]
		part = token[1]
		inflection = token[6]
		if part == "動詞" and inflection == "連体形":
			appearance = True
			count += 1
			surface = "%pat%"
		nowTemp.append(surface)
		join = "".join(nowTemp)
	verbRentai = Learn.verbRentai
	if count != 0 and not join in verbRentai[count]:
		if not count in verbRentai:
			verbRentai[count] = []
		verbRentai[count].append(join)

def makeVerbKateiTemp():
	tokens = analyzer.tokens
	nowTemp = []
	count = 0
	appearance = False
	for token in tokens:
		surface = token[0]
		part = token[1]
		inflection = token[6]
		if part == "動詞" and inflection == "仮定形":
			appearance = True
			count += 1
			surface = "%pat%"
		nowTemp.append(surface)
		join = "".join(nowTemp)
	verbKatei = Learn.verbKatei
	if count != 0 and not join in verbKatei[count]:
		if not count in verbKatei:
			verbKatei[count] = []
		verbKatei[count].append(join)
		
def makeVerbMeireiTemp():
	tokens = analyzer.tokens
	nowTemp = []
	count = 0
	appearance = False
	for token in tokens:
		surface = token[0]
		part = token[1]
		inflection = token[6]
		if part == "動詞" and inflection == ("命令ro" or "命令e"):
			appearance = True
			count += 1
			surface = "%pat%"
		nowTemp.append(surface)
		join = "".join(nowTemp)
	verbMeirei = Learn.verbMeirei
	if count != 0 and not join in verbMeirei[count]:
		if not count in verbMeirei:
			verbMeirei[count] = []
		verbMeirei[count].append(join)
		
#形容詞を使ったテンプレートを生成
def makeAdjTemp():
	tokens = analyzer.tokens
	nowTemp = []
	count = 0
	appearance = False
	for token in tokens:
		surface = token[0]
		part = token[1]
		inflection = token[6]
		if part == "形容詞" and inflection == "基本形":
			appearance = True
			count += 1
			surface = "%pat%"
		nowTemp.append(surface)
		join = "".join(nowTemp)
	adj = Learn.adj
	if count != 0 and not join in adj[count]:
		if not count in adj:
			adj[count] = []
		adj[count].append(join)

def makeAdjMizenTemp():
	tokens = analyzer.tokens
	nowTemp = []
	count = 0
	appearance = False
	for token in tokens:
		surface = token[0]
		part = token[1]
		inflection = token[6]
		if part == "形容詞" and inflection == "未然形":
			appearance = True
			count += 1
			surface = "%pat%"
		nowTemp.append(surface)
		join = "".join(nowTemp)
	adjMizen = Learn.adjMizen
	if count != 0 and not join in adjMizen[count]:
		if not count in adjMizen:
			adjMizen[count] = []
		adjMizen[count].append(join)

def makeAdjRennyoTemp():
	tokens = analyzer.tokens
	nowTemp = []
	count = 0
	appearance = False
	for token in tokens:
		surface = token[0]
		part = token[1]
		inflection = token[6]
		if part == "形容詞" and inflection == "連用形":
			appearance = True
			count += 1
			surface = "%pat%"
		nowTemp.append(surface)
		join = "".join(nowTemp)
	adjRennyo = Learn.adjRennyo
	if count != 0 and not join in adjRennyo[count]:
		if not count in adjRennyo:
			adjRennyo[count] = []
		adjRennyo[count].append(join)
		
def makeAdjRentaiTemp():
	tokens = analyzer.tokens
	nowTemp = []
	count = 0
	appearance = False
	for token in tokens:
		surface = token[0]
		part = token[1]
		inflection = token[6]
		if part == "形容詞" and inflection == "連体形":
			appearance = True
			count += 1
			surface = "%pat%"
		nowTemp.append(surface)
		join = "".join(nowTemp)
	adjRentai = Learn.adjRentai
	if count != 0 and not join in adjReitai[count]:
		if not count in adjRentai:
			adjRentai[count] = []
		adjRentai[count].append(join)
		
def makeAdjKateiTemp():
	tokens = analyzer.tokens
	nowTemp = []
	count = 0
	appearance = False
	for token in tokens:
		surface = token[0]
		part = token[1]
		inflection = token[6]
		if part == "形容詞" and inflection == "仮定形":
			appearance = True
			count += 1
			surface = "%pat%"
		nowTemp.append(surface)
		join = "".join(nowTemp)
	adjKatei = Learn.adjKatei
	if count != 0 and not join in adjKatei[count]:
		if not count in adjKatei:
			adjKatei[count] = []
		adjKatei[count].append(join)

#形容動詞を使ったテンプレートを生成
def makeAdjVerbTemp():
	tokens = analyzer.tokens
	nowTemp = []
	count = 0
	appearance = False
	for token in tokens:
		surface = token[0]
		part = token[1]
		typeOfPart = token[2]
		if part == "名詞" and typeOfPart == "形容動詞語幹":
			appearance = True
			count += 1
			surface = "%pat%"
		nowTemp.append(surface)
		join = "".join(nowTemp)
	adjVerb = Learn.adjVerb
	if count != 0 and not join in adjVerb[count]:
		if not count in adjVerb:
			adjVerb[count] = []
		adjVerb[count].append(join)
		
#常識学習
def commonSense():
	#変数定義など
	tokens = analyzer.tokens
	global did
	global notFound
	did = False
	notFound = True
	keyTokens = []
	valueTokens = []
	key = ""
	value = ""
	definition = Learn.definition
	for token in tokens:
		surface = token[0]
		part = token[1]
		typeOfPart = token[2]
		#係助詞ならば
		if typeOfPart == "係助詞":
			did = True
		#まだ係助詞が登場していなければ
		if not did:
			keyTokens.append(token)
		else:
			valueTokens.append(token)
	for token in keyTokens:
		surface = token[0]
		part = token[1]
		typeOfPart = token[2]
		if token[1] == "名詞" and token[2] != "非自立":
			key += token[0]
	for token in valueTokens:
		surface = token[0]
		part = token[1]
		typeOfPart = token[2]
		if part == "名詞" and typeOfPart != "非自立" or part == "動詞" or part == "形容詞" or typeOfPart == "形容動詞語幹":
			value += token[0]
	#常識を追加
	if did == True:
		if not key in definition:
			definition[key] = []
		for v in definition[key]:
			if v == value:
				notFound = False
		if notFound:
			definition[key].append(value)
		#三段論法
		for key, value in definition.items():
			for type1 in value:
				if type1 in definition:
					for type2 in definition[type1]:
							if not type2 in value:
								value.append(type2)

#活用がある単語を入力すると、その単語の活用を返す
def inflections(word):
	#形態素解析
	tokens = analyzer.main(word)
	#抜き出し
	token = tokens[1]
	#見出し
	surface = token[0]
	#品詞
	part = token[1]
	#品詞細分類1
	typeOfPart = token[2]
	#活用型
	utilization = token[5]
	#活用形
	normal = token[7]
	#読み
	read = token[8]
	#活用リスト
	inflectionsList = []
	#語幹を抽出
	#動詞
	if part == "動詞":
		#五段動詞
		if re.search("五段", utilization):
			#五段動詞・カ行
			if re.search("カ行", utilization):
				stem = normal.replace("く", "")
				#五段動詞・カ行イ音便
				if re.search("イ音便", utilization):
					inflectionsList = [[stem + "か", stem + "こ"], [stem + "き", stem + "い"], stem + "く", stem + "く", stem + "け", stem + "け"]
				#五段動詞・カ行促音便
				elif re.search("促音便", utilization):
					inflectionsList = [[stem + "か", stem + "こ"], [stem + "き", stem + "っ"], stem + "く", stem + "く", stem + "け", stem + "け"]
				#五段動詞・カ行ユク
				else:
					inflectionsList = [["ゆか", "ゆこ"], ["ゆき", ""], "ゆく", "ゆく", "ゆけ", "ゆけ"]
			#五段動詞・ガ行
			elif re.search("ガ行", utilization):
				stem = normal.replace("ぐ", "")
				inflectionsList = [[stem + "が", stem + "ご"], [stem + "ぎ", stem + "げ"], stem + "ぐ", stem + "ぐ", stem + "げ", stem + "げ"]
			#五段動詞・サ行
			elif re.search("サ行", utilization):
				stem = normal.replace("す", "")
				inflectionsList = [[stem + "さ", stem + "そ"], [stem + "し", stem + "し"], stem + "す", stem + "す", stem + "せ", stem + "せ"]
			#五段動詞・タ行
			elif re.search("タ行", utilization):
				stem = normal.replace("つ", "")
				inflectionsList = [[stem + "た", stem + "と"], [stem + "ち", stem + "っ"], stem + "つ", stem + "つ", stem + "て", stem + "て"]
			#五段動詞・ナ行
			elif re.search("ナ行", utilization):
				stem = normal.replace("ぬ", "")
				inflectionsList = [[stem + "な", stem + "の"], [stem + "に", stem + "ん"], stem + "ぬ", stem + "ぬ", stem + "ね", stem + "ね"]
			#五段動詞・バ行
			elif re.search("バ行", utilization):
				stem = normal.replace("ぶ", "")
				inflectionsList = [[stem + "ば", stem + "ぼ"], [stem + "び", stem + "ん"], stem + "ぶ", stem + "ぶ", stem + "べ", stem + "べ"]
			#五段動詞・マ行
			elif re.search("マ行", utilization):
				stem = normal.replace("む", "")
				inflectionsList = [[stem + "ま", stem + "も"], [stem + "み", stem + "ん"], stem + "む", stem + "む", stem + "め", stem + "め"]
			#五段動詞・ラ行
			elif re.search("ラ行", utilization):
				stem = normal.replace("る", "")
				#五段動詞・ラ行特殊
				if re.search("特殊", utilization):
					inflectionsList = [[stem + "ら", stem + "ろ"], [stem + "い", stem + "っ"], stem + "る", stem + "る", stem + "れ", stem + "い"]
				#五段動詞・ラ行
				else:
					inflectionsList = [[stem + "ら", stem + "ろ"], [stem + "り", stem + "っ"], stem + "る", stem + "る", stem + "れ", stem + "れ"]
			#五段動詞・ワ行
			elif re.search("ワ行", utilization):
				stem = normal.replace("う", "")
				inflectionsList = [[stem + "わ", stem + "お"], [stem + "い", stem + "っ"], stem + "う", stem + "う", stem + "え", stem + "え"]
		#一段動詞
		elif utilization == "一段":
			#一段動詞・2モーラ
			if len(read) == 2:
				stem = normal[0]
			#一段動詞・3モーラ
			else:
				stem = normal .replace("る", "")
			inflectionsList = [stem, stem, stem + "る", stem + "る", stem + "れ", stem + "ろ"]
		#カ変動詞
		elif re.search("カ変", utilization):
			if normal == "来る":
				inflectionsList = ["来", "来", "来る", "来る", "来れ", "来い"]
			elif normal == "くる":
				inflectionsList = ["こ", "き", "くる", "くる", "くれ", "こい"]
			#カタカナで送信するようなやつは知らん
		#サ変動詞
		elif re.search("サ変", utilization):
			#サ変動詞・スル
			if normal == "する":
				inflectionsList = [["し", "せ", "さ"], "し", "する", "する", "すれ", ["しろ", "せよ"]]
			#サ変動詞・-スル
			elif re.search("スル", read):
				stem = normal.replace("する", "")
				inflectionsList = [[stem + "し", stem + "せ", stem + "せ"], stem + "し", stem + "する", stem + "する", stem + "すれ", stem + "しろ"]
			#サ変動詞・-ズル
			elif re.search("ズル", read):
				stem = normal.replace("ずる", "")
				inflectionsList = [[stem + "じ", stem + "ぜ", stem + "ぜ"], stem + "じ", stem + "ずる", stem + "ずる", stem + "ずれ", stem + "じろ"]
	#形容詞
	elif part == "形容詞":
		stem = normal.replace("い", "")
		inflectionsList = [stem + "かろ", [stem + "く", stem + "かっ"], stem + "い", stem + "けれ", ""]
	return inflectionsList
	
#任意のテンプレートを生成
def makeTemp(fileName, temp):
	fn = fileName + ".pickle"
	with open(fn, "rb") as f:
		openFile = pickle.load(f)
	count = temp.count("%") / 2
	if count != 0 and not temp in openFile:
		if not count in openFile:
			openFile[count] = []
		openFile[count].append(temp)
	with open(fn, "wb") as f:
		pickle.dump(openFile, f)

#nociwの追加関数
def nociwAppender(key, value):
	with open("nociw.pickle", "rb") as f:
		nociw = pickle.load(f)
	nociw[key] = value
	with open("nociw.pickle", "wb") as f:
		pickle.dump(nociw, f)
		
#タイマー関数
def timerStart():
	global start
	start = time.time()

def timerEnd():
	global end
	end = time.time()
	return end - start
	
#終了時に実行
def end():
	with open("noun.pickle", "wb") as f:
		pickle.dump(Learn.noun, f)
	with open("properNoun.pickle", "wb") as f:
		pickle.dump(Learn.properNoun, f)
	with open("numberNoun.pickle", "wb") as f:
		pickle.dump(Learn.numberNoun, f)
	with open("proNoun.pickle", "wb") as f:
		pickle.dump(Learn.proNoun, f)
	with open("verb.pickle", "wb") as f:
		pickle.dump(Learn.verb, f)
	with open("verbMizen.pickle", "wb") as f:
		pickle.dump(Learn.verbMizen, f)
	with open("verbRennyo.pickle", "wb") as f:
		pickle.dump(Learn.verbRennyo, f)
	with open("verbRentai.pickle", "wb") as f:
		pickle.dump(Learn.verbRentai, f)
	with open("verbKatei.pickle", "wb") as f:
		pickle.dump(Learn.verbKatei, f)
	with open("verbMeirei.pickle", "wb") as f:
		pickle.dump(Learn.verbMeirei, f)
	with open("adj.pickle", "wb") as f:
		pickle.dump(Learn.adj, f)
	with open("adjMizen.pickle", "wb") as f:
		pickle.dump(Learn.adjMizen, f)
	with open("adjRennyo.pickle", "wb") as f:
		pickle.dump(Learn.adjRennyo, f)
	with open("adjRentai.pickle", "wb") as f:
		pickle.dump(Learn.adjRentai, f)
	with open("adjKatei.pickle", "wb") as f:
		pickle.dump(Learn.adjKatei, f)
	with open("adjVerb.pickle",  "wb") as f:	
		pickle.dump(Learn.adjVerb, f)
	with open("definition.pickle", "wb") as f:
		pickle.dump(Learn.definition, f)

#全てのテンプレートを削除
def reset():
	with open("noun.pickle", "wb") as f:
		pickle.dump({1 : []}, f)
	with open("properNoun.pickle", "wb") as f:
		pickle.dump({1 : []}, f)
	with open("numberNoun.pickle", "wb") as f:
		pickle.dump({1 : []}, f)
	with open("proNoun.pickle", "wb") as f:
		pickle.dump({1 : []}, f)
	with open("verb.pickle", "wb") as f:
		pickle.dump({1 : []}, f)
	with open("verbMizen.pickle", "wb") as f:
		pickle.dump({1 : []}, f)
	with open("verbRennyo.pickle", "wb") as f:
		pickle.dump({1 : []}, f)
	with open("verbRentai.pickle", "wb") as f:
		pickle.dump({1 : []}, f)
	with open("verbKatei.pickle", "wb") as f:
		pickle.dump({1 : []}, f)
	with open("verbMeirei.pickle", "wb") as f:
		pickle.dump({1 : []}, f)
	with open("adj.pickle", "wb") as f:
		pickle.dump({1 : []}, f)
	with open("adjMizen.pickle", "wb") as f:
		pickle.dump({1 : []}, f)
	with open("adjRennyo.pickle", "wb") as f:
		pickle.dump({1 : []}, f)
	with open("adjRentai.pickle", "wb") as f:
		pickle.dump({1 : []}, f)
	with open("adjKatei.pickle", "wb") as f:
		pickle.dump({1 : []}, f)
	with open("adjVerb.pickle",  "wb") as f:	
		pickle.dump({1 : []}, f)
	with open("definition.pickle", "wb") as f:
		pickle.dump({}, f)
