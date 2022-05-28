from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email,username, first_name, password,**other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email,username, first_name, password, **other_fields)

    def create_user(self, email,username, first_name, password,**other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email,username=username,first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):
    Afghanistan = 'Afghanistan'
    Albania='Albania'
    Algeria='Algeria'
    Andorra='Andorra'
    Angola='Angola'
    Argentina='Argentina'
    Armenia='Armenia'
    Australia='Australia'
    Austria='Austria'
    Azerbaijan='Azerbaijan'
    Bahamas='Bahamas'
    Bahrain='Bahrain'
    Bangladesh='Bangladesh'
    Barbados='Barbados'
    Belarus='Belarus'
    Belgium='Belgium'
    Belize='Belize'
    Benin='Benin'
    Bhutan='Bhutan'
    Bolivia='Bolivia'
    Bosnia_and_Herzegovina='Bosnia and Herzegovina'
    Botswana='Botswana'
    Brazil='Brazil'
    Brunei='Brunei'
    Bulgaria='Bulgaria'
    Burkina_Faso='Burkina Faso'
    Burundi='Burundi'
    Côte_d_Ivoire='Côte d Ivoire'
    Cabo_Verde='Cabo Verde'
    Cambodia='Cambodia'
    Cameroon='Cameroon'
    Canada='Canada'
    Central_African_Republic='Central African Republic'
    Chad='Chad'
    Chile='Chile'
    China='China'
    Colombia='Colombia'
    Comoros='Comoros'
    Congo='Congo'
    Costa_Rica='Costa Rica'
    Croatia='Croatia'
    Cuba='Cuba'
    Cyprus='Cyprus'
    Czechia='Czechia'
    Democratic_Republic_of_the_Congo='Democratic Republic of the Congo'
    Denmark='Denmark'
    Djibouti='Djibouti'
    Dominica='Dominica'
    Dominican_Republic='Dominican Republic'
    Ecuador='Ecuador'
    Egypt='Egypt'
    El_Salvador='El Salvador'
    Equatorial_Guinea='Equatorial Guinea'
    Eritrea='Eritrea'
    Estonia='Estonia'
    Eswatini='Eswatini'
    Ethiopia='Ethiopia'
    Fiji='Fiji'
    Finland='Finland'
    France='France'
    Gabon='Gabon'
    Gambia='Gambia'
    Georgia='Georgia'
    Germany='Germany'
    Ghana='Ghana'
    Greece='Greece'
    Grenada='Grenada'
    Guatemala='Guatemala'
    Guinea='Guinea'
    Guinea_Bissau='Guinea-Bissau'
    Guyana='Guyana'
    Haiti='Haiti'
    Holy_See='Holy See'
    Honduras='Honduras'
    Hungary='Hungary'
    Iceland='Iceland'
    India='India'
    Indonesia='	Indonesia'
    Iran='Iran'
    Iraq='Iraq'
    Ireland='Ireland'
    Israel='Israel'
    Italy='Italy'
    Jamaica='Jamaica'
    Japan='Japan'
    Jordan='Jordan'
    Kazakhstan='Kazakhstan'
    Kenya='Kenya'
    Kiribati='Kiribati'
    Kuwait='Kuwait'
    Kyrgyzstan='Kyrgyzstan'
    Laos='Laos'
    Latvia='Latvia'
    Lebanon='Lebanon'   
    Lesotho='Lesotho'
    Liberia='Liberia'
    Libya='Libya'
    Liechtenstein='Liechtenstein'
    Lithuania='Lithuania'
    Luxembourg='Luxembourg'
    Madagascar='Madagascar'
    Malawi='Malawi'
    Malaysia='Malaysia'
    Maldives='Maldives'
    Mali='Mali'
    Malta='Malta'
    Marshall_Islands='Marshall Islands'
    Mauritania='Mauritania'
    Mauritius='Mauritius'
    Mexico='Mexico'
    Micronesia='Micronesia'
    Moldova='Moldova'
    Monaco='Monaco'
    Mongolia='Mongolia'
    Montenegro='Montenegro'
    Morocco='Morocco'
    Mozambique='Mozambique'
    Myanmar='Myanmar'
    Namibia='Namibia'
    Nauru='Nauru'
    Netherlands='Netherlands'
    New_Zealand='New Zealand'
    Nicaragua='Nicaragua'
    Niger='Niger'
    Nigeria='Nigeria'
    North_Korea='North Korea'
    North_Macedonia='North Macedonia'
    Norway='Norway'
    Oman='Oman'
    Pakistan='Pakistan'
    Palau='Palau'
    Palestine_State='Palestine State'
    Panama='Panama'
    Papua_New_Guinea='Papua New Guinea'
    Paraguay='Paraguay'
    Peru='Peru'
    Philippines='Philippines'
    Poland='Poland'
    Portugal='Portugal'
    Qatar='Qatar'
    Romania='Romania'
    Russia='Russia'
    Rwanda='Rwanda'
    Saint_Kitts_and_Nevis='Saint Kitts and Nevis'
    Saint_Lucia='Saint Lucia'
    Saint_Vincent_and_the_Grenadines='Saint Vincent and the Grenadines'
    Samoa='Samoa'
    San_Marino='San Marino'
    Sao_Tome_and_Principe='Sao Tome and Principe'
    Saudi_Arabia='Saudi Arabia'
    Senegal='Senegal'
    Serbia='Serbia'
    Seychelles='Seychelles'
    Sierra_Leone='Sierra Leone'
    Singapore='Singapore'
    Slovakia='Slovakia'
    Slovenia='Slovenia'
    Solomon_Islands='Solomon Islands'
    Somalia='Somalia'
    South_Africa='South Africa'
    South_Korea='South Korea'
    South_Sudan='South Sudan'
    Spain='Spain'
    Sri_Lanka='Sri Lanka'
    Sudan='Sudan'
    Suriname='Suriname'
    Sweden='Sweden'
    Switzerland='Switzerland'
    Syria='Syria'
    Tajikistan='Tajikistan'
    Tanzania='Tanzania'
    Thailand='Thailand'
    Timor_Leste='Timor-Leste'
    Togo='Togo'
    Tonga='Tonga'
    Trinidad_and_Tobago='Trinidad and Tobago'
    Tunisia='Tunisia'
    Turkey='Turkey'
    Turkmenistan='Turkmenistan'
    Tuvalu='Tuvalu'
    Uganda='Uganda'
    Ukraine='Ukraine'
    United_Arab_Emirates='United Arab Emirates'
    United_Kingdom='United Kingdom'
    United_States_of_America='United States of America'
    Uruguay='Uruguay'
    Uzbekistan='Uzbekistan'
    Vanuatu='Vanuatu'
    Venezuela='Venezuela'
    Vietnam='Vietnam'
    Yemen='Yemen'
    Zambia='Zambia'
    Zimbabwe='Zimbabwe'

    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    GRADUATE = 'GR'
    SCHOOL = [
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        (GRADUATE, 'Graduate'),
    ]


    YEAR_IN_SCHOOL_CHOICES = [
        (Afghanistan,'Afghanistan'),
        (Albania,'Albania'),
        (Algeria,'Algeria'),
        (Andorra,'Andorra'),
        (Angola,'Angola'),
        (Argentina,'Argentina'),
        (Armenia,'Armenia'),
        (Australia,'Australia'),
        (Austria,'Austria'),
        (Azerbaijan,'Azerbaijan'),
        (Bahamas,'Bahamas'),
        (Bahrain,'Bahrain'),
        (Bangladesh,'Bangladesh'),
        (Barbados,'Barbados'),
        (Belarus,'Belarus'),
        (Belgium,'Belgium'),
        (Belize,'Belize'),
        (Benin,'Benin'),
        (Bhutan,'Bhutan'),
        (Bolivia,'Bolivia'),
        (Bosnia_and_Herzegovina,'Bosnia and Herzegovina'),
        (Botswana,'Botswana'),
        (Brazil,'Brazil'),
        (Brunei,'Brunei'),
        (Bulgaria,'Bulgaria'),
        (Burkina_Faso,'Burkina Faso'),
        (Burundi,'Burundi'),
        (Côte_d_Ivoire,'Côte d Ivoire'),
        (Cabo_Verde,'Cabo Verde'),
        (Cambodia,'Cambodia'),
        (Cameroon,'Cameroon'),
        (Canada,'Canada'),
        (Central_African_Republic,'Central African Republic'),
        (Chad,'Chad'),
        (Chile,'Chile'),
        (China,'China'),
        (Colombia,'Colombia'),
        (Comoros,'Comoros'),
        (Congo,'Congo'),
        (Costa_Rica,'Costa Rica'),
        (Croatia,'Croatia'),
        (Cuba,'Cuba'),
        (Cyprus,'Cyprus'),
        (Czechia,'Czechia'),
        (Democratic_Republic_of_the_Congo,'Democratic Republic of the Congo'),
        (Denmark,'Denmark'),
        (Djibouti,'Djibouti'),
        (Dominica,'Dominica'),
        (Dominican_Republic,'Dominican Republic'),
        (Ecuador,'Ecuador'),
        (Egypt,'Egypt'),
        (El_Salvador,'El Salvador'),
        (Equatorial_Guinea,'Equatorial Guinea'),
        (Eritrea,'Eritrea'),
        (Estonia,'Estonia'),
        (Eswatini,'Eswatini'),
        (Ethiopia,'Ethiopia'),
        (Fiji,'Fiji'),
        (Finland,'Finland'),
        (France,'France'),
        (Gabon,'Gabon'),
        (Gambia,'Gambia'),
        (Georgia,'Georgia'),
        (Germany,'Germany'),
        (Ghana,'Ghana'),
        (Greece,'Greece'),
        (Grenada,'Grenada'),
        (Guatemala,'Guatemala'),
        (Guinea,'Guinea'),
        (Guinea_Bissau,'Guinea-Bissau'),
        (Guyana,'Guyana'),
        (Haiti,'Haiti'),
        (Holy_See,'Holy See'),
        (Honduras,'Honduras'),
        (Hungary,'Hungary'),
        (Iceland,'Iceland'),
        (India,'India'),
        (Indonesia,'Indonesia'),
        (Iran,'Iran'),
        (Iraq,'Iraq'),
        (Ireland,'Ireland'),
        (Israel,'Israel'),
        (Italy,'Italy'),
        (Jamaica,'Jamaica'),
        (Japan,'Japan'),
        (Jordan,'Jordan'),
        (Kazakhstan,'Kazakhstan'),
        (Kenya,'Kenya'),
        (Kiribati,'Kiribati'),
        (Kuwait,'Kuwait'),
        (Kyrgyzstan,'Kyrgyzstan'),
        (Laos,'Laos'),
        (Latvia,'Latvia'),
        (Lebanon,'Lebanon'),  
        (Lesotho,'Lesotho'),
        (Liberia,'Liberia'),
        (Libya,'Libya'),
        (Liechtenstein,'Liechtenstein'),
        (Lithuania,'Lithuania'),
        (Luxembourg,'Luxembourg'),
        (Madagascar,'Madagascar'),
        (Malawi,'Malawi'),
        (Malaysia,'Malaysia'),
        (Maldives,'Maldives'),
        (Mali,'Mali'),
        (Malta,'Malta'),
        (Marshall_Islands,'Marshall Islands'),
        (Mauritania,'Mauritania'),
        (Mauritius,'Mauritius'),
        (Mexico,'Mexico'),
        (Micronesia,'Micronesia'),
        (Moldova,'Moldova'),
        (Monaco,'Monaco'),
        (Mongolia,'Mongolia'),
        (Montenegro,'Montenegro'),
        (Morocco,'Morocco'),
        (Mozambique,'Mozambique'),
        (Myanmar,'Myanmar'),
        (Namibia,'Namibia'),
        (Nauru,'Nauru'),
        (Netherlands,'Netherlands'),
        (New_Zealand,'New Zealand'),
        (Nicaragua,'Nicaragua'),
        (Niger,'Niger'),
        (Nigeria,'Nigeria'),
        (North_Korea,'North Korea'),
        (North_Macedonia,'North Macedonia'),
        (Norway,'Norway'),
        (Oman,'Oman'),
        (Pakistan,'Pakistan'),
        (Palau,'Palau'),
        (Palestine_State,'Palestine State'),
        (Panama,'Panama'),
        (Papua_New_Guinea,'Papua New Guinea'),
        (Paraguay,'Paraguay'),
        (Peru,'Peru'),
        (Philippines,'Philippines'),
        (Poland,'Poland'),
        (Portugal,'Portugal'),
        (Qatar,'Qatar'),
        (Romania,'Romania'),
        (Russia,'Russia'),
        (Rwanda,'Rwanda'),
        (Saint_Kitts_and_Nevis,'Saint Kitts and Nevis'),
        (Saint_Lucia,'Saint Lucia'),
        (Saint_Vincent_and_the_Grenadines,'Saint Vincent and the Grenadines'),
        (Samoa,'Samoa'),
        (San_Marino,'San Marino'),
        (Sao_Tome_and_Principe,'Sao Tome and Principe'),
        (Saudi_Arabia,'Saudi Arabia'),
        (Senegal,'Senegal'),
        (Serbia,'Serbia'),
        (Seychelles,'Seychelles'),
        (Sierra_Leone,'Sierra Leone'),
        (Singapore,'Singapore'),
        (Slovakia,'Slovakia'),
        (Slovenia,'Slovenia'),
        (Solomon_Islands,'Solomon Islands'),
        (Somalia,'Somalia'),
        (South_Africa,'South Africa'),
        (South_Korea,'South Korea'),
        (South_Sudan,'South Sudan'),
        (Spain,'Spain'),
        (Sri_Lanka,'Sri Lanka'),
        (Sudan,'Sudan'),
        (Suriname,'Suriname'),
        (Sweden,'Sweden'),
        (Switzerland,'Switzerland'),
        (Tajikistan,'Tajikistan'),
        (Tanzania,'Tanzania'),
        (Thailand,'Thailand'),
        (Timor_Leste,'Timor-Leste'),
        (Togo,'Togo'),
        (Tonga,'Tonga'),
        (Trinidad_and_Tobago,'Trinidad and Tobago'),
        (Tunisia,'Tunisia'),
        (Turkey,'Turkey'),
        (Turkmenistan,'Turkmenistan'),
        (Tuvalu,'Tuvalu'),
        (Uganda,'Uganda'),
        (Ukraine,'Ukraine'),
        (United_Arab_Emirates,'United Arab Emirates'),
        (United_Kingdom,'United Kingdom'),
        (United_States_of_America,'United States of America'),
        (Uruguay,'Uruguay'),
        (Uzbekistan,'Uzbekistan'),
        (Vanuatu,'Vanuatu'),
        (Venezuela,'Venezuela'),
        (Vietnam,'Vietnam'),
        (Yemen,'Yemen'),
        (Zambia,'Zambia'),
        (Zimbabwe,'Zimbabwe'),
        
    ]

    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    avatar = models.ImageField(null=True,default="avatar.svg")
    start_date = models.DateTimeField(default=timezone.now)
    address = models.CharField(max_length=150, default="Wuhan")
    country = models.CharField(max_length=150,choices=YEAR_IN_SCHOOL_CHOICES)
    year_in_school = models.CharField(
        max_length=2,
        choices=SCHOOL,
        default=FRESHMAN,
    )

    about = models.TextField(_(
        'about'), max_length=500, blank=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ 'username','first_name']

    def __str__(self):
        return self.username

class Slider(models.Model):
    title = models.CharField(max_length=100,null=True)
    Description = models.CharField(max_length=150,null=True)
    image = models.ImageField(null=True,default="avatar.svg")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=200)
    intro = models.CharField(max_length=150, null=True)
    highlights = models.CharField(max_length=300, null=True)
    image = models.ImageField(null=True,default="avatar.svg")
    description = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class AboutTiles(models.Model):
    title = models.CharField(max_length=200)
    avatar = models.ImageField(null=True,default="avatar.svg")
    description = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class Team(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    avatar = models.ImageField(null=True,default="avatar.svg")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=200)
    intro = models.CharField(max_length=150, null=True)
    avatar = models.ImageField(null=True,default="avatar.svg")
    highlights = models.CharField(max_length=300, null=True)
    description = models.TextField()
    event_date = models.DateField()
    location = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=200)
    highlights = models.CharField(max_length=300, null=True)
    image = models.ImageField(null=True,default="avatar.svg")
    description = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Upcomming_Event(models.Model):
    name = models.CharField(max_length=200)
    event_date = models.DateField()
    location = models.CharField(max_length=200)
    description = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Testomonial(models.Model):
    name = models.CharField(max_length=200)
    about = models.CharField(max_length=200)
    avatar = models.ImageField(null=True,default="avatar.svg")
    testomonial = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=200)
    intro = models.CharField(max_length=150, null=True)
    avatar = models.ImageField(null=True,default="avatar.svg")
    description = models.TextField()
    highlights = models.CharField(max_length=500)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]




class Gallery(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(null=True,default="avatar.svg")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Partner(models.Model):
    image = models.ImageField(null=True,default="avatar.svg")
    title = models.CharField(max_length=150)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
            return self.title


class Contact(models.Model):
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=200)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=True)  # Validators should be a list
    # phone_number = models.IntegerField()
    message = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


