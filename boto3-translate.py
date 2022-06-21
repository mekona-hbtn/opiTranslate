#!/usr/bin/python3

import argparse
import boto3

translate = boto3.client(service_name='translate', region_name='us-east-1', use_ssl=True)
parser = argparse.ArgumentParser(description="Translate text into desired language")

parser.add_argument("--text", "-text", help="Text to be translated.")
parser.add_argument("--input-lang", "-il", default="auto", help="Pick the language text is in. Default set to auto.")
parser.add_argument("--output-lang", "-ol", default="en", help="Language text will be translated to. Default set to English.")

args = parser.parse_args()


result = translate.translate_text(Text=args.text, 
            SourceLanguageCode=args.input_lang, TargetLanguageCode=args.output_lang)
print('TranslatedText: ' + result.get('TranslatedText'))
print('SourceLanguageCode: ' + result.get('SourceLanguageCode'))
print('TargetLanguageCode: ' + result.get('TargetLanguageCode'))
