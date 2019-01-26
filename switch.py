#!/usr/bin/python3
#kanto kor pirka nociw AI system
#switch.py:appsかresponseか決める
#©2019 Mamoru Itoi

#モジュール読み込み
import re

#pirka内部のモジュール読み込み
import apps
import gui

#メイン処理
def main():
	triggers = apps.triggers
	text = gui.text
	for trigger, function in triggers.items():
		match = re.search(trigger, text)
		if match:
			return function
	return False
