from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from bs4 import BeautifulSoup
import pandas as pd
import requests
from pathlib import Path

# Create your views here.
@csrf_exempt #csrf 보안토큰 요청 생략가능 설정
def exchange(request):
    try:
        url = 'https://finance.naver.com/marketindex/'
        res = requests.get(url)
        html_str = res.text
        soup = BeautifulSoup(html_str)

        hlsts = soup.find_all(class_='h_lst')
        hlist = ['<b>'+hlst.text+'</b>' for hlst in hlsts]

        hinfo = soup.find_all(class_='head_info')
        hinfo1 = []
        hinfo2 = []
        for h in hinfo:
            temp = h.text.replace('\n', ' ').split()
            if len(temp) == 4:
                hinfo1.append(''.join(temp[:2]))
                hinfo2.append(''.join(temp[2:]))
            else:
                hinfo1.append(''.join(temp[0]))
                hinfo2.append(' '.join(temp[1:]))

        exchange_df = pd.DataFrame({"통화명":hlist
                                    , "환율":hinfo1
                                    , "전일대비":hinfo2})
        exchange = exchange_df.values.tolist()
        return JsonResponse({"msg":exchange})
    except:
        pass


@csrf_exempt #csrf 보안토큰 요청 생략가능 설정
def select(request):
    try:
        basedir = str(Path.cwd())
        # basedir #'D:\\emspy\\python_web\\emsjango'
        url = basedir+'/file/ajax/sido.txt'

        sido_df = pd.read_csv(url, sep='\t', names=['sido','gu','dong'])

        sido_df.dropna(inplace=True)
        gudong = sido_df[sido_df.dong == sido_df.gu].index
        sido_df = sido_df.drop(gudong)

        #unique 값만 가져오기
        sido_select = request.POST.get('si')
        gu_select = request.POST.get('gu')
        print(sido_select)
        print(gu_select)
        
        if sido_select == None and gu_select == None:
            sido = sido_df.iloc[:, 0]
            select = sido
        elif (sido_select != None) and (gu_select == None):
            gu = sido_df.loc[(sido_df.sido==sido_select), "gu"]
            select = gu
        elif (sido_select != None) and (gu_select != None):
            dong = sido_df.loc[(sido_df.gu==gu_select), "dong"]
            select = dong
        else: pass
        
        select = sorted(select.unique())
        return JsonResponse({'sido':select})
        
    except:
        pass
