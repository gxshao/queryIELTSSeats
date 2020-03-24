import requests as requests
import time

def scheduledQuery():
    url = "https://ielts.neea.cn/myHome/52943457/queryTestSeats"
    params = {
        'queryMonths':'2020-05,2020-06,2020-07', 
        'queryProvinces':'30,31,32,33',
        'neeaAppId':'',
        'productId':'IELTSPBT',
        'levelCode':'',
        '_':'1585032254126'}
    c = {
        'domain_port_https':'443', 
        'domain_port_http':'80', 
        'domain_name_edu':'ielts.neea.edu.cn', 
        'domain_name_net':'ielts.neea.cn',
        'BIGipServerhw_ielts_internal_pool':'51038218.23040.0000', 
        '1laYpfWboXsu443S':'IYmgjJPOfF6NjHPME.4mJHbsIh0fJYFobKzrXPE5KO3gkT.rmZy40V674pXPwqaB', 
        '1laYpfWboXsu443T':'41TGN0X5RZLCrq3qiVaOb8TTnWIKb9r.FsSsfym5Wp90aNntG53nW2sfutLnfN4pQVE.818aGmk.pLw__KFxIjoaLuHKplttR1nG1oqMgBbycoVJlhZtThni7T9Pf2JntZFaYPpaJMZa8_pYjvAT9PEqW3hoteRiE1rli94QTg6Sd64WCzLZu5gxtPxPNiBu.PHmgudn08_PqfjnZBeik8goHnBCV0_U_LT_B4OmIy_wGlEl0oNujIQBbYHfMzFONkLFPvKaTDFv2y60NNbezcZpEoZqj97V0tnZufEdJVonK4ZuZmRyG4HbhMyJZ6wVyLML5TFYfWas.SHyjfwWKVP2fUOY_ROkpTi6eCxHVST3uHycVO.wacfY.G5vpjK7zeS0', 
        '_ga':'GA1.3.48660123.1585020538', 
        '_gid':'GA1.3.2052652049.1585020538', 
        'JSESSIONID':'YOUROWNSESSION',
        'locale':'zh_CN'}
    count = 0
    schoolKey = "centerNameCn"
    dateKey = "adminDateCn"
    statusKey = "seatStatus"
    while True:
        print("Ready to query seats in ShangHai")
        r = requests.get(url = url, params = params, cookies = c) 
        data = r.json()
        flag = False
        for i in data:
            arr = data[i]
            for obj in arr:
                if obj[statusKey] == 1:
                    print("提醒，有位置了。。时间：{}，地点：{}".format(obj[dateKey], obj[schoolKey]))
                    flag = True
        count += 1
        if flag == False:
            print("这次查询还是没位置！")
        print("===========================Query count: " + count.__str__()+ " ========================")
        time.sleep(60)

if __name__ == "__main__":
    scheduledQuery()
