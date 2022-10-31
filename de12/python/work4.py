name=input("名前は？")
waist=float(input("腹囲は？"))
age=int(input("年はいくつ？"))
height=float(input("身長は？"))
# 数字の場合はint、小数点の場合はfloatな。忘れんなよ
# input入れると入力できるようになるぞ
print(name, "さんは腹囲", waist, "cmで年齢は",age, "才ですね。")
# ここにコメントを書きます。
# コロン忘れんなよ
# 頑張れよ
if waist>=85:
    print(name,"さん、内臓脂肪蓄積注意です")
else:
    print(name,"さん、腹囲は問題ありません")

if age>=40:
     print(name,"さん男性ホルモンの分泌減少注意です"  )
    
else:
    print(name,"さん大丈夫です。" )


if height>=170.8:
        print(name ,"平均身長以上です")

else:
      print(name, "平均身長以下です")

