from rest_framework.routers import SimpleRouter
from .views import CSVUploadView
router_input_csv = SimpleRouter()
router_input_csv.register('input_csv',CSVUploadView,basename='input_csv')