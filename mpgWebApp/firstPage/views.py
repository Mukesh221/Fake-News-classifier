from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
 
# Create your views here.
import joblib 

reloadModel=joblib.load('./models/fakenews.pkl')

def index(request):
    context={'a':'HelloWorld!!'}
    return render (request,'index.html',context)
    #return HttpResponse{'a':1}

def predictMPG(request):
    if request.method == 'POST':
        temp={}
        temp['title']=request.POST.get('titleVal')
        temp['text']=request.POST.get('textVal')


     
    #df=pd.DataFrame(list(temp.items()),columns=['column1','column2'])
    testDtaa=pd.DataFrame({'x':temp}).transpose()
    scoreval=reloadModel.predict(testDtaa)
    

     
    if scoreval==1:
        x=True
    else:
        x=False
    
    context={'scoreval':x}

    #context={'a':temp['text']}
    return render(request,'index.html',context)