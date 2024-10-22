import csv

from .ed import encrypt_with_key,decrypt_with_key



def initiate():
    "makes new file if dosent exist , call only if necessary , not needed in code"
    file = open("data.csv","a")

def writedata(row:list|tuple):
  try:
    file=open("data.csv","a",newline='')
    w = csv.writer(file)
    w.writerow(row)
    file.close()
    return True
  except Exception as e:
     return e
    
def readdata():
  try:
    file=open("data.csv","r",newline='')
    lines = []
    for i in csv.reader(file):
      lines.append(i)
    return lines
  except Exception as e:
    print(f"some error occured - {e}")


def write(application,user,password):
  iterable = [application,user,encrypt_with_key(password)]
  writedata(iterable)

def returnapps():
  "returns list of apps"
  data = readdata()
  apps = []
  for i in data:
    apps.append(i[0])

  return apps

def returnpass(app):
  "returns info stored"
  data = readdata()
  for i in data:
    if i[0] == app:
      return {"App Name":app,"Login":i[1],"Password":decrypt_with_key(i[2])}
  return {"App Name":app,"Login":"Not Found","Password":"Not Found"}

def deletedata(app):
  "deletes info stored for specific app"
  data = readdata()
  newdata = data.copy()
  line=0
  while line<len(data):
    if data[line][0] == app:
      newdata.pop(line)
      file=open("data.csv","w",newline='')
      obj = csv.writer(file)
      obj.writerows(newdata)
      return 'OK'
    line+=1
  return 'OK'

