from calendar import month
import datetime
from dateutil.relativedelta import relativedelta
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .forms import *
from .models import *
from django.views.generic import ListView,UpdateView,DeleteView,DetailView
import random
from django.db.models import Q

# Create your views here.
def Index(request):
    return render(request,"bankcards/index.html" )


def CreditView(request):
    credits = CardData.objects.filter(Series__Type__Type = "Кредитная карта")

    context = {"credits":credits}

    return render(request,"bankcards/credit.html",context)


def DebetView(request):
    debets = CardData.objects.filter(Series__Type__Type = "Дебетовая карта")

    context = {"debets":debets}

    return render(request,"bankcards/debet.html",context)


class CardUpdateView(UpdateView):
    model = CardData
    template_name = 'bankcards/update.html'
    form_class = CardForm
    success_url = reverse_lazy("home")

class CardDetailView(DetailView):
    model = CardData
    template_name = 'bankcards/detail.html'
    context_object_name = "card"

def CreateCreditCard(request):
    error = ''
    if request.method == 'POST':
        form = CreateForm(request.POST)
        series = request.POST.get("Series")
        kol = request.POST.get("kolvo")
        if form.is_valid():
            if series == "Visa":
                t=0
                while int(t)<int(kol):
                    num = random.randint(11111111,99999999)
                    cr = CardData.objects.create(Series_id=1,Numbers = int("44555566" + str(num)),End_date = datetime.datetime.now() + relativedelta(years=+1) + relativedelta(months=+6))
                    cr.save()
                    t=t+1
            else:
                k=0
                while int(k)<int(kol):
                    num = random.randint(11111111,99999999)
                    cr = CardData.objects.create(Series_id=3,Numbers = int("55445566" + str(num)),End_date = datetime.datetime.now() + relativedelta(years=+1) + relativedelta(months=+6))
                    cr.save()
                    k=k+1
            return redirect('credit')
        else:
            error = "Форма была неверно введена"
    form = CreateForm
    context = {'form':form,
    'error':error,
    }
    return render(request,'bankcards/createcard.html',context)

def CreateDebetCard(request):
    error = ''
    if request.method == 'POST':
        form = CreateForm(request.POST)
        series = request.POST.get("Series")
        kol = request.POST.get("kolvo")
        if form.is_valid():
            if series == "Visa":
                t=0
                while int(t)<int(kol):
                    num = random.randint(11111111,99999999)
                    cr = CardData.objects.create(Series_id=2,Numbers = int("44663344" + str(num)),End_date = datetime.datetime.now() + relativedelta(years=+1) + relativedelta(months=+6))
                    cr.save()
                    t=t+1
            else:
                k=0
                while int(k)<int(kol):
                    num = random.randint(11111111,99999999)
                    cr = CardData.objects.create(Series_id=4,Numbers = int("55663344" + str(num)),End_date = datetime.datetime.now() + relativedelta(years=+1) + relativedelta(months=+6))
                    cr.save()
                    k=k+1
            return redirect('debet')
        else:
            error = "Форма была неверно введена"
    form = CreateForm
    context = {'form':form,
    'error':error,
    }
    return render(request,'bankcards/createcard.html',context)

class CardDetailView(DetailView):
    model = CardData
    template_name = 'bankcards/detail.html'
    context_object_name = "card"

class CardDeleteView(DeleteView):
    model = CardData
    template_name = 'bankcards/index.html'
    success_url = reverse_lazy("home")

class SearchCreditResultsView(ListView):
    model = CardData
    template_name = 'bankcards/searchcredit_results.html'
 
    def get_queryset(self): # новый
        query = self.request.GET.get('q')
        query1 = self.request.GET.get('date1')
        query2 = self.request.GET.get('num')
        query3 = self.request.GET.get('date2')
        query5 = self.request.GET.get('sum')
        query6 = self.request.GET.get('act')
        if query == "Visa":
            if query6 == "all":
                object_list = CardData.objects.filter(
                    Q(Series__id__icontains=1,Numbers__icontains=query2, Relase_date__icontains=query1,End_date__icontains=query3,Summ__icontains=query5)
                    )
                return object_list
            elif query6 == "notactiv":
                object_list = CardData.objects.filter(
                    Q(Series__id__icontains=1,Numbers__icontains=query2, Relase_date__icontains=query1,End_date__icontains=query3,Summ__icontains=query5,Status__in=("не активирована","не активирована"))
                )
                return object_list
            elif query6 == "activ":
                object_list = CardData.objects.filter(
                    Q(Series__id__icontains=1,Numbers__icontains=query2, Relase_date__icontains=query1,End_date__icontains=query3,Summ__icontains=query5,Status__in=("активирована", 'активирована'))
                )
                return object_list

        elif query == "MasterCard":
            if query6 == "all":
                object_list = CardData.objects.filter(
                    Q(Series__id__icontains=3,Numbers__icontains=query2, Relase_date__icontains=query1,End_date__icontains=query3,Summ__icontains=query5)
                    )
                return object_list
            elif query6 == "notactiv":
                object_list = CardData.objects.filter(
                    Q(Series__id__icontains=3,Numbers__icontains=query2, Relase_date__icontains=query1,End_date__icontains=query3,Summ__icontains=query5,Status__in=("не активирована","не активирована"))
                )
                return object_list
            elif query6 == "activ":
                object_list = CardData.objects.filter(
                    Q(Series__id__icontains=3,Numbers__icontains=query2, Relase_date__icontains=query1,End_date__icontains=query3,Summ__icontains=query5,Status__in=("активирована", 'активирована'))
                )
                return object_list
        elif query == "allser":
            if query6 == "all":
                object_list = CardData.objects.filter(
                    Q(Series__Type__id__icontains=1,Numbers__icontains=query2, Relase_date__icontains=query1,End_date__icontains=query3,Summ__icontains=query5)
                    )
                return object_list
            elif query6 == "notactiv":
                object_list = CardData.objects.filter(
                    Q(Series__Type__id__icontains=1,Numbers__icontains=query2, Relase_date__icontains=query1,End_date__icontains=query3,Summ__icontains=query5,Status__in=("не активирована","не активирована"))
                )
                return object_list
            elif query6 == "activ":
                object_list = CardData.objects.filter(
                    Q(Series__Type__id__icontains=1,Numbers__icontains=query2, Relase_date__icontains=query1,End_date__icontains=query3,Summ__icontains=query5,Status__in=("активирована", 'активирована'))
                )
                return object_list


class SearchDebetResultsView(ListView):
    model = CardData
    template_name = 'bankcards/searchdebet_results.html'
 
    def get_queryset(self): # новый
        query = self.request.GET.get('debetcard')
        query1 = self.request.GET.get('debetnum')
        query2 = self.request.GET.get('debetdate1')
        query4 = self.request.GET.get('debetdate2')
        query5 = self.request.GET.get('debetsum')
        query6 = self.request.GET.get('debetact')
        if query == "Visa":
            if query6 == "allser":
                object_list = CardData.objects.filter(
                    Q(Series__id__icontains=2,Numbers__icontains=query1, Relase_date__icontains=query2,End_date__icontains=query4,Summ__icontains=query5)
                    )
                return object_list
            elif query6 == "notactiv":
                object_list = CardData.objects.filter(
                    Q(Series__id__icontains=2,Numbers__icontains=query1, Relase_date__icontains=query2,End_date__icontains=query4,Summ__icontains=query5,Status__in=("не активирована","не активирована"))
                )
                return object_list
            elif query6 == "activ":
                object_list = CardData.objects.filter(
                    Q(Series__id__icontains=2,Numbers__icontains=query1, Relase_date__icontains=query2,End_date__icontains=query4,Summ__icontains=query5,Status__in=("активирована", 'активирована'))
                )
                return object_list

        elif query == "MasterCard":
            if query6 == "allser":
                object_list = CardData.objects.filter(
                    Q(Series__id__icontains=4,Numbers__icontains=query1, Relase_date__icontains=query2,End_date__icontains=query4,Summ__icontains=query5)
                    )
                return object_list
            elif query6 == "notactiv":
                object_list = CardData.objects.filter(
                    Q(Series__id__icontains=4,Numbers__icontains=query1, Relase_date__icontains=query2,End_date__icontains=query4,Summ__icontains=query5,Status__in=("не активирована","не активирована"))
                )
                return object_list
            elif query6 == "activ":
                object_list = CardData.objects.filter(
                    Q(Series__id__icontains=4,Numbers__icontains=query1, Relase_date__icontains=query2,End_date__icontains=query4,Summ__icontains=query5,Status__in=("активирована", 'активирована'))
                )
                return object_list
        elif query == "all":
            if query6 == "allser":
                object_list = CardData.objects.filter(
                    Q(Series__Type__id__icontains=2,Numbers__icontains=query1, Relase_date__icontains=query2,End_date__icontains=query4,Summ__icontains=query5)
                    )
                return object_list
            elif query6 == "notactiv":
                object_list = CardData.objects.filter(
                    Q(Series__Type__id__icontains=2,Numbers__icontains=query1, Relase_date__icontains=query2,End_date__icontains=query4,Summ__icontains=query5,Status__in=("не активирована","не активирована"))
                )
                return object_list
            elif query6 == "activ":
                object_list = CardData.objects.filter(
                    Q(Series__Type__id__icontains=2,Numbers__icontains=query1, Relase_date__icontains=query2,End_date__icontains=query4,Summ__icontains=query5,Status__in=("активирована", 'активирована'))
                )
                return object_list


def Deadline(request):
    md = CardData.objects.all()
    if md.End_date - datetime.datetime.now() < 0:
        md.Status = 'активирована'
        md.save()
        return render(request,'bankcards/index.html')