from sqlalchemy.orm import Session
from app.model.article import Article
from app.dto.article_dto import ArticleCreateDTO, ArticleUpdateDTO

class ArticleRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_article(self, article_id: int):
        return self.db.query(Article).filter(Article.id == article_id).first()

    def create_article(self, article: ArticleCreateDTO):
        db_article = Article(**article.dict())
        self.db.add(db_article)
        self.db.commit()
        self.db.refresh(db_article)
        return db_article

    def update_article(self, article_id: int, article: ArticleUpdateDTO):
        db_article = self.get_article(article_id)
        if db_article:
            update_data = article.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_article, key, value)
            self.db.commit()
            self.db.refresh(db_article)
        return db_article

    def delete_article(self, article_id: int):
        db_article = self.get_article(article_id)
        if db_article:
            self.db.delete(db_article)
            self.db.commit()
        return db_article

    def get_articles(self, skip: int = 0, limit: int = 10):
        return self.db.query(Article).offset(skip).limit(limit).all()
