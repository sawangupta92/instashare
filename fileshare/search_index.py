from haystack import indexes
from sharing.models import employee
class employeeIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	author = indexes.CharField(model_attr='address')
	def get_model(self):
        return employee
    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())
