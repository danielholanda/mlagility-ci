# labels: test_group::monthly author::pszemraj name::grammar-synthesis-large downloads::429 license::cc-by-nc-sa-4.0 task::Text2Text_Generation
from transformers import pipeline

corrector = pipeline(
              'text2text-generation',
              'pszemraj/grammar-synthesis-large',
              )
raw_text = 'i can has cheezburger'
results = corrector(raw_text)
print(results)
