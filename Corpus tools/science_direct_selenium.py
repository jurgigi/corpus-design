
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def get_content_sd():
	sections = ["sec0005", "sec0010", "sec0015", "sec0020", "sec0025", "sec0030", "sec0035", "sec0040", "sec0045",
				"sec0050", "sec0055", "sec0060", "sec0065", "sec0070", "sec0075", "sec0080", "sec0085", "sec0090", "sec0095"]

	options = webdriver.ChromeOptions()
	options.add_argument(r" ") #e.g. C:\Users\You\AppData\Local\Google\Chrome\User Data
#	options.add_argument(r' ') 
	driver = webdriver.Chrome(chrome_options=options)
	driver.get("https://doi.org/10.1016/j.gyobfe.2011.04.009")
	
	time.sleep( )#change value if needed
	
	science_direct_dois = [" "]# insert DOI link
	
	for doi in science_direct_dois:
		print(f"---------------------------------------------------\nNavigating to: {doi}")
		driver.get(doi)
		time.sleep(3)
		output = ""
#		output = driver.find_element(By.ID, " ").text #change element
		
		for sec in sections:
			try:
				txt = driver.find_element(By.ID, sec).text
				output += "\n"+txt
			except:
				print("----")
		print(output)
	
	
get_content_sd()	
