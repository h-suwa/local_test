# coding: utf-8
# pom.xmlを抽出し、使用しているライブラリを取得
 
import os
import commands 
import shutil

def main():
	count = 0
	filename = open("./Project_NameList.txt")#プロジェクト名のリストを取得
	for name in filename:#txtファイルを読み、名前を抽出
		name = name[:-1]
		if os.path.exists("C:\Users\電気通信大学\Desktop\git_clone\"+name+"/pom.xml"):
			os.makedirs("C:\Users\電気通信大学\Desktop\pom\"+name)#ディレクトリの作成
			shutil.copy("C:\Users\電気通信大学\Desktop\"+name+"\pom.xml", 
			"/Users/fujino/Desktop/pom/"+name+"/")
			commands.getoutput("cp " +"C:\Users\電気通信大学\Desktop\ICSME\data\"+name+"\pom.xml" + " "+"C:\Users\電気通信大学\Desktop\pom\"+name+"\pom.xml")
			count+=1
			print name
	#print count
main()