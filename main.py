import requests
r=requests.get("http://hydra.kg/stat/first.json")
html=''
for rec in r.json():
    n=rec["Number"]
    if rec['Start']=='': html+="<div class='free'>"+n+"</div>" 
    else: html+="<div class='busy'>"+n+"</div>"

top=""
with open("top.html",'r',encoding = 'utf-8') as f: top=f.read()

bot=""
with open("bot.html",'r',encoding = 'utf-8') as f: bot=f.read()
    
with open("output.html",'w',encoding = 'utf-8') as f:
    f.write(top)
    f.write(html)
    f.write(bot)
