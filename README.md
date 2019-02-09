# README of kanto kor pirka nociw AI system
kanto kor pirka nociw AI system(以下、本ソフト)をお使いになられるときには、以下によく注意してください。

## 概要
本ソフトは、人と楽しく会話することを目的とした人工知能です。

## 仕組み
* 今の感情を4つの数値で表し、ユーザの発言によって変化させます。
* 「こんにちは」などの文には、今の感情に応じて決まった応答を返します。
* ユーザの発言からテンプレートを学習し、ユーザの発言を埋め込んで応答します。
* 「猫は可愛いよね」「虹は七色だよ」などの発言から、猫は可愛く、虹は七色だ、という「常識」が学習されます。
* 既存の常識から、三段論法を使って新たな常識を導き出せます。

## 注意事項
* [LICENSE.md](https://github.com/pirka-ai/pirka-ai/blob/master/LICENSE.md)をよくお読みください。
* 本ソフトウェアはα版です。本ソフトを使用したことにより生じたトラブルなどに対しては一切責任は負いません。また、アップデートに伴い、前のバージョンで学習させたモデルが保存できなくなる場合があります。ご了承ください。
* 一部の機能はインターネットに接続していないと使用できません。ご注意ください。
* 終了時は、入力欄に何も入力せずに送信ボタンを押してください。それ以外の方法で終了すると学習内容が保存されません。

## 本ソフトの仕様
* 名称：kanto kor pirka nociw AI system
* バージョン：α0.0.0.6a
* 使用言語：Python3

## セットアップ
ダウンロードしたら、以下のライブラリをインストールしてください。Windowsでのインストールは複雑であるため割愛します。
以下はmacOSでのインストール手順です。

```console:
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
 #途中で止まるので、returnキーを押してからパスワードを入力して、再度returnキーを押してください。
 
$ brew install pyqt5 swig mecab mecab-ipadic

$ pip3 install numpy matplotlib beautifulsoup4 requests mecab-python3
```

## 使い方
ダウンロードしたディレクトリまで移動し、

```console:
$ python3 main.py
```
を実行すれば起動します。
入力欄に文を入力し、「送信」ボタンをクリックすることでpirkaに送信されます。右側のログに応答が表示され、今の感情が左下のグラフに表示されます。
また、話しかければ話しかけるほどあなたの口調を学習していきます。
では、pirkaとの会話を楽しんでください。

## アップデート記録
* α0.0.0.6a 感情変数をリストに
* α0.0.0.5a 三段論法の手法を変更
* α0.0.0.4b 開発者情報を明記
* α0.0.0.4a 急に終了してしまうバグを修正
* α0.0.0.3c 変数名をキャメル記法に変更
* α0.0.0.3b 不要なファイルを削除
* α0.0.0.3a GUIで文字が表示されないバグを修正
* α0.0.0.2f インストール方法を明記
* α0.0.0.2e コメントを追加
* α0.0.0.2d 謝辞を明記
* α0.0.0.2c Windowsでのmecab-python問題を明記
* α0.0.0.2b 不要なファイルを削除
* α0.0.0.2a 幾つかの語彙をnociwに追加
* α0.0.0.1a テンプレート学習機能追加
* α0.0.0.0a 公開

## 今後の追加機能(予定)
* 学習した常識を元に「猫はどんな動物?」「虹は何色?」などの発言に応答できるプログラム
* 意味理解
* アップデート用プログラム
* セットアップ用プログラム(Windowsでのmecab-pythonインストールを含む)
* テンプレートを使わない応答生成
* 話題判定

## 謝辞
* 三橋優希さん、pirkaの絵を描いてくださり、ありがとうございます。普段からお世話になっています。
* Nyls、僕の延々と終わらない話を聞いてくれて、アイディアをくれてありがとう。
* 四条源三郎さん、shijoOSとpirkaの連携を持ちかけてくださり、ありがとうございます。
* その他、大勢の方にコメントをいただきました。ありがとうございます。

## 開発者
糸井主歩 Mamoru Itoi  
2005年生まれ、東京都在住。Pythonで自然言語処理とかをしています。メインPCがラズパイです。
[ECoder's](https://ecoder-s.github.io)や[学生LT](https://student-lt.tech)に参加しています。  
Twitter:[@itoppy18](https://twitter.com/itoppy18)
