from enum import Enum

DucklingEntities = \
[
    'time'          ,
    'timezone'      ,
    'temperature'   ,
    'number'        ,
    'ordinal'       ,
    'distance'      ,
    'volume'        ,
    'money'         ,
    'duration'      ,
    'email'         ,
    'url'           ,
    'phone_number'
]

SpacyEnitites = \
[
    'PERSON'        ,
    'NORP'          ,
    'FACILITY'      ,
    'ORG'           ,
    'GPE'           ,
    'LOC'           ,
    'PRODUCT'       ,
    'EVENT'         ,
    'WORK_OF_ART'   ,
    'LANGUAGE'      ,
    'PERCENT'
]

class EntityType(Enum):
    Time            = 'time'
    TimeZone        = 'timezone'
    Tempertaure     = 'temperature'
    Number          = 'number'
    Ordinal         = 'ordinal'
    Distance        = 'distance'
    Volume          = 'volume'
    Money           = 'money'
    Duration        = 'duration'
    Email           = 'email'
    URl             = 'url'
    PhoneNumber     = 'phone_number'
    Person          = 'PERSON'
    Nationality     = 'NORP'
    ReligiousGroup  = 'NORP'
    PoliticalGroup  = 'NORP'
    Facility        = 'FACILITY'
    Organization    = 'ORG'
    Country         = 'GPE'
    City            = 'GPE'
    State           = 'GPE'
    OtherLocation   = 'LOC'
    Vehicle         = 'PRODUCT'
    Food            = 'PRODUCT'
    Object          = 'PRODUCT'
    Product         = 'PRODUCT'
    Event           = 'EVENT'
    WorkOfArt       = 'WORK_OF_ART'
    LanguageName    = 'LANGUAGE'
    Percentage      = 'PERCENTAGE'