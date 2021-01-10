import string
import pandas as pd
import re

## A collection of functions

def Quran():
    """
    Will return a the Quran as a DataFrame, with columns:
    - Surah Name
    - Surah Number
    - Verse Number
    - Verse Text
    """

    quran_df = pd.read_csv('data/quran_data.csv')

    return quran_df

def Hadith():
    """
    Will return a DataFrame of Hadith
    """

    hadith_df = pd.read_csv('data/all_hadiths_clean.csv')

    return hadith_df

def Translation():
    """
    Will return a DataFrame with the English translation of The Quran

    Using English Saheeh Internation first, but will add others later
    """

    translation_df = pd.read_csv("data/en-sahih.csv")


    return translation_df

def cleaner(documents):
    """
    Main function which will take in Pandas.series of arabic text (i.e. quran_df['Verse Text']) and return a list of clean arabic Text
    """
    import re


    arabic_punctuations = '''`÷×؛<>_()*&^%][ـ،/:"؟.,'{}~¦+|!”…“–ـ'''
    english_punctuations = string.punctuation
    punctuations_list = arabic_punctuations + english_punctuations

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


    def normalize_arabic(text):
        text = re.sub("[إأآا]", "ا", text)
        text = re.sub("ى", "ي", text)
        text = re.sub("ؤ", "ء", text)
        text = re.sub("ئ", "ء", text)
        text = re.sub("ة", "ه", text)
        text = re.sub("گ", "ك", text)
        return text


    def remove_diacritics(text):
        text = re.sub(arabic_diacritics, '', text)
        return text


    def remove_punctuations(text):
        translator = str.maketrans('', '', punctuations_list)
        return text.translate(translator)


    def remove_repeating_char(text):
        return re.sub(r'(.)\1+', r'\1', text)

    def remove_weird_chars(text):
        return text.replace('\u200f', '')

    cleaning_funcs = [normalize_arabic, remove_diacritics, remove_punctuations, remove_weird_chars]

    clean_arabic = []

    for document in documents:

        for f in cleaning_funcs:
            document = f(document)

        clean_arabic.append(document)

    return clean_arabic
