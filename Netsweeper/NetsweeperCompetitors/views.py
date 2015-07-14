from django.shortcuts import render, HttpResponseRedirect
from django.db.models import Avg
from .models import Competitor, GlobalMarketShare, GlobalMarket, Product, CompetitorCategories, Category, \
    VerticalMarket, VerticalMarketShare, CompanyFeatures, Feature, AdditionalInfo, ResourceCategory, \
    ResourceFile
from .forms import SelectCompetitor, CategoriesForm, FeaturesForm, VerticalMarketForm, GlobalMarketForm, \
    ProductDetailsForm, PrintPageForm, LoginForm, CompetitorDocsForm, SalesDocsForm, ChangePasswordForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import Netsweeper.settings as settings



"""Build market share data"""
def build_market_share(shares, competitors):
    shareDict = {}
    for item in shares:
        shareDict[item.competitor.id] = item.share
    for c in competitors:
        if not c['id'] in shareDict:
            shareDict[c['id']] = 0
    return shareDict

"""Query global market table and return values for use in template"""
def build_globalmarket_display(competitors, marketObject=False):
    market_display = {}

    if marketObject:
        marketNames = GlobalMarket.objects.filter(pk__in=marketObject).values_list('name', flat=True)
    else:
        marketNames = GlobalMarket.objects.distinct().values_list('name', flat=True)

    for market in marketNames:
        shares = GlobalMarketShare.objects.filter(global_market__name=market)
        marketshare = build_market_share(shares, competitors)
        market_display[market] = marketshare
    return market_display

"""Query vertical market table and return values for use in template"""
def build_verticalmarket_display(competitors, marketObject=False):
    market_display = {}

    if marketObject:
        marketNames = VerticalMarket.objects.filter(pk__in=marketObject).values_list('name', flat=True)
    else:
        marketNames = VerticalMarket.objects.distinct().values_list('name', flat=True)

    for market in marketNames:
        shares = VerticalMarketShare.objects.filter(vertical_market__name=market)
        marketshare = build_market_share(shares, competitors)
        market_display[market] = marketshare
    return market_display

def login_view(request):
    form = LoginForm(label_suffix='')

    message = ''

    if request.method == 'POST':
        form = LoginForm(request.POST, label_suffix='')
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
                else:
                    message = 'This account has been disabled.'
            else:
                message = 'The username and password are incorrect'
    return render(request, 'NetsweeperCompetitors/login.html', {'form' : form,
                                                                'message' : message})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/')

@login_required
def index(request):
    return render(request, 'NetsweeperCompetitors/index.html')

"""Filter results on the global market template"""
@login_required
def globalmarket(request):
    form = GlobalMarketForm(label_suffix="")
    graphType = 'column'
    message = ''

    competitor_selection = Competitor.objects.distinct().filter(globalMarket__isnull=False).values('id', 'name').order_by('name')
    market_display = build_globalmarket_display(competitor_selection)

    """On form submission, sort companies and show only selected"""
    if request.method == 'POST':
        form = GlobalMarketForm(request.POST, label_suffix="")
        if form.is_valid():

            graphType = form.cleaned_data.get('graphType')
            """Retrieve values from form and pass to build_globalmarket_display()"""
            if form.cleaned_data.get('selection').count() != 0:
                companyObject = form.cleaned_data.get('selection')
                competitor_selection = Competitor.objects.filter(pk__in=companyObject).values('id', 'name').order_by('name')
                market_display = build_globalmarket_display(competitor_selection)

            if form.cleaned_data.get('globalMarketSelect') != None:
                globalMarketObject = form.cleaned_data.get('globalMarketSelect')
                market_display = build_globalmarket_display(competitor_selection, globalMarketObject)

        else:
            message = 'There was an error with the form. Please try again.'
            return render(request, 'NetsweeperCompetitors/globalmarket.html', {'form': form,
                                                                               'graph': graphType,
                                                                               'message': message,
                                                                               'competitor': competitor_selection,
                                                                               'market': market_display})

    return render(request, 'NetsweeperCompetitors/globalmarket.html', {'form': form,
                                                                       'graph': graphType,
                                                                       'message': message,
                                                                       'competitor': competitor_selection,
                                                                       'market' : market_display})

"""Data for vertical markets"""
@login_required
def verticalmarket(request):
    form = VerticalMarketForm(label_suffix="")
    graphType = 'column'
    message = ''

    competitor_selection = Competitor.objects.distinct().filter(verticalMarket__isnull=False).values('id', 'name').order_by('name')
    market_display = build_verticalmarket_display(competitor_selection)

    """On form submission, filter and show only selected competitors"""
    if request.method == 'POST':
        form = VerticalMarketForm(request.POST, label_suffix="")
        if form.is_valid():

            graphType = form.cleaned_data.get('graphType')

            if form.cleaned_data.get('selection').count() != 0:
                companyObject = form.cleaned_data.get('selection')
                competitor_selection = Competitor.objects.filter(pk__in=companyObject).values('id', 'name').order_by('name')
                market_display = build_verticalmarket_display(competitor_selection)

            if form.cleaned_data.get('verticalMarketSelect').count() != 0:
                verticalMarketObject = form.cleaned_data.get('verticalMarketSelect')
                market_display = build_verticalmarket_display(competitor_selection, verticalMarketObject)

        else:
            message = 'There was an error with the form. Please try again.'
            return render(request, 'NetsweeperCompetitors/verticalmarket.html', {'form': form,
                                                                                 'graph': graphType,
                                                                                 'message': message,
                                                                                 'competitor': competitor_selection,
                                                                                 'market': market_display})

    return render(request, 'NetsweeperCompetitors/verticalmarket.html', {'form': form,
                                                                         'graph': graphType,
                                                                         'message': message,
                                                                         'competitor': competitor_selection,
                                                                         'market': market_display})

"""View and filter results on the channels template"""
@login_required
def channels(request):
    channelValues = Competitor.objects.all().order_by('name').values('id', 'name', 'direct', 'partners') \
        .exclude(direct=0, partners=0)
    form = SelectCompetitor(label_suffix="")
    graphType = 'column'
    companyIds = []
    message = ''

    if request.method == 'POST':
        form = SelectCompetitor(request.POST, label_suffix="")
        if form.is_valid():
            graphType = form.cleaned_data.get('graphType')
            if form.cleaned_data.get('selection').count() != 0:
                companyObject = form.cleaned_data.get('selection')
                channelValues = Competitor.objects.filter(pk__in= companyObject).order_by('name').values('id', 'name', 'direct', 'partners')

        else:
            message = 'There was an error with the form. Please try again.'
            return render(request, 'NetsweeperCompetitors/channels.html', {'channelValues': channelValues,
                                                                           'form': form,
                                                                           'graph': graphType,
                                                                           'company': companyIds,
                                                                           'message': message})


    return render(request, 'NetsweeperCompetitors/channels.html', {'channelValues': channelValues,
                                                                   'form': form,
                                                                   'graph': graphType,
                                                                   'company': companyIds,
                                                                   'message': message})

"""View and filter results on the technology template"""
@login_required
def technology(request):
    technologies = Competitor.objects.all().order_by('name').values('id', 'name', 'appliance', 'saas').exclude(appliance=0, saas=0)
    form = SelectCompetitor(label_suffix="")
    graphType = 'column'
    companyIds = []
    message = ''

    if request.method == 'POST':
        form = SelectCompetitor(request.POST, label_suffix="")
        if form.is_valid():
            graphType = form.cleaned_data.get('graphType')
            if form.cleaned_data.get('selection').count() != 0:
                companyObject = form.cleaned_data.get('selection')
                technologies = Competitor.objects.filter(pk__in= companyObject).order_by('name').values('id', 'name', 'appliance', 'saas')

        else:
            message = 'There was an error with the form. Please try again.'
            return render(request, 'NetsweeperCompetitors/verticalmarket.html', {'technologies': technologies,
                                                                                 'form': form,
                                                                                 'graph': graphType,
                                                                                 'company': companyIds,
                                                                                 'message': message})
    return render(request, 'NetsweeperCompetitors/technology.html', {'technologies': technologies,
                                                                     'form': form,
                                                                     'graph': graphType,
                                                                     'company': companyIds,
                                                                     'message': message})

"""View and filter results on the revenue template"""
@login_required
def revenue(request):
    revenue = Competitor.objects.values('id', 'name').annotate(total_rev=Avg('revenueestimate__totalRevenue'), filter_rev=Avg('revenueestimate__filteringRevenue')).exclude(total_rev__icontains= 'None', filter_rev__icontains='None').order_by('name')
    form = SelectCompetitor(label_suffix="")
    graphType = 'column'
    companyIds = []
    message = ''

    if request.method == 'POST':
        form = SelectCompetitor(request.POST, label_suffix="")
        if form.is_valid():
            graphType = form.cleaned_data.get('graphType')
            if form.cleaned_data.get('selection').count() != 0:
                companyObject = form.cleaned_data.get('selection')
                revenue = Competitor.objects.filter(pk__in= companyObject).values('id', 'name').annotate(total_rev=Avg('revenueestimate__totalRevenue'), filter_rev=Avg('revenueestimate__filteringRevenue')).order_by('name')
                for item in revenue:
                    if item['total_rev']is None and item['filter_rev'] is None:
                        item['total_rev'] = 0
                        item['filter_rev'] = 0
                        message = 'One or more selected companies do not have any revenue data. Data will appear as a blank graph.'

        else:
            message = 'There was an error with the form. Please try again.'
            return render(request, 'NetsweeperCompetitors/revenue.html', {'revenue': revenue,
                                                                          'form': form,
                                                                          'graph': graphType,
                                                                          'company': companyIds,
                                                                          'message': message})

    return render(request, 'NetsweeperCompetitors/revenue.html', {'revenue': revenue,
                                                                  'form': form,
                                                                  'graph': graphType,
                                                                  'company': companyIds,
                                                                  'message': message})

"""View and filter reults on the features template"""
@login_required
def features(request):
    form = FeaturesForm(label_suffix="")
    companyIds = []
    features = {}
    message = ''
    competitor_selection = {}
    feature_names={}
    showDetails = False
    only_feature_selected = False



    if request.method == 'POST':
        form = FeaturesForm(request.POST, label_suffix="")
        if form.is_valid():
            if form.cleaned_data.get('selection').count() != 0:
                companyObject = form.cleaned_data.get('selection')
                competitor_selection = Competitor.objects.filter(pk__in=companyObject).values('id', 'name').order_by('name')
                for c in competitor_selection:
                    features[c['name']] = CompanyFeatures.objects.filter(competitor__pk=c['id']).values('featureSpecs', 'feature__name', 'competitor')

            elif form.cleaned_data.get('selection').count() == 0 and form.cleaned_data.get('feature_select') != 0:

                competitor_selection = Competitor.objects.all()
                featureObject = form.cleaned_data.get('featureSelect')

                for f in featureObject:
                    features[f.name] = Competitor.objects.filter(features=f)

                only_feature_selected = True

            if form.cleaned_data.get('featureSelect').count() != 0:
                featureObject = form.cleaned_data.get('featureSelect')
                feature_names = Feature.objects.filter(pk__in=featureObject).values('name')
            elif form.cleaned_data.get('featureSelect').count() == 0:
                feature_names = Feature.objects.values('name')

            if form.cleaned_data.get('showFeatureDetails'):
                showDetails = True

        else:
            message = 'There was an error with the form. Please try again.'
            return render(request, 'NetsweeperCompetitors/features.html', {'form': form,
                                                                           'company': companyIds,
                                                                           'message': message,
                                                                           'features': features,
                                                                           'feature_names': feature_names,
                                                                           'competitor': competitor_selection,
                                                                           'showDetails': showDetails,
                                                                           'only_feature': only_feature_selected})

    return render(request, 'NetsweeperCompetitors/features.html', {'form': form,
                                                                   'company': companyIds,
                                                                   'message': message,
                                                                   'features': features,
                                                                   'feature_names': feature_names,
                                                                   'competitor': competitor_selection,
                                                                   'showDetails': showDetails,
                                                                   'only_feature': only_feature_selected})

"""View and filter esults on the categories template"""
@login_required
def categories(request):
    form = CategoriesForm(label_suffix="")
    companyIds = []
    categories = {}
    message = ''
    competitor_selection = {}
    category_names={}

    if request.method == 'POST':
        form = CategoriesForm(request.POST, label_suffix="")
        if form.is_valid():
            if form.cleaned_data.get('selection').count() != 0:
                companyObject = form.cleaned_data.get('selection')
                competitor_selection = Competitor.objects.filter(pk__in=companyObject).values('id', 'name').order_by('name')
                for c in competitor_selection:
                    categories[c['name']] = CompetitorCategories.objects.filter(competitor__pk=c['id']).values('details', 'category__name', 'competitor')

            if form.cleaned_data.get('categorySelect').count() != 0:
                categoryObject = form.cleaned_data.get('categorySelect')
                category_names = Category.objects.filter(pk__in=categoryObject).values('name')
            else:
                category_names = Category.objects.all().values('name')

        else:
            message = 'There was an error with the form. Please try again.'
            return render(request, 'NetsweeperCompetitors/revenue.html', {'form': form,
                                                                          'company': companyIds,
                                                                          'message': message,
                                                                          'categories': categories,
                                                                          'category_names': category_names,
                                                                          'competitor': competitor_selection})

    return render(request, 'NetsweeperCompetitors/categories.html', {'form': form,
                                                                     'company': companyIds,
                                                                     'message': message,
                                                                     'categories': categories,
                                                                     'category_names': category_names,
                                                                     'competitor': competitor_selection})

@login_required
def details(request):
    form = ProductDetailsForm(label_suffix="")
    competitor_selection = Competitor.objects.all()
    products = Product.objects.all()
    partners = False
    message = ''

    if request.method == 'POST':
        form = ProductDetailsForm(request.POST, label_suffix="")
        if form.is_valid():
            if form.cleaned_data.get('selection').count() != 0:
                companyObject = form.cleaned_data.get('selection')
                competitor_selection = Competitor.objects.filter(pk__in=companyObject).order_by('name')
            if form.cleaned_data.get('infoSelect') == 'Competitor Partnerships':
                partners = True
            else:
                partners = False
        else:
            message = 'There was an error with the form. Please try again.'
            return render(request, 'NetsweeperCompetitors/details.html',{'form': form,
                                                                         'competitors' : competitor_selection,
                                                                         'products' : products,
                                                                         'partners' : partners,
                                                                         'message': message})

    return render(request, 'NetsweeperCompetitors/details.html',{'form': form,
                                                                 'competitors' : competitor_selection,
                                                                 'products' : products,
                                                                 'partners' : partners,
                                                                 'message': message})

@login_required
def printpage(request):
    form = PrintPageForm(label_suffix="")
    competitor_selection = ''
    products = []
    showCategories = False
    showPartners = False
    message = ''

    if request.method == 'POST':
        form = PrintPageForm(request.POST, label_suffix="")
        if form.is_valid():
            showCategories = form.cleaned_data.get('showCategories')
            showPartners = form.cleaned_data.get('showPartners')
            if form.cleaned_data.get('selection'):
                companyObject = form.cleaned_data.get('selection')
                competitor_selection = Competitor.objects.get(pk=companyObject.id)
                products = Product.objects.filter(competitor__name= competitor_selection.name)
        else:
            message = 'There was an error with the form. Please try again.'
            return render(request, 'NetsweeperCompetitors/printpage.html', {'form': form,
                                                                            'competitor': competitor_selection,
                                                                            'products': products,
                                                                            'showCategories': showCategories,
                                                                            'showPartners': showPartners,
                                                                            'message': message})

    return render(request, 'NetsweeperCompetitors/printpage.html', {'form': form,
                                                                    'competitor': competitor_selection,
                                                                    'products': products,
                                                                    'showCategories': showCategories,
                                                                    'showPartners': showPartners,
                                                                    'message': message})

@login_required
def competitordocs(request):
    files = {}
    form = CompetitorDocsForm(label_suffix="")
    message = ''

    selection = Competitor.objects.filter(additionalinfo__isnull=False).distinct()

    if request.method == 'POST':
        form = CompetitorDocsForm(request.POST, label_suffix="")
        if form.is_valid():
            selection = form.cleaned_data.get('selection')

        else:
            message = 'There was an error with the form. Please try again.'

    file_list_competitors = AdditionalInfo.objects.filter(competitor__in=selection)
    for competitor in file_list_competitors:
        files[competitor.competitor.name] = AdditionalInfo.objects.filter(competitor__name=competitor.competitor.name)

    return render(request, 'NetsweeperCompetitors/competitordocs.html', {'files' : files,
                                                                         'form' : form,
                                                                         'message' : message})

@login_required
def salesdocs(request):
    files = {}
    form = SalesDocsForm(label_suffix="")
    categories = ResourceCategory.objects.all().order_by('name')
    message = ''

    if request.method == 'POST':
        form = SalesDocsForm(request.POST, label_suffix="")
        if form.is_valid():
            categories = form.cleaned_data.get('selection')
        else:
            message = 'There was an error with the form. Please try again.'

    for category in categories:
        files[category.name] = ResourceFile.objects.filter(resource_category__name = category.name)

    return render(request, 'NetsweeperCompetitors/salesdocs.html', {'files' : files,
                                                                    'form' : form,
                                                                    'message' : message})

@login_required
def changepassword(request):
    form = ChangePasswordForm(label_suffix="")
    message = ''
    success = False

    if request.method == 'POST':
        form = ChangePasswordForm(request.POST, label_suffix="")
        user = request.user
        if form.is_valid():
            old_password = form.cleaned_data.get('old_password')
            new_password = form.cleaned_data.get('new_password')
            confirm_password = form.cleaned_data.get('confirm_password')

            if user.check_password(old_password):
                if len(new_password) == 0 or new_password == '' or new_password == ' ':
                    message = 'You have not entered a valid new password. Please try again'
                elif new_password != confirm_password:
                    message = 'New password does not match the confirmed password. Please try again'
                elif len(new_password) > 0 and new_password == confirm_password:
                    user.set_password(new_password)
                    user.save()
                    message = 'Password successfully changed.'
                    success = True
            else:
                message = 'You have entered your old password incorrectly. Please try again.'

    return render(request, 'NetsweeperCompetitors/changepassword.html', {'form' : form,
                                                                         'message' : message,
                                                                         'success' : success})