from textblob import TextBlob

myList = ["Incorret","spellin"]
corrected_list=[]

for word in myList:
	corrected_list.append(TextBlob(word))

print("corrected list words are:")

for word in corrected_list:
	print(word.correct(), end=" ")
		