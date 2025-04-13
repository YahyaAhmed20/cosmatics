from modeltranslation.translator import translator, TranslationOptions
from .models import Slide
from .models import Service

# ,WhyChooseUs,WhyChooseUsItem

class SlideTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'description')

translator.register(Slide, SlideTranslationOptions)



class ServiceTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

translator.register(Service, ServiceTranslationOptions)





# class WhyChooseUsTranslationOptions(TranslationOptions):
#     fields = ('title', 'subtitle', 'description')

# # Translation options for WhyChooseUsItem
# class WhyChooseUsItemTranslationOptions(TranslationOptions):
#     fields = ('title', 'description')

# # Register models for translation
# translator.register(WhyChooseUs, WhyChooseUsTranslationOptions)
# translator.register(WhyChooseUsItem, WhyChooseUsItemTranslationOptions)
