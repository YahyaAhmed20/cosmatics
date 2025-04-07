# services/translation.py
from modeltranslation.translator import translator, TranslationOptions
from .models import SpecialService

class SpecialServiceTranslationOptions(TranslationOptions):
    fields = ()  # ممكن تسيبها فاضية طالما الحقول كلها موروثة من Service

translator.register(SpecialService, SpecialServiceTranslationOptions)
