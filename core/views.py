from django.views.generic import TemplateView, ListView
from core.models import Manager, Post


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        context['managers'] = Manager.objects.all()
        return context

