from fastapi import APIRouter, HTTPException
from slowapi import Limiter
from slowapi.util import get_remote_address
from api.models.summarize import TextToSummarize
from api.scripts.summarize import summarize
from starlette.requests import Request

limiter = Limiter(key_func=get_remote_address)

router = APIRouter()

@router.post("/summarize/")
@limiter.limit("60/minute")
async def summarize_text(data: TextToSummarize, request: Request):
    if data.sentences_count < 1:
        raise HTTPException(status_code=400, detail="The number of sentences must be at least 1")
    
    summarized_text = summarize(data.text, data.sentences_count)

    return {"summary": summarized_text}
