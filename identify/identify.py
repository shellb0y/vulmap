#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import time
from module.color import color
from module.time import now
from module import globals
from module.md5 import random_md5
from requests.packages import urllib3
urllib3.disable_warnings()


class Identify:
    def __init__(self, url):
        self.url = url
        self.raw_data = None
        self.vul_info = {}
        self.ua = globals.get_value("UA")  # 获取全局变量UA
        self.timeout = globals.get_value("TIMEOUT")  # 获取全局变量UA
        self.delay = globals.get_value("DELAY")
        self.headers = globals.get_value("HEADERS")  # 获取全局变量HEADERS
        self.ceye_domain = globals.get_value("ceye_domain")
        self.ceye_token = globals.get_value("ceye_token")
        self.ceye_api = globals.get_value("ceye_api")

    @staticmethod
    def start(url, webapps_identify):
        ua = globals.get_value("UA")  # 获取全局变量UA
        timeout = globals.get_value("TIMEOUT")  # 获取全局变量UA
        headers = {'User-Agent': ua}
        try:
            resp = requests.get(url, headers=headers, timeout=timeout, verify=False)
        except:
            resp = "null"
        start = Identify(url)
        start.flink(webapps_identify, resp, url)
        start.tomcat(webapps_identify, resp, url)
        start.fastjson(webapps_identify)
        start.elasticsearch(webapps_identify, resp, url)
        start.jenkins(webapps_identify, resp, url)
        start.weblogic(webapps_identify, resp, url)
        start.spring(webapps_identify, resp, url)
        start.solr(webapps_identify, resp, url)
        start.nexus(webapps_identify, resp, url)
        start.jboss(webapps_identify, resp, url)
        start.drupal(webapps_identify, resp, url)
        start.struts2(webapps_identify, resp, url)
        start.shiro(webapps_identify, resp, url)
        if webapps_identify:
            for a in webapps_identify:
                print("\r{0}{1}".format(now.timed(de=0) + color.yel_info(), color.yellow(" The identification target is: " + a + "          ")))
        else:
            webapps_identify.append("all")
            print("\r{0}{1}".format(now.timed(de=0) + color.yel_info(), color.yellow(" Unable to identify target, Run all pocs           ")))


    def flink(self, webapps_identify, resp, url):
        name = "Flink"
        time.sleep(0.2)
        Identify.identify_prt(name)
        try:
            if r"<flink-root></flink-root>" in resp.text:
                webapps_identify.append("flink")
        except:
            pass

    def shiro(self, webapps_identify, resp, url):
        name = "Shiro"
        time.sleep(0.2)
        Identify.identify_prt(name)
        headers = {'User-Agent': self.ua, 'Content-Type': "application/json"}
        cookies = {"rememberMe": "dGVzdAo="}
        try:
            resp = requests.get(url, headers=headers, cookies=cookies, timeout=5, verify=False)
            if r"deleteMe" in resp.headers['Set-Cookie']:
                webapps_identify.append("shiro")
        except:
            pass
    
    def struts2(self, webapps_identify, resp, url):
        name = "Struts2"
        time.sleep(0.2)
        Identify.identify_prt(name)
        try:
            if r".do" in url:
                webapps_identify.append("struts2")
            elif r".action" in url:
                webapps_identify.append("struts2")
        except:
            pass

    def drupal(self, webapps_identify, resp, url):
        name = "Drupal"
        time.sleep(0.2)
        Identify.identify_prt(name)
        try:
            if r"Drupal" in resp.headers['X-Generator']:
                webapps_identify.append("drupal")
            elif r"Powered by" in resp.text and r"Drupal" in resp.text:
                webapps_identify.append("drupal")
        except:
            pass

    def nexus(self, webapps_identify, resp, url):
        name = "Nexus"
        time.sleep(0.2)
        Identify.identify_prt(name)
        try:
            if r"Nexus Repository Manager" in resp.text:
                webapps_identify.append("nexus")
            elif r"Nexus" in resp.headers['Server']:
                webapps_identify.append("nexus")
        except:
            pass

    def jboss(self, webapps_identify, resp, url):
        name = "JBoss"
        time.sleep(0.2)
        Identify.identify_prt(name)
        try:
            if r"JBoss Wiki" in resp.text:
                webapps_identify.append("jboss")
            elif resp.headers['X-Powered-By']:
                if r"JBoss" in resp.headers['X-Powered-By']:
                    webapps_identify.append("jboss")
        except:
            pass

    def tomcat(self, webapps_identify, resp, url):
        name = "Tomcat"
        time.sleep(0.2)
        Identify.identify_prt(name)
        try:
            if r"Apache Tomcat" in resp.text:
                webapps_identify.append("tomcat")
        except:
            pass

    def elasticsearch(self, webapps_identify, resp, url):
        name = "Elasticsearch"
        time.sleep(0.2)
        Identify.identify_prt(name)
        try:
            if r"You Know, for Search" in resp.text and r"lucene_version" in resp.text and r"tagline" in resp.text:
                webapps_identify.append("elasticsearch")
        except:
            pass

    def jenkins(self, webapps_identify, resp, url):
        name = "Jenkins"
        time.sleep(0.2)
        Identify.identify_prt(name)
        try:
            if r"X-Jenkins" in resp.headers:
                webapps_identify.append("jenkins")
        except:
            pass

    def weblogic(self, webapps_identify, resp, url):
        name = "Weblogic"
        time.sleep(0.2)
        Identify.identify_prt(name)
        try:
            if r"From RFC 2068" in resp.text and r"Hypertext Transfer Protocol" in resp.text:
                webapps_identify.append("weblogic")
        except:
            pass

    def solr(self, webapps_identify, resp, url):
        name = "Solr"
        time.sleep(0.2)
        Identify.identify_prt(name)
        try:
            if r"Solr Admin" in resp.text:
                webapps_identify.append("solr")
        except:
            pass

    def spring(self, webapps_identify, resp, url):
        name = "Spring"
        time.sleep(0.2)
        Identify.identify_prt(name)
        try:
            if r"timestamp" in resp.text and r"status" in resp.text and r"path" in resp.text and r"message" in resp.text:
                webapps_identify.append("spring")
            elif 'WWW-Authenticate' in resp.headers:
                if r"Spring" in resp.headers['WWW-Authenticate'] and r"Basic" in resp.headers['WWW-Authenticate']:
                    webapps_identify.append("spring")
            elif 'Www-Authenticate' in resp.headers:
                if r"Spring" in resp.headers['Www-Authenticate'] and r"Basic" in resp.headers['Www-Authenticate']:
                    webapps_identify.append("spring")
            elif r"X-Application-Context" in resp.headers:
                webapps_identify.append("spring")
            else:
                r = requests.get(self.url + "/233/233/233", headers=self.headers, timeout=self.timeout, verify=False)
                if r"timestamp" in r.text and r"status" in r.text and r"path" in r.text and r"message" in r.text:
                    webapps_identify.append("spring")
                elif 'WWW-Authenticate' in resp.headers:
                    if r"Spring" in r.headers['WWW-Authenticate'] and r"Basic" in r.headers['WWW-Authenticate']:
                        webapps_identify.append("spring")
                elif 'Www-Authenticate' in resp.headers:
                    if r"Spring" in r.headers['Www-Authenticate'] and r"Basic" in r.headers['Www-Authenticate']:
                        webapps_identify.append("spring")
                elif r"X-Application-Context" in r.headers:
                    webapps_identify.append("spring")
        except:
            pass

    def fastjson(self, webapps_identify):
        name = "Fastjson"
        Identify.identify_prt(name)
        md = random_md5()
        dns = md + "." + self.ceye_domain
        payload1 = '{"e":{"@type":"java.net.Inet4Address","val":"%s"}}' %dns
        payload2 = '{"@type":"java.net.Inet4Address","val":"%s"}' %dns
        payload3 = '{{"@type":"java.net.URL","val":"http://%s"}:"x"}' %dns
        payload4 = '{"@type":"com.alibaba.fastjson.JSONObject", {"@type": "java.net.URL", "val":"%s"}}""}' %dns
        payload5 = '{"a":"'
        headers = {'User-Agent': self.ua, 'Content-Type': "application/json"}
        try:
            requests.post(self.url, data=payload1, headers=headers, timeout=self.timeout, verify=False)
            requests.post(self.url, data=payload2, headers=headers, timeout=self.timeout, verify=False)
            requests.post(self.url, data=payload3, headers=headers, timeout=self.timeout, verify=False)
            requests.post(self.url, data=payload4, headers=headers, timeout=self.timeout, verify=False)
            request = requests.get(self.ceye_api + self.ceye_token)
            if md in request.text:
                webapps_identify.append("fastjson")
            else:
                request = requests.post(self.url, data=payload5, headers=headers, timeout=self.timeout, verify=False)
                if r"nested exception is com.alibaba.fastjson.JSONException:" in request.text:
                    if r"application/json" == request.headers['Content-Type']:
                        webapps_identify.append("fastjson")
        except:
            pass

    @staticmethod
    def identify_prt(name):
        print("\r{0}{1}{2}".format(now.timed(de=0), color.yel_info(), color.cyan(" Identify whether the target is: " + color.magenta(name))), end="          ")

