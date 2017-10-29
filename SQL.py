# -*- coding: utf-8 -*-
from mysql.connector import errorcode
from urllib2 import urlopen
import mysql.connector as mc
import re
import json

# AIzaSyBIiH_njTY15PILISTXRYBs1EE_3giJlR8
user='root'
password='1'
host='127.0.0.1'
database='craigslist'
tableName = 'ad'

cnx = mc.connect(user=user, password=password)
c1 = cnx.cursor()

tables = {}
tables['ad']=('''
create table ad (
adId int(7) not null AUTO_INCREMENT,
zipCode varchar(8),
location varchar(100),
price int(6),
model varchar(30) ,
url varchar(100) ,
gps varchar(80),
description varchar(100),
PRIMARY KEY(adId)
)
''')


def create_database():
    try:
        c1.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(database))
        print('DataBase Created!')
    except mc.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

def create_table():
    for name, ddl in tables.iteritems():
        try:
            c1.execute(ddl)
            print('Table', name, 'Created!')
        except mc.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")

try:
    cnx.database = database
except mc.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        print('Create database now.....')
        create_database()
        cnx.database = database
    else:
        print(err)
        exit(1)
old = ''
try:
    cnx.database = database
    c1 = cnx.cursor()
    fhandle = open('LosAngeles.txt','r')
    for line in fhandle:
        s = line.split('?')
        adId = s[0]
        zipCode = s[1]
        location = s[2]
        price = int(s[3])
        model = s[4]
        url = s[5]
        description = s[6].decode('utf-8')
        description = re.sub(r'([^\s\w]|_)+', '', description)
        gps = s[7][:-1]
        query =  ("INSERT INTO ad "
                       "( zipCode, location, price, model,url,gps,description) "
                       "VALUES (%s, %s, %s, %s, %s, %s, %s)")
        queryData = (zipCode, location, price, model,url,gps,description)
        c1.execute(query,queryData)
        cnx.commit()
    c1.close()
    cnx.close()
    fhandle.close()
except mc.Error as e:
    print(e)
    print('Create talbe now...')
    create_table()
