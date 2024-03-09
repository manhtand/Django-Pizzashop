from django.views.generic import TemplateView
from .models import Pizza
from django.shortcuts import render, redirect
from django.http import JsonResponse
import json


class SpeisekarteView(TemplateView):
    template_name = 'pages/speisekarte.html'
    model = Pizza

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pizzas'] = self.model.objects.all()
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        try:
            return JsonResponse({'success': True})
        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
