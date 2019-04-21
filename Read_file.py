# 留言分析程式

data = []
k = 0
words = []
with open('reviews.txt', 'r') as f :
	for line in f :
		data.append(line)
		k += 1
		if k % 100000 == 0: #餘數為0的意思
			print(len(data))
print('資料搜索完畢，共有', len(data), '筆資料！')

# 自己寫的。很慢！！！
for letters in data:
	for word in letters:
		words.append(word)

Mean_words = len(words) / len(data)
print('留言平均長度為：', Mean_words, '字')

# 答案簡單版。很快！！！  
sum_len = 0
for letters in data:
	sum_len = sum_len + len(letters)
print('留言平均長度為：',sum_len / len(data) , '字')