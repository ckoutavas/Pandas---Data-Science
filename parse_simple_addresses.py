# how to parse simple address to complex address in a df

import pandas as pd
import numpy as np
import usaddress

# create functions use try and except to skip blank strings

def AddressNumber(x):
    try:
        data = usaddress.tag(x)
        if 'AddressNumber' in data[0].keys():
            return data[0]['AddressNumber']
    except:
        pass

def StreetNamePreDirectional(x):
    try:
        data = usaddress.tag(x)
        if 'StreetNamePreDirectional' in data[0].keys():
            return data[0]['StreetNamePreDirectional']
    except:
        pass
    
def StreetName(x):
    try:
        data = usaddress.tag(x)
        if 'StreetName' in data[0].keys():
            return data[0]['StreetName']
    except:
        pass
    
def StreetNamePostType(x):
    try:
        data = usaddress.tag(x)
        if 'StreetNamePostType' in data[0].keys():
            return data[0]['StreetNamePostType']
    except:
        pass
    
def StreetNamePostDirectional(x):
    try:
        data = usaddress.tag(x)
        if 'StreetNamePostDirectional' in data[0].keys():
            return data[0]['StreetNamePostDirectional']
    except:
        pass
    
def OccupancyType(x):
    try:
        data = usaddress.tag(x)
        if 'OccupancyType' in data[0].keys():
            return data[0]['OccupancyType']
    except:
        pass
    
def OccupancyIdentifier(x):
    try:
        data = usaddress.tag(x)
        if 'OccupancyIdentifier' in data[0].keys():
            return data[0]['OccupancyIdentifier']
    except:
        pass
    
def PlaceName(x):
    try:
        data = usaddress.tag(x)
        if 'PlaceName' in data[0].keys():
            return data[0]['PlaceName']
    except:
        pass
    
def StateName(x):
    try:
        data = usaddress.tag(x)
        if 'StateName' in data[0].keys():
            return data[0]['StateName']
    except:
        pass
    
def ZipCode(x):
    try:
        data = usaddress.tag(x)
        if 'ZipCode' in data[0].keys():
            return data[0]['ZipCode']
    except:
        pass


# apply the functions using lambda functions for the full concat address

df['AddressNumber'] = df.apply(lambda x: AddressNumber(x['concat_address']), axis=1)
df['StreetNamePreDirectional'] = df.apply(lambda x: StreetNamePreDirectional(x['concat_address']), axis=1)
df['StreetName'] = df.apply(lambda x: StreetName(x['concat_address']), axis=1)
df['StreetNamePostType'] = df.apply(lambda x: StreetNamePostType(x['concat_address']), axis=1)
df['StreetNamePostDirectional'] = df.apply(lambda x: StreetNamePostDirectional(x['concat_address']), axis=1)
df['OccupancyType'] = df.apply(lambda x: OccupancyType(x['concat_address']), axis=1)
df['OccupancyIdentifier'] = df.apply(lambda x: OccupancyIdentifier(x['concat_address']), axis=1)
df['PlaceName'] = df.apply(lambda x: PlaceName(x['concat_address']), axis=1)
df['StateName'] = df.apply(lambda x: StateName(x['concat_address']), axis=1)
df['ZipCode'] = df.apply(lambda x: ZipCode(x['concat_address']), axis=1)
df.fillna('', inplace=True)


# view all the keys

for addr in df['concat_address']:
    data = usaddress.tag(addr)
    print(data[0].keys())
