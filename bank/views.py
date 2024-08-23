from django.http.response import HttpResponse
from django.shortcuts import render

from bank.forms import PercentForm
from bank.services.utils import annuitet, proper_annuitet


def percent_result(request):
    if request.method == "POST":
        form = PercentForm(data=request.POST)
        if form.is_valid():
            money = form.cleaned_data.get("money")
            percent = form.cleaned_data.get("percent")
            year = form.cleaned_data.get("year")

            result = proper_annuitet(annuitet(money, percent, year))
            return render(request, "main.html", {"form": form, "res": result})

        return HttpResponse("<h4>Неверные данные, попробуйте еще раз</h4>")

    return render(request, "main.html", {"form": PercentForm()})
