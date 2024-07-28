from pydantic import BaseModel

class TextToSummarize(BaseModel):
    text: str
    sentences_count: int = 3

