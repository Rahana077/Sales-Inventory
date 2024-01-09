from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
app_name = 'transactions'
from .views import (
    PurchaseListView,
    PurchaseDetailView,
    PurchaseCreateView,
    PurchaseUpdateView,
    PurchaseDeleteView,
    SaleListView,
    SaleDetailView,
    # SaleCreateView,
    SaleUpdateView,
    # SaleDeleteView,
)

urlpatterns = [
    path('purchases/', PurchaseListView.as_view(), name="purchaseslist"),
    path('purchase/<slug:slug>/', PurchaseDetailView.as_view(), name='purchase-detail'),
    path('new-purchase/', PurchaseCreateView.as_view(), name='purchase-create'),
    path('purchase/<int:pk>/update/', PurchaseUpdateView.as_view(), name='purchase-update'),
    path('purchase/<int:pk>/delete/', PurchaseDeleteView.as_view(), name='purchase-delete'),
    path('sales/',SaleListView.as_view(), name="saleslist"),
    path('sale/<int:pk>/', SaleDetailView.as_view(), name='sale-detail'),
    # path('new-sale/', SaleCreateView.as_view(), name='sale-create'),  #sales page
    path('sale/<slug:slug>/update/', SaleUpdateView.as_view(), name='sale-update'),
    # path('sale/<slug:slug>/', SaleDeleteView.as_view(), name='sale-delete'),
    path('billing_details/',views.billing_details,name='billing_details'),#sales page
    path('add_item/<slug:slug>/',views.add_item,name='add_item'),
    path('delete_bill/',views.delete_bill_single,name='delete_bill_single'),
    path('print_bill/',views.generate_bill,name='print_bill'),
    path('sale-delete/<int:pk>/',views.sale_delete,name='sale-delete'),

 

]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)