from sqlalchemy.orm import Session
from app.repository.article_repository import ArticleRepository
from app.dto.article_dto import ArticleCreateDTO, ArticleUpdateDTO

class ArticleService:

    def __init__(self, db: Session):
        self.repository = ArticleRepository(db)

    def get_article(self, article_id: int):
        return self.repository.get_article(article_id)

    def create_article(self, article: ArticleCreateDTO):
        return self.repository.create_article(article)

    def update_article(self, article_id: int, article: ArticleUpdateDTO):
        return self.repository.update_article(article_id, article)

    def delete_article(self, article_id: int):
        return self.repository.delete_article(article_id)

    def get_articles(self, skip: int = 0, limit: int = 10):
        return self.repository.get_articles(skip, limit)
