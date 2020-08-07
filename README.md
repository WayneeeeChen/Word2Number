# - Description：

	最近案子在做與品牌相關的議題，需要建 Knowledge Graph 去做 edge 的學習，
	但尤於機器學習只吃數值，因此當我們需要從評論中探勘出最符合該品牌的形象字時，
	就必須將各單字做編碼便轉成數字，才能丟入機器學習中。
			
# - 實作 idea：

	1.當資料被 crawl 後，可能是一連串的英文句子，因此我們第一步須根據資料將多餘的字元清除，並統一將所有單字轉換為小寫，才能確保英文單字不會被重複編碼。
	2.在做完初步處理後，我們將每一個單字以 dataframe 的結構存入，以這種方式去存入，可幫助我們在處理資料時更方便，例如：sort_index()、sort_values() 等等。
	3.接著逐行掃檔，若是第一次出現給它新的一個編號；否則找出重複英文單字的編號，並將該 word 改成編號形式。
	
# - 成果：
	＊ 針對這 12 個品牌
	https://github.com/WayneeeeChen/Word2Number/blob/master/Output/brandname.png
	＊ 共編了13706個號碼
	![image](https://github.com/WayneeeeChen/Word2Number/blob/master/Output/1.png)
	＊ 將原檔所有英文字母轉成數字
	![image](https://github.com/WayneeeeChen/Word2Number/blob/master/Output/3.png)
	![image](https://github.com/WayneeeeChen/Word2Number/blob/master/Output/3.png)
