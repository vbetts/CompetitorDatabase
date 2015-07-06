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
    class Meta:
        verbose_name_plural="Categories"
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
    class Meta:
        verbose_name_plural="Target Market"
        verbose_name="Target Market"
    def __str__(self):
        return self.name

class Competitor(models.Model):
    dataSource = models.ManyToManyField(CompetitorDataSource, verbose_name="Competitor Data Sources")
    target_Market = models.ManyToManyField(TargetMarket, verbose_name="Target Markets")
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
    class Meta:
        verbose_name_plural="Competitor Filtering Categories"

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
    document_name = models.CharField("Document Name", max_length=255, blank=False)
    document = models.FileField("Add extra documentation")
    description = models.TextField("Description", max_length=3000, blank=True)
    class Meta:
        verbose_name_plural="Additional Info"
    def __str__(self):
        return self.competitor.name

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
    class Meta:
        verbose_name_plural="Product Features"

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

class ResourceCategory(models.Model):
    name = models.CharField("Resource Category",
                                         max_length=255,
                                         blank=False)
    description = models.TextField("Description",
                             max_length=3000,
                             blank=True)
    class Meta:
        verbose_name = "Sales Resource Category"
        verbose_name_plural="Sales Resource Categories"
    def __str__(self):
        return self.name

class ResourceFile(models.Model):
    resource_category = models.ForeignKey(ResourceCategory)
    document_name = models.CharField("Document Name",
                                     max_length=255,
                                     blank=False)
    resource_file = models.FileField("Document Upload")
    description = models.TextField("Description",
                             max_length=3000,
                             blank=True)
    class Meta:
        verbose_name = "Sales Resource File"
        verbose_name_plural="Sales Resource Files"
    def __str__(self):
        return self.document_name

class Region(models.Model):
    name = models.CharField("Region", max_length=255, blank=False)
    class Meta:
        verbose_name="Region"
        verbose_name_plural="Regions"
    def __str__(self):
        return self.name

class Clients(models.Model):
    name = models.CharField("Client Name", max_length=255, blank=False)
    region = models.ForeignKey(Region)
    telco = models.BooleanField("Telco")
    education = models.BooleanField("Education")
    background = models.TextField("Client Background", max_length=3000, blank=True)
    use_cases = models.TextField("Use Cases", max_length=5000, blank=True)
    netsweeper_uses = models.TextField("Netsweeper Uses", max_length=5000, blank=True)
    admin_only = models.BooleanField("This record is visible to admins only")
    class Meta:
        verbose_name="Client"
        verbose_name_plural="Clients"
    def __str__(self):
        return self.name

