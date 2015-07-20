from django.contrib import admin
from django.contrib.admin import AdminSite

from .models import Competitor, Category, ResourceCategory, ResourceFile, AdditionalInfo, Review, Platform, Installation, \
    RevenueEstimate, Product, Feature, TargetMarket, RevenueDataSource, GlobalMarket, VerticalMarket, Clients, Region


class MyAdminSite(AdminSite):
    site_header = 'Netsweeper Competitors Administration'


class RevenueEstimateInline(admin.TabularInline):
    model = RevenueEstimate
    extra = 1


class FeaturesInline(admin.TabularInline):
    model = Competitor.features.through
    extra = 1


class CategoriesInline(admin.TabularInline):
    model = Competitor.categories.through
    extra = 1


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


# Functions from here until CompetitorAdmin remove the specified model from the main menu on the admin site
# Users may still add and edit fields in the model through related models Clients, Competitors and Sales Resource Files
# Simplifies admin page for users
class RevenueEstimateAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class AdditionalInfoAdmin(admin.ModelAdmin):
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


class ResourceCategoriesAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class RegionAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


# Set fieldsets and inlines for create/edit competitor
class CompetitorAdmin(admin.ModelAdmin):
    fieldsets = [
        ('General Company Information', {'fields': ['name',
                                                    'acquired',
                                                    'acquired_by',
                                                    'merged_with',
                                                    'status',
                                                    'focus',
                                                    'url',
                                                    'number_of_categories',
                                                    'notes'],
                                         }),
        ('Partnerships', {'fields': ['channel_partners',
                                     'technology_partners',
                                     'oem_partners'],
                          }),
        ('Channels', {'fields': ['direct',
                                 'partners'],
                      }),
        ('Technologies', {'fields': ['saas',
                                     'appliance'],
                          }),
        ('SWOT Analysis', {'fields': ['strengths',
                                      'weaknesses'],
                           })
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


# Set fieldsets and inlines for create/edit Resource File
class ResourceFileAdmin(admin.ModelAdmin):
    list_display = ('document_name', 'resource_category')
    list_filter = ('resource_category',)

# Register models to the admin site
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
admin.site.register(ResourceCategory, ResourceCategoriesAdmin)
admin.site.register(ResourceFile, ResourceFileAdmin)
admin.site.register(AdditionalInfo, AdditionalInfoAdmin)
admin.site.register(Clients)
admin.site.register(Region, RegionAdmin)
