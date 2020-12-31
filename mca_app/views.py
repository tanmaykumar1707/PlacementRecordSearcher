from django.shortcuts import render, HttpResponse
import pandas as pd
# Create your views here.

def index(request):
    # return HttpResponse("This is first page")
    conext = {
        

    }
    sheetid = "1SWTx2PPEB5OxzjL50dd-SnQtLsWYnbC7pphqhkv7NUQ"
    sheet_name="NIT Agartala MCA Placement Record  2018-21 Batch"
    URL = 'https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(sheetid,sheet_name)
    URL = URL.replace(" ", "%20")
    comp = pd.read_csv(URL)

    sheetid1="1FxDSMSavXbs-PPEUeF7JQEbJTHaceikXrltXeKG_Aok"
    sheet_name1="MCA_Candidates"
    URL1 = 'https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(sheetid1,sheet_name1)
    URL1 = URL1.replace(" ", "%20")
    cand = pd.read_csv(URL1)
    if request.method == "POST":
        print(request.POST["enroll"])
        t = request.POST["enroll"]
        t =t.upper()
        comp_list=[]
        comp_list = cand.loc[cand.iloc[:,1] == t]["company_id"]
        eli_df = pd.DataFrame()
        if(len(comp_list)):    
            for x in comp_list:
                temp=comp[comp.c_id==x]
                eli_df=eli_df.append(temp)
            x=eli_df[eli_df.iloc[:,7]=="upcoming"]
            y=eli_df[eli_df.iloc[:,7]=="running"]
            z=eli_df[eli_df.iloc[:,7]=="completed"]
            print(x)
            shape = x.shape
            print(shape[0])
            conext ={
            "enroll":request.POST["enroll"],
            "upcoming_data":x.transpose().to_dict(),
            "running":y.transpose().to_dict(),
            "completed":z.transpose().to_dict()

            }
        else:
            print("Nothing Found")
    return render(request,'index.html',conext)

def about(request):
    return HttpResponse("This is about  page")