from django.shortcuts import render, HttpResponse,redirect
from django.db import connections ,connection
from decimal import Decimal
from django.http import JsonResponse

from django.http import HttpRequest
import json
# Create your 
import os
import datetime
from datetime import datetime
from django.conf import settings
def Product_Info(request):
    cursor = connections["form1_db"].cursor()
    inventorydb = connections["inventory"].cursor()
    

    if request.method == "POST"  and request.is_ajax():
        
        ProductCode= request.POST.get("ProductCode")
        Category= request.POST.get("Category")
        PType = request.POST.get("type")
        Valuation= request.POST.get("Valuation")
        Scheme = request.POST.get("Scheme")
        Active = request.POST.get("Active")
        ProductTitle=request.POST.get("Product_Title")
        OIUnit=request.POST.get("OIUNIT")
        Packing=request.POST.get("Packing")
        SalDisc = request.POST.get("SalDisc")
        PurDisc=request.POST.get("PurDisc")
        Comm=request.POST.get("Comm")
        TradePrice=request.POST.get("TradePrice")
        PR=request.POST.get("PR")
        SalPrice=request.POST.get("SalPrice")
        DSTPrice=request.POST.get("DSTPrice")
        WSPrice=request.POST.get("WSPrice")
        Company=request.POST.get("Company")
        Vendor=request.POST.get("Vendor")
        oldprice=request.POST.get("oldprice")
        ROLevel = request.POST.get("ROLevel")
        OuterInOf =request.POST.get("OuterInOf")
        Innerof=request.POST.get("Innerof")
        Shelf=request.POST.get("Shelf")
        InventoryAC=request.POST.get("InventoryAC")
        SALE_AC=request.POST.get("SALE_AC") 
        COG_AC=request.POST.get("COG_AC")
        IMAGE=request.FILES.get('image')
        Trade_T= request.POST.get("Trade_T")
        Project_T=request.POST.get("Project_T")
        Branch_T=request.POST.get("Branch_T")
        LocCode=request.POST.get("LocCode")
        innerUnit =request.POST.get("innerUnit")
        print(IMAGE,'url')
       
        if Scheme is None :
            Scheme = 'Null'
        if OIUnit == '':
            OIUnit = 'Null'
        if innerUnit == '':
            innerUnit ='Null'
        if Packing == '':
            Packing ='Null'
        if SalDisc == '':
            SalDisc ='Null'
        if PurDisc == '':
            PurDisc ='Null'
        if  Comm == '' :
            Comm='Null'
        if DSTPrice == '':
            DSTPrice="Null"
        if WSPrice == '':
            WSPrice='Null'  
        if oldprice == '' :
           oldprice='Null'
        if ROLevel == '' :
            ROLevel="Null"
        if OuterInOf == '':
            OuterInOf='Null' 
        if Innerof == '':
            Innerof='Null'
        if Shelf == '' :
            Shelf="Null"   
        CompCode = None
        if Company is None:
            CompCode='Null'
            
        else:
            Compstring, CompCode=Company.split('::')
        VendCode = None
        if Vendor is None:
            VendCode='Null'
            
        else:
            Venstring, VendCode=Vendor.split('::')
       
        
         
        

        if Trade_T is not None and Project_T is not None and Branch_T is not None and  Category is not None:
            TString , TCode= Trade_T.split('::')
            PString , PCode= Project_T.split('::')
            BString , BCode= Branch_T.split('::')
            CString , CCode=Category.split('::')
            InvString , InvCode= InventoryAC.split('::')
            SACString , SACCode= SALE_AC.split('::')
            CogString , CogCode= COG_AC.split('::')
            Locstring,LoCode=LocCode.split('::')
            message=None
            
            if  IMAGE is not None:
                img=IMAGE
                user_folder = 'ProductImage/'
                img_extension = os.path.splitext(img.name)[1]
                if not os.path.exists(user_folder):
                    os.mkdir(user_folder)
                io=ProductTitle
                img_save_path="{}{}{}".format(user_folder,io,img_extension)
                
                inventorydb.execute("CALL `inventory`.`ProductAdd`(@ReturnMessage,{},{},{},{},{},'{}','{}',{},'{}','{}','{}',{},{},'{}',{},{},{},{},{},{},{},{},{},'{}',{},{},{},'{}',{},{},{},{},{},{})".format(TCode,PCode,BCode,ProductCode,CCode,PType,Valuation,Shelf,Active,img_save_path,ProductTitle,OIUnit,innerUnit,Packing,SalDisc,PurDisc,Comm,TradePrice,PR,SalPrice,DSTPrice,WSPrice,VendCode,oldprice,ROLevel,OuterInOf,Innerof,TString,InvCode,SACCode,CogCode,LoCode,CompCode,Scheme))
                inventorydb.execute("SELECT @ReturnMessage")
                for retu in inventorydb.fetchone():
                    message=retu
            
                with open(img_save_path, 'wb+') as f:
                    for chunk in img.chunks():
                        f.write(chunk)
                return JsonResponse({"message":message,"success":True},status=200)
            else:
                IMAGE='Null'
                inventorydb.execute("CALL `inventory`.`ProductAdd`(@ReturnMessage,{},{},{},{},{},'{}','{}',{},'{}',{},'{}',{},{},'{}',{},{},{},{},{},{},{},{},{},'{}',{},{},{},'{}',{},{},{},{},{},{})".format(TCode,PCode,BCode,ProductCode,CCode,PType,Valuation,Shelf,Active,IMAGE,ProductTitle,OIUnit,innerUnit,Packing,SalDisc,PurDisc,Comm,TradePrice,PR,SalPrice,DSTPrice,WSPrice,VendCode,oldprice,ROLevel,OuterInOf,Innerof,TString,InvCode,SACCode,CogCode,LoCode,CompCode,Scheme))
                inventorydb.execute("SELECT @ReturnMessage")
                for retu in inventorydb.fetchone():
                    message=retu  
                return JsonResponse({"message":message,"success":True},status=200)      
        return JsonResponse({"success":False}, status=400) 
        

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
    for cat in inventorydb.fetchall():
        Category.append(cat)
    

    context = {
        'Trade':Trade,
        'Trade_Value':Trade_Value,
        'Category':Category
      
        
        
    }


    return render(request , 'organization/Product_Info.html', context)


def directupload(request):
    

    # if request.method == 'POST':
    #     if request.is_ajax():

            
    #         img = request.FILES.get('image')
    #         print(img)
    #         user_folder = 'ProductImage/'
    #         img_extension = os.path.splitext(img.name)[1]
    #         if not os.path.exists(user_folder):
    #             os.mkdir(user_folder)
    #         io='Inonhj' 
    #         img_save_path="{},{},{}".format(user_folder,io,img_extension)
    #         with open(img_save_path, 'wb+') as f:
    #             for chunk in img.chunks():
    #                 f.write(chunk)
    #         # print(file)
            

            # today_folder = datetime.now().strftime("%B%d_%Y")

            # # Set full path to today_folder where file will be saved
            # path_to_img = os.path.join(settings.MEDIA_ROOT)
            # print(path_to_img )
            # # Check if today_folder already exists
           

            # img_path = os.path.join(path_to_img, file.name)

            # # Start writing to the disk
            # with open(img_path, 'wb+') as destination:

            #     if file.multiple_chunks:  # size is over than 2.5 Mb
            #         for chunk in file.chunks():
            #             destination.write(chunk)
            #     else:
            #         destination.write(file.read())

    return render(request, 'organization/avioddb.html')