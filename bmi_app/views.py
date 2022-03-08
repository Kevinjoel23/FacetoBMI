from django.shortcuts import render
from . import program
import cv2
import numpy as np
import os
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from bmi_app.forms import ImageForm
from django.views.generic import DetailView
from bmi_app.models import BMI_model
import sys
import joblib
sys.modules['sklearn.externals.joblib'] = joblib


# Create your views here.

class Image(TemplateView):
    form = ImageForm
    template_name = 'image.html'

    def post(self, request, *args, **kwargs):
        form = ImageForm(request.POST, request.FILES)

        base_dir = os.path.dirname(os.path.abspath(__file__))
        model_path = os.path.join(base_dir, 'bmi_predictor.model')
        bmi_model = joblib.load(model_path)

        if form.is_valid():
            obj = form.save()
            pred_bmi = program.predict_BMI(obj.image, bmi_model)
            pred_fat = program.predict_fat(pred_bmi, obj.gender, obj.age)

            obj.bmi = pred_bmi
            obj.fat = pred_fat
            obj.save()

            return HttpResponseRedirect(reverse_lazy('result_display', kwargs={'pk': obj.id}))

        context = self.get_context_data(form=form)
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class ResultDisplay(DetailView):
    model = BMI_model
    template_name = 'result_display.html'
    context_object_name = 'context'
