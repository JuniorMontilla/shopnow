from django.conf.urls.defaults import  patterns,url

urlpatterns = patterns('shopnow.apps.product.views',
        url(r'^add/product$', 'view_product', name='product_view')
)
