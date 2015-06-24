from django.contrib import admin
from django.contrib.admin import AdminSite

from .models import Competitor, Category, AdditionalInfo, Review, Platform, Installation, RevenueEstimate, Product, Feature, TargetMarket, RevenueDataSource, GlobalMarket, VerticalMarket

class MyAdminSite(AdminSite):
    site_header='Netsweeper Competitors Administration'


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
    verbose_name = "Target Market"
    verbose_name_plural = "Target Markets"

class ProductInline(admin.StackedInline):
    model = Product
    extra = 1

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1

class FileInline(admin.TabularInline):
    model = AdditionalInfo
    extra = 1

class RevenueEstimateAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

class RevenueDataAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

class VerticalMarketAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}
class GlobalMarketAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}
class FeatureAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}
class TargetMarketAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}
class ProductAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}
class ReviewAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}
class PlatformAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}
class InstallationAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}
class CategoryAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

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
                                                     'notes'],
                                         'classes' : ('suit-tab', 'suit-tab-general',)}),
        ('Partnerships', {'fields' : ['channel_partners',
                                      'technology_partners',
                                      'oem_partners'],
                          'classes' : ('suit-tab', 'suit-tab-partner',)}),
        ('Channels', {'fields' : ['direct',
                                  'partners'],
                      'classes' : ('suit-tab', 'suit-tab-channel',)}),
        ('Technologies', {'fields' : ['saas',
                                      'appliance'],
                          'classes' : ('suit-tab', 'suit-tab-technologies',)}),
        ('SWOT Analysis', {'fields' : ['strengths',
                                       'weaknesses'],
                           'classes' : ('suit-tab', 'suit-tab-swot',)})
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
admin.site.register(RevenueEstimate, RevenueEstimateAdmin)
admin.site.register(RevenueDataSource, RevenueDataAdmin)
admin.site.register(VerticalMarket, VerticalMarketAdmin)
admin.site.register(GlobalMarket, GlobalMarketAdmin)
admin.site.register(Feature, FeatureAdmin)
admin.site.register(TargetMarket, TargetMarketAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Platform, PlatformAdmin)
admin.site.register(Installation, InstallationAdmin)
admin.site.register(Category, CategoryAdmin)