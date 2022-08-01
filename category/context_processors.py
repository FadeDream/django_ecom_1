from category.models import Category


# bellow function should be added on settings
def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)
