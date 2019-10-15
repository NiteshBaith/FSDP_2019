# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 12:50:46 2019

@author: praveen.kumawat
"""

import win32com.client
import pyodbc
import pandas as pd
import os
import urllib
import json
import pyodbc

def outlook_is_running():
    import win32ui
    try:
        win32ui.FindWindow(None, "Microsoft Outlook")
        print('In Micro')
        return True
    except win32ui.error:
        return False

if not outlook_is_running():
    
    os.startfile("outlook")
    print('Start')
	

cnxn = pyodbc.connect
conn = pyodbc.connect()


def downloadPR(CSV_URL):
    response = urllib.request.urlopen(CSV_URL)
    with open('Power_reviewPR.csv','wb') as csvFile:
        for line in list(response.readlines())[2:]:
            csvFile.write(line)

def downloadAll(CSV_URL):
    response = urllib.request.urlopen(CSV_URL)
    with open('Power_review.csv','wb') as csvFile:
        for line in list(response.readlines())[2:]:
            csvFile.write(line)			

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
print(outlook)
inbox = outlook.GetDefaultFolder(6)
messages = inbox.Items
donebox = outlook.GetDefaultFolder(6).Folders("Read")

INSERT_SQL = '''  
        Insert Into [dbo].[LiveData] (Body,Subject,Sender,[Date]) 
		Values (?,?,?,?)
       '''
EXEC_SQL = ''' EXEC dbo.LiveData_Clean '''


for message in messages:
    Subject = message.Subject
    Sender = message.SenderEmailAddress
    date = message.ReceivedTime
    Body = message.Body.encode('utf-8')
    print(Body,Subject,Sender,date)
    try:
        print('I am trying inside try block')
        cursor_1=conn.cursor()
        cursor_1.execute(INSERT_SQL,Body,Subject,Sender,date)
        conn.commit()
        cursor_1.close()
        conn.close()
        cursor = cnxn.cursor()
        cursor.execute(INSERT_SQL,Body,Subject,Sender,date)
        cnxn.commit()
        cursor.close()
    except:
        print('I am trying inside Except block')
        pass

for message in messages:
    Subject = message.Subject
    date = message.ReceivedTime
    print(Subject,date)
    if Subject.find('FW: Your Report is Ready: PR Yesterday') == 0:
        Body = str(message.Body).split('\n')
        Body = [b.strip() for b in Body]
        for b in Body:
            if b.startswith('https://reporting-services.powerreviews.com'):
                token = b.split('/')[-1]
                print(token)
                url = 'https://reporting-services.powerreviews.com/download/file?token=' + token
                contents = urllib.request.urlopen(url).read()
                urls = json.loads(contents)['urls']
                for url in urls:
                    downloadPR(url)
                break
            
    if Subject.find('FW: Your Report is Ready:') == 0:    
        Body = str(message.Body).split('\n')
        Body = [b.strip() for b in Body]
        for b in Body:
            if b.startswith('https://reporting-services.powerreviews.com'):
                token = b.split('/')[-1]
                print(token)
                url = 'https://reporting-services.powerreviews.com/download/file?token=' + token
                contents = urllib.request.urlopen(url).read()
                urls = json.loads(contents)['urls']
                for url in urls:
                    downloadAll(url)
                break
            
    if Subject.find ('ShopLC Customer Feedback - Daily Report') == 0:
        print('I am about to download Narvar')
        attachments = message.attachments
        attachement = attachments.item(1)
        attachement.SaveASFile(os.getcwd() + '\\narvar.csv')
        
	
    message.Move(donebox)