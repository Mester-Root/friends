# !/usr/bin/python
# the me
while True:
    #-----------------------
    try:
        import datetime
    except:
        os.system('pip install datetime')
    try:
        import hashlib
    except:
        os.system('pip install hashlib')
    try:
        import base64
    except:
        os.system("pip install base64")
    #----------------------
    color = '\033[1;30m'
    color1 = '\033[2m'
    green = "\033[32m"
    red = "\033[31m"
    blue = "\033[36m"
    pink = "\033[35m"
    yellow = "\033[93m"
    darkblue = "\033[34m"
    white = "\033[00m"
    mark = '\x1b[38;5;4m'
    mark1 = '\x1b[48;5;15m'
    mark2 = '\x1b[0m'
    import uuid,datetime,random,hashlib,base64
    uid = (uuid.uuid1())
    uid2 = (uuid.uuid1())
    uid3 = (uuid.uuid1())
    timer = (datetime.datetime.now())
    timer1 = (datetime.datetime.today())
    import os,sys,time
    
    try:
    	os.system("clear")
    except:
    	os.system("cls")
    #-----
    color='\033[93m'
    time.sleep(1)
    banner = (f"""\n{darkblue}{mark1}< {timer} > {mark2}
	{yellow}
	
	  +hydNNNNdyh+
        +mMMMMMMMMMMMMm+
      `dMMm\033[0m:\033[92mNMMMMMMN\033[0m:\033[92mmMMd`
      hMMMMMMMMMMMMMMMMMMh
  \033[92m..  yyyyyyyyyyyyyyyyyyyy  ..                     
\033[92m.mMMm`MMMMMMMMMMMMMMMMMMMM`mMMm.
\033[92m:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
-MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM-
 +yy+ MMMMMMMMMMMMMMMMMMMM +yy+
      mMMMMMMMMMMMMMMMMMMm
      `/++MMMMh++hMMMM++/`
          MMMMo  oMMMM
          MMMMo  oMMMM
          oNMm-  -mMNs
          
          [rubika.ir/TheServer] > [saleh=mr root]
          [rubika.ir/PowerFis] > [Black Kabos]
--------------------------------------------------------          
          {pink}[python panel.py account @username]{red}
                   (or)
          {darkblue}[python panel.py group @username]
                   {red}(or)
         {green} [python panel.py channel @username]
---------------------------------------------------------""")
    for bnr in banner:
        sys.stdout.write(bnr)
        sys.stdout.flush()
        time.sleep(0.01)
    #--------
    time.sleep(1)
    try:
    	account = sys.argv[1]
    	channel = sys.argv[1]
    	group = sys.argv[1]
    	username = sys.argv[2]
    except:
    	time.sleep(1)
    	print(f"{red}\nerror please enter python panel.py [method] [@username]")
    	time.sleep(1)
    	sys.exit()
    	
    if account == "account".lower():
        print()
        os.system("clear")
        time.sleep(1)
        print()
        logo = (F"""{blue}
        
             ,____
                      |---.\\
              ___     |    `
             / .-\  ./=)
            |  |"|_/\/|
            ;  |-;| /_| 
           / \_| |/ \ |
          /      \/\( |
          |   /  |` ) |
          /   \ _/    |
         /--._/  \    |
         `/|)    |    /
           /     |   |
         .'      |   |
        /         \  |
       (_.-.__.__./  /
       
       {darkblue}[ACCOUNT CODE]
       [POWER REPORT]
       \n
       """)
        
        for bnr in logo:
            sys.stdout.write(bnr)
            sys.stdout.flush()
            time.sleep(0.01)
        print()
        time.sleep(1)
        ip = ["192.168.45:443","127.0.0.1:5000","189.233.14:800","198.761.24:8080","248.216.56:443","4075:80","6.2.1.3:80","311.451.67:9050","135.9.2.1:5000"]
        code = random.choice(ip)
        report = (f"('/[{code}]:{uid},{timer},{uid}/')")
        time.sleep(1)
        print(F'\n{blue}code [account] for {yellow}<{username}> :\n {white} ___________________\n\n{red}'+report+F'\n\n{white} ___________________')
        print()
        time.sleep(6)
        sys.exit()
        
    
    elif channel == 'channel'.lower():
        time.sleep(1)
        print()
        try:
            os.system("clear")
        except:
            os.system("cls")
        time.sleep(1)
        echo = '''\033[2m
        
^__^
(oo)/_______
(__)/       )>>>>\033[56;60m
    ||—————||
    ||     ||
    
   \033[87;91m [channel code]'''
        for pt in echo:
            sys.stdout.write(pt)
            sys.stdout.flush()
            time.sleep(0.01)
        print('\n\n\n\n\n\n\n\n\n')
        time.sleep(1)
        try:
            import base64
        except:
            os.system("pip install base64")
        import base64
        cod = ["reportUser","filterAccount","filteringUserAgent","FilteredUsername","reported0101","thereport","filtererguid","reporter","reporting","user report","report user","Accountreoort","ReportUserAgent","ReportUsername","FilterAccount","FilterUser","FilterUsername","This user reports's","report-user"]
        cod1 = (random.choice(cod))
        maincode = (base64.b64encode(cod1.encode('utf-8')))
        
        print(f'{blue}code for channel  {yellow}[{username}]:\n\n\033[0;60m________________\n\n{red}')
        time.sleep(0.5)
        print(maincode)
        print('\n\n\033[0;37m_______________')
        time.sleep(5)
        sys.exit()
    elif group == 'group'.lower():
        time.sleep(1)
        try:
            os.system("clear")
        except:
            os.system("cls")
        print()
        poster = (F'''{blue}
        _
 _ __ ___ _ __   ___  _ __| |_ ___ _ __
| '__/ _ \ '_ \ / _ \| '__| __/ _ \ '__|
| | |  __/ |_) | (_) | |  | ||  __/ |
|_|  \___| .__/ \___/|_|   \__\___|_|   
         |_|
         
        {red} [GROUP CODE]
         ''')
        for eo in poster:
            sys.stdout.write(eo)
            sys.stdout.flush()
            time.sleep(0.01)
        time.sleep(1)
        try:
            import hashlib
        except:
            os.system("pip install hashlib")
        print()
        time.sleep(1)
        mycode = ["code--report-user","reportaccount","reporter-username","/r/xeb/x09/eporting","filter_u0","filtering_username","filtered01","filtereracoount","blockaccpunt","filteredusername","filters0101","reports"]
        mecode = str(random.choice(mycode))
        hashcode = str(hashlib.md5(mecode.encode()))
        print('\n'+F'{blue}code group for <{username}> :\n\n{white}_______________\n\n')
        print(hashcode)
        print(f'\n\n{white}_______________')
        print()
        time.sleep(5)
        sys.exit()