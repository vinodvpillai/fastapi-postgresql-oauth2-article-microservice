from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.dto.article_dto import ArticleCreateDTO, ArticleUpdateDTO, ArticleResponseDTO
from app.service.article_service import ArticleService 
from app.core.security import get_current_user

class ArticleController:
    def __init__(self):
        self.router = APIRouter()
        self.router.post("/", response_model=ArticleResponseDTO)(self.create_article)
        self.router.get("/{article_id}", response_model=ArticleResponseDTO)(self.read_article)
        self.router.put("/{article_id}", response_model=ArticleResponseDTO)(self.update_article)
        self.router.delete("/{article_id}", response_model=ArticleResponseDTO)(self.delete_article)
        self.router.get("/", response_model=list[ArticleResponseDTO])(self.read_articles)

    async def create_article(self, article: ArticleCreateDTO, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
        service = ArticleService(db)
        return service.create_article(article)

    async def read_article(self, article_id: int, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
        service = ArticleService(db)
        db_article = service.get_article(article_id)
        if db_article is None:
            raise HTTPException(status_code=404, detail="Article not found")
        return db_article

    async def update_article(self, article_id: int, article: ArticleUpdateDTO, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
        service = ArticleService(db)
        db_article = service.update_article(article_id, article)
        if db_article is None:
            raise HTTPException(status_code=404, detail="Article not found")
        return db_article

    async def delete_article(self, article_id: int, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
        service = ArticleService(db)
        db_article = service.delete_article(article_id)
        if db_article is None:
            raise HTTPException(status_code=404, detail="Article not found")
        return db_article

    async def read_articles(self, skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
        service = ArticleService(db)
        return service.get_articles(skip, limit)

article_controller = ArticleController()
article_router = article_controller.router