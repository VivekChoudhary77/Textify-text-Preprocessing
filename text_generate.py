#import the library
import tensorflow as tf
from transformers import GPT2LMHeadModel, GPT2Tokenizer

def output_generate(input_sentence):
    #load Model
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2-large")
    model=GPT2LMHeadModel.from_pretrained("gpt2-large",pad_token_id=tokenizer.eos_token_id)

    #Tokenize Sentences
    input_ids = tokenizer.encode(input_sentence, return_tensors='pt')

    #Generate and Decode Text
    output = model.generate(input_ids, max_length=50, num_beams=5, no_repeat_ngram_size=2, early_stopping=True)
    text=tokenizer.decode(output[0], skip_special_tokens=True)

    #Output Result
    return text
