from selenium import webdriver
import time
import os
import pyautogui
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase



browser=webdriver.Firefox()

def sonuclar_aciklandi_mi():
    browser.get("https://ais.osym.gov.tr/")
    time.sleep(2)
    giris=browser.find_element_by_xpath("/html/body/div[4]/div[1]/div[2]/a[2]")
    giris.click()
    time.sleep(2)
    tcno=browser.find_element_by_name("TcKimlikNo")
    password=browser.find_element_by_name("Sifre")
    tcno.send_keys()
    password.send_keys()
    login_button=browser.find_element_by_xpath("//*[@id='btnSubmitLogin']")
    login_button.click()
    time.sleep(3)
    sonuclarim=browser.find_element_by_xpath("//*[@id='anaMenu']/ul[1]/li[3]/a")
    sonuclarim.click()
    time.sleep(3)
def ss_al():
    pyautogui.screenshot("/Users/user/Desktop/OSYM/resim.png")
    time.sleep(2)
def mail_yolla():
    message=MIMEMultipart()
    message["From"]="mail"
    message["To"]="mail"
    message["Subject"]="ÖSYM SONUÇLARI"

    mesaj="Ösym Screenshot"
    message.attach(MIMEText(mesaj,"plain"))

    filename="resim.png"
    attachmend=open(filename,"rb")
    part=MIMEBase("application","octet-stream")
    part.set_payload((attachmend).read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition","attachmend;filename="+filename)
    message.attach(part)

    text=message.as_string()
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("mail","sifre")
    server.sendmail("mail","mail",text)
    server.quit()
try:
    print("[+]Sunucuya'da Bağlantı Var!")
    sonuclar_aciklandi_mi()
    ss_al()
    mail_yolla()
    time.sleep(1)
    os.system("rm -r /Users/user/Desktop/OSYM/Screenshots/resim.png")
    try:
        browser.close()
    except:
        pass
    os.system("python3 osym.py")
except:
    print("*"*40)
    print("[-]Sunucuya Ulaşılamıyor!\n\n")
    print("[!]Sunucuya Yeniden Bağlanılmaya Çalışılacak...")
    print("*"*40)
    try:
        browser.close()
    except:
        pass
    time.sleep(10)
    os.system("python3 osym.py")
