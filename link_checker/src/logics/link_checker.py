import re
from src.repositories.link_repository import get_all_links

AFFILIATE_PATTERNS = [
    "utm_medium=Affilio",
    "utm_content=PUBLIC",
    "utm_content=PRIVATE",
    "utm_content=WIDGET",
]


def check_affiliate_link(url: str) -> bool:
    """Check if a URL contains an affiliate pattern."""
    return any(pattern in url for pattern in AFFILIATE_PATTERNS)


def analyze_links(db):
    """Analyze all links and count how many are affiliates."""
    links = get_all_links(db)
    affiliate_count = sum(1 for link in links if check_affiliate_link(link.url))

    return {
        "total_links": len(links),
        "affiliate_links": affiliate_count,
        "affiliate_percentage": (affiliate_count / len(links) * 100) if links else 0
    }
