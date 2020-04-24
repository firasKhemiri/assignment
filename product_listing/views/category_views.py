"""This module has the Category model views."""
from django.views import generic

from product_listing.constants import Constants
from product_listing.models import Category
from product_listing.utils.views_utils import get_category_products,\
    paginate_products, order_products


class CategoryListView(generic.ListView):
    """Get all categories and divide them throughout different pages."""
    model = Category
    template_name = 'other_templates/category_list.html'
    context_object_name = 'categories'


class SingleCategoryView(generic.DetailView):
    """Retrieve the data of a specific category."""
    model = Category
    template_name = 'other_templates/category_products.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        # Retrieve the category products which hasn't expired yet.
        context = super(SingleCategoryView, self).get_context_data(**kwargs)
        category = Category.objects.get(pk=self.kwargs.get('pk'))
        products = get_category_products(category=category)

        # Sort products if required.
        if 'order_by' in self.request.GET:
            if int(self.request.GET['order_by']) != Constants.DEFAULT:
                products = order_products(products=products,
                                          ordering=int(self.request.GET['order_by']))
                context['order_by'] = self.request.GET['order_by']
        else:
            context['order_by'] = Constants.DEFAULT

        # Divide the list of products to different pages, each page has 4 elements.
        page = self.request.GET.get('page', 1)
        products = paginate_products(products=products, page=page, elements_count=4)

        # Update context data and pass it to the template.
        context['products'] = products
        context['category'] = category
        return context
