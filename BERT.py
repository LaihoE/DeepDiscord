import torch
from transformers import BertForQuestionAnswering
from transformers import BertTokenizer
import os

textfilepath=os.path.join(os.path.dirname(__file__),"Text_QnA","studytext.txt")

def gobert(question,text):
    model = BertForQuestionAnswering.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')
    tokenizer = BertTokenizer.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')

    textfile=open(textfilepath,encoding='UTF-8')

    chonkystring=""
    for x in textfile:
        chonkystring+=x

    answer_text = chonkystring
    input_ids = tokenizer.encode(question, answer_text)
    tokens = tokenizer.convert_ids_to_tokens(input_ids)

    sep_index = input_ids.index(tokenizer.sep_token_id)
    num_seg_a = sep_index + 1


    num_seg_b = len(input_ids) - num_seg_a
    segment_ids = [0]*num_seg_a + [1]*num_seg_b

    assert len(segment_ids) == len(input_ids)

    outputs = model(torch.tensor([input_ids]), # The tokens representing our input text.
                                 token_type_ids=torch.tensor([segment_ids]), # The segment IDs to differentiate question from answer_text
                                 return_dict=True)

    start_scores = outputs.start_logits
    end_scores = outputs.end_logits

    answer_start = torch.argmax(start_scores)
    answer_end = torch.argmax(end_scores)
    answer = ' '.join(tokens[answer_start:answer_end+1])
    answer = tokens[answer_start]
    for i in range(answer_start + 1, answer_end + 1):
        if tokens[i][0:2] == '##':
            answer += tokens[i][2:]
        else:
            answer += ' ' + tokens[i]
    return answer
