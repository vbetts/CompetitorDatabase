from django import forms
from .models import Competitor, Feature, Category, GlobalMarket, VerticalMarket


#for querying directly from Competitor table
class SelectCompetitor(forms.Form):
    GRAPH_CHOICES = ('column', 'column'), ('line', 'line'), ('scatter', 'scatter')

    selection = forms.ModelMultipleChoiceField(queryset=Competitor.objects.all().order_by('name'),
                                               label="Filter by Company",
                                               required=False,
                                               widget=forms.SelectMultiple(attrs={'class': "form-control", 'id': "competitorName",}))
    graphType = forms.ChoiceField(choices=(GRAPH_CHOICES),
                                  label="Choose a type of graph to represent your data",
                                  required=False,
                                  widget=forms.Select(attrs={'class': "form-control",
                                                             'id': "graphType",}))

#Show only competitors with vertical market values in the competitor selection field
class VerticalMarketForm(forms.Form):
    GRAPH_CHOICES = ('column', 'column'), ('line', 'line'), ('scatter', 'scatter')

    selection = forms.ModelMultipleChoiceField(queryset=Competitor.objects.distinct().filter(verticalMarket__isnull=False).order_by('name'),
                                               label="Filter by Company",
                                               required=False,
                                               widget=forms.SelectMultiple(attrs={'class': "form-control", 'id': "competitorName",}))

    graphType = forms.ChoiceField(choices=(GRAPH_CHOICES),
                                  label="Choose a type of graph to represent your data",
                                  required=False,
                                  widget=forms.Select(attrs={'class': "form-control",
                                                             'id': "graphType",}))

    verticalMarketSelect = forms.ModelMultipleChoiceField(queryset=VerticalMarket.objects.all().order_by('name'),
                                                        label="Filter by Market",
                                                        required=False,
                                                        widget=forms.SelectMultiple(attrs={'class': "form-control",
                                                                                           'id': "marketName",}))

#Show only competitors with global market values in the selection field
class GlobalMarketForm(forms.Form):
    GRAPH_CHOICES = ('column', 'column'), ('line', 'line'), ('scatter', 'scatter')

    selection = forms.ModelMultipleChoiceField(queryset=Competitor.objects.distinct().filter(globalMarket__isnull=False).order_by('name'),
                                               label="Filter by Company",
                                               required=False,
                                               widget=forms.SelectMultiple(attrs={'class': "form-control", 'id': "competitorName",}))
    graphType = forms.ChoiceField(choices=(GRAPH_CHOICES),
                                  label="Choose a type of graph to represent your data",
                                  required=False,
                                  widget=forms.Select(attrs={'class': "form-control",
                                                             'id': "graphType",}))
    globalMarketSelect = forms.ModelMultipleChoiceField(queryset=GlobalMarket.objects.all().order_by('name'),
                                                        label="Filter by Market",
                                                        required=False,
                                                        widget=forms.SelectMultiple(attrs={'class': "form-control",
                                                                                           'id': "marketName",}))


#Show only competitors with category data in the selection field
class CategoriesForm(forms.Form):
    selection = forms.ModelMultipleChoiceField(queryset=Competitor.objects.distinct().filter(categories__isnull = False).order_by('name'),
                                               label="Select one or more companies to view their filtering categories",
                                               required=True,
                                               widget=forms.SelectMultiple(attrs={'class': "form-control", 'id': "competitorName", 'required': "true"}))

    categorySelect = forms.ModelMultipleChoiceField(queryset=Category.objects.all().order_by('name'),
                                                    label="Filter by Category",
                                                    required=False,
                                                    widget=forms.SelectMultiple(attrs={'class': "form-control",
                                                                                       'id': "categoryName",}))

#Show only competitors with feature data in the selection field
class FeaturesForm(forms.Form):
    selection = forms.ModelMultipleChoiceField(queryset=Competitor.objects.distinct().filter(features__isnull=False).order_by('name'),
                                               label="Select one or more companies to view their product features",
                                               required=True,
                                               widget=forms.SelectMultiple(attrs={'class': "form-control", 'id': "competitorName", 'required': "true"}))

    featureSelect = forms.ModelMultipleChoiceField(queryset=Feature.objects.all().order_by('name'),
                                                    label="Filter by Feature",
                                                    required=False,
                                                    widget=forms.SelectMultiple(attrs={'class': "form-control",
                                                                                       'id': "featureName",}))

class ProductDetailsForm(forms.Form):
    INFO_CHOICES = ('Product Details', 'Product Details'), ('Competitor Partnerships', 'Competitor Partnerships')

    infoSelect = forms.ChoiceField(choices=(INFO_CHOICES),
                                  label="Choose the type of data you would like to view",
                                  required=True,
                                  widget=forms.Select(attrs={'class': "form-control",
                                                             'id': "infoType",}))
    selection = forms.ModelMultipleChoiceField(queryset=Competitor.objects.all().order_by('name'),
                                               label="Select one or more companies to view their product features",
                                               required=False,
                                               widget=forms.SelectMultiple(attrs={'class': "form-control", 'id': "competitorName", 'required': "true"}))

class PrintPageForm(forms.Form):
    selection = forms.ModelChoiceField(queryset=Competitor.objects.all().order_by('name'),
                                               label="Select a competitor to generate a datasheet",
                                               required=True,
                                               widget=forms.Select(attrs={'class': "form-control", 'required': "true", 'style': "width: 250px"}))
    showCategories = forms.BooleanField(label="Show Competitor Web Filtering Categories", required=False)
    showPartners = forms.BooleanField(label="Show Competitor Partnerships", required=False)
