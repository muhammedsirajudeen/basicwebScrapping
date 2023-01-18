from bs4 import BeautifulSoup
import requests
import pandas as pd
import time

#gets the link from the page



def job_link():
	df_1=pd.DataFrame()
	df_1["title"]=[" "]
	df_1["posted on"]=[" "]
	df_1["close date"]=[" "]
	df_1["description"]=[" "]
	with open("it.html") as fp:
		soup=BeautifulSoup(fp,'html.parser')
	
	data=soup.find_all(class_="jobTitleLink")
	count=0
	for url in data:
		time.sleep(1)
		html_content = requests.get(url["href"]).text
		soup_secondpage = BeautifulSoup(html_content, "lxml")
		job_data=soup_secondpage.find_all("p")
		df_2=pd.DataFrame()
		
		try:
			df_2["title"]= [job_data[0].text]
		except:
			df_2["title"]=[" "]

		try:	
			df_2["posted on"]= [job_data[2].text]
		except:
			df_2["posted on"]=[" "]

		try:	
			df_2["close date"] =[job_data[4].text]
		except:
			df_2["close date"]=[" "]
		try:

			df_2["description"]= job_data[7].text
		except:
			df_2["description"]=[" "]
		
		df_1=pd.concat([df_1, df_2], axis=0)
		print(df_1)
		count=count+1
		if count==450:
			df_1.to_csv('file1.csv')
			break

		
		


		

			



job_link()






