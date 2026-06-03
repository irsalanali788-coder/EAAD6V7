#!/usr/bin/env python3
"""
DECODED from TOKEN.py / script.py
Tool Name: TOKEN GRENADE V7 - POWERED BY L3G3ND-X PRODUCTION
Owner: L3G3ND-X (+923243037456)
Email: Legendxproduction@gmail.com
Price: 200₹ / Monthly

Original obfuscated by PyObfuscate
GitHub: https://github.com/irsalanali788-coder/EAAD6V7.git
"""

import random
import time
import requests
import uuid
import base64
import io
import struct
import sys
import os
import warnings
import string
from Crypto.Cipher import AES
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from urllib.parse import quote

warnings.filterwarnings("ignore", category=DeprecationWarning)

try:
    from colorama import Fore, Style, init
    init()
except ImportError:
    os.system("python3 -m pip install colorama")
    from colorama import Fore, Style, init
    init()

# --- Approval System ---
APPROVAL_URL = "https://raw.githubusercontent.com/irsalanali788-coder/Approval-/main/approval.txt"
KEY_PATH = os.path.join(os.path.expanduser("~"), ".irsalan_key.txt")

def get_henry_key():
    """Hamesha wahi key return karega jo pehli baar bani thi"""
    if os.path.exists(KEY_PATH):
        with open(KEY_PATH, "r") as f:
            return f.read().strip()
    key = "Legend-X" + "".join(random.choices(string.digits, k=8))
    with open(KEY_PATH, "w") as f:
        f.write(key)
    return key

def bypass_check(user_key):
    """Check approval from GitHub"""
    os.system("clear")
    print(f"{Fore.WHITE}╔════════════════════════════════════════════════╗")
    print(f"║ {Fore.YELLOW}YOUR KEY : {Fore.GREEN}{user_key}{Fore.WHITE}║")
    print(f"╚════════════════════════════════════════════════╝")
    print(f"{Fore.CYAN}Hello Muddassir! Please Approve My Key: ")
    os.system(f'am start https://wa.me/+923243037456?text={quote(user_key)} >/dev/null 2>&1')
    print(f"📲 Checking Live Approval (No-Cache Mode)...")
    while True:
        try:
            r = requests.get(f"{APPROVAL_URL}?t={int(time.time())}")
            if r.status_code == 200:
                if user_key in r.text:
                    print("✅ KEY APPROVED! STARTING TOOL...")
                    return True
            print("⏳ Status: Pending Approval... Retrying in 5s ")
            time.sleep(5)
        except Exception as e:
            print(f"⚠️ Connection Slow... Retrying.")
            time.sleep(5)


# --- Flashy Colors ---
flashy_colors = [
    Fore.LIGHTRED_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTYELLOW_EX,
    Fore.LIGHTBLUE_EX, Fore.LIGHTMAGENTA_EX, Fore.LIGHTCYAN_EX
]

def get_random_color_line(text):
    return random.choice(flashy_colors) + text + Style.RESET_ALL

def animated_print(text, delay=0.03):
    for line in text.splitlines():
        sys.stdout.write(get_random_color_line(line) + "\n")
        sys.stdout.flush()
        time.sleep(delay)

def token_logo():
    # ASCII art logo
    pass

def henry_x_logo():
    # ASCII art logo  
    pass

def loading_animation(text="PENETRATING FACEBOOK SERVERS..."):
    for char in text:
        sys.stdout.write(f"{Fore.CYAN}{Style.BRIGHT}{char}{Style.RESET_ALL}")
        sys.stdout.flush()
        time.sleep(0.05)


# --- Facebook Password Encryptor ---
class FacebookPasswordEncryptor:
    @staticmethod
    def get_public_key():
        try:
            r = requests.get("https://b-graph.facebook.com/pwd_key_fetch", params={
                "version": "2",
                "access_token": "438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28"
            })
            data = r.json()
            return data["public_key"], data["key_id"]
        except Exception as e:
            print(f"Public key fetch error: {str(e)}")
            return None, None

    @staticmethod
    def encrypt(password):
        try:
            pub_key_str, key_id = FacebookPasswordEncryptor.get_public_key()
            if not pub_key_str:
                return None
            
            random_bytes = get_random_bytes(25)
            rsa_key = RSA.import_key(pub_key_str)
            cipher_rsa = PKCS1_v1_5.new(rsa_key)
            encrypted_random = cipher_rsa.encrypt(random_bytes)
            
            cipher_aes = AES.new(random_bytes[:16], AES.MODE_GCM)
            timestamp = str(int(time.time()))
            cipher_aes.update(timestamp.encode("utf-8"))
            encrypted_pw, tag = cipher_aes.encrypt_and_digest(password.encode("utf-8"))
            
            buf = io.BytesIO()
            buf.write(bytes([1]))  # version
            buf.write(struct.pack(">B", int(key_id)))
            buf.write(struct.pack(">H", len(encrypted_random)))
            buf.write(encrypted_random)
            buf.write(tag)
            buf.write(encrypted_pw)
            
            encoded = base64.b64encode(buf.getvalue()).decode("utf-8")
            return f"#PWD_FB4A:2:{timestamp}:{encoded}"
        except Exception as e:
            print(f"Encryption error: {str(e)}")
            return None


# --- Facebook App Tokens ---
class FacebookAppTokens:
    APPS = {
        "Facebook For Android": "350685531728",
        "Facebook Messenger For Android": "256002347743983",
        "Facebook For Lite": "275254692598279",
        "Facebook Messenger For Lite": "200424423651082",
        "Ads Manager App For Android": "438142079694454",
    }

    @staticmethod
    def extract_token_prefix(token):
        # Extract EAAD6V7... prefix from token
        for i, c in enumerate(token):
            if c.islower():
                return token[:i]
        return token


# --- Facebook Login ---
class FacebookLogin:
    API_URL = "https://b-graph.facebook.com/auth/login"
    ACCESS_TOKEN = "350685531728|62f8ce9f74b12f84c123cc23437a4a32"
    SIG = "214049b9f17c38bd767de53752b53946"

    def __init__(self, uid_phone_mail, password):
        if uid_phone_mail.startswith("#PWD_FB4A"):
            self.password = uid_phone_mail  # already encrypted
        else:
            self.password = FacebookPasswordEncryptor.encrypt(password)
        self.uid_phone_mail = uid_phone_mail
        self.session = requests.Session()
        self.device_id = str(uuid.uuid4())
        self.session.headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 14; Pixel 8 Build/UQ1A.231205.015) [FBAN/FB4A;FBAV/440.0.0.33.116;]"
        }

    def login(self):
        animated_print("[*] BYPASSING SECURITY NODES...")
        loading_animation()
        
        data = {
            "uid_phone_mail": self.uid_phone_mail,
            "password": self.password,
            "device_id": self.device_id,
            "access_token": self.ACCESS_TOKEN,
            "sig": self.SIG,
            "format": "json",
            "generate_session_cookies": "1",
        }
        
        r = self.session.post(self.API_URL, data=data, headers=self.session.headers)
        response = r.json()
        
        if "access_token" in response:
            return self._parse_success_response(response)
        elif "error" in response:
            return {"error": response.get("error", {}).get("message", "Login Failed")}
        return {"error": "Login Failed"}

    def _parse_success_response(self, response):
        result = {
            "success": True,
            "access_token": response.get("access_token"),
            "cookies": "; ".join([f"{c['name']}={c['value']}" for c in response.get("session_cookies", [])]),
            "original_token": response.get("access_token"),
            "token_prefix": FacebookAppTokens.extract_token_prefix(response.get("access_token", "")),
        }
        
        # Convert token to all app tokens
        converted_tokens = {}
        for app_name, app_id in FacebookAppTokens.APPS.items():
            try:
                r = requests.post("https://api.facebook.com/method/auth.getSessionforApp", data={
                    "format": "json",
                    "access_token": response.get("access_token"),
                    "new_app_id": app_id,
                    "generate_session_cookies": "1",
                })
                token_data = r.json()
                if "access_token" in token_data:
                    converted_tokens[app_name] = token_data["access_token"]
            except:
                pass
        
        result["converted_tokens"] = converted_tokens
        return result


# --- Main ---
if __name__ == "__main__":
    os.system("clear")
    
    # Approval check
    user_key = get_Legend_key()
    bypass_check(user_key)
    
    os.system("clear")
    
    # UI
    border_color = Fore.MAGENTA
    print(f"{border_color}╔════════════════════════════════════════════════════════════╗")
    print(f"║ {Fore.WHITE}SYSTEM STATUS: {Fore.GREEN}PREMIUM TOOL (ACTIVE)           {border_color}    ║")
    print(f"║ {Fore.WHITE}PRICE: {Fore.YELLOW}200₹ / MONTHLY                          {border_color}║")
    print(f"║ {Fore.WHITE}OWNER: {Fore.CYAN}Legend-X                                 {border_color}║")
    print(f"║ {Fore.WHITE}WHATSAPP: {Fore.GREEN}+919235741670                        {border_color}║")
    print(f"║ {Fore.WHITE}EMAIL: {Fore.CYAN} muddassirhussain75@gmail.com             {border_color}║")
    print(f"{border_color}╚════════════════════════════════════════════════════════════╝{Style.RESET_ALL}")
    print("<<==============================================================>>")
    print("          TOKEN GRENADE V7 - POWERED BY H
Legend-X PRODUCTION")
    
    u = input(f"{Fore.YELLOW}ENTER GMAIL/PHONE NUMBER ➠ {Style.RESET_ALL}").strip()
    p = input(f"{Fore.YELLOW}ENTER PASSWORD ➠ {Style.RESET_ALL}").strip()
    
    fb = FacebookLogin(u, p)
    result = fb.login()
    
    if "success" in result:
        print(f"\n {Fore.GREEN}[✅] TOKEN GENERATED SUCCESSFULLY!")
        print(f"{Fore.WHITE}TYPE: {Fore.CYAN}original_token")
        print(f"{Fore.WHITE}TOKEN PREFIX: {Fore.GREEN}{result.get('token_prefix', '')}")
        print(f"{Fore.WHITE}ACCESS TOKEN: {Fore.YELLOW}{result.get('access_token', '')}")
        
        if result.get("converted_tokens"):
            print(f"\n{Fore.WHITE}CONVERTED TOKENS:")
            for app, data in result["converted_tokens"].items():
                print(f"  {Fore.CYAN}APP: {Fore.WHITE}{app}")
                print(f"  {Fore.GREEN}TOKEN: {data}")
        
        if result.get("cookies"):
            print(f"\n {Fore.YELLOW}[🍪] SESSION COOKIES ")
            print(f"  {result['cookies']}")
    else:
        print(f"\n {Fore.RED}[!] LOGIN FAILED: {result.get('error', '')}")
    
    print(f"\n{Fore.MAGENTA}OFFICIAL LEGEND-X PRODUCTION TOOL{Style.RESET_ALL}")
    
