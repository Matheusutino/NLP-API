import nltk
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

nltk.download('punkt')

def summarize(text: str, sentences_count: int) -> str:
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    
    summary = summarizer(parser.document, sentences_count)
    summarized_text = " ".join([str(sentence) for sentence in summary])
    
    return summarized_text
