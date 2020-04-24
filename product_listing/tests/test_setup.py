"""Setup dummy instances to be used in testing."""
from product_listing.tests.helpers import create_dummy_company,\
    create_dummy_category, create_dummy_product


def test_setup():
    """Test setup"""
    # Create companies
    company1 = create_dummy_company(1)
    company2 = create_dummy_company(2)
    company3 = create_dummy_company(3)
    # Company 4 does not have any products.
    create_dummy_company(4)

    # Create categories
    category1 = create_dummy_category(1)
    category2 = create_dummy_category(2)
    category3 = create_dummy_category(3)
    category4 = create_dummy_category(4)
    # Category 5 does not have any products.
    create_dummy_category(5)

    # Create products
    create_dummy_product(uuid=1, name="a", price=25, school=2, company=company2,
                         categories=(category1, category2),
                         end_date="09/09/2020")
    create_dummy_product(uuid=2, name="b", price=250, school=4, company=company1,
                         categories=(category2, category4),
                         end_date="10/09/2020")
    create_dummy_product(uuid=3, name="c", price=150, school=1, company=company3,
                         categories=(category3, category1), end_date="11/08/2020")
    create_dummy_product(uuid=4, name="d", price=50, school=1, company=company1,
                         categories=(category1, category2, category3), end_date="12/06/2020")
