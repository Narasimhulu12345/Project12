from django.core.mail import send_mail
from django.http import HttpResponse
from project9.settings import EMAIL_HOST_USER
from .forms import RegForm
# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'home.html')
        rf=RegForm()
        con_dic={'rf':rf}
        return render(request,'home.html',context=con_dic)
class Reg(View):
    def post(self,request):
        otp=str(random.randint(10000000,99999999))
        print(otp)
        mobno=request.POST["t7"]
        emailid=request.POST["t6"]
        mobno=request.POST["MobileNo"]
        emailid=request.POST["Emailid"]
        resp = requests.post('https://textbelt.com/text', {
            'phone': mobno,
            'message': otp,