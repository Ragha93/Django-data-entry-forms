from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
from django.conf import settings
from django.urls import reverse
from django.core.validators import MinLengthValidator



class Userprofileinfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    Teamname = models.CharField(max_length=30)
    date = models.DateTimeField(default = datetime.datetime.now(),null=True)
    timenow = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username

class Mytimein(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userloggedin')
    date = models.DateTimeField(default = datetime.datetime.now(),null=True)

    def __str__(self):
            return self.user.username

class Wts_table(models.Model):
        Error = 'Error'
        NoError = 'No Error'
        INPUT_WTS_CHOICES = (
        (Error, 'Error'),
        (NoError, 'No Error'),
        )

        # MainFields1
        asin=models.CharField(max_length=10,validators=[MinLengthValidator(10)], unique=True, verbose_name="ASIN")
        vendorCode= models.CharField(max_length=10,  null=True,verbose_name="VendorCode")
        # searchable
        Asinsitestatus=models.CharField(max_length=1000,null=True,verbose_name="SiteStatus", blank=True)

        asinsearchable=models.CharField(max_length=1000,null=True,choices=INPUT_WTS_CHOICES,verbose_name="The ASIN is searchable in customer search bar.(If not, open up a Buyability Troubleshooting task for the ASIN)")
        comment1 = models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)

        asinretailcontribution=models.CharField(max_length=1000,null=True,choices=INPUT_WTS_CHOICES,verbose_name="Does the ASIN having Retail Contribution?(If the ASIN doesn’t have retail contribution then don’t proceed for further audit)")
        comment2=models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)

        asinobsolete=models.CharField(max_length=1000,null=True,choices=INPUT_WTS_CHOICES,verbose_name="Does the ASIN is Obselete? (If the ASIN is Obselete then don’t proceed for further audit)")
        comment3=models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)

        # Categorty
        asincurrentcategory=models.CharField(max_length=1000,null=True,verbose_name="asinspecific", blank=True)

        asincorrectcategory=models.CharField(max_length=1000,null=True,choices=INPUT_WTS_CHOICES,verbose_name="Does vendor product appear under correct category?")
        comment4=models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)

        # TITLE
        item_name=models.CharField(max_length=1000,null=True,verbose_name="Title", blank=True)

        asinreflectproduct=models.CharField(max_length=1000,null=True,choices=INPUT_WTS_CHOICES,verbose_name="Does the title correctly reflect the product on the detail page?")
        comment5=models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)

        asinnomismatchbtwnattributes=models.CharField(max_length=1000,null=True,choices=INPUT_WTS_CHOICES,verbose_name="There is no mismatch between related attributes (Brand Name, Color, Unit Count and Number of Items)")
        comment6=models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)

        asintitleguideline=models.CharField(max_length=1000,null=True,choices=INPUT_WTS_CHOICES,verbose_name="Title fits the general guideline of: Brand Name – Model no/style no – Product Type- Variation attributes (Size, Color, Pattern, & Hand orientation)?")
        comment7=models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)

        # Image
        asinmainimage=models.CharField(max_length=1000,null=True,choices=INPUT_WTS_CHOICES,verbose_name="ASIN has main image")
        comment8=models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)

        asinmainimagewhitebg=models.CharField(max_length=1000,null=True,choices=INPUT_WTS_CHOICES,verbose_name="Main image has a white background?")
        comment9=models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)

        asinimageborderwatermanrtextcheck=models.CharField(max_length=1000,null=True,choices=INPUT_WTS_CHOICES,verbose_name="The main image does not have Borders, watermarks, text, or other decorations?")
        comment10=models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)

        asinimagematchtitle=models.CharField(max_length=1000,null=True,choices=INPUT_WTS_CHOICES,verbose_name="Images match what the title says the item is")
        comment11=models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)

        asinimagematchcolorsize=models.CharField(max_length=1000,null=True,choices=INPUT_WTS_CHOICES,verbose_name="Is the image consistent with product color and pack size?")
        comment12=models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)

        asinimageplaceholdercheck=models.CharField(max_length=1000,null=True,choices=INPUT_WTS_CHOICES,verbose_name="There are no Image place holders for images? (with text such as temporary image or no image available)")
        comment13=models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)

        asinimagegraphratings=models.CharField(max_length=1000,null=True,choices=INPUT_WTS_CHOICES,verbose_name="Images do not contain graphs of product ratings")
        comment14=models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)

        asinimagepromotextcheck=models.CharField(max_length=1000,null=True,choices=INPUT_WTS_CHOICES,verbose_name="Image does not have any Promotional text such as sale or free ship")
        comment15=models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)

        asinimagecustomerdepict=models.CharField(max_length=1000,null=True,choices=INPUT_WTS_CHOICES,verbose_name="Do the images depict what a customer would expect to receive if they made a purchase? [Other products, items or accessories that are not part of the product listing; only include exactly what the customer is buying]")
        comment16=models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)

        # BRAND
        brand_name=models.CharField(max_length=1000,null=True,verbose_name="Brandname", blank=True)

        asinbrandnamecorrect=models.CharField(max_length=1000,null=True,choices=INPUT_WTS_CHOICES,verbose_name="Is the brand name accurate/correct?  (Check 'verified brand' from Bonsai)")
        comment17=models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)

        asinbrandhyperlink=models.CharField(max_length=1000,null=True,choices=INPUT_WTS_CHOICES,verbose_name="Does the Brand hyperlink link to an Amazon Brand Store or a search result page pre-populated with the brand’s ASINs")
        comment18=models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)

        # Bullets
        bullet_point1=models.CharField(max_length=1000,null=True,verbose_name="BulletPoint1",blank=True)
        bullet_point2=models.CharField(max_length=1000,null=True,verbose_name="BulletPoint2",blank=True)
        bullet_point3=models.CharField(max_length=1000,null=True,verbose_name="BulletPoint3",blank=True)
        bullet_point4=models.CharField(max_length=1000,null=True,verbose_name="BulletPoint4",blank=True)
        bullet_point5=models.CharField(max_length=1000,null=True,verbose_name="BulletPoint5",blank=True)
        bullet_point6=models.CharField(max_length=1000,null=True,verbose_name="BulletPoint6",blank=True)
        bullet_point7=models.CharField(max_length=1000,null=True,verbose_name="BulletPoint7",blank=True)
        bullet_point8=models.CharField(max_length=1000,null=True,verbose_name="BulletPoint8",blank=True)

        asinbulltpointrelevant=models.CharField(max_length=1000,null=True,choices=INPUT_WTS_CHOICES,verbose_name="Is the content relevant to the ASIN?")
        comment19=models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)

        asinbulletwarrantyinfo=models.CharField(max_length=1000,null=True,choices=INPUT_WTS_CHOICES,verbose_name="Does the Bullets Include Warranty info if applicable")
        comment20=models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)

        asinbulletshort=models.CharField(max_length=1000,null=True,choices=INPUT_WTS_CHOICES,verbose_name="Is the bullet point Short Crisp; no vague statements")
        comment21=models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)

        asinbulletnumerals=models.CharField(max_length=1000,null=True,choices=INPUT_WTS_CHOICES,verbose_name="Are Numbers written as numerals (1, 2, 3, etc.)?")
        comment22=models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)

        # ReleaseDate
        asinsitemsg=models.CharField(max_length=1000,null=True,verbose_name="Sitemessage",blank=True)

        asinreleasedate1=models.CharField(max_length=1000,null=True,choices=INPUT_WTS_CHOICES,verbose_name="Product does not advertise a generic or future release date, but indicates that it is currently buyable.")
        comment23=models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)

        #VariationColorSize
        asinvariationcheck=models.CharField(max_length=1000,null=True,choices=INPUT_WTS_CHOICES,verbose_name="Variations are appropriate to the parent ASIN and not separate products all together. ")
        comment24=models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)

        color_name=models.CharField(max_length=1000,null=True,verbose_name="Color Name",blank=True)

        asincolorname=models.CharField(max_length=1000,null=True,choices=INPUT_WTS_CHOICES,verbose_name="Color name is correct and has the same name as the correct child ASIN. ")
        comment25=models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)

        size_name=models.CharField(max_length=1000,null=True,verbose_name="Size Name",blank=True)

        asinsizecheck=models.CharField(max_length=1000,null=True,choices=INPUT_WTS_CHOICES,verbose_name="Size is correct and spelled correctly. Ex: SMALL ")
        comment27=models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)

        #Orphanasins
        asinnotorphan=models.CharField(max_length=1000,null=True,choices=INPUT_WTS_CHOICES,verbose_name="ASIN is not an orphan ASIN")
        comment28=models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)

        # A+Content
        asinsiteadescstatus=models.CharField(max_length=1000,null=True,choices=INPUT_WTS_CHOICES,verbose_name="AsinA+status")
        comment29=models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)

        asinapluscontent=models.CharField(max_length=1000,null=True,choices=INPUT_WTS_CHOICES,verbose_name="Does the product have A+ Content?")
        comment30=models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)

        asinrelevantproduct=models.CharField(max_length=1000,null=True,choices=INPUT_WTS_CHOICES,verbose_name="A+ content is relevant to the product")
        comment31=models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)

        # ASIN productdescription fully automated
        # asinproductdesc=models.CharField(max_length=1000,null=True,verbose_name="Product Description")
        # asindescription=models.CharField(max_length=1000,null=True,verbose_name="Product has a product description. For media ASINs, if the product description is not available, evaluate manufacturer’s site or editorial reviews and provide recommendations to AM")
        # asindescriptionless2000=models.CharField(max_length=1000,null=True,verbose_name="Product description has less than 2000 characters.")
        # asindescriptionmore50=models.CharField(max_length=1000,null=True,verbose_name="Product description has more than 50 characters.")
        # asindescriptionsymbolcheck=models.CharField(max_length=1000,null=True,verbose_name="Product description does not contain ™, ®,€,…,†,&Dagger;,•,¢,£,¥,©,±,¶,~,â, Ltd., Inc., LLC, Corp,.STD, Co.In, .Com, St., Company name")
        # asindescriptioncontactinfo=models.CharField(max_length=1000,null=True,verbose_name="Product description does not contain contact information")
        # ASIN productdescription fully automated

        # General
        asinappropriate=models.CharField(max_length=1000,null=True,choices=INPUT_WTS_CHOICES,verbose_name="Product is not inappropriate")
        comment32=models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)

        #SearchKeywords
        asin_subject_keywords=models.CharField(max_length=1000,null=True,verbose_name="Keywords",blank=True)

        asinkeyword=models.CharField(max_length=1000,null=True,choices=INPUT_WTS_CHOICES,verbose_name="There are keywords for this ASIN. (if no, add some)")
        comment33=models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)

        asinvariationword=models.CharField(max_length=1000,null=True,choices=INPUT_WTS_CHOICES,verbose_name="There are not multiple variations of the same word (example: with different spelling)")
        comment34=models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)

        asinleafnode=models.CharField(max_length=1000,null=True,choices=INPUT_WTS_CHOICES,verbose_name="ASIN has a leaf node")
        comment35=models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)

        # Automated headers not to be added in update field*******************************************************************************************************************************
        asinhastitle= models.CharField(max_length=10,choices=INPUT_WTS_CHOICES)
        comment36 = models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)
        asintitleduplicatewords = models.CharField(max_length=10,choices=INPUT_WTS_CHOICES)
        comment37 = models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)
        asintitlesymbol = models.CharField(max_length=10,choices=INPUT_WTS_CHOICES)
        comment38 = models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)
        asintitlecasing = models.CharField(max_length=10,choices=INPUT_WTS_CHOICES)
        comment39= models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)
        asinimagehighresolution = models.CharField(max_length=10,choices=INPUT_WTS_CHOICES)
        comment40= models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)
        asinbrandname =  models.CharField(max_length=10,choices=INPUT_WTS_CHOICES)
        comment41 = models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)
        asinbrandnametitleimagematch = models.CharField(max_length=10,choices=INPUT_WTS_CHOICES)
        comment42 = models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)
        asinbulletcheck = models.CharField(max_length=10,choices=INPUT_WTS_CHOICES)
        comment43 = models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)
        asinspellinggrammar = models.CharField(max_length=10,choices=INPUT_WTS_CHOICES)
        comment44 = models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)
        asinmeasurements = models.CharField(max_length=10,choices=INPUT_WTS_CHOICES)
        comment45 = models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)
        asinbulletplaceholder = models.CharField(max_length=10,choices=INPUT_WTS_CHOICES)
        comment46 = models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)
        asinbulletduplicate = models.CharField(max_length=10,choices=INPUT_WTS_CHOICES)
        comment47 = models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)
        asinexternalsitelink = models.CharField(max_length=10,choices=INPUT_WTS_CHOICES)
        comment48 = models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)
        asincompetetiors = models.CharField(max_length=10,choices=INPUT_WTS_CHOICES)
        comment49 = models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)
        asinhtmlcode = models.CharField(max_length=10,choices=INPUT_WTS_CHOICES)
        comment50= models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)
        asinbulletbegin =models.CharField(max_length=10,choices=INPUT_WTS_CHOICES)
        comment51= models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)
        asincontactinfo = models.CharField(max_length=10,choices=INPUT_WTS_CHOICES)
        comment52= models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)
        asinpromomaterial =models.CharField(max_length=10,choices=INPUT_WTS_CHOICES)
        comment53= models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)
        asinshippinginfo = models.CharField(max_length=10,choices=INPUT_WTS_CHOICES)
        comment54= models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)
        asinbulletsymbols = models.CharField(max_length=10,choices=INPUT_WTS_CHOICES)
        comment55= models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)
        asinproduct_description = models.CharField(max_length=1000,null=True,verbose_name="ProductDescription", blank=True)
        asinproductdesciptioncheck = models.CharField(max_length=10,choices=INPUT_WTS_CHOICES)
        comment56= models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)
        asinproddesclesscharc = models.CharField(max_length=10,choices=INPUT_WTS_CHOICES)
        comment57= models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)
        asinproddescmorecharac =models.CharField(max_length=10,choices=INPUT_WTS_CHOICES)
        comment58= models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)
        asinproductdescsymbols = models.CharField(max_length=10,choices=INPUT_WTS_CHOICES)
        comment59= models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)
        asinproductdescpcontactinfo =models.CharField(max_length=10,choices=INPUT_WTS_CHOICES)
        comment60= models.CharField(max_length=1000,null=True,verbose_name="Comment", blank=True)
        # Automated headers not to be added in update field*******************************************************************************************************************************

        # TOOL data
        allocatedto=models.CharField(max_length=1000,null=True,verbose_name="Allocated User")
        allocationdate=models.DateTimeField(max_length=1000,default=timezone.now(), verbose_name="Allocated Date")


        def __str__(self):
            return self.asin

        def get_absolute_url(self):
            return reverse("listasins")
            # return reverse("detail", kwargs={'pk':self.pk})
