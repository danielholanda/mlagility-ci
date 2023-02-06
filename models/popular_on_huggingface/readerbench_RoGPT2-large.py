# labels: test_group::monthly author::readerbench name::RoGPT2-large downloads::372 task::Text_Generation
# TensorFlow
from transformers import AutoTokenizer, TFAutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained('readerbench/RoGPT2-large')
model = TFAutoModelForCausalLM.from_pretrained('readerbench/RoGPT2-large')
inputs = tokenizer.encode("Este o zi de vara", return_tensors='tf')
text = model.generate(inputs, max_length=1024,  no_repeat_ngram_size=2)
print(tokenizer.decode(text[0]))

# PyTorch
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained('readerbench/RoGPT2-large')
model = AutoModelForCausalLM.from_pretrained('readerbench/RoGPT2-large')
inputs = tokenizer.encode("Este o zi de vara", return_tensors='pt')
text = model.generate(inputs, max_length=1024,  no_repeat_ngram_size=2)
print(tokenizer.decode(text[0]))
