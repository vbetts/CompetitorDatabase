from django.contrib import admin

from .models import Competitor, Category, AdditionalInfo, Review, Platform, Installation, RevenueEstimate, Product, Feature, TargetMarket, CompetitorDataSource, RevenueDataSource, GlobalMarket, VerticalMarket

class CompanyDataSourceInline(admin.TabularInline):
    model = Competitor.dataSource.through
    extra = 1
class RevenueEstimateInline(admin.TabularInline):
    model = RevenueEstimate
    extra = 1
class FeaturesInline(admin.TabularInline):
    model = Competitor.features.through
    extra = 1
class CategoriesInline(admin.TabularInline):
    model = Competitor.categories.through
    extra=1
class GlobalMarketInline(admin.TabularInline):
    model = Competitor.globalMarket.through
    extra = 1
class VerticalMarketInline(admin.TabularInline):
    model = Competitor.verticalMarket.through
    extra = 1
class TargetMarketInline(admin.TabularInline):
    model = Competitor.target_Market.through
    extra = 1
class ProductInline(admin.StackedInline):
    model = Product
    extra = 1
class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1
class FileInline(admin.TabularInline):
    model = AdditionalInfo
    extra = 1

class CompetitorAdmin(admin.ModelAdmin):
    fieldsets = [
        ('General Company Information', {'fields' : ['name',
                                                     'acquired',
                                                     'acquired_by',
                                                     'merged_with',
                                                     'status',
                                                     'focus',
                                                     'url',
                                                     'number_of_categories',
                                                     'notes']}),
        ('Partnerships', {'fields' : ['channel_partners',
                                      'technology_partners',
                                      'oem_partners']}),
        ('Channels', {'fields' : ['direct',
                                  'partners']}),
        ('Technologies', {'fields' : ['saas',
                                      'appliance']}),
        ('SWOT Analysis', {'fields' : ['strengths',
                                       'weaknesses']})
    ]
    inlines = [
        GlobalMarketInline,
        VerticalMarketInline,
        TargetMarketInline,
        CategoriesInline,
        FeaturesInline,
        ProductInline,
        ReviewInline,
        RevenueEstimateInline,
        CompanyDataSourceInline,
        FileInline,
        ]
    exclude = ('dataSource',)
    list_display = ('name', 'last_updated')
    list_filter = ('last_updated',)
    search_fields = ['name',
                     'prodName',
                     'focus',
                     'status',
                     'prodStatus',
                     'strengths',
                     'weaknesses']

admin.site.register(Competitor, CompetitorAdmin)
admin.site.register(RevenueEstimate)
admin.site.register(RevenueDataSource)
admin.site.register(VerticalMarket)
admin.site.register(GlobalMarket)
admin.site.register(Feature)
admin.site.register(CompetitorDataSource)
admin.site.register(TargetMarket)
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Platform)
admin.site.register(Installation)
admin.site.register(Category)