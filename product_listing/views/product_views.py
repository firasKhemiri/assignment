"""This module has the Product model views."""
from datetime import datetime, timezone

from django.views import generic

from product_listing.constants import Constants
from product_listing.models.product import Product
from product_listing.utils.views_utils import order_products, paginate_products


class ProductListView(generic.ListView):
    """This class Retrieves all products."""
    template_name = 'product_list.html'
    context_object_name = 'products'
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)

        # Get only non-expired products.
        products = Product.objects.filter(end_date__gt=datetime.now(tz=timezone.utc))

        # Sort products if required.
        if 'order_by' in self.request.GET:
            if int(self.request.GET['order_by']) != Constants.DEFAULT:
                products = order_products(products=products,
                                          ordering=int(self.request.GET['order_by']))
                context['order_by'] = self.request.GET['order_by']
            else:
                context['order_by'] = Constants.DEFAULT
        else:
            context['order_by'] = Constants.DEFAULT

        # Divide the list of products to different pages, each page has 4 elements.
        page = self.request.GET.get('page', 1)
        products = paginate_products(products=products, page=page, elements_count=4)

        context['products'] = products
        return context


# Retrieve a single product.
class SingleProductView(generic.DetailView):
    """This class Retrieve a single products."""
    model = Product
    template_name = 'single_product.html'
    context_object_name = 'product'
