# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 04:56:23 2020

@author: rolly
"""

from selenium import webdriver


class Surabi(object):
    def openSite(self,url):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        
    def textName(self,name):
        return self.driver.find_element_by_name(name).text
    
    def attrName(self,name,attr):
        return self.driver.find_element_by_name(name).get_attribute(attr)
    
    def fillName(self,name,content):
        return self.driver.find_element_by_name(name).send_keys(content)
    
    def clickName(self,name):
        return self.driver.find_element_by_name(name).click()
    
    def textClass(self,classname):
        return self.driver.find_element_by_class_name(classname).text
    
    def textClasses(self,classname,i):
        return self.driver.find_elements_by_class_name(classname)[i].text
    
    def textXpath(self,xpath):
        # xpath = "//option[@value='"+semester+"']"
        # "//input[@value='Cari' and @name='Cari']"
        # "//table[@class='box' and @align='left']/tbody/tr"
        return self.driver.find_element_by_xpath(xpath).text
    
    def clickXpath(self,xpath):
        return self.driver.find_element_by_xpath(xpath).click()
    
    def closeSite(self,url):
        self.driver.get(url)
        self.driver.close()