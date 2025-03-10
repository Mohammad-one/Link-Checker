from sqlalchemy.orm import Session
from src.models.link import Link

def get_all_links(db: Session):
    """Fetch all links from the website_crawler database."""
    return db.query(Link).all()

def get_affiliate_links(db: Session):
    """Fetch links that contain known affiliate patterns."""
    return db.query(Link).filter(Link.url.like('%utm_medium=Affilio%')).all()
