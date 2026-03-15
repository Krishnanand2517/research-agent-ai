from ddgs import DDGS
from schema import SearchResult


def search_web(query: str, max_results: int = 5) -> list[SearchResult]:
    """
    Search the web and return a list of results.
    Each result contains:
    - title
    - url
    - snippet
    """

    results = []

    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=max_results):
            results.append(
                {"title": r["title"], "url": r["href"], "snippet": r["body"]}
            )

    return results
