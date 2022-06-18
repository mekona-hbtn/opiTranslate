#!/usr/bin/python3

import boto3
import sys

translate = boto3.client(service_name='translate', region_name='us-east-1', use_ssl=True)
argv = sys.argv

result = translate.translate_text(Text=argv[1], 
            SourceLanguageCode=argv[2], TargetLanguageCode=argv[3])
print('TranslatedText: ' + result.get('TranslatedText'))
print('SourceLanguageCode: ' + result.get('SourceLanguageCode'))
print('TargetLanguageCode: ' + result.get('TargetLanguageCode'))
