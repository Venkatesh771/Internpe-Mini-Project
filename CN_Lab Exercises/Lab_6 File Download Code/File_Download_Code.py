#6.Web HTTP File Download Python Code:
import requests
url = "https://images.pexels.com/photos/1108099/pexels-photo-1108099.jpeg?auto=compress&cs=tinysrgb&w=600"
filename = "pic.jpeg"
response = requests.get(url)
with open(filename, "wb") as f:
f.write(response.content)
print("File downloaded successfully!\nYou Can Check The Folder With File Name As ",filename)
