#!/usr/bin/python3
#kanto kor pirka nociw AI system
#response.py:会話の応答の生成
#稼ぐために学んではいけない。学ぶために学べ。-ビル・ゲイツ
#©2019 Mamoru Itoi

#モジュール読み込み
import random
import re
import pickle

#pirka内部のモジュール読み込み
import analyzer
import feelings
import gui
import learn
from data import *

response = ""

#メイン処理
def main():
	make()
	Pirka.mode = "output"
	
#応答生成処理
def make():
	joy = feelings.joy
	trust = feelings.trust
	fear = feelings.fear
	surprise = feelings.surprise
	global response
	response = ""
	#応答候補リスト
	candidate = []
	#マッチした単語リスト
	words = []
	#入力応答用辞書「kanto」を開く
	with open("kanto.pickle", "rb") as f:
		Kanto.kanto = pickle.load(f)
		kanto = Kanto.kanto
	for k, v in Kanto.kanto.items():
		text = gui.text
		#正規表現が入力にマッチするかチェック
		match = re.search(k, text)
		#マッチしたら
		if match:
			for item in v:
				#候補に応答を追加
				candidate.append(item)
				#リストにマッチした単語を追加
				words.append(match.group())
	#もし、何かしらの正規表現が候補リストにあれば
	if candidate != []:
		nowresponse = candidate[0]
		diff = abs(candidate[0][1] - joy) + abs(candidate[0][2] - trust) + abs(candidate[0][3] - fear) + abs(candidate[0][4] - surprise)
		i = -1
		for item in candidate:
			i += 1
			#今の感情と、kantoに指定されている感情値の差を計算。
			nowdiff = abs(item[1] - joy) + abs(item[2] - trust) + abs(item[3] - fear) + abs(item[4] - surprise)
			if nowdiff < diff:
				#今の感情と指定されている感情の差が最も小さい候補を応答にする
				nowresponse = item
				diff = nowdiff
		response = nowresponse[0]
		#%pat%は、マッチした単語に置き換える
		response = response.replace("%pat%", words[i])
	else:
		#テンプレートを使った応答生成処理
		noun = Learn.noun
		properNoun = Learn.properNoun
		numberNoun = Learn.numberNoun
		proNoun = Learn.proNoun
		verb = Learn.verb
		verbMizen = Learn.verbMizen
		verbRennyo = Learn.verbRennyo
		verbRentai = Learn.verbRentai
		verbKatei = Learn.verbKatei
		verbMeirei = Learn.verbMeirei
		adj = Learn.adj
		adjMizen = Learn.adjMizen
		adjRennyo = Learn.adjRennyo
		adjRentai = Learn.adjRentai
		adjKatei = Learn.adjKatei
		adjVerb = Learn.adjVerb
		tokens = analyzer.tokens
		for token in tokens:
			#見出しを取得
			surface = token[0]
			#品詞を取得
			part = token[1]
			#品詞の二次分類を取得
			typeOfPart = token[2]
			#活用を取得
			inflection = token[6]
			#①入力に含まれている品詞を判定
			#②それを使ったテンプレートがあれば
			#③テンプレートへの当てはめを行い
			#④応答にする
			if part == "名詞":
				if inflection == "一般":
					response = random.choice(noun[1]).replace("%pat%", surface)
				elif inflection == "固有名詞":
					response = random.choice(properNoun[1]).replace("%pat%", surface)
				elif inflection == "数":
					response = random.choice(numberNoun[1]).replace("%pat%", surface)
				elif inflection == "代名詞":
					response = random.choice(proNoun[1]).replace("%pat%", surface)
			elif part == "動詞":
				if inflection == "未然形":
					response = random.choice(verbMizen[1]).replace("%pat%", surface)
				elif inflection == "連用形":
					response = random.choice(verbRennyo[1]).replace("%pat%", surface)
				elif inflection == "連体形":
					response = random.choice(verbRentai[1]).replace("%pat%", surface)
				elif inflection == "仮定形":
					response = random.choice(verbKatei[1]).replace("%pat%", surface)
				elif inflection == "命令形":
					response = random.choice(verbMeirei[1]).replace("%pat%", surface)
				else:
					response = random.choice(verb[1]).replace("%pat%", surface)
			elif part == "形容詞":
				if inflection == "未然形":
					response = random.choice(adjMizen[1]).replace("%pat%", surface)
				elif inflection == "連用形":
					response = random.choice(adjRennyo[1]).replace("%pat%", surface)
				elif inflection == "連体形":
					response = random.choice(adjRentai[1]).replace("%pat%", surface)
				elif inflection == "仮定形":
					response = random.choice(adjKatei[1]).replace("%pat%", surface)
				else:
					response = random.choice(adj[1]).replace("%pat%", surface)
			elif part == "名詞" and typeOfPart == "形容動詞語幹":
				response = random.choice(adjVerb[1]).replace("%pat%", surface)
	#もし、常識学習が行われたら
	if learn.did == True:
		if learn.notFound == True:
			response = "へえ〜！知らなかった！"
			feelings.surprise += 0.25
		#もし今までにある常識だったら
		else:
			response = "知ってるよ。"
			feelings.surprise -= 0.25
