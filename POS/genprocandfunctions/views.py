from django.shortcuts import render,HttpResponse,redirect
from django.db import connections ,connection
from .forms import Login_Form
import socket
from django.http import HttpRequest




def lousy_secret(request):
    if not request.session.get('logged_in'):
        return redirect('genprocandfunctions:Login')
    return redirect('accounts:home')

def Login(request):
    cursor = connections["form2_db"].cursor()
   
    
    if request.method=="POST":
        form = Login_Form(request.POST)
        if form.is_valid():
            User_Id = form['User_Id'].data
            Location_Id = form['Location_Id'].data
            Password = form['Password'].data
            request.session['logged_in'] = True
            cursor.execute("CALL `genprocandfunctions`.`User_Login`(@ReturnMessage, @TradeCode, @ProjectCode, @BranchCode,@UserName,@userType, '{}', '{}' , '{}' , '{}' )".format(socket.gethostname(),User_Id , Location_Id, Password))
            cursor.execute("SELECT @TradeCode,@ProjectCode,@BranchCode,@UserName,@userType ;")
            li = []
            for sess in cursor.fetchone():
                val = str(sess)
                li.append(val)
            
            
            request.session['TradeCode'] = li[0]
            request.session['ProjectCode'] = li[1] 
            request.session['BranchCode'] = li[2] 
            request.session['UserName'] = li[3] 
            request.session['UserType'] = li[4] 
            
            return redirect("accounts:home")
             

    else:
        form = Login_Form()

    context ={'form':form}  

    return render(request, "index.html",context)


def login_session(request):
    response = "<h1>Welcome to Sessions of dataflair</h1><br>"
    if request.session.get('UserType'):
        response += "UserType : {0} <br>".format(request.session.get('UserType'))
    if request.session.get('TradeCode'):
        response += "TradeCode : {0} <br>".format(request.session.get('TradeCode'))
        return HttpResponse(response)
    else:
        return redirect("/")



    
    # cursor = connection.cursor()
    # # cursor.execute("CALL GetOfficeByCountry('kl');")
    # cursor.callproc('GetOfficeByCountry',['kl',])
    # #multidb
    # # cur = connections["use_db"].cursor()
    # # cur.callproc('GetOfficeByCountry',['kl',])
    # SELECT @TradeCode;SELECT @ProjectCode;SELECT @BranchCode;SELECT @UserName;SELECT @userType;



    # cursor.execute("CALL `genprocandfunctions`.`User_Login`(@ReturnMessage, @TradeCode, @ProjectCode, @BranchCode,@UserName,@userType, 'inpc1', 225, 1, '123zxcasd');")
    # cursor.execute("SELECT @ReturnMessage; ")
    # print(cursor.fetchall())
    # cursor = connections["form2_db"].cursor()
    # user_id = request.POST.get("user_id")
    # location_id = request.POST.get("location_id")
    # password = request.POST.get('password')
    # print(user_id,location_id,password)
    # # cursor.callproc('User_Login',['ReturnMessage','TradeCode','ProjectCode,','BranchCode','UserName','userType', 'inpc1',user_id , location_id, password])
              

    # cursor.execute("CALL `genprocandfunctions`.`User_Login`(@ReturnMessage, @TradeCode, @ProjectCode, @BranchCode,@UserName,@userType, 'inpc1', '{}' , '{}' , '{}' )".format(user_id , location_id, password))
    # cursor.execute("SELECT @ReturnMessage;")
    # print(cursor.fetchall())