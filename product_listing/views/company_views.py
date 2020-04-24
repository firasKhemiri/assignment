"""This module has the Company model views."""
from django.views import generic

from product_listing.constants import Constants
from product_listing.models import Company
from product_listing.utils.views_utils import paginate_products, \
    get_company_products, order_products


class CompanyListView(generic.ListView):
    """This class get all companies and divide them throughout different pages."""
    model = Company
    template_name = 'other_templates/company_list.html'
    context_object_name = 'companies'
    paginate_by = 4


class SingleCompanyView(generic.DetailView):
    """This class Retrieves a single company and its products."""
    model = Company
    template_name = 'other_templates/company_products.html'
    context_object_name = 'company'

    def get_context_data(self, **kwargs):
        # Retrieve the company products which hasn't expired yet.
        company = Company.objects.get(pk=self.kwargs.get('pk'))
        products = get_company_products(company=company)
        context = super(SingleCompanyView, self).get_context_data(**kwargs)

        # Sort products if required.
        if self.request.method == 'GET' and 'order_by' in self.request.GET:
            if int(self.request.GET['order_by']) != Constants.DEFAULT:
                products = order_products(products=products,
                                          ordering=int(self.request.GET['order_by']))
                context['order_by'] = self.request.GET['order_by']
        else:
            context['order_by'] = Constants.DEFAULT

        # Divide the list of products to different pages, each page has 4 elements.
        products = paginate_products(products=products,
                                     page=self.request.GET.get('page', 1), elements_count=4)

        # Update context data and pass it to the template.
        context['products'] = products
        context['company'] = company
        return context
