# Creator : Kuldeep singh
# github profile : 


# a script with functions to load T5-small
# also provide inference 

from transformers import pipeline

def text_summarizer_inference(text, classifier):
    '''
    Uses huggingface pipeline to summarize the text.
    # have to implement some fallbacks if hugginface gives some error.
    '''
    model_output = classifier(text)
    summary = model_output[0]['summary_text'].strip()
    return summary


if __name__ == "__main__":
    classifier = pipeline("summarization")
    long_text = "Paris is the capital and most populous city of France, with an estimated population of 2,175,601 residents as of 2018, in an area of more than 105 square kilometres (41 square miles). The City of Paris is the centre and seat of government of the region and province of Île-de-France, or Paris Region, which has an estimated population of 12,174,880, or about 18 percent of the population of France as of 2017."
    summary = text_summarizer_inference(long_text, classifier)
    print('Long Text : {}'.format(long_text))
    print('Summary : {}'.format(summary))