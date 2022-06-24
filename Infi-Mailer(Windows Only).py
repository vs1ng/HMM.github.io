import smtplib ,  time , webbrowser , threading , multiprocessing , re , sys , colorama , os
from validate_email_address import validate_email
from requests import ConnectTimeout
from termcolor import colored
def time_before_end():
    print(colored("[!] An error was raised , Please retry.",'red'))
    time.sleep(1)
    print()
    print(colored("[!] Exiting in 7 seconds.",'red'))
    time.sleep(13)
    sys.exit()
def mailchecker(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    print(colored("[~] Running Helios Mail Checker..",'red'))
    time.sleep(2)
    isvalid = validate_email(email)
    if isvalid == True and re.fullmatch(regex, email) == True:
        print(colored("[~] Email is valid , Proceed.",'green'))
    elif isvalid == True:
        print(colored("[~] Email is valid , Proceed.",'green'))
    else:
        print(colored("[!] WARNING : Email does not exist or has invalid charectors ; Please check and re-try. ",'red'))
def main(): 
    os.system('color')
    colorama.init()
    print()
    print(colored("""Welcome to,
                                                        /$$   /$$           /$$ /$$                          
                                                        | $$  | $$          | $$|__/                          
                                                        | $$  | $$  /$$$$$$ | $$ /$$  /$$$$$$   /$$$$$$$      
                                                        | $$$$$$$$ /$$__  $$| $$| $$ /$$__  $$ /$$_____/      
                                                        | $$__  $$| $$$$$$$$| $$| $$| $$  \ $$|  $$$$$$       
                                                        | $$  | $$| $$_____/| $$| $$| $$  | $$ \____  $$      
                                                        | $$  | $$|  $$$$$$$| $$| $$|  $$$$$$/ /$$$$$$$/      
                                                        |__/  |__/ \_______/|__/|__/ \______/ |_______/       
                                                                /$$      /$$                                   
                                                                | $$$    /$$$                                   
                                                                | $$$$  /$$$$  /$$$$$$   /$$$$$$$ /$$$$$$$      
                                                                | $$ $$/$$ $$ |____  $$ /$$_____//$$_____/      
                                                                | $$  $$$| $$  /$$$$$$$|  $$$$$$|  $$$$$$       
                                                                | $$\  $ | $$ /$$__  $$ \____  $$\____  $$      
                                                                | $$ \/  | $$|  $$$$$$$ /$$$$$$$//$$$$$$$/      
                                                                |__/     |__/ \_______/|_______/|_______/       
                                                    /$$      /$$           /$$ /$$ /$$                         
                                                    | $$$    /$$$          |__/| $$|__/                         
                                                    | $$$$  /$$$$  /$$$$$$  /$$| $$ /$$ /$$$$$$$   /$$$$$$      
                                                    | $$ $$/$$ $$ |____  $$| $$| $$| $$| $$__  $$ /$$__  $$     
                                                    | $$  $$$| $$  /$$$$$$$| $$| $$| $$| $$  \ $$| $$  \ $$     
                                                    | $$\  $ | $$ /$$__  $$| $$| $$| $$| $$  | $$| $$  | $$     
                                                    | $$ \/  | $$|  $$$$$$$| $$| $$| $$| $$  | $$|  $$$$$$$     
                                                    |__/     |__/ \_______/|__/|__/|__/|__/  |__/ \____  $$     
                                                                                                /$$  \ $$     
                                                                                                |  $$$$$$/     
                                                                                                \______/  ""","red"))
    cnt = colored("Infinite-User Client","blue",attrs=['underline']) 
    bywho = colored("brought to you by ",'red') + colored("Vinayak Singh ",'magenta')
    print("                                                                  "+bywho) 
    print("                                                                      "+cnt) 
    print()                                                                                          
    lol = ""
    while len(lol) == 0:
        lol=input(colored("Have you read the instructions before use (-.-) ? y/n ",'cyan'))
        if lol == "y":
            continue
        elif lol == "no":
            webbrowser.open_new("https://vs1ng.github.io/instuctions.html")
            print("I hope you have read the instructions now!")
            time.sleep(5)
            continue
        else:
            pass
    else:
        pass
    sender_email = ""
    sender_pass = ""
    subject = ""
    body=""
    inputforfishok = ""
    while len(sender_email) == 0 and len(sender_pass) == 0 and len(subject) == 0 and len(body) == 0 and len(inputforfishok) == 0:
        sender_email=input(colored("[+] Enter sender's email: ",'blue'))
        mailchecker(sender_email)
        sender_pass=input(colored("[+] Enter sender's password: ",'blue'))
        subject=input(colored("[+] Enter Subject for the email: ",'blue'))
        body=input(colored("[+] Enter the message you want to send: ",'blue'))
        inputforfishok=input(colored("[+] Enter how many people would you like to mail: ",'blue'))
    msg= f'Subject: {subject}\n\n{body}'
    inputforfishok = int(inputforfishok)
    for x in range(inputforfishok):
        rec_mail=input(colored("[+] Enter the reciver's email: ",'blue'))
        mailchecker(rec_mail)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    try:
        s.login(sender_email,sender_pass)
    except smtplib.SMTPSenderRefused as r:
        print(colored("[!] Either an authentication error occured , or the sender credidentials were invalid."))
        time_before_end()
    except ConnectionResetError as q:
        print(colored("[!] Your connection was reset , Please Try again.",'red'))
        time_before_end()
    except ConnectTimeout as w:
        print(colored("[!] Your connection timed out , Please try again.",'red'))
        time_before_end()
    except smtplib.SMTPAuthenticationError as e:
        print(colored("[!] An authentication error occured , Please retry and check your account.",'red'))
        time_before_end()
    except smtplib.SMTPServerDisconnected as r:
        print(colored("[!] The server disconnected , Please retry.",'red'))
        time_before_end()
    finally:
        pass
    try:
        s.sendmail(sender_email,rec_mail,msg)
    except ConnectionResetError as q:
        print(colored("[!] Your connection was reset , Please Try again.",'red'))
        time_before_end()
    except ConnectTimeout as w:
        print(colored("[!] Your connection timed out , Please try again.",'red'))
        time_before_end()
    finally:
        pass
    s.quit()
    print("Sent mail!")
a = threading.Thread(target=main)
a.start()
