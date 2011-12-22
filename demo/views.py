# -*- coding: utf-8
import sys
import re
import datetime
from pprint import pprint

from django.conf import settings

from django.contrib.auth.views import logout_then_login
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required

from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext as _

from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.template.defaultfilters import slugify
from django.template.loader import render_to_string
from django.views.generic import ListView, DetailView, TemplateView

class MyListView(ListView):
    template_name = "demo/my_list.html"
    
    def get_queryset(self):
        pass


class MyDetailView(DetailView):
    template_name = "demo/my_detail.html"
    
    def get_queryset(self):
        pass
    
    def get_context_data(self, **kwargs):
        context = kwargs
        context['pk'] = self.kwargs['pk']
        return super(MyDetailView, self).get_context_data(**context)


my_list = login_required(MyListView.as_view())