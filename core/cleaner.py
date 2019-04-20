import re
import string


class Cleaner:

    @classmethod
    def keep_only_arabic(cls, text):
        if not text:
            return text
        else:
            text = re.findall(r'[\u0600-\u06FF]+', text)
            # Remove all items in the resulting list that have len(item) <= 1
            text = [word for word in text if len(word) > 1]
            text = ' '.join(text)
            return text

    @classmethod
    def remove_diacritics(cls, text):
        arabic_diacritics = re.compile("""
                                     ّ    | # Tashdid
                                     َ    | # Fatha
                                     ً    | # Tanwin Fath
                                     ُ    | # Damma
                                     ٌ    | # Tanwin Damm
                                     ِ    | # Kasra
                                     ٍ    | # Tanwin Kasr
                                     ْ    | # Sukun
                                     ـ     # Tatwil/Kashida
                                 """, re.VERBOSE)
        if not text:
            return text
        else:
            text = re.sub(arabic_diacritics, '', text)
            return text

    @classmethod
    def remove_punctuations(cls, text):
        arabic_punctuations = '''`÷×؛<>_()*&^%][ـ،/:"؟.,'{}~¦+|!”…“–ـ'''
        english_punctuations = string.punctuation
        punctuations_list = arabic_punctuations + english_punctuations

        if not text:
            return text
        else:
            translator = str.maketrans('', '', punctuations_list)
            return text.translate(translator)

    @classmethod
    def normalize_arabic(cls, text):
        """Normalize text
        """
        if not text:
            return text
        else:
            text = re.sub("[إأآ]", "ا", text)
            text = re.sub("ى", "ي", text)
            text = re.sub("ؤ", "و", text)
            text = re.sub("ئ", "ي", text)
            text = re.sub("ة", "ت", text)
            text = re.sub("گ", "ك", text)
            return text
