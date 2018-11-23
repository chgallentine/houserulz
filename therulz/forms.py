# -*- coding: utf-8 -*-
# @Author: Charlie Gallentine
# @Date:   2018-06-12 21:12:27
# @Last Modified by:   Charlie Gallentine
# @Last Modified time: 2018-06-12 21:12:38
from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)