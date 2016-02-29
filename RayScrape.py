import requests
from bs4 import BeautifulSoup

def soupSetup(place):
    r=requests.get("http://www.booneweather.com/Forecast/"+place)
    soup=BeautifulSoup(r.content,"html.parser")
    return soup

def getForecastvar(place):
    soupvar=soupSetup(place)
    forecastTxt=soupvar.find_all('p', {'class': 'forecast_text'})
    return forecastTxt

def summaryForecast(place):
    forecastTxt=getForecastvar(place)
    build_forecast=forecastTxt[0].text +"\n"+ forecastTxt[1].text
    return build_forecast

def extendedForecast(place):
    forecastTxt=getForecastvar(place)
    build_forecast=forecastTxt[4].text
    return build_forecast

def buildDailyForecast(place):
    soupvar=soupSetup(place)
    daily=soupvar.find_all("table",{"class":"five_day"})
    strForecast=""
    for item in daily:
        #for string in item.strings:
        lstring=[x for x in list(item.strings) if len(x)>1]
        '''for strBase in lstring:
            print('len = %s' % len(strBase))
            if len(strBase)>1 : lstring.remove(strBase)'''
        i=0

        for strBase in lstring:
            #print strBase
            weekd=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
            if strBase in weekd:
                if strForecast=="":
                    strForecast="Forecast for "+strBase+". "
                else:
                    strForecast=strForecast+" Forecast for "+strBase+". "
            elif strBase[:2]=="Hi":
                strBase=strBase.replace("\n","")
                strForecast=strForecast+"Temperatures: "+strBase+". "
            else:
                strForecast=strForecast+strBase+". "
        #strip punctuation except period and comma
        strForecast=strForecast.replace(";",",")
        strForecast = "".join(c for c in strForecast if c not in ('!','&',':'))
        #print strForecast
        return strForecast







#print soup

#print summaryForecast("Deep+Gap")
#print summaryForecast("Boone")
#print curForecast
#print "extended forecast"
#print extendedForecast(getForecastvar("Deep+Gap"))

#print buildDailyForecast("Deep+Gap")
#print buildDailyForecast("Boone")