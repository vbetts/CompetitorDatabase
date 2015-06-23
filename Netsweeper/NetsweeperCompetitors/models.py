from django.db import models

# Create your models here.

class CompetitorDataSource(models.Model):
    name = models.CharField("Data Source Name",
                            max_length=255,
                            blank=False)
    def __str__(self):
        return self.name

class Feature(models.Model):
    name = models.CharField(max_length=255, blank=False)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255, blank=False)
    def __str__(self):
        return self.name

class GlobalMarket(models.Model):
    name = models.CharField(max_length=255, blank=False)
    def __str__(self):
        return self.name

class VerticalMarket(models.Model):
    name = models.CharField(max_length=255, blank=False)
    def __str__(self):
        return self.name

class TargetMarket(models.Model):
    name=models.CharField(max_length=255, blank=False)
    def __str__(self):
        return self.name

class Competitor(models.Model):
    dataSource = models.ManyToManyField(CompetitorDataSource)
    target_Market = models.ManyToManyField(TargetMarket)
    features = models.ManyToManyField(Feature, through='CompanyFeatures')
    categories = models.ManyToManyField(Category, through='CompetitorCategories')
    globalMarket = models.ManyToManyField(GlobalMarket, through='GlobalMarketShare')
    verticalMarket = models.ManyToManyField(VerticalMarket, through='VerticalMarketShare')
    name = models.CharField("Company Name",
                            max_length=255,
                            blank=False)
    acquired = models.BooleanField("Acquired")
    acquired_by = models.CharField(max_length=255, blank=True)
    merged_with = models.CharField(max_length=255, blank=True)
    channel_partners = models.TextField("Channel Partners",
                                        max_length=5000,
                                        blank=True)
    technology_partners = models.TextField("Technology Partners",
                                        max_length=5000,
                                        blank=True)
    oem_partners = models.TextField("OEM Partners",
                                        max_length=5000,
                                        blank=True)
    status = models.TextField("Company Status",
                              max_length=1000,
                              blank=True)
    focus = models.TextField("Company Focus",
                             max_length=3000,
                             blank=True)
    url = models.URLField("Website",
                          max_length=255,
                          blank=True)
    saas = models.DecimalField("SaaS",
                               blank=True,
                               null=False,
                               default=0,
                               decimal_places=2,
                               max_digits=12,
                               help_text="Enter in format: 00.00")
    direct = models.IntegerField("Direct",
                                 blank= True,
                                 null=False,
                                 default=0)
    partners = models.IntegerField(blank= True,
                                   null=False,
                                   default=0)
    appliance = models.DecimalField(blank= True,
                                    null=False,
                                    default=0,
                                    decimal_places=2,
                                    max_digits=12,
                                    help_text="Enter in format: 00.00")
    notes = models.TextField("Notes",
                             max_length=3000,
                             blank=True)
    strengths = models.TextField("Strengths",
                                 max_length=3000,
                                 blank=True)
    weaknesses = models.TextField("Weaknesses",
                                  max_length=3000,
                                  blank=True)
    number_of_categories = models.IntegerField(blank=True,
                                               null=False,
                                               default=0)
    last_updated = models.DateTimeField("Last Updated", auto_now=True)
    def __str__(self):
        return self.name

class CompetitorCategories(models.Model):
    competitor = models.ForeignKey(Competitor)
    category = models.ForeignKey(Category)
    details = models.TextField("Sub-Categories", blank=True, null=True, max_length=3000)

class Platform(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Installation(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Product(models.Model):
    competitor = models.ForeignKey(Competitor)
    name = models.CharField(max_length=255,
                            blank=False)
    status = models.TextField(max_length=3000, blank=True)
    platform = models.ManyToManyField(Platform, blank=True)
    installation = models.ManyToManyField(Installation, blank=True)

    urlDB = models.CharField("URL Database", max_length=255, blank=True)
    price = models.DecimalField(blank=True,
                                null=False,
                                default=0,
                                decimal_places=2,
                                max_digits=12,
                                help_text="Enter in format: 00.00")
    notes = models.TextField(max_length=3000, blank=True)
    def __str__(self):
        return self.name

class Review(models.Model):
    competitor = models.ForeignKey(Competitor)
    review = models.TextField(max_length=255, blank=True)

class RevenueDataSource(models.Model):
    name = models.CharField("Data Source Name",
                            max_length=255,
                            blank=False)
    def __str__(self):
        return self.name

class AdditionalInfo(models.Model):
    competitor = models.ForeignKey(Competitor)
    document = models.FileField("Add extra documentation")

class RevenueEstimate(models.Model):
    competitor = models.ForeignKey(Competitor)
    dataSource = models.ForeignKey(RevenueDataSource)
    totalRevenue = models.DecimalField("Estimated Total Revenue (millions)",
                                       blank=True,
                                       null=False,
                                       default=0,
                                       decimal_places=2,
                                       max_digits=12,
                                       help_text="Enter in format: 00.00")
    filteringRevenue = models.DecimalField("Estimated Filtering Revenue (millions)",
                                           blank=True,
                                           null=False,
                                           default=0,
                                           decimal_places=2,
                                           max_digits=12,
                                           help_text="Enter in format: 00.00")

class CompanyFeatures(models.Model):
    competitor = models.ForeignKey(Competitor)
    feature = models.ForeignKey(Feature)
    featureSpecs = models.TextField("Technical Details", blank=True, null=True, max_length=3000)

class GlobalMarketShare(models.Model):
    competitor = models.ForeignKey(Competitor)
    global_market = models.ForeignKey(GlobalMarket)
    share = models.DecimalField(blank=True,
                                null=False,
                                default=0,
                                decimal_places=2,
                                max_digits=12,
                                help_text="Enter in format: 00.00")

class VerticalMarketShare(models.Model):
    competitor = models.ForeignKey(Competitor)
    vertical_market = models.ForeignKey(VerticalMarket)
    share = models.DecimalField(blank=True,
                                null=False,
                                default=0,
                                decimal_places=2,
                                max_digits=12,
                                help_text="Enter in format: 00.00")