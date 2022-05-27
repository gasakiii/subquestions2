# 情景画像中の文字領域の可読性についての主観評価実験

English version is here: [README_ENG](/README_ENG.md)

## 目的
現在，画像はスマートフォンやSNSの普及などにより広く通信に用いられています．
一方で，画像は容量が大きいため，通信に利用する場合は圧縮しなければなりません．
画像を圧縮する場合，画像内で重要であると考えられる文字領域を高品質に保つ必要があります．
しかし，文字の可読性に関しては客観評価だけでは不十分であると考えられます．

そこで，画像内の文字領域の品質に関する主観評価をお願いしたいと思います．

お忙しいところではあると思いますが，よろしくお願いします．

画像は全部で30枚、文字領域は93個あります． 10分程度で終わるものとなっているのでよろしくお願いします．

## リポジトリ内容
こちらのリポジトリをコピーすることで、pythonを利用して画像を表示しつつ、スコアをterminal上で入力することができます。

## プログラムの準備
画像表示はローカルでの実行を推奨します。プログラムはpython3で動きます。

まず、以下のコマンドを実行することでこのリポジトリをローカルに入れることができます。

```
$ git clone https://github.com/gasakiii/subquestions2.git
```

次に、コピーしたディレクトリ（subquestions）に移動して、環境構築を行います。

```
$ cd subquestions
```

minicondaの場合、以下のコマンドで新しい環境を構築し、必要なパッケージ（numpy, matplotlib, pillow, opencv)をインストールしてください。

必要なパッケージを持つ環境が既にある場合は、スキップしても大丈夫です。

```
$ conda create --name gasakiii python==3.7
$ conda activate gasakiii
$ pip install -r requirements.txt
```

## 実験方法
準備ができたら、以下のコマンドを実行して評価実験を開始することができます。第一引数に指定されたidを入力する必要があります。

```
$ python main.py {id}
```

実行すると、指定の文字領域が赤枠で囲まれた画像と、terminal上に以下の文字が表示されます。

<p align="center">
  <img width="240" height="320" src="https://github.com/gasakiii/subquestions/blob/main/temp_img/85_1_1.png">
</p>
<!-- ![temp](https://github.com/gasakiii/subquestions/blob/main/temp_img/85_1_1.png "サンプル") -->

```
+--------------------------------------------------
| image  1 / 30, number of text region 1 / 3
+--------------------------------------------------
| 5点 ： 全て問題なく読める
| 4点 ： 概ね読めるが、一部読みづらい文字がある
| 3点 ： 一部読めない文字がある
| 2点 ： 大半が読めない
| 1点 ： 全く読めない
+--------------------------------------------------
Put your score >> 
```

```
image  1 / 30, number of text region 1 / 3
```

imageは現在の画像数を表していて、number of text regionは現在の画像中の文字領域数を表しています。

赤枠で囲まれている文字領域のスコアを、指定された得点にそって決定し、入力してください。

1-5点のスコアを入力し、Enterを押すと次の文字領域あるいは画像に移ります。


## 提出方法

全ての画像について回答すると、ディレクトリ内に、"result_{id}.txt"が生成されます。

これを以下のリンクに送信してください。

https://www.dropbox.com/request/rIWq2KDb8yV8hnrJfW62

提出していただいてアンケートは終了となります！ご協力ありがとうございました！


## オプション：作成した環境を削除する

今回作成した環境を削除したい場合は、以下のコマンドを実行することで削除することができます。


```
$ conda deactivate gasakiii
$ conda remove -n gasakiii --all
```

deactivateできない場合は、一度terminalを再起動してから環境を削除（上記２行目を実行）してください。

よろしくお願いいたします。

