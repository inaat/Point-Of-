
from django.shortcuts import render,HttpResponse,redirect
from django.db import connections ,connection
from decimal import Decimal
from django.http import JsonResponse

from django.http import HttpRequest
import json
# Create your views here.


def Home(request):



    return render(request , 'home.html')
def organization(request):
    cursor = connections["form1_db"].cursor()
    Project=[]
    Branch=[]
    Book=[]
    Account_ids=[]
    BCode=None
    if request.method == "POST" and request.is_ajax():
        accountid=request.POST.get("Accounts")
        titleofaccount=request.POST.get("titleofaccount")
        accountnature=request.POST.get("accountnature")
        type_accountnautre=request.POST.get("type_accountnautre")
        status= request.POST.get("status")
        subsccount=request.POST.get("Subsccounts")
        project_T= request.POST.get("Project_T")
        branch_T= request.POST.get("Branch_T")
        trade_T=request.POST.get("Trade_T")
        book_T=request.POST.get("Book_T")
      
        c = subsccount.count('')
      
        
        
        if project_T is not None and  branch_T is not None and book_T is not None:
            pString , pCode= project_T.split('::')
            bString , bCode= branch_T.split('::')
            bkString , bkCode= book_T.split('::')
            accoun= accountid[-6:]
            
        
            userid='789'
            message=None
            if subsccount == '' :
                
                print("is not None")
                cursor.execute("CALL `accounts`.`AddAccount`(@ReturnMessage,'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}',null)".format(trade_T,pCode,bCode,userid,bkCode,accoun,titleofaccount,accountnature,type_accountnautre,status))
                cursor.execute("SELECT @ReturnMessage")
                
                for retu in cursor.fetchone():
                    message=retu
                print(message)
                return JsonResponse({"message":message,"success":True},status=200)
                
            else:
                print("INAyat")
                subccoun= subsccount[-6:]
                cursor.execute("CALL `accounts`.`AddAccount`(@RetMess,'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(trade_T,pCode,bCode,userid,bkCode,accoun,titleofaccount,accountnature,type_accountnautre,status,subccoun))
                cursor.execute("SELECT @RetMess")
                
                for retu in cursor.fetchone():
                    message=retu
                    
                print(message)
            return JsonResponse({"message":message,"success":True}, status=200)
        return JsonResponse({"success":False}, status=400)    
    
    if request.method =="GET" and request.is_ajax():
        Trade_T= request.GET.get("Trade_T")
        Project_T= request.GET.get("Project_T")
        Branch_T= request.GET.get("Branch_T")
        Book_T=request.GET.get("Book_T")
        if Project_T is not None:
            PString , PCode= Project_T.split('::')
            cursor.execute("CALL `accounts`.`Branches_Code_`('{}' )".format(PCode))
            for project in cursor.fetchall():
                Branch.append(project)
        if Branch_T is not None:
            BString , BCode= Branch_T.split('::')
        
            
           
            cursor.execute("CALL `accounts`.`Book_Code_`('{}' )".format(BCode))
            for project in cursor.fetchall():
                Book.append(project)
               
        if Book_T is not None:
            
            BkString , BkCode= Book_T.split('::')
            
            
                           
            cursor.execute("Call `accounts`.`Account_List`({},{})".format(BCode,BkCode))
            
            for account_ids in cursor.fetchall():
               Account_ids.append(account_ids)
        try:
            
            cursor.execute("CALL `accounts`.`Project_Code_`('{}' )".format(Trade_T))
            for project in cursor.fetchall():
                Project.append(project) 
            
           
           
                
            
        except:
            return JsonResponse({"success":False}, status=400)
        return JsonResponse({"Project":Project,"Branch":Branch,"Book":Book,"Account_ids":Account_ids}, status=200)
        
    

    
    
   
    Trade=[]
    Trade_Value=[]
    cursor.execute("CALL `accounts`.`Trade_Code_`()")
    for trade in cursor.fetchall():
        Trade.append(trade)
    
       
    cursor.execute("select `trades`.`Trade_Code` from trades;")
    for trade in cursor.fetchall():
        Trade_Value.append(trade) 


    context = {
       
        'Trade':Trade,
        'Trade_Value':Trade_Value,
      
        
        
    }
    

    return render(request , 'organization/organization.html', context )

def Product_Info(request):
    cursor = connections["form1_db"].cursor()
    inventorydb = connections["inventory"].cursor()
    Trade=[]
    Trade_Value=[]
    cursor.execute("CALL `accounts`.`Trade_Code_`()")
    for trade in cursor.fetchall():
        Trade.append(trade)
    
       
    cursor.execute("select `trades`.`Trade_Code` from trades;")
    for trade in cursor.fetchall():
        Trade_Value.append(trade) 
    
    Category=[]
    
    inventorydb.execute("CALL `inventory`.`Find_Category`()")
    for cat in cursor.fetchall():
        Category.append(cat)
    print(Category,'CAt')
    context = {
        'Trade':Trade,
        'Trade_Value':Trade_Value,
        'Category':Category
      
        
        
    }


    return render(request , 'organization/Product_Info.html', context)



def AccoundFind(request):
    if request.method == "GET" and request.is_ajax():
        cursor = connections["form1_db"].cursor()
        Trade_T= request.GET.get("Trade_T")
        Project_T= request.GET.get("Project_T")
        Branch_T= request.GET.get("Branch_T")
        Book_T=request.GET.get("Book_T")
        accountid=request.GET.get("Accounts")

        if accountid is not  None:
            
            AcString , ACCID= accountid.split('::')
            pString , pCode= Project_T.split('::')
            bString , bCode= Branch_T.split('::')
            bkString , bkCode= Book_T.split('::')
            
            cursor.execute("CALL `accounts`.`account_find`('{}','{}','{}','{}','{}')".format(Trade_T,pCode,bCode,bkCode,ACCID))

            Account_Find=[]
            for result in cursor.fetchall():
                Account_Find.append(result)
            
            
            AcString = None 
            ACCID = None
            return JsonResponse({"Account_Find":Account_Find,"success":True}, status=200)
    return JsonResponse({"success":False}, status=400)




def ProjectCodeFind(request):
    
   
    if request.method == "GET" and request.is_ajax():
        cursor = connections["form1_db"].cursor()
        Trade_T= request.GET.get("Trade_T")
        Project_T= request.GET.get("Project_T")
        Project=[]
        Branch=[]
        
        
        cursor.execute("CALL `accounts`.`Project_Code_`('{}' )".format(Trade_T))
        for project in cursor.fetchall():
            Project.append(project) 
        if Project_T is not None:
            PString , PCode= Project_T.split('::')
            cursor.execute("CALL `accounts`.`Branches_Code_`('{}' )".format(PCode))
            for project in cursor.fetchall():
                Branch.append(project)  
        return JsonResponse({"Project":Project,"Branch":Branch,"success":True}, status=200)
    return JsonResponse({"success":False}, status=400)

def Account_List_By_Type(request):
    if request.method == "GET" and request.is_ajax():
        cursor = connections["form1_db"].cursor()
        Trade_T= request.GET.get("Trade_T")
        Project_T= request.GET.get("Project_T")
        Branch_T= request.GET.get("Branch_T")
        Inventory=[]
        SaleAC = []
        COGSAC = []

        if Trade_T is not None and  Project_T is not None and Branch_T is not None:
            pString , pCode= Project_T.split('::')
            bString , bCode= Branch_T.split('::')
           
            cursor.execute("CALL `accounts`.`Account_List_By_Type`('{}','{}','{}','INV' )".format(Trade_T,pCode,bCode))
            for inv in cursor.fetchall():
                Inventory.append(inv)
            cursor.execute("CALL `accounts`.`Account_List_By_Type`('{}','{}','{}','SFR' )".format(Trade_T,pCode,bCode))
            for sale in cursor.fetchall():
                SaleAC.append(sale)      
            cursor.execute("CALL `accounts`.`Account_List_By_Type`('{}','{}','{}','COG' )".format(Trade_T,pCode,bCode))
            for COG in cursor.fetchall():
                COGSAC.append(COG) 

        
        
        
        return JsonResponse({"Inventory":Inventory,"SaleAC":SaleAC,"COGSAC":COGSAC,"success":True}, status=200)
    return JsonResponse({"success":False}, status=400)

