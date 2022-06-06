import boto3

# boto3 client kullanarak aws translate'i çağırıyoruz.
translate = boto3.client(service_name='translate', region_name='eu-central-1', use_ssl=True)

# çevirilecek metni kullanıcıdan alıyoruz
str = input("Lutfen çevirilecek metni girin en --> tr\n")

# aws translate nesnesinin translate_text fonksiyonu ile çeviri işlemini gerçekleştiriyoruz
result = translate.translate_text(Text=str, SourceLanguageCode="en", TargetLanguageCode="tr")

### Sonuçları yazdırıyoruz.
print('TranslatedText: ' + result.get('TranslatedText'))

print('SourceLanguageCode: ' + result.get('SourceLanguageCode'))
print('TargetLanguageCode: ' + result.get('TargetLanguageCode'))