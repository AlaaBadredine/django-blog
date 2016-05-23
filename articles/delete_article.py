from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy
from articles.models import Article

class AuthorDelete(DeleteView):
    model = Article
    success_url = reverse_lazy('articles_all')
    template_name = 'delete_article.html'


