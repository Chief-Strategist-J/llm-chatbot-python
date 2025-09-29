from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Any, Dict
from services.rag_service import RAGService

router: APIRouter = APIRouter(prefix="/search", tags=["search"])

class SearchRequest(BaseModel):
    query: str

@router.post("/rag")
async def search_rag(request: SearchRequest) -> Dict[str, Any]:
    if not request.query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty")
    
    try:
        rag_service: RAGService = RAGService()
        result: Dict[str, Any] = rag_service.search_and_generate(request.query)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Search failed: {str(e)}")
