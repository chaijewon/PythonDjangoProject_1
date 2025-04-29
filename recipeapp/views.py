from django.shortcuts import render
from recipeapp import models
# Create your views here.
# 웹관련 모든 서버는 => request,response

def index(request):
    return render(request,"recipe/index.html")
#forward
def recipeList(request):
    try:
        page=request.GET['page']
    except Exception as e:
        page="1"
    # 정수(X) => str
    # request.getParameter("page")
    #request.POST['fd']
    curpage=int(page)
    # 오라클로부터 데이터 받기
    list,totalpage=models.recipeListData(curpage)

    recipe_list=[]
    for r in list:
        rr={"no":r[0],"title":r[1],"poster":r[2],
            "chef":r[3]}
        recipe_list.append(rr)
        #딕트형으로 변경 => 튜플
        # list : [] , set : {} , tuple : ()
    BLOCK=10
    startPage=((curpage-1)//BLOCK * BLOCK)+1
    endPage = ((curpage-1)//BLOCK * BLOCK) + BLOCK
    print(range(startPage,endPage))
    if endPage>totalpage:
        endPage=totalpage

    return render(request,"recipe/list.html",
                  {"rd":recipe_list,"curpage":int(curpage),
                   "startPage":int(startPage),"endPage":int(endPage),
                   "totalpage":int(totalpage),"range":range(int(startPage),int(endPage)+1)})
def recipeDetail(request):
    no=request.GET['no']
    # String no=request.getParameter("no")
    rd,rmake,rdata=models.recipeDetailData(int(no))
    print(rd)
    # rd = () = {}:JSON
    '''
      no,title,chef,chef_poster,chef_profile,
      info1,info2,info3,content,foodmake,data.poster
    '''
    recipe_data={
        "no":rd[0],
        "title":rd[1],
        "chef":rd[2],
        "chef_poster":rd[3],
        "chef_profile":rd[4],
        "info1":rd[5],
        "info2":rd[6],
        "info3":rd[7],
        "content":rd[8],
        "poster":rd[9]
    }
    fm=rmake.split("\n")
    posters=[]
    make=[]
    #재료 => ,
    data=rdata.split(",")

    for m in range(len(fm)-1):
        temp=fm[m].split("^")
        print(temp)
        make.append(temp[0])
        posters.append(temp[1])
    detail={
        "detail":recipe_data,
        "posters":posters,
        "make":make,
        "data":data
    }
    print(detail)
    return render(request,
                  "recipe/detail.html",{
        "rd":detail
    })









