

import os
import getpass
from bs4 import BeautifulSoup

import mechanize
import ssl
import sys


from dotenv import load_dotenv
load_dotenv()

def check_ip():
    username = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')

    br=mechanize.Browser()

    ssl._create_default_https_context = ssl._create_unverified_context
    br.set_handle_robots(False)
    response=br.open("https://netaccess.iitm.ac.in/account/login")


    br.select_form(nr=0)

    br.form["userLogin"]=username
    br.form["userPassword"]=P
    url1=br.geturl()
    result=br.submit()
    url2=br.geturl()
    if (url1==url2):
        print("ERROR: Wrong username or password")
        exit(1)

    br.visit_response(result)
	
    br.follow_link(br.find_link(url_regex="approve"))
    br.select_form(nr=0)
    br.form["duration"] = ["2"]
    result=br.submit()

    soup = BeautifulSoup(br.response().read(), 'html.parser')

    return(soup.find(class_ = "alert-info").find('strong').text)


def netaccess():
    username = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')
    br=mechanize.Browser()

    ssl._create_default_https_context = ssl._create_unverified_context
    br.set_handle_robots(False)
    response=br.open("https://netaccess.iitm.ac.in/account/login")
    br.select_form(nr=0)

    br.form["userLogin"]=username
    br.form["userPassword"]=password
    url1=br.geturl()
    result=br.submit()
    url2=br.geturl()
    if (url1==url2):
        print("ERROR: Wrong username or password")
        exit(1)
    br.visit_response(result)
    br.follow_link(br.find_link(url_regex="approve"))
    br.select_form(nr=0)
    br.form["duration"] = ["2"]
    result=br.submit()
    return("done")
