from django.shortcuts import render
import mysql.connector as sql
nam=''
em=''
pwd=''

# Create your views here.
def signupaction(request):
    global nam,em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost", user="root", passwd="777290", database='library')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="Name":
                nam=value
            if key=="Email":
                em=value
            if key=="Password":
                pwd=value
        c="insert into users('{}', '{}', '{}')".format(nam,em,pwd)
        cursor.execute(c)
        m.commit()

    return render(request, 'signup_page.html')
