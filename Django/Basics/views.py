from django.shortcuts import render

#Ceate your views here.

def Largest(request):
    if request.method=="POST":
        Number1=int(request.POST.get('txtnumber1'))
        Number2=int(request.POST.get('txtnumber2'))
        Number3=int(request.POST.get('txtnumber3'))
        if(Number1>Number2)&(Number1>Number3):
            Largest=Number1
        elif(Number2>Number1)&(Number2>Number3):
            Largest=Number2
        else:
            Largest=Number3
        return render(request,'Basics/Largest.html',{'largest':Largest})
    else:
        return render(request,'Basics/Largest.html')

def Calculator(request):
    if request.method=="POST":
        Number1=int(request.POST.get('txtnumber1'))
        Number2=int(request.POST.get('txtnumber2'))
        btn=request.POST.get('btn')
        if(btn=='+'):
            result=Number1+Number2
        elif(btn=='-'):
            result=Number1-Number2
        elif(btn=='x'):
            result=Number1*Number2
        else:
            result=Number1/Number2
        return render(request,'Basics/Calculator.html',{'sum':result})
    else:   
        return render(request,'Basics/Calculator.html')

def Salarycal(request):
    if request.method=="POST":
        Firstname=request.POST.get('txtfname')
        Lastname=request.POST.get('txtlname')
        Gender=request.POST.get('Gender')
        Martial=request.POST.get('Martial')
        Department=request.POST.get('ddldept')
        Basicsalary=int(request.POST.get('txtsal'))
        if(Gender=='Male'):
            if(Martial=='Single'):
                name='Mr'+'.'+Firstname+' '+Lastname
            else:
                name='Mr'+'.'+Firstname+' '+Lastname
        elif(Gender=='Female'):
            if(Martial=='Single'):
                name='Miss'+'.'+Firstname+' '+Lastname
            else:
                name='Mrs'+'.'+Firstname+' '+Lastname
        if(Basicsalary>=10000):
             TA=0.4*Basicsalary
             DA=0.35*Basicsalary
             HRA=0.3*Basicsalary
             LIC=0.25*Basicsalary
             PF=0.2*Basicsalary
        elif(Basicsalary>=5000):
             TA=0.35*Basicsalary
             DA=0.3*Basicsalary
             HRA=0.25*Basicsalary
             LIC=0.2*Basicsalary
             PF=0.15*Basicsalary
        else:
             TA=0.3*Basicsalary
             DA=0.25*Basicsalary
             HRA=0.2*Basicsalary
             LIC=0.15*Basicsalary
             PF=0.1*Basicsalary
        DEDUCTION=LIC+PF
        NET=Basicsalary+TA+DA+HRA-(LIC+PF)
        return render(request,'Basics/Salarycal.html',{'Name':name,'Gender':Gender,'Martial':Martial,'Department':Department,'TA':TA,'DA':DA,'HRA':HRA,'LIC':LIC,'PF':PF,'Deduction':DEDUCTION,'NET':NET,'Basicsalary':Basicsalary})
        
    else:
        return render(request,'Basics/Salarycal.html')




