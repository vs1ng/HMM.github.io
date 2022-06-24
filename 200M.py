import smtplib ,  time , webbrowser , threading , re , sys , os
from turtle import color
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
    cnt = colored("Limited-User Client","blue",attrs=['underline']) 
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
    sender_email=input(colored("[?] Enter Sender email: ",'blue'))
    mailchecker(sender_email)
    sender_password=input(colored("[?] Enter Sender Password: ",'blue'))
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    print(colored("[~] Attempting login..",'red'))
    try:
        s.login(sender_email,sender_password)
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
    subject=input("[~] Enter the subject of the email: ")
    body=input("[~] Enter the body/main message of the email:")
    msg= f'Subject: {subject}\n\n{body}'
    for i in range(0,200):
        whomtosend = input(colored("[?] Enter reiciver email "+ " ({}/200".format(i),'blue'))
        mailchecker(whomtosend)
        s.sendmail(sender_email,whomtosend,msg)
        print(colored('[!] Mail sucessfully sent to {} ({}/200)'.format(whomtosend,i),'green'))
        i += 1
a = threading.Thread(target=main)
a.start()
   

