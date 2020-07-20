from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

class Home(View):
    template_name = "solve_me_home.html"
    print(f'template name: {template_name}')
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})